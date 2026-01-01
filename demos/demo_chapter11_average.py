#!/usr/bin/env python3
"""
Chapter 11 Average Program Demo
===============================
Demonstrates compiling and analyzing the Average Jack program
for multi-core execution with shared keyboard/screen I/O.

The Average program:
1. Asks "How many numbers?"
2. Reads N numbers from keyboard
3. Computes and displays the average

Memory-mapped I/O (shared across all cores):
- Screen: 16384-24575 (8K words, 256x512 pixels)
- Keyboard: 24576 (single register)
"""

import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from JackCompiler import ExpressionEvaluator
from VMParser import VMParser
from PetriEmitter import PetriEmitter
from Petri.Token import Token


def compile_project(project_dir, os_dir, os_files=None):
    """Compile Jack project with OS libraries."""
    temp_dir = tempfile.mkdtemp(prefix="jack_")
    
    # Copy Jack files
    for f in os.listdir(project_dir):
        if f.endswith('.jack'):
            shutil.copy(os.path.join(project_dir, f), temp_dir)
    
    # Compile
    compiler = ExpressionEvaluator(temp_dir, overwrite=True)
    
    # Copy OS VM files (only specified ones, or all if None)
    for f in os.listdir(os_dir):
        if f.endswith('.vm'):
            if os_files is None or f in os_files:
                shutil.copy(os.path.join(os_dir, f), temp_dir)
    
    return temp_dir


def analyze_parallelism(emitter, num_cores):
    """Analyze parallelism potential."""
    net = emitter.net
    net.allocate_memory(verbose=False)
    net.assign_cpu_cores(num_cores, verbose=False)
    
    # Group by level
    levels = {}
    for trans_name, level in net.transition_levels.items():
        if level not in levels:
            levels[level] = []
        levels[level].append(trans_name)
    
    # Calculate parallel cycles
    parallel_cycles = 0
    for level in sorted(levels.keys()):
        trans_at_level = levels[level]
        
        # Group by core
        core_work = {}
        for t in trans_at_level:
            core = net.cpu_assignments.get(t, 0)
            if core not in core_work:
                core_work[core] = 0
            core_work[core] += 1
        
        # Cycles = max work on any core
        max_work = max(core_work.values()) if core_work else 0
        parallel_cycles += max_work
    
    return parallel_cycles, len(levels)


def main():
    print("=" * 70)
    print("  Chapter 11: Average Program Analysis")
    print("=" * 70)
    
    project_dir = "tecs/projects/11/Average"
    os_dir = "tecs/tools/OS"
    
    if not os.path.exists(project_dir):
        print(f"\n  [ERROR] Project not found: {project_dir}")
        return 1
    
    temp_dir = None
    try:
        # Only include OS files that Average actually needs
        average_os_files = [
            'Sys.vm',      # Bootstrap
            'Keyboard.vm', # readInt
            'Array.vm',    # new
            'Memory.vm',   # alloc (used by Array)
            'Output.vm',   # printString, printInt, println
            'Math.vm',     # divide
            'String.vm',   # used by Output/Keyboard
        ]
        
        # Compile
        print(f"\n  Compiling Average program...")
        temp_dir = compile_project(project_dir, os_dir, average_os_files)
        
        # Count VM commands per file
        print(f"\n  VM Files:")
        total_commands = 0
        for f in sorted(os.listdir(temp_dir)):
            if f.endswith('.vm'):
                path = os.path.join(temp_dir, f)
                with open(path) as vf:
                    count = sum(1 for l in vf if l.strip() and not l.strip().startswith('//'))
                print(f"    {f:20} {count:5} commands")
                total_commands += count
        print(f"    {'TOTAL':20} {total_commands:5} commands")
        
        # Build Petri net
        print(f"\n  Building Petri net...")
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        print(f"    Places:      {len(net.places)}")
        print(f"    Transitions: {len(net.transitions)}")
        print(f"    Arcs:        {len(net.arcs)}")
        
        # Analyze parallelism for different core counts
        print(f"\n  Parallelism Analysis:")
        print(f"    {'Cores':<8} {'Cycles':<12} {'Levels':<10} {'Speedup':<10}")
        print(f"    {'-'*40}")
        
        baseline = None
        for num_cores in [1, 2, 4, 8, 16]:
            # Rebuild for fresh analysis
            parser = VMParser(temp_dir)
            emitter = parser.emitter
            
            cycles, levels = analyze_parallelism(emitter, num_cores)
            
            if baseline is None:
                baseline = cycles
            
            speedup = baseline / cycles if cycles > 0 else 1.0
            print(f"    {num_cores:<8} {cycles:<12} {levels:<10} {speedup:<10.2f}x")
        
        # Memory-mapped I/O info
        print(f"\n  Memory-Mapped I/O (Shared Resources):")
        print(f"    Screen:   16384-24575 (8K words)")
        print(f"    Keyboard: 24576 (1 word)")
        print(f"\n    All cores share these I/O addresses.")
        print(f"    Keyboard reads poll address 24576.")
        print(f"    Screen writes go to addresses 16384-24575.")
        
        # Program flow
        print(f"\n  Program Flow:")
        print(f"    1. Sys.init calls Main.main")
        print(f"    2. Main.main:")
        print(f"       - Keyboard.readInt('How many numbers?')")
        print(f"       - Array.new(length)")
        print(f"       - Loop: Keyboard.readInt for each number")
        print(f"       - Loop: Sum all numbers")
        print(f"       - Output.printString('The average is: ')")
        print(f"       - Output.printInt(sum / length)")
        
        # OS function breakdown
        print(f"\n  OS Functions Used:")
        os_funcs = {
            'Keyboard': ['init', 'keyPressed', 'readChar', 'readLine', 'readInt'],
            'Output': ['init', 'printChar', 'printString', 'printInt', 'println'],
            'Array': ['new', 'dispose'],
            'Memory': ['init', 'peek', 'poke', 'alloc', 'deAlloc'],
            'String': ['new', 'dispose', 'length', 'charAt', 'appendChar', 'intValue'],
            'Math': ['init', 'multiply', 'divide'],
            'Sys': ['init', 'halt', 'wait']
        }
        for module, funcs in os_funcs.items():
            print(f"    {module}: {', '.join(funcs)}")
        
        print(f"\n  [OK] Analysis complete")
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
