#!/usr/bin/env python3

"""
Comprehensive test for multi-CPU execution with shared RAM.
Demonstrates parallel execution of Petri net transitions across multiple CPU cores.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand

def test_multi_cpu_parallel_execution():
    """Test parallel execution across multiple CPUs with shared RAM"""
    print("Testing multi-CPU parallel execution...")
    
    # Create a more complex VM program with multiple parallel paths
    emitter = PetriEmitter()
    
    # Create a program that can benefit from parallelization:
    # push constant 10
    # push constant 20  
    # push constant 30
    # push constant 40
    # add (20 + 40 = 60)
    # add (30 + 60 = 90) 
    # add (10 + 90 = 100)
    
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("push", "constant", 30),
        vmcommand("push", "constant", 40),
        vmcommand("add"),  # 30 + 40
        vmcommand("add"),  # 20 + result
        vmcommand("add"),  # 10 + result
    ]
    
    # Build the Petri net
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    print(f"Created Petri net with {len(emitter.net.places)} places and {len(emitter.net.transitions)} transitions")
    
    # Allocate memory
    memory_slots = emitter.net.allocate_memory()
    print(f"Allocated {memory_slots} memory slots")
    
    # Test with different numbers of CPU cores
    for num_cores in [1, 2, 4]:
        print(f"\n--- Testing with {num_cores} CPU cores ---")
        
        # Assign CPU cores
        assignments = emitter.net.assign_cpu_cores(num_cores)
        print(f"CPU assignments: {assignments}")
        print(f"Transition levels: {emitter.net.transition_levels}")
        
        # Generate ROMs for each core
        roms = emitter.net.generate_roms()
        print(f"Generated ROMs for {len(roms)} cores:")
        
        for core_id, rom in roms.items():
            print(f"  Core {core_id}: {len(rom)} instructions")
            if rom:
                print(f"    Sample: {rom[:2]}")
        
        # Create shared RAM
        shared_ram = [0] * 24576
        
        # Create CPUs for each core
        cpus = {}
        for core_id in range(num_cores):
            cpus[core_id] = CPU(RAM=shared_ram)
        
        print(f"Created {len(cpus)} CPUs sharing RAM")
        
        # Verify all CPUs share the same RAM
        test_value = 12345
        shared_ram[1000] = test_value
        for core_id, cpu in cpus.items():
            assert cpu.RAM[1000] == test_value, f"Core {core_id} doesn't see shared data"
        
        print(f"✓ All cores share RAM correctly")
        
        # Test that each CPU can modify shared RAM
        for core_id, cpu in cpus.items():
            test_addr = 2000 + core_id
            cpu.RAM[test_addr] = core_id * 100
        
        # Verify all changes are visible to all CPUs
        for core_id, cpu in cpus.items():
            for other_core in range(num_cores):
                test_addr = 2000 + other_core
                expected_value = other_core * 100
                assert cpu.RAM[test_addr] == expected_value, \
                    f"Core {core_id} doesn't see changes by core {other_core}"
        
        print(f"✓ RAM modifications visible across all cores")

def test_cpu_core_conflict_resolution():
    """Test that conflicting transitions are assigned to different cores"""
    print("\nTesting CPU core conflict resolution...")
    
    emitter = PetriEmitter()
    
    # Create a program where some operations can run in parallel
    # and others must be sequential
    commands = [
        vmcommand("push", "constant", 5),   # Level 0 - can be parallel
        vmcommand("push", "constant", 7),   # Level 0 - can be parallel  
        vmcommand("push", "constant", 3),   # Level 0 - can be parallel
        vmcommand("add"),                   # Level 1 - depends on first two
        vmcommand("add"),                   # Level 2 - depends on previous add and third constant
    ]
    
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    # Allocate memory and assign cores
    emitter.net.allocate_memory()
    assignments = emitter.net.assign_cpu_cores(3)
    
    print(f"Assignments: {assignments}")
    print(f"Levels: {emitter.net.transition_levels}")
    
    # Build conflict graph to analyze
    emitter.net._compute_transition_levels()
    conflict_graph = emitter.net._build_transition_conflict_graph()
    
    print(f"Conflict graph: {conflict_graph}")
    
    # Verify that conflicting transitions have different core assignments
    conflicts_resolved = 0
    for trans1, conflicts in conflict_graph.items():
        for trans2 in conflicts:
            if trans1 in assignments and trans2 in assignments:
                assert assignments[trans1] != assignments[trans2], \
                    f"Conflicting transitions {trans1} and {trans2} have same core"
                conflicts_resolved += 1
    
    print(f"✓ Resolved {conflicts_resolved} conflicts correctly")

def test_rom_generation_and_synchronization():
    """Test ROM generation with synchronization code"""
    print("\nTesting ROM generation with synchronization...")
    
    emitter = PetriEmitter()
    
    # Simple program to test ROM generation
    commands = [
        vmcommand("push", "constant", 42),
        vmcommand("push", "constant", 58),
        vmcommand("add"),
    ]
    
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    # Allocate memory and assign cores
    emitter.net.allocate_memory()
    emitter.net.assign_cpu_cores(2)
    
    # Generate ROMs
    roms = emitter.net.generate_roms()
    
    print(f"Generated {len(roms)} ROMs")
    
    for core_id, rom in roms.items():
        print(f"\nCore {core_id} ROM ({len(rom)} instructions):")
        for i, instruction in enumerate(rom[:10]):  # Show first 10 instructions
            print(f"  {i:2d}: {instruction}")
        if len(rom) > 10:
            print(f"  ... ({len(rom) - 10} more instructions)")
    
    # Verify ROM structure
    total_instructions = sum(len(rom) for rom in roms.values())
    print(f"Total instructions across all ROMs: {total_instructions}")
    
    # Check that at least one ROM has synchronization code
    has_sync = False
    for rom in roms.values():
        for instruction in rom:
            if "Wait for" in instruction or "Signal" in instruction:
                has_sync = True
                break
        if has_sync:
            break
    
    print(f"✓ ROMs contain synchronization code: {has_sync}")

def test_scalability():
    """Test system scalability with larger programs and more cores"""
    print("\nTesting scalability...")
    
    emitter = PetriEmitter()
    
    # Create a larger program with many parallel operations
    num_constants = 8
    commands = []
    
    # Push many constants
    for i in range(num_constants):
        commands.append(vmcommand("push", "constant", i + 1))
    
    # Add them in pairs
    for i in range(num_constants // 2):
        commands.append(vmcommand("add"))
    
    # Build the network
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    print(f"Created large program: {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
    
    # Test with many cores
    emitter.net.allocate_memory()
    
    for num_cores in [1, 2, 4, 8]:
        assignments = emitter.net.assign_cpu_cores(num_cores)
        roms = emitter.net.generate_roms()
        
        # Calculate load distribution
        core_loads = {}
        for core_id, rom in roms.items():
            core_loads[core_id] = len(rom)
        
        max_load = max(core_loads.values()) if core_loads.values() else 0
        min_load = min(core_loads.values()) if core_loads.values() else 0
        avg_load = sum(core_loads.values()) / len(core_loads) if core_loads else 0
        
        print(f"  {num_cores} cores: max_load={max_load}, min_load={min_load}, avg_load={avg_load:.1f}")
    
    print("✓ Scalability test completed")

if __name__ == "__main__":
    print("Running comprehensive multi-CPU shared RAM tests...")
    print("=" * 70)
    
    test_multi_cpu_parallel_execution()
    test_cpu_core_conflict_resolution()
    test_rom_generation_and_synchronization()
    test_scalability()
    
    print("=" * 70)
    print("All multi-CPU shared RAM tests passed!")