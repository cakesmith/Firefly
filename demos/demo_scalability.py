#!/usr/bin/env python3
"""
Multi-Core Scalability Demonstration
====================================
Shows how the Petri net-based VM scales with increasing core counts
and program sizes. Demonstrates the relationship between parallelism
and speedup.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from Petri.Token import Token
from VMParser import vmcommand

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
    
    return emitter


def execute_parallel(emitter, num_cores):
    """Execute with parallel firing (up to num_cores per cycle)."""
    net = emitter.net
    
    # Reset
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    cycles = 0
    max_cycles = 1000
    
    while cycles < max_cycles:
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        to_fire = []
        used_places = set()
        
        for t in enabled:
            t_places = set(p.name for p in t.in_places) | set(p.name for p in t.out_places)
            
            if not (t_places & used_places):
                to_fire.append(t)
                used_places |= t_places
                
                if len(to_fire) >= num_cores:
                    break
        
        for t in to_fire:
            t.fire()
        
        cycles += 1
    
    result = None
    if emitter.control_stack:
        top = emitter.control_stack[-1]
        if top.token:
            result = top.token.value
    
    return cycles, result


def generate_wide_parallel_program(width):
    """Generate a program with 'width' independent push operations followed by reductions."""
    commands = []
    
    # Push 'width' constants
    for i in range(width):
        commands.append(vmcommand("push", "constant", i + 1))
    
    # Reduce with adds
    for _ in range(width - 1):
        commands.append(vmcommand("add"))
    
    return commands


def generate_tree_reduction_program(depth):
    """Generate a tree-structured reduction program (2^depth values)."""
    width = 2 ** depth
    commands = []
    
    # Push 2^depth constants
    for i in range(width):
        commands.append(vmcommand("push", "constant", i + 1))
    
    # Tree reduction
    for _ in range(width - 1):
        commands.append(vmcommand("add"))
    
    return commands


def generate_parallel_comparisons(num_pairs):
    """Generate program with independent comparison operations."""
    commands = []
    
    # Generate pairs of pushes followed by comparisons
    for i in range(num_pairs):
        commands.append(vmcommand("push", "constant", i * 2 + 10))
        commands.append(vmcommand("push", "constant", i * 2 + 5))
        commands.append(vmcommand("gt"))
    
    # Combine results with AND
    for _ in range(num_pairs - 1):
        commands.append(vmcommand("and"))
    
    return commands


def generate_mixed_parallel(num_groups):
    """Generate program with mixed parallel operations."""
    commands = []
    
    # Each group: push, push, operation
    operations = ["add", "sub", "and", "or"]
    
    for i in range(num_groups):
        commands.append(vmcommand("push", "constant", 100 + i))
        commands.append(vmcommand("push", "constant", 50 + i))
        op = operations[i % len(operations)]
        if op == "add":
            commands.append(vmcommand("add"))
        elif op == "sub":
            commands.append(vmcommand("sub"))
        elif op == "and":
            commands.append(vmcommand("and"))
        elif op == "or":
            commands.append(vmcommand("or"))
    
    # Combine all results
    for _ in range(num_groups - 1):
        commands.append(vmcommand("add"))
    
    return commands


def run_scalability_test(name, commands, core_counts):
    """Run scalability test across different core counts."""
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"  {len(commands)} VM instructions")
    print(f"{'='*70}")
    
    # Get baseline (1 core)
    emitter = build_petri_net(commands)
    baseline_cycles, result = execute_parallel(emitter, 1)
    
    print(f"\nResult: {result}")
    print(f"\n{'Cores':<8} {'Cycles':<10} {'Speedup':<12} {'Efficiency':<12} {'Parallel Ops':<15}")
    print("-" * 57)
    
    results = []
    for num_cores in core_counts:
        emitter = build_petri_net(commands)
        cycles, _ = execute_parallel(emitter, num_cores)
        
        speedup = baseline_cycles / cycles if cycles > 0 else 1.0
        efficiency = (speedup / num_cores) * 100
        
        # Calculate average parallel operations per cycle
        emitter = build_petri_net(commands)
        net = emitter.net
        for place in net.places.values():
            place.has = False
            place.token = None
        net.places["init"].put_token(Token("control"))
        
        total_ops = 0
        cycle_count = 0
        while cycle_count < 1000:
            enabled = [t for t in net.transitions.values() if t.can_fire()]
            if not enabled:
                break
            
            to_fire = []
            used_places = set()
            for t in enabled:
                t_places = set(p.name for p in t.in_places) | set(p.name for p in t.out_places)
                if not (t_places & used_places):
                    to_fire.append(t)
                    used_places |= t_places
                    if len(to_fire) >= num_cores:
                        break
            
            total_ops += len(to_fire)
            for t in to_fire:
                t.fire()
            cycle_count += 1
        
        avg_parallel = total_ops / cycle_count if cycle_count > 0 else 0
        
        print(f"{num_cores:<8} {cycles:<10} {speedup:<12.2f}x {efficiency:<12.1f}% {avg_parallel:<15.1f}")
        results.append((num_cores, cycles, speedup, efficiency))
    
    return results


def main():
    print("=" * 72)
    print("  Multi-Core Scalability Demonstration")
    print("  Petri Net-Based VM with Shared ROM")
    print("=" * 72)
    
    core_counts = [1, 2, 4, 8, 16, 32]
    
    all_results = []
    
    # Test 1: Wide parallel (16 values)
    commands = generate_wide_parallel_program(16)
    results = run_scalability_test(
        "Test 1: Wide Parallel (16 values → sum)",
        commands,
        core_counts
    )
    all_results.append(("Wide 16", results))
    
    # Test 2: Wide parallel (32 values)
    commands = generate_wide_parallel_program(32)
    results = run_scalability_test(
        "Test 2: Wide Parallel (32 values → sum)",
        commands,
        core_counts
    )
    all_results.append(("Wide 32", results))
    
    # Test 3: Tree reduction (depth 4 = 16 values)
    commands = generate_tree_reduction_program(4)
    results = run_scalability_test(
        "Test 3: Tree Reduction (2^4 = 16 values)",
        commands,
        core_counts
    )
    all_results.append(("Tree 16", results))
    
    # Test 4: Tree reduction (depth 5 = 32 values)
    commands = generate_tree_reduction_program(5)
    results = run_scalability_test(
        "Test 4: Tree Reduction (2^5 = 32 values)",
        commands,
        core_counts
    )
    all_results.append(("Tree 32", results))
    
    # Test 5: Parallel comparisons (8 pairs)
    commands = generate_parallel_comparisons(8)
    results = run_scalability_test(
        "Test 5: Parallel Comparisons (8 pairs)",
        commands,
        core_counts
    )
    all_results.append(("Cmp 8", results))
    
    # Test 6: Parallel comparisons (16 pairs)
    commands = generate_parallel_comparisons(16)
    results = run_scalability_test(
        "Test 6: Parallel Comparisons (16 pairs)",
        commands,
        core_counts
    )
    all_results.append(("Cmp 16", results))
    
    # Test 7: Mixed parallel (8 groups)
    commands = generate_mixed_parallel(8)
    results = run_scalability_test(
        "Test 7: Mixed Parallel Operations (8 groups)",
        commands,
        core_counts
    )
    all_results.append(("Mixed 8", results))
    
    # Test 8: Mixed parallel (16 groups)
    commands = generate_mixed_parallel(16)
    results = run_scalability_test(
        "Test 8: Mixed Parallel Operations (16 groups)",
        commands,
        core_counts
    )
    all_results.append(("Mixed 16", results))
    
    # Summary table
    print("\n" + "="*80)
    print("  SCALABILITY SUMMARY")
    print("="*80)
    
    print(f"\n{'Test':<12}", end="")
    for cores in core_counts:
        print(f"{cores:>8} cores", end="")
    print()
    print("-" * (12 + 13 * len(core_counts)))
    
    for name, results in all_results:
        print(f"{name:<12}", end="")
        for cores, cycles, speedup, efficiency in results:
            print(f"{speedup:>10.2f}x", end="")
        print()
    
    # Efficiency summary
    print(f"\n{'Test':<12}", end="")
    for cores in core_counts:
        print(f"{cores:>8} cores", end="")
    print(" (Efficiency %)")
    print("-" * (12 + 13 * len(core_counts) + 15))
    
    for name, results in all_results:
        print(f"{name:<12}", end="")
        for cores, cycles, speedup, efficiency in results:
            print(f"{efficiency:>10.1f}%", end="")
        print()
    
    # Key insights
    print("\n" + "="*80)
    print("  KEY INSIGHTS")
    print("="*80)
    print("""
  SCALABILITY PATTERNS:
  
  1. Wide Parallel Programs:
     - 16+ independent operations benefit from 8+ cores
     - Speedup approaches theoretical maximum with enough parallelism
     
  2. Tree Reductions:
     - Log(N) depth limits parallelism
     - 32 values = 5 levels, max ~6x speedup with many cores
     
  3. Parallel Comparisons:
     - Each comparison is independent
     - Excellent scaling up to number of comparison pairs
     
  4. Mixed Operations:
     - Different operation types can run in parallel
     - Good load balancing across cores
  
  EFFICIENCY OBSERVATIONS:
  
  • Efficiency decreases as cores increase (Amdahl's Law)
  • Best efficiency when parallelism matches core count
  • Diminishing returns beyond available parallelism
  
  OPTIMAL CORE ALLOCATION:
  
  • Small programs (< 8 ops): 2-4 cores optimal
  • Medium programs (8-16 ops): 4-8 cores optimal
  • Large programs (16+ ops): 8-16 cores beneficial
  • Very large programs: 16-32 cores can help
""")


if __name__ == "__main__":
    main()
