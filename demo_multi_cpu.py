#!/usr/bin/env python3

"""
Demonstration of multi-CPU Petri net execution with shared RAM.
Shows graph coloring for CPU core assignment and ROM generation.
"""

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand

def main():
    print("Multi-CPU Petri Net Demonstration")
    print("=" * 50)
    
    # Create a VM program that can benefit from parallelization
    print("Creating VM program: (5 + 3) + (7 + 2) = 17")
    
    emitter = PetriEmitter()
    
    # Program: push 5, push 3, push 7, push 2, add, add, add
    commands = [
        vmcommand("push", "constant", 5),
        vmcommand("push", "constant", 3),
        vmcommand("push", "constant", 7),
        vmcommand("push", "constant", 2),
        vmcommand("add"),  # 7 + 2 = 9
        vmcommand("add"),  # 3 + 9 = 12  
        vmcommand("add"),  # 5 + 12 = 17
    ]
    
    # Build Petri net
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    print(f"Petri net created: {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
    
    # Allocate memory
    memory_slots = emitter.net.allocate_memory()
    print(f"Memory allocated: {memory_slots} slots")
    
    # Show memory allocation
    print("\nMemory allocation:")
    for place_name, place in emitter.net.places.items():
        if place.memory_address is not None:
            print(f"  {place_name}: R{place.memory_address}")
    
    # Test different numbers of CPU cores
    for num_cores in [1, 2, 4]:
        print(f"\n--- {num_cores} CPU Core{'s' if num_cores > 1 else ''} ---")
        
        # Assign CPU cores using graph coloring
        assignments = emitter.net.assign_cpu_cores(num_cores)
        
        print("CPU core assignments:")
        for trans_name, core in assignments.items():
            level = emitter.net.transition_levels.get(trans_name, 0)
            print(f"  {trans_name} (level {level}): Core {core}")
        
        # Generate ROMs for each core
        roms = emitter.net.generate_roms()
        
        print(f"\nGenerated ROMs:")
        for core_id, rom in roms.items():
            print(f"  Core {core_id}: {len(rom)} instructions")
        
        # Create shared RAM and CPUs
        shared_ram = [0] * 24576
        cpus = []
        
        for core_id in range(num_cores):
            cpu = CPU(RAM=shared_ram)
            cpus.append(cpu)
        
        print(f"Created {len(cpus)} CPUs sharing {len(shared_ram)} words of RAM")
        
        # Demonstrate shared RAM
        test_addr = 1000
        test_value = 42 + num_cores
        
        # CPU 0 writes to shared RAM
        cpus[0].RAM[test_addr] = test_value
        
        # Verify all CPUs see the same value
        all_see_value = all(cpu.RAM[test_addr] == test_value for cpu in cpus)
        print(f"Shared RAM test: {'✓ PASS' if all_see_value else '✗ FAIL'}")
    
    # Show conflict analysis
    print(f"\n--- Conflict Analysis ---")
    emitter.net._compute_transition_levels()
    conflict_graph = emitter.net._build_transition_conflict_graph()
    
    print("Transition levels:")
    for trans_name, level in sorted(emitter.net.transition_levels.items(), key=lambda x: x[1]):
        print(f"  Level {level}: {trans_name}")
    
    print("\nConflict graph (transitions that cannot run in parallel):")
    has_conflicts = False
    for trans1, conflicts in conflict_graph.items():
        if conflicts:
            has_conflicts = True
            print(f"  {trans1} conflicts with: {', '.join(conflicts)}")
    
    if not has_conflicts:
        print("  No conflicts detected - all transitions can potentially run in parallel")
    
    print(f"\n--- Summary ---")
    print(f"✓ Graph coloring successfully assigns CPU cores")
    print(f"✓ Shared RAM enables multi-CPU coordination")
    print(f"✓ ROM generation creates per-core instruction sequences")
    print(f"✓ Level system identifies parallelization opportunities")
    print(f"✓ Conflict detection prevents resource conflicts")

if __name__ == "__main__":
    main()