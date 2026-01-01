#!/usr/bin/env python3

"""
Test CPU core assignment using graph coloring and shared RAM functionality.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand

def test_cpu_core_assignment():
    """Test that CPU cores are assigned using graph coloring"""
    print("Testing CPU core assignment...")
    
    # Create a simple VM program with parallel operations
    emitter = PetriEmitter()
    
    # Create operations that can run in parallel
    # push constant 5
    # push constant 3  
    # add
    # push constant 2
    # add
    
    cmd1 = vmcommand("push", "constant", 5)
    cmd2 = vmcommand("push", "constant", 3)
    cmd3 = vmcommand("add")
    cmd4 = vmcommand("push", "constant", 2)
    cmd5 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    emitter.push_constant(cmd4)
    emitter.add(cmd5)
    
    # Allocate memory
    emitter.net.allocate_memory()
    
    # Assign CPU cores (test with 2 cores)
    assignments = emitter.net.assign_cpu_cores(2)
    
    print(f"CPU assignments: {assignments}")
    print(f"Transition levels: {emitter.net.transition_levels}")
    
    # Verify that assignments were made
    assert len(assignments) == len(emitter.net.transitions)
    
    # Verify that all assignments are valid core numbers
    for trans_name, core in assignments.items():
        assert 0 <= core < 2, f"Invalid core assignment: {core}"
    
    print("✓ CPU core assignment test passed")

def test_generate_roms():
    """Test ROM generation for multiple CPU cores"""
    print("Testing ROM generation...")
    
    emitter = PetriEmitter()
    
    # Create a simple program
    cmd1 = vmcommand("push", "constant", 10)
    cmd2 = vmcommand("push", "constant", 20)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    
    # Allocate memory and assign cores
    emitter.net.allocate_memory()
    emitter.net.assign_cpu_cores(2)
    
    # Generate ROMs
    roms_result = emitter.net.generate_roms()
    
    # Extract core ROMs from the result structure
    core_roms = roms_result['cores']
    shared_rom = roms_result['shared']
    stats = roms_result['stats']
    
    print(f"Generated ROMs for {len(core_roms)} cores")
    print(f"Shared ROM: {len(shared_rom)} instructions")
    print(f"Stats: {stats}")
    
    for core, rom in core_roms.items():
        print(f"Core {core}: {len(rom)} instructions")
        if rom:
            print(f"  First few: {rom[:3]}")
    
    # Verify ROM structure
    assert 'cores' in roms_result, "Should have 'cores' key"
    assert 'shared' in roms_result, "Should have 'shared' key"
    assert 'stats' in roms_result, "Should have 'stats' key"
    assert all(isinstance(rom, list) for rom in core_roms.values()), "ROMs should be lists"
    
    print("✓ ROM generation test passed")

def test_shared_ram():
    """Test multiple CPUs sharing the same RAM"""
    print("Testing shared RAM functionality...")
    
    # Create shared RAM
    shared_ram = [0] * 24576
    shared_ram[100] = 42  # Put test value in RAM
    
    # Create two CPUs sharing the same RAM
    cpu1 = CPU(RAM=shared_ram)
    cpu2 = CPU(RAM=shared_ram)
    
    # Verify they share the same RAM object
    assert cpu1.RAM is cpu2.RAM, "CPUs should share the same RAM object"
    assert cpu1.RAM[100] == 42, "CPU1 should see shared data"
    assert cpu2.RAM[100] == 42, "CPU2 should see shared data"
    
    # Test that changes are visible to both CPUs
    cpu1.RAM[200] = 123
    assert cpu2.RAM[200] == 123, "Changes by CPU1 should be visible to CPU2"
    
    cpu2.RAM[300] = 456
    assert cpu1.RAM[300] == 456, "Changes by CPU2 should be visible to CPU1"
    
    print("✓ Shared RAM test passed")

def test_cpu_without_shared_ram():
    """Test CPU with its own RAM (not shared)"""
    print("Testing CPU with individual RAM...")
    
    # Create CPUs without shared RAM
    cpu1 = CPU()
    cpu2 = CPU()
    
    # Verify they have separate RAM
    assert cpu1.RAM is not cpu2.RAM, "CPUs should have separate RAM objects"
    assert len(cpu1.RAM) == 24576, "CPU1 should have full RAM"
    assert len(cpu2.RAM) == 24576, "CPU2 should have full RAM"
    
    # Test that changes are isolated
    cpu1.RAM[100] = 42
    cpu2.RAM[100] = 84
    
    assert cpu1.RAM[100] == 42, "CPU1 RAM should be isolated"
    assert cpu2.RAM[100] == 84, "CPU2 RAM should be isolated"
    
    print("✓ Individual RAM test passed")

def test_parallel_execution_simulation():
    """Test simulating parallel execution with multiple CPUs and shared RAM"""
    print("Testing parallel execution simulation...")
    
    # Create shared RAM
    shared_ram = [0] * 24576
    
    # Create a Petri net with parallel operations
    emitter = PetriEmitter()
    
    # Program: two parallel constant pushes followed by an add
    cmd1 = vmcommand("push", "constant", 15)
    cmd2 = vmcommand("push", "constant", 25)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    
    # Allocate memory and assign cores
    emitter.net.allocate_memory()
    assignments = emitter.net.assign_cpu_cores(2)
    roms = emitter.net.generate_roms()
    
    # Create CPUs for each core with shared RAM
    cpus = {}
    for core in range(2):
        cpus[core] = CPU(RAM=shared_ram)
    
    print(f"Created {len(cpus)} CPUs with shared RAM")
    print(f"Shared RAM size: {len(shared_ram)}")
    print(f"CPU assignments: {assignments}")
    
    # Verify setup
    assert len(cpus) == 2, "Should have 2 CPUs"
    for cpu in cpus.values():
        assert cpu.RAM is shared_ram, "All CPUs should share the same RAM"
    
    print("✓ Parallel execution simulation test passed")

def test_conflict_detection():
    """Test that conflicting transitions get different CPU cores"""
    print("Testing conflict detection...")
    
    emitter = PetriEmitter()
    
    # Create operations that will conflict (share resources)
    cmd1 = vmcommand("push", "constant", 1)
    cmd2 = vmcommand("push", "constant", 2)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)  # This will conflict with the pushes at the same level
    
    # Allocate memory and assign cores
    emitter.net.allocate_memory()
    assignments = emitter.net.assign_cpu_cores(3)
    
    # Build conflict graph to verify detection
    emitter.net._compute_transition_levels()
    conflict_graph = emitter.net._build_transition_conflict_graph()
    
    print(f"Conflict graph: {conflict_graph}")
    print(f"Assignments: {assignments}")
    
    # Verify that conflicting transitions have different cores
    for trans1, conflicts in conflict_graph.items():
        for trans2 in conflicts:
            if trans1 in assignments and trans2 in assignments:
                assert assignments[trans1] != assignments[trans2], \
                    f"Conflicting transitions {trans1} and {trans2} should have different cores"
    
    print("✓ Conflict detection test passed")

if __name__ == "__main__":
    print("Running CPU core assignment and shared RAM tests...")
    print("=" * 60)
    
    test_cpu_core_assignment()
    test_generate_roms()
    test_shared_ram()
    test_cpu_without_shared_ram()
    test_parallel_execution_simulation()
    test_conflict_detection()
    
    print("=" * 60)
    print("All CPU core assignment tests passed!")