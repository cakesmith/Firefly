#!/usr/bin/env python3
"""
Chapter 11 ComplexArrays Multi-Core Demo
========================================
Compiles ComplexArrays and demonstrates multi-core execution
with speedup analysis from 1 to 8 cores.

ComplexArrays tests nested array access, pointer aliasing,
and complex expressions - good for showing parallelism potential.
"""

import sys
import os
import tempfile
import shutil
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from PetriEmitter import PetriEmitter
from Petri.Token import Token


def compile_project(project_dir, os_dir, os_files):
    """Compile Jack project with specified OS libraries."""
    temp_dir = tempfile.mkdtemp(prefix="jack_")
    
    for f in os.listdir(project_dir):
        if f.endswith('.jack'):
            shutil.copy(os.path.join(project_dir, f), temp_dir)
    
    compiler = ExpressionEvaluator(temp_dir, overwrite=True)
    
    for f in os.listdir(os_dir):
        if f.endswith('.vm'):
            if f in os_files:
                shutil.copy(os.path.join(os_dir, f), temp_dir)
    
    return temp_dir


def execute_sequential(net):
    """Execute Petri net firing ONE transition per step (true sequential)."""
    cycles = 0
    max_cycles = 50000
    
    while cycles < max_cycles:
        # Find first enabled transition
        enabled = None
        for t in net.transitions.values():
            if t.can_fire():
                enabled = t
                break
        
        if enabled is None:
            break
        
        enabled.fire()
        cycles += 1
    
    return cycles


def execute_parallel(net, num_cores):
    """Execute Petri net with parallel firing limited by core count."""
    cycles = 0
    max_cycles = 50000
    
    while cycles < max_cycles:
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        
        if not enabled:
            break
        
        # Fire up to num_cores transitions per cycle
        to_fire = enabled[:num_cores]
        for t in to_fire:
            t.fire()
        
        cycles += 1
    
    return cycles


def analyze_parallelism(emitter, num_cores):
    """Analyze parallelism potential for given core count."""
    net = emitter.net
    net.allocate_memory(verbose=False)
    net.assign_cpu_cores(num_cores, verbose=False)
    
    # Group transitions by level
    levels = {}
    for trans_name, level in net.transition_levels.items():
        if level not in levels:
            levels[level] = []
        levels[level].append(trans_name)
    
    # Calculate parallel cycles
    parallel_cycles = 0
    total_work = 0
    
    for level in sorted(levels.keys()):
        trans_at_level = levels[level]
        total_work += len(trans_at_level)
        
        # Group by core assignment
        core_work = {}
        for t in trans_at_level:
            core = net.cpu_assignments.get(t, 0)
            if core not in core_work:
                core_work[core] = 0
            core_work[core] += 1
        
        # Cycles = max work on any core at this level
        max_work = max(core_work.values()) if core_work else 0
        parallel_cycles += max_work
    
    return parallel_cycles, len(levels), total_work


def main():
    print("=" * 70)
    print("  Chapter 11: ComplexArrays Multi-Core Execution Demo")
    print("=" * 70)
    
    project_dir = "tecs/projects/11/ComplexArrays"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(project_dir):
        print(f"\n  [ERROR] Project not found: {project_dir}")
        return 1
    
    # OS files needed
    os_files = [
        'Sys.vm',
        'Array.vm',
        'Memory.vm',
        'Output.vm',
        'String.vm',
        'Math.vm',
    ]
    
    temp_dir = None
    try:
        print(f"\n  Compiling ComplexArrays...")
        temp_dir = compile_project(project_dir, os_dir, os_files)
        
        # Count VM commands
        vm_count = 0
        for f in os.listdir(temp_dir):
            if f.endswith('.vm'):
                with open(os.path.join(temp_dir, f)) as vf:
                    vm_count += sum(1 for l in vf if l.strip() and not l.strip().startswith('//'))
        
        print(f"  VM commands: {vm_count}")
        
        # Build initial Petri net for stats
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        print(f"  Places: {len(net.places)}")
        print(f"  Transitions: {len(net.transitions)}")
        
        # Analyze parallelism for 1-8 cores
        print(f"\n  Multi-Core Parallelism Analysis")
        print(f"  " + "-" * 60)
        print(f"  {'Cores':<8} {'Cycles':<12} {'Speedup':<12} {'Efficiency':<12}")
        print(f"  " + "-" * 60)
        
        baseline_cycles = None
        results = []
        
        for num_cores in [1, 2, 4, 6, 8]:
            # Rebuild fresh for each analysis
            parser = VMParser(temp_dir)
            emitter = parser.emitter
            
            cycles, levels, total_work = analyze_parallelism(emitter, num_cores)
            
            if baseline_cycles is None:
                baseline_cycles = cycles
            
            speedup = baseline_cycles / cycles if cycles > 0 else 1.0
            efficiency = (speedup / num_cores) * 100
            
            results.append((num_cores, cycles, speedup, efficiency))
            print(f"  {num_cores:<8} {cycles:<12} {speedup:<12.2f}x {efficiency:<12.1f}%")
        
        print(f"  " + "-" * 60)
        
        # Show transition distribution
        print(f"\n  Transition Level Distribution (8 cores):")
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        net.allocate_memory(verbose=False)
        net.assign_cpu_cores(8, verbose=False)
        
        levels = {}
        for trans_name, level in net.transition_levels.items():
            if level not in levels:
                levels[level] = []
            levels[level].append(trans_name)
        
        # Show first 10 levels
        print(f"  {'Level':<8} {'Transitions':<15} {'Parallelism':<15}")
        print(f"  " + "-" * 40)
        
        for level in sorted(levels.keys())[:10]:
            trans_count = len(levels[level])
            parallelism = min(trans_count, 8)
            bar = "#" * parallelism + "." * (8 - parallelism)
            print(f"  {level:<8} {trans_count:<15} [{bar}]")
        
        if len(levels) > 10:
            print(f"  ... ({len(levels) - 10} more levels)")
        
        # Core utilization
        print(f"\n  Core Assignment Distribution (8 cores):")
        core_counts = {i: 0 for i in range(8)}
        for trans_name, core in net.cpu_assignments.items():
            if core < 8:
                core_counts[core] += 1
        
        total_trans = len(net.transitions)
        for core in range(8):
            count = core_counts[core]
            pct = (count / total_trans) * 100 if total_trans > 0 else 0
            bar_len = int(pct / 5)
            bar = "#" * bar_len
            print(f"  Core {core}: {count:>5} transitions ({pct:>5.1f}%) {bar}")
        
        # Value computation verification
        print(f"\n  ComplexArrays Expected Results:")
        print(f"    Test 1: b[2] = 5")
        print(f"    Test 2: a[5] = 40")
        print(f"    Test 3: c = 0")
        print(f"    Test 4: c[1] = 77")
        print(f"    Test 5: b[1] = 110")
        
        # Speedup summary
        print(f"\n  Speedup Summary:")
        max_speedup = max(r[2] for r in results)
        best_cores = [r[0] for r in results if r[2] == max_speedup][0]
        print(f"    Best speedup: {max_speedup:.2f}x with {best_cores} cores")
        print(f"    Sequential cycles: {baseline_cycles}")
        print(f"    Parallel cycles ({best_cores} cores): {results[-1][1]}")
        
        # Efficiency analysis
        print(f"\n  Efficiency Analysis:")
        for num_cores, cycles, speedup, efficiency in results:
            status = "Good" if efficiency > 50 else "Fair" if efficiency > 25 else "Low"
            print(f"    {num_cores} cores: {efficiency:.1f}% efficiency ({status})")
        
        print(f"\n  [OK] Demo complete")
        return 0
        
    except Exception as e:
        print(f"\n  [ERROR] {e}")
        import traceback
        traceback.print_exc()
        return 1
        
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    sys.exit(main())
