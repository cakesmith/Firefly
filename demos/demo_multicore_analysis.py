#!/usr/bin/env python3
"""
Multi-Core TECS VM Analysis Demo
================================
Detailed analysis of parallelization in the Petri net-based VM.
Shows actual data dependencies and potential parallelism.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
    """Execute strictly sequentially - one transition per cycle."""
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
        
        # Fire only ONE transition (sequential)
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
    """
    Simulate multi-core execution using the Petri net firing semantics.
    Multiple enabled transitions can fire in the same step.
    """
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
        
        # In multi-core, we can fire up to num_cores transitions per cycle
        # But we need to check for conflicts (shared input/output places)
        to_fire = []
        used_places = set()
        
        for t in enabled:
            # Check if this transition conflicts with already selected ones
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


def analyze_program(name, description, commands, expected=None):
    """Analyze a program's parallelization potential."""
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"  {description}")
    print(f"{'='*70}")
    
    # Show program
    print(f"\nProgram:")
    for i, cmd in enumerate(commands):
        if cmd.segment:
            print(f"  {i+1}. {cmd.command} {cmd.segment} {cmd.index}")
        else:
            print(f"  {i+1}. {cmd.command}")
    
    # Sequential execution (baseline)
    emitter = build_petri_net(commands)
    seq_cycles, seq_result, seq_trace = execute_sequential(emitter)
    
    print(f"\n--- Sequential Execution (1 op/cycle) ---")
    print(f"Cycles: {seq_cycles}")
    print(f"Result: {seq_result}", end="")
    if expected is not None:
        print(f" {'[OK]' if seq_result == expected else '[FAIL]'}")
    else:
        print()
    
    # Multi-core executions
    print(f"\n--- Multi-Core Comparison ---")
    print(f"{'Cores':<8} {'Cycles':<10} {'Speedup':<12} {'Parallel Ops/Cycle':<20}")
    print("-" * 50)
    
    for num_cores in [1, 2, 4, 8]:
        emitter = build_petri_net(commands)
        mc_cycles, mc_result, mc_trace = execute_parallel(emitter, num_cores)
        
        speedup = seq_cycles / mc_cycles if mc_cycles > 0 else 1.0
        avg_parallel = sum(len(f) for f in mc_trace) / len(mc_trace) if mc_trace else 0
        
        print(f"{num_cores:<8} {mc_cycles:<10} {speedup:<12.2f}x {avg_parallel:<20.1f}")
    
    # Detailed trace for 4 cores
    print(f"\n--- Detailed 4-Core Execution Trace ---")
    emitter = build_petri_net(commands)
    mc_cycles, mc_result, mc_trace = execute_parallel(emitter, 4)
    
    for i, fired in enumerate(mc_trace):
        parallel_indicator = " [PARALLEL]" if len(fired) > 1 else ""
        print(f"  Cycle {i+1}: {', '.join(fired)}{parallel_indicator}")
    
    return seq_cycles, mc_cycles


def main():
    print("=" * 72)
    print("  Multi-Core TECS VM - Parallelization Analysis")
    print("=" * 72)
    
    results = []
    
    # Test 1: Simple sequential
    commands = [
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 3),
        vmcommand("add"),
    ]
    s, m = analyze_program(
        "Test 1: Simple Add",
        "5 + 3 = 8",
        commands, 8
    )
    results.append(("Simple Add", s, m))
    
    # Test 2: Four independent pushes then adds
    commands = [
        vmcommand("push", "constant", 1),
        vmcommand("push", "constant", 2),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 4),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    s, m = analyze_program(
        "Test 2: Four Values Sum",
        "1 + 2 + 3 + 4 = 10",
        commands, 10
    )
    results.append(("Four Sum", s, m))
    
    # Test 3: Parallel pairs
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("add"),
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 15),
        vmcommand("add"),
        vmcommand("add"),
    ]
    s, m = analyze_program(
        "Test 3: Parallel Pairs",
        "(10+20) + (5+15) = 50",
        commands, 50
    )
    results.append(("Parallel Pairs", s, m))
    
    # Test 4: Many independent operations
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
    s, m = analyze_program(
        "Test 4: Independent Negations",
        "(-1) + (-2) + (-3) = -6",
        commands, -6
    )
    results.append(("Ind. Negations", s, m))
    
    # Test 5: Comparison chain
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 5),
        vmcommand("gt"),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 7),
        vmcommand("lt"),
        vmcommand("and"),
    ]
    s, m = analyze_program(
        "Test 5: Parallel Comparisons",
        "(10>5) AND (3<7) = true (-1)",
        commands, -1
    )
    results.append(("Parallel Cmp", s, m))
    
    # Test 6: Wide parallel
    commands = [
        vmcommand("push", "constant", 1),
        vmcommand("push", "constant", 2),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 4),
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 6),
        vmcommand("push", "constant", 7),
        vmcommand("push", "constant", 8),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
        vmcommand("add"),
    ]
    s, m = analyze_program(
        "Test 6: Wide Parallel (8 values)",
        "Sum 1..8 = 36",
        commands, 36
    )
    results.append(("Wide (8 vals)", s, m))
    
    # Summary
    print("\n" + "="*70)
    print("  SUMMARY: Speedup Results (Sequential vs 4-Core)")
    print("="*70)
    print(f"\n{'Test':<20} {'Sequential':<12} {'4-Core':<10} {'Speedup':<10} {'Savings':<10}")
    print("-" * 62)
    
    for name, single, multi in results:
        speedup = single / multi if multi > 0 else 1.0
        savings = ((single - multi) / single) * 100 if single > 0 else 0
        print(f"{name:<20} {single:<12} {multi:<10} {speedup:<10.2f}x {savings:<10.1f}%")
    
    # ROM generation stats
    print("\n" + "="*70)
    print("  ROM Generation Statistics")
    print("="*70)
    
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("add"),
        vmcommand("push", "constant", 5),
        vmcommand("add"),
    ]
    
    emitter = build_petri_net(commands)
    net = emitter.net
    net.allocate_memory()
    net.assign_cpu_cores(4)
    
    roms = net.generate_roms()
    
    print(f"\nProgram: push 10, push 20, add, push 5, add")
    print(f"\nShared ROM segments: {roms['stats']['shared_segments']}")
    print(f"Total shared instructions: {roms['stats']['total_shared_instructions']}")
    print(f"Original instructions: {roms['stats']['original_instructions']}")
    print(f"Optimized instructions: {roms['stats']['optimized_instructions']}")
    print(f"ROM savings: {roms['stats']['savings_percent']:.1f}%")
    print(f"Execution levels: {roms['stats']['num_levels']}")
    
    print(f"\nPer-Core ROM sizes:")
    for core_id, rom in roms['cores'].items():
        print(f"  Core {core_id}: {len(rom)} lines")
    
    # Key insights
    print("\n" + "="*70)
    print("  KEY INSIGHTS")
    print("="*70)
    print("""
  PARALLELIZATION BENEFITS:
  
  1. Push operations are independent - can all run in parallel
  2. Binary operations (add, sub) depend on their operands
  3. Best speedup when many independent operations exist
  
  SPEEDUP PATTERNS:
  
  • Simple Add: Limited speedup (sequential dependency)
  • Parallel Pairs: Good speedup (independent sub-expressions)
  • Wide Parallel: Best speedup (many independent pushes)
  
  The Petri net naturally exposes parallelism by tracking
  data dependencies through places and transitions.
""")


if __name__ == "__main__":
    main()
