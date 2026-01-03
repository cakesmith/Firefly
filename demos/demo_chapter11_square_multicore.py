#!/usr/bin/env python3
"""
Chapter 11 Square Game - Optimized Multi-Core Petri Net
========================================================
Compiles Square Jack program to VM, builds Petri net with
memory optimization and multi-core assignment, then outputs
results for 1, 2, 4, and 8 core scenarios.

Architecture:
- Memory optimizer uses graph coloring to minimize memory slots
- CPU core assignment distributes transitions across cores
- Outputs statistics and analysis for each core configuration
"""

import sys
import os
import tempfile
import shutil
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from Petri.Token import Token

# Hack memory map
SCREEN_BASE = 16384
SCREEN_END = 24575
KBD_ADDR = 24576


class SharedMemory:
    """Shared memory with screen and keyboard I/O."""
    
    def __init__(self):
        self.ram = [0] * 32768
        self.screen = [0] * 8192
        self.keyboard = 0
        
        # Initialize pointers
        self.ram[0] = 256   # SP
        self.ram[1] = 300   # LCL
        self.ram[2] = 400   # ARG
        self.ram[3] = 3000  # THIS
        self.ram[4] = 3010  # THAT
        
        # Initialize heap
        self.ram[2048] = 14334
        self.ram[2049] = 2050
        
        # Stats
        self.screen_writes = 0
        self.total_writes = 0
        self.total_reads = 0
    
    def read(self, addr):
        self.total_reads += 1
        if addr == KBD_ADDR:
            return self.keyboard
        elif SCREEN_BASE <= addr <= SCREEN_END:
            return self.screen[addr - SCREEN_BASE]
        elif 0 <= addr < len(self.ram):
            return self.ram[addr]
        return 0
    
    def write(self, addr, value):
        self.total_writes += 1
        value = value & 0xFFFF
        if SCREEN_BASE <= addr <= SCREEN_END:
            self.screen[addr - SCREEN_BASE] = value
            self.screen_writes += 1
        elif 0 <= addr < len(self.ram):
            self.ram[addr] = value


def compile_square(memory: SharedMemory):
    """Compile Square and build Petri net with memory callbacks."""
    project_dir = "tecs/projects/11/Square"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(project_dir):
        raise FileNotFoundError(f"Project not found: {project_dir}")
    
    temp_dir = tempfile.mkdtemp(prefix="square_multicore_")
    
    try:
        for f in os.listdir(project_dir):
            if f.endswith('.jack'):
                shutil.copy(os.path.join(project_dir, f), temp_dir)
        
        print("  Compiling Jack to VM...")
        ExpressionEvaluator(temp_dir, overwrite=True)
        
        os_files = ['Sys.vm', 'Memory.vm', 'Screen.vm', 'Keyboard.vm', 
                    'Math.vm', 'Output.vm', 'String.vm', 'Array.vm']
        for f in os_files:
            src = os.path.join(os_dir, f)
            if os.path.exists(src):
                shutil.copy(src, temp_dir)
        
        print("  Building Petri net...")
        parser = VMParser(
            temp_dir,
            memory_read_callback=memory.read,
            memory_write_callback=memory.write
        )
        
        return parser.emitter.net, temp_dir, parser.emitter
        
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e


def analyze_petri_net(net):
    """Analyze Petri net structure."""
    # Count transition types
    push_trans = sum(1 for n in net.transitions if n.startswith('push_'))
    arith_trans = sum(1 for n in net.transitions if any(n.startswith(op) for op in ['add_', 'sub_', 'neg_', 'lt_', 'gt_', 'eq_', 'and_', 'or_', 'not_']))
    call_trans = sum(1 for n in net.transitions if n.startswith('call_'))
    return_trans = sum(1 for n in net.transitions if n.startswith('return_') or n.startswith('dispatch_'))
    
    return {
        'total_places': len(net.places),
        'total_transitions': len(net.transitions),
        'total_arcs': len(net.arcs),
        'push_transitions': push_trans,
        'arithmetic_transitions': arith_trans,
        'call_transitions': call_trans,
        'return_transitions': return_trans,
    }


def execute_sequential(net, max_steps=50000):
    """Execute Petri net sequentially using event-driven approach."""
    net.initialize_enabled_set()
    
    steps = 0
    fired_total = 0
    last_report = 0
    
    while steps < max_steps:
        # Use the optimized event-driven single-step execution
        fired = net.execute_step_single()
        if not fired:
            break
        fired_total += 1
        steps += 1
        
        if steps - last_report >= 5000:
            print(f"      Step {steps:,}...")
            last_report = steps
    
    return steps, fired_total


def execute_parallel_optimized(net, num_cores, max_steps=50000):
    """
    Execute Petri net with parallel firing using event-driven optimization.
    Uses the net's _potentially_enabled set to avoid scanning all transitions.
    """
    # Reset tokens
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    net.initialize_enabled_set()
    
    steps = 0
    fired_total = 0
    parallel_firings = 0
    last_report = 0
    
    # Pre-build place sets for each transition (optimization)
    trans_places = {}
    for t in net.transitions.values():
        trans_places[t.name] = frozenset(p.name for p in t.in_places) | frozenset(p.name for p in t.out_places)
    
    while steps < max_steps:
        # Find enabled transitions from potentially enabled set (event-driven)
        enabled = []
        still_potentially_enabled = set()
        
        for trans_name in net._potentially_enabled:
            transition = net.transitions[trans_name]
            if transition.can_fire():
                enabled.append(transition)
            elif any(p.has for p in transition.in_places):
                still_potentially_enabled.add(trans_name)
        
        if not enabled:
            break
        
        # Select up to num_cores non-conflicting transitions
        to_fire = []
        used_places = set()
        
        for t in enabled:
            t_places = trans_places[t.name]
            
            if not (t_places & used_places):
                to_fire.append(t)
                used_places |= t_places
                
                if len(to_fire) >= num_cores:
                    break
        
        # Fire selected transitions and update potentially enabled set
        for t in to_fire:
            if t.can_fire():
                t.fire()
                fired_total += 1
                
                # Update potentially enabled set
                for out_place in t.out_places:
                    if out_place.has:
                        for consumer in out_place.consumers:
                            still_potentially_enabled.add(consumer.name)
        
        net._potentially_enabled = still_potentially_enabled
        
        if len(to_fire) > 1:
            parallel_firings += 1
        
        steps += 1
        
        if steps - last_report >= 5000:
            print(f"      Step {steps:,} (fired {fired_total:,})...")
            last_report = steps
    
    return steps, fired_total, parallel_firings


def run_multicore_analysis(net, emitter):
    """Run analysis for 1, 2, 4, and 8 core configurations."""
    results = {}
    
    # Use a smaller step count for analysis (full execution takes too long)
    analysis_steps = 20000
    
    # First, get sequential baseline
    print(f"\n  Running sequential baseline ({analysis_steps:,} steps max)...")
    
    # Reset for sequential run
    for place in net.places.values():
        place.has = False
        place.token = None
    net.places["init"].put_token(Token("control"))
    
    start_time = time.time()
    seq_steps, seq_fired = execute_sequential(net, max_steps=analysis_steps)
    seq_time = time.time() - start_time
    
    results['sequential'] = {
        'steps': seq_steps,
        'fired': seq_fired,
        'time': seq_time,
    }
    
    print(f"    Sequential: {seq_steps:,} steps, {seq_fired:,} transitions fired ({seq_time:.2f}s)")
    
    # Cache core assignments to avoid recomputing
    cached_assignments = {}
    
    # Run for each core configuration
    for num_cores in [1, 2, 4, 8]:
        print(f"\n  Analyzing {num_cores}-core configuration...")
        
        # Assign CPU cores (cache the max core assignment and reuse)
        if 8 not in cached_assignments:
            print(f"    Computing core assignments...")
            assign_start = time.time()
            cached_assignments[8] = net.assign_cpu_cores(8, verbose=False)
            assign_time = time.time() - assign_start
            print(f"    Core assignment took {assign_time:.2f}s")
        
        # Derive assignments for fewer cores by modulo
        if num_cores < 8:
            assignments = {t: (c % num_cores) for t, c in cached_assignments[8].items()}
        else:
            assignments = cached_assignments[8]
        
        # Count transitions per core
        core_counts = [0] * num_cores
        for trans_name, core_id in assignments.items():
            core_counts[core_id % num_cores] += 1
        
        # Execute with parallel firing
        print(f"    Executing parallel simulation...")
        start_time = time.time()
        par_steps, par_fired, parallel_firings = execute_parallel_optimized(net, num_cores, max_steps=analysis_steps)
        par_time = time.time() - start_time
        
        # Calculate metrics
        speedup = seq_steps / par_steps if par_steps > 0 else 1.0
        efficiency = (speedup / num_cores) * 100
        parallelism = parallel_firings / par_steps * 100 if par_steps > 0 else 0
        
        results[num_cores] = {
            'steps': par_steps,
            'fired': par_fired,
            'time': par_time,
            'speedup': speedup,
            'efficiency': efficiency,
            'parallelism': parallelism,
            'core_distribution': core_counts,
            'parallel_firings': parallel_firings,
        }
        
        print(f"    {num_cores}-core: {par_steps:,} steps, speedup={speedup:.2f}x, efficiency={efficiency:.1f}% ({par_time:.2f}s)")
    
    return results


def print_results(analysis, mem_stats, core_results):
    """Print comprehensive results."""
    print("\n" + "=" * 70)
    print("  PETRI NET ANALYSIS RESULTS")
    print("=" * 70)
    
    print("\n  NETWORK STRUCTURE:")
    print(f"    Total Places:       {analysis['total_places']:,}")
    print(f"    Total Transitions:  {analysis['total_transitions']:,}")
    print(f"    Total Arcs:         {analysis['total_arcs']:,}")
    print(f"    Push Transitions:   {analysis['push_transitions']:,}")
    print(f"    Arithmetic Trans:   {analysis['arithmetic_transitions']:,}")
    print(f"    Call Transitions:   {analysis['call_transitions']:,}")
    print(f"    Return Transitions: {analysis['return_transitions']:,}")
    
    print("\n  MEMORY OPTIMIZATION:")
    print(f"    Total Places:       {mem_stats['total_places']:,}")
    print(f"    Memory Slots Used:  {mem_stats['slots_used']:,}")
    print(f"    Memory Saved:       {mem_stats['slots_saved']:,} ({mem_stats['savings_pct']:.1f}%)")
    print(f"    Memory Range:       {mem_stats['start_addr']} - {mem_stats['end_addr']}")
    
    print("\n  MULTI-CORE EXECUTION COMPARISON:")
    print("-" * 70)
    print(f"  {'Cores':<8} {'Steps':<12} {'Speedup':<12} {'Efficiency':<14} {'Parallelism':<12}")
    print("-" * 70)
    
    seq = core_results['sequential']
    print(f"  {'Seq':<8} {seq['steps']:<12,} {'1.00x':<12} {'100.0%':<14} {'N/A':<12}")
    
    for num_cores in [1, 2, 4, 8]:
        r = core_results[num_cores]
        print(f"  {num_cores:<8} {r['steps']:<12,} {r['speedup']:.2f}x{'':<8} {r['efficiency']:.1f}%{'':<9} {r['parallelism']:.1f}%")
    
    print("-" * 70)
    
    print("\n  CORE DISTRIBUTION (transitions per core):")
    for num_cores in [1, 2, 4, 8]:
        r = core_results[num_cores]
        dist = r['core_distribution']
        dist_str = ", ".join(f"C{i}:{c:,}" for i, c in enumerate(dist))
        print(f"    {num_cores}-core: {dist_str}")
    
    # Find best configuration
    best_cores = max([1, 2, 4, 8], key=lambda c: core_results[c]['speedup'])
    best = core_results[best_cores]
    
    print("\n  BEST CONFIGURATION:")
    print(f"    Cores:              {best_cores}")
    print(f"    Speedup:            {best['speedup']:.2f}x")
    print(f"    Efficiency:         {best['efficiency']:.1f}%")
    print(f"    Parallel Firings:   {best['parallel_firings']:,} ({best['parallelism']:.1f}% of steps)")
    
    # Parallelism analysis
    print("\n  PARALLELISM ANALYSIS:")
    if best['parallelism'] < 1.0:
        print("    This program exhibits SEQUENTIAL execution patterns.")
        print("    Reasons for limited parallelism:")
        print("      - Control flow creates strict ordering (each op waits for previous)")
        print("      - Function calls serialize execution within call chains")
        print("      - Stack-based VM semantics create data dependencies")
        print("")
        print("    The Petri net correctly models these dependencies.")
        print("    Parallelism would appear in programs with:")
        print("      - Independent computations (e.g., parallel array processing)")
        print("      - Multiple concurrent function calls")
        print("      - Data-parallel operations")
    else:
        print(f"    Program exhibits {best['parallelism']:.1f}% parallel execution.")
        print(f"    {best['parallel_firings']:,} steps had multiple transitions fire simultaneously.")


def main():
    print("=" * 70)
    print("  Chapter 11: Square - Optimized Multi-Core Petri Net Analysis")
    print("=" * 70)
    print()
    
    # Create shared memory
    memory = SharedMemory()
    
    # Compile Square
    try:
        print("  COMPILATION PHASE:")
        net, temp_dir, emitter = compile_square(memory)
    except Exception as e:
        print(f"  [ERROR] {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # Analyze network structure
    print("\n  ANALYSIS PHASE:")
    analysis = analyze_petri_net(net)
    print(f"    Places: {analysis['total_places']:,}")
    print(f"    Transitions: {analysis['total_transitions']:,}")
    print(f"    Arcs: {analysis['total_arcs']:,}")
    
    # Memory optimization
    print("\n  MEMORY OPTIMIZATION PHASE:")
    print("    Running optimized graph coloring memory allocator...")
    print("    Algorithm: Liveness analysis + interference graph + greedy coloring")
    print("    Optimizations: Pre-built lookup tables, reduced reachability depth")
    start_time = time.time()
    slots_used = net.allocate_memory(verbose=True)
    alloc_time = time.time() - start_time
    
    mem_stats = {
        'total_places': analysis['total_places'],
        'slots_used': slots_used,
        'slots_saved': analysis['total_places'] - slots_used,
        'savings_pct': (analysis['total_places'] - slots_used) / analysis['total_places'] * 100 if analysis['total_places'] > 0 else 0,
        'start_addr': net.PLACE_MEMORY_BASE,
        'end_addr': net.PLACE_MEMORY_BASE + slots_used - 1,
        'alloc_time': alloc_time,
    }
    
    print(f"    Slots used: {slots_used:,} (saved {mem_stats['slots_saved']:,}, {mem_stats['savings_pct']:.1f}%)")
    print(f"    Allocation time: {alloc_time:.2f}s")
    
    # Multi-core analysis
    print("\n  MULTI-CORE ANALYSIS PHASE:")
    core_results = run_multicore_analysis(net, emitter)
    
    # Print comprehensive results
    print_results(analysis, mem_stats, core_results)
    
    # Cleanup
    shutil.rmtree(temp_dir)
    
    print("\n" + "=" * 70)
    print("  Analysis complete.")
    print("=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
