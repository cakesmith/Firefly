#!/usr/bin/env python3
"""
Multicore TECS VM Demonstration
===============================
Demonstrates parallel execution of VM programs using Petri net-based
multi-core CPU scheduling with detailed statistics.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from Petri.Token import Token
from VMParser import vmcommand

def parse_vm_file(filepath):
    """Parse a .vm file and return list of vmcommand objects."""
    commands = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('//'):
                continue
            
            parts = line.split()
            if not parts:
                continue
                
            cmd = parts[0]
            
            # Zero-arg commands
            if cmd in ['add', 'sub', 'neg', 'lt', 'eq', 'gt', 'and', 'or', 'not', 'return']:
                commands.append(vmcommand(cmd))
            # One-arg commands
            elif cmd in ['label', 'goto', 'if-goto']:
                if len(parts) >= 2:
                    commands.append(vmcommand(cmd, parts[1]))
            # Two-arg commands
            elif cmd in ['push', 'pop', 'function', 'call']:
                if len(parts) >= 3:
                    commands.append(vmcommand(cmd, parts[1], int(parts[2])))
    
    return commands


def build_petri_net(commands):
    """Build a Petri net from VM commands."""
    emitter = PetriEmitter()
    
    for cmd in commands:
        if cmd.command == "push" and cmd.segment == "constant":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
        elif cmd.command == "sub":
            emitter.sub(cmd)
        elif cmd.command == "neg":
            emitter.neg(cmd)
        elif cmd.command == "lt":
            emitter.lt(cmd)
        elif cmd.command == "eq":
            emitter.eq(cmd)
        elif cmd.command == "gt":
            emitter.gt(cmd)
        elif cmd.command == "and":
            emitter.and_op(cmd)
        elif cmd.command == "or":
            emitter.or_op(cmd)
        elif cmd.command == "not":
            emitter.not_op(cmd)
        elif cmd.command == "label":
            emitter.label(cmd)
        elif cmd.command == "goto":
            emitter.goto(cmd)
        elif cmd.command == "if-goto":
            emitter.ifgoto(cmd)
    
    return emitter


def simulate_single_core(emitter):
    """Simulate single-core execution and count cycles."""
    net = emitter.net
    cycles = 0
    max_cycles = 1000  # Safety limit
    
    # Reset tokens
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    while cycles < max_cycles:
        fired = net.execute_step()
        if not fired:
            break
        cycles += 1
    
    return cycles


def simulate_multicore(emitter, num_cores):
    """
    Simulate multi-core execution with level-based parallelism.
    Returns (cycles, transitions_per_cycle, core_utilization).
    """
    net = emitter.net
    
    # Allocate memory and assign CPU cores
    net.allocate_memory()
    assignments = net.assign_cpu_cores(num_cores)
    
    # Group transitions by level
    levels = {}
    for trans_name, level in net.transition_levels.items():
        if level not in levels:
            levels[level] = []
        levels[level].append(trans_name)
    
    # Simulate execution
    cycles = 0
    transitions_fired = []
    core_work = {i: 0 for i in range(num_cores)}
    
    for level in sorted(levels.keys()):
        level_transitions = levels[level]
        
        # Group by core for this level
        core_trans = {i: [] for i in range(num_cores)}
        for trans_name in level_transitions:
            core = assignments.get(trans_name, 0)
            core_trans[core].append(trans_name)
        
        # Find max work at this level (determines cycles for this level)
        max_work_this_level = max(len(trans) for trans in core_trans.values()) if core_trans else 0
        
        if max_work_this_level > 0:
            cycles += max_work_this_level
            
            for core, trans_list in core_trans.items():
                core_work[core] += len(trans_list)
            
            transitions_fired.append({
                'level': level,
                'transitions': level_transitions,
                'parallel_work': max_work_this_level
            })
    
    # Calculate utilization
    total_work = sum(core_work.values())
    max_possible_work = cycles * num_cores if cycles > 0 else 1
    utilization = (total_work / max_possible_work) * 100 if max_possible_work > 0 else 0
    
    return cycles, transitions_fired, core_work, utilization


def run_demo(vm_file, description):
    """Run a complete demonstration for a VM file."""
    print(f"\n{'='*70}")
    print(f"  {description}")
    print(f"  File: {vm_file}")
    print(f"{'='*70}")
    
    # Parse and build
    commands = parse_vm_file(vm_file)
    print(f"\nVM Commands: {len(commands)}")
    for i, cmd in enumerate(commands):
        if cmd.segment:
            print(f"  {i+1}. {cmd.command} {cmd.segment} {cmd.index if cmd.index is not None else ''}")
        else:
            print(f"  {i+1}. {cmd.command}")
    
    emitter = build_petri_net(commands)
    net = emitter.net
    
    # Network stats
    print(f"\nPetri Net Structure:")
    print(f"  Places: {len(net.places)}")
    print(f"  Transitions: {len(net.transitions)}")
    print(f"  Arcs: {len(net.arcs)}")
    
    # Memory allocation
    memory_slots = net.allocate_memory()
    print(f"  Memory slots allocated: {memory_slots}")
    
    # Single-core baseline
    single_cycles = simulate_single_core(emitter)
    print(f"\n--- Single Core Execution ---")
    print(f"  Cycles: {single_cycles}")
    
    # Multi-core simulations
    print(f"\n--- Multi-Core Execution Comparison ---")
    print(f"{'Cores':<8} {'Cycles':<10} {'Speedup':<10} {'Utilization':<12} {'Savings':<10}")
    print(f"{'-'*50}")
    
    results = []
    for num_cores in [1, 2, 4, 8]:
        cycles, fired_info, core_work, utilization = simulate_multicore(emitter, num_cores)
        
        speedup = single_cycles / cycles if cycles > 0 else 1.0
        savings = ((single_cycles - cycles) / single_cycles) * 100 if single_cycles > 0 else 0
        
        print(f"{num_cores:<8} {cycles:<10} {speedup:<10.2f}x {utilization:<12.1f}% {savings:<10.1f}%")
        
        results.append({
            'cores': num_cores,
            'cycles': cycles,
            'speedup': speedup,
            'utilization': utilization,
            'savings': savings,
            'core_work': core_work
        })
    
    # Detailed breakdown for best multi-core config
    best_multicore = max([r for r in results if r['cores'] > 1], key=lambda x: x['speedup'])
    print(f"\n--- Detailed Analysis ({best_multicore['cores']} cores) ---")
    
    # Re-run to get detailed info
    net.assign_cpu_cores(best_multicore['cores'])
    
    print(f"\nTransition Levels (parallelization opportunities):")
    levels = {}
    for trans_name, level in net.transition_levels.items():
        if level not in levels:
            levels[level] = []
        levels[level].append(trans_name)
    
    for level in sorted(levels.keys()):
        trans_list = levels[level]
        print(f"  Level {level}: {len(trans_list)} transitions")
        for t in trans_list[:5]:  # Show first 5
            core = net.cpu_assignments.get(t, 0)
            print(f"    - {t} → Core {core}")
        if len(trans_list) > 5:
            print(f"    ... and {len(trans_list) - 5} more")
    
    print(f"\nCore Workload Distribution:")
    for core, work in best_multicore['core_work'].items():
        bar = '#' * (work * 2) if work > 0 else '-'
        print(f"  Core {core}: {bar} ({work} transitions)")
    
    return results


def main():
    print("=" * 72)
    print("  TECS VM Multi-Core Execution Demonstration")
    print("  Petri Net-Based Parallel Scheduling")
    print("=" * 72)
    
    # Find all example VM files
    examples_dir = "examples"
    vm_files = []
    
    if os.path.exists(examples_dir):
        for f in os.listdir(examples_dir):
            if f.endswith('.vm'):
                vm_files.append(os.path.join(examples_dir, f))
    
    if not vm_files:
        print("No VM files found in examples/ directory")
        return
    
    # Run demos
    all_results = {}
    
    for vm_file in sorted(vm_files):
        name = os.path.basename(vm_file).replace('.vm', '')
        description = name.replace('_', ' ').title()
        
        try:
            results = run_demo(vm_file, description)
            all_results[name] = results
        except Exception as e:
            print(f"\n[SKIP] {vm_file}: {e}")
    
    # Summary
    print("\n" + "="*70)
    print("  SUMMARY: Multi-Core Speedup Across All Examples")
    print("="*70)
    print(f"\n{'Example':<25} {'1-Core':<10} {'2-Core':<10} {'4-Core':<10} {'8-Core':<10}")
    print(f"{'-'*65}")
    
    for name, results in all_results.items():
        row = f"{name:<25}"
        for r in results:
            row += f" {r['cycles']:<10}"
        print(row)
    
    print(f"\n{'Example':<25} {'Best Speedup':<15} {'Best Cores':<12} {'Cycle Savings':<15}")
    print(f"{'-'*65}")
    
    for name, results in all_results.items():
        best = max(results, key=lambda x: x['speedup'])
        print(f"{name:<25} {best['speedup']:<15.2f}x {best['cores']:<12} {best['savings']:<15.1f}%")
    
    print("\n" + "="*70)
    print("  Key Insights:")
    print("="*70)
    print("  • Speedup depends on parallelizable operations at each level")
    print("  • Independent push operations can execute in parallel")
    print("  • Binary operations (add, sub, etc.) depend on their operands")
    print("  • Graph coloring ensures no resource conflicts between cores")
    print("  • Shared ROM allows any core to execute any instruction")


if __name__ == "__main__":
    main()
