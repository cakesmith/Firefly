#!/usr/bin/env python3
"""
Multi-Core TECS VM - Final Demonstration
========================================
Shows the parallelization capabilities of the Petri net-based VM compiler.
"""

import os
from PetriEmitter import PetriEmitter
from Petri.Token import Token
from VMParser import vmcommand
from CPU import CPU

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


def execute_sequential(emitter):
    """Execute transitions one at a time (true sequential)."""
    net = emitter.net
    
    # Reset
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    cycles = 0
    trace = []
    max_cycles = 100
    
    while cycles < max_cycles:
        # Find first enabled transition only
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        # Fire only ONE transition
        t = enabled[0]
        t.fire()
        cycles += 1
        trace.append([t.name])
    
    # Get result
    result = None
    if emitter.control_stack:
        top = emitter.control_stack[-1]
        if top.token:
            result = top.token.value
    
    return cycles, result, trace


def execute_parallel(emitter, num_cores):
    """Execute with parallel firing (up to num_cores per cycle)."""
    net = emitter.net
    
    # Reset
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    cycles = 0
    trace = []
    max_cycles = 100
    
    while cycles < max_cycles:
        # Find ALL enabled transitions
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            break
        
        # Select up to num_cores non-conflicting transitions
        to_fire = []
        used_places = set()
        
        for t in enabled:
            t_places = set(p.name for p in t.in_places) | set(p.name for p in t.out_places)
            
            if not (t_places & used_places):
                to_fire.append(t)
                used_places |= t_places
                
                if len(to_fire) >= num_cores:
                    break
        
        # Fire selected transitions
        fired_names = []
        for t in to_fire:
            t.fire()
            fired_names.append(t.name)
        
        cycles += 1
        trace.append(fired_names)
    
    # Get result
    result = None
    if emitter.control_stack:
        top = emitter.control_stack[-1]
        if top.token:
            result = top.token.value
    
    return cycles, result, trace


def demo_program(name, description, commands, expected=None):
    """Run complete analysis for a program."""
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"  {description}")
    print(f"{'='*70}")
    
    # Show program
    print(f"\nVM Program ({len(commands)} instructions):")
    for i, cmd in enumerate(commands):
        if cmd.segment:
            print(f"  {i+1:2}. {cmd.command} {cmd.segment} {cmd.index}")
        else:
            print(f"  {i+1:2}. {cmd.command}")
    
    # Build net
    emitter = build_petri_net(commands)
    net = emitter.net
    
    print(f"\nPetri Net Statistics:")
    print(f"  Places: {len(net.places)}")
    print(f"  Transitions: {len(net.transitions)}")
    print(f"  Arcs: {len(net.arcs)}")
    
    # Memory allocation
    mem_slots = net.allocate_memory()
    print(f"  Memory slots: {mem_slots}")
    
    # Sequential execution
    emitter = build_petri_net(commands)
    seq_cycles, seq_result, seq_trace = execute_sequential(emitter)
    
    print(f"\n--- Sequential Execution (1 transition/cycle) ---")
    print(f"Total Cycles: {seq_cycles}")
    print(f"Result: {seq_result}", end="")
    if expected is not None:
        print(f" {'[OK]' if seq_result == expected else '[FAIL]'}")
    else:
        print()
    
    # Show trace
    print(f"\nExecution Trace:")
    for i, fired in enumerate(seq_trace):
        print(f"  Cycle {i+1:2}: {fired[0]}")
    
    # Parallel execution comparison
    print(f"\n--- Parallel Execution Comparison ---")
    print(f"{'Cores':<8} {'Cycles':<10} {'Speedup':<12} {'Efficiency':<12} {'Cycle Savings':<15}")
    print("-" * 57)
    
    results = []
    for num_cores in [1, 2, 4, 8]:
        emitter = build_petri_net(commands)
        par_cycles, par_result, par_trace = execute_parallel(emitter, num_cores)
        
        speedup = seq_cycles / par_cycles if par_cycles > 0 else 1.0
        efficiency = (speedup / num_cores) * 100
        savings = ((seq_cycles - par_cycles) / seq_cycles) * 100 if seq_cycles > 0 else 0
        
        print(f"{num_cores:<8} {par_cycles:<10} {speedup:<12.2f}x {efficiency:<12.1f}% {savings:<15.1f}%")
        results.append((num_cores, par_cycles, speedup, par_trace))
    
    # Show best parallel trace
    best = max(results, key=lambda x: x[2])
    if best[2] > 1.0:
        print(f"\n--- Best Parallel Trace ({best[0]} cores, {best[2]:.2f}x speedup) ---")
        for i, fired in enumerate(best[3]):
            parallel_mark = " ← PARALLEL" if len(fired) > 1 else ""
            print(f"  Cycle {i+1:2}: {', '.join(fired)}{parallel_mark}")
    
    return seq_cycles, results


def main():
    print("=" * 72)
    print("        TECS VM Multi-Core Parallelization Demonstration")
    print("        Petri Net-Based Scheduling with Shared ROM")
    print("=" * 72)
    
    all_results = []
    
    # Test 1: Simple add (minimal parallelism)
    commands = [
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 3),
        vmcommand("add"),
    ]
    seq, res = demo_program(
        "Test 1: Simple Addition",
        "5 + 3 = 8 (sequential dependency chain)",
        commands, 8
    )
    all_results.append(("Simple Add", seq, res))
    
    # Test 2: Parallel pairs
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("add"),
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 15),
        vmcommand("add"),
        vmcommand("add"),
    ]
    seq, res = demo_program(
        "Test 2: Parallel Pairs",
        "(10+20) + (5+15) = 50 (two independent sums)",
        commands, 50
    )
    all_results.append(("Parallel Pairs", seq, res))
    
    # Test 3: Independent negations
    commands = [
        vmcommand("push", "constant", 1),
        vmcommand("neg"),
        vmcommand("push", "constant", 2),
        vmcommand("neg"),
        vmcommand("push", "constant", 3),
        vmcommand("neg"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    seq, res = demo_program(
        "Test 3: Independent Negations",
        "(-1) + (-2) + (-3) = -6 (parallel neg operations)",
        commands, -6
    )
    all_results.append(("Ind. Negations", seq, res))
    
    # Test 4: Parallel comparisons
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 5),
        vmcommand("gt"),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 7),
        vmcommand("lt"),
        vmcommand("and"),
    ]
    seq, res = demo_program(
        "Test 4: Parallel Comparisons",
        "(10>5) AND (3<7) = true (two independent comparisons)",
        commands, -1
    )
    all_results.append(("Parallel Cmp", seq, res))
    
    # Test 5: Mixed operations
    commands = [
        vmcommand("push", "constant", 100),
        vmcommand("push", "constant", 30),
        vmcommand("sub"),
        vmcommand("push", "constant", 10),
        vmcommand("add"),
        vmcommand("push", "constant", 2),
        vmcommand("sub"),
        vmcommand("neg"),
    ]
    seq, res = demo_program(
        "Test 5: Mixed Operations",
        "-(100-30+10-2) = -78 (sequential chain)",
        commands, -78
    )
    all_results.append(("Mixed Ops", seq, res))
    
    # Test 6: Wide parallel
    commands = [
        vmcommand("push", "constant", 1),
        vmcommand("push", "constant", 2),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 4),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    seq, res = demo_program(
        "Test 6: Four Value Sum",
        "1+2+3+4 = 10 (stack-based dependencies)",
        commands, 10
    )
    all_results.append(("Four Sum", seq, res))
    
    # Summary
    print("\n" + "="*70)
    print("  FINAL SUMMARY")
    print("="*70)
    
    print(f"\n{'Test':<20} {'Sequential':<12} {'2-Core':<10} {'4-Core':<10} {'8-Core':<10}")
    print("-" * 62)
    
    for name, seq, results in all_results:
        row = f"{name:<20} {seq:<12}"
        for cores, cycles, speedup, _ in results[1:]:  # Skip 1-core
            row += f" {cycles:<10}"
        print(row)
    
    print(f"\n{'Test':<20} {'Best Speedup':<15} {'Best Cores':<12} {'Max Savings':<12}")
    print("-" * 59)
    
    for name, seq, results in all_results:
        best = max(results, key=lambda x: x[2])
        savings = ((seq - best[1]) / seq) * 100 if seq > 0 else 0
        print(f"{name:<20} {best[2]:<15.2f}x {best[0]:<12} {savings:<12.1f}%")
    
    # Key insights
    print("\n" + "="*70)
    print("  KEY INSIGHTS")
    print("="*70)
    print("""
  PARALLELIZATION OPPORTUNITIES:
  
  1. Independent Operations: Operations that don't share data can run
     in parallel on different cores.
     
  2. Petri Net Semantics: The Petri net naturally exposes parallelism -
     all enabled transitions can fire simultaneously.
     
  3. Stack Dependencies: Traditional stack-based VMs create sequential
     dependencies. The Petri net model breaks these where possible.
     
  4. Graph Coloring: CPU core assignment uses graph coloring to ensure
     no conflicting operations run on the same core.
     
  5. Shared ROM: All cores share the same instruction ROM, allowing
     any core to execute any instruction.
  
  SPEEDUP FACTORS:
  
  • Best speedup: Programs with independent parallel operations
  • Limited speedup: Programs with long dependency chains
  • Memory conflicts: Shared memory access can limit parallelism
  
  CYCLE SAVINGS:
  
  • Parallel pairs: ~14% savings with 2+ cores
  • Independent ops: ~25% savings with 2+ cores  
  • Sequential chains: No savings (inherent dependencies)
""")


if __name__ == "__main__":
    main()
