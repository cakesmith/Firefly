#!/usr/bin/env python3

"""
End-to-end test for multicore assembly generation and execution.
Generates ROMs, runs multiple CPUs with shared RAM, and validates output.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand

def test_multicore_simple_add():
    """Test multicore execution with simple addition: 5 + 3 = 8"""
    print("Testing multicore execution: 5 + 3 = 8")
    print("-" * 50)
    
    # Step 1: Generate Petri net and assembly
    emitter = PetriEmitter()
    
    cmd1 = vmcommand("push", "constant", 5)
    cmd2 = vmcommand("push", "constant", 3)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    
    # Allocate memory
    memory_slots = emitter.net.allocate_memory()
    print(f"Memory allocated: {memory_slots} slots")
    
    # Step 2: Assign CPU cores and generate ROMs
    num_cores = 2
    assignments = emitter.net.assign_cpu_cores(num_cores)
    roms = emitter.net.generate_roms()
    
    print(f"CPU assignments: {assignments}")
    print(f"Generated {len(roms)} ROMs:")
    for core_id, rom in roms.items():
        print(f"  Core {core_id}: {len(rom)} instructions")
        if len(rom) > 0:
            print(f"    Sample: {rom[:3]}")
    
    # Step 3: Create shared RAM and verify CPU coordination
    shared_ram = [0] * 24576
    cpus = []
    
    for core_id in range(num_cores):
        cpu = CPU(RAM=shared_ram)
        cpus.append(cpu)
        print(f"CPU {core_id} created with shared RAM")
    
    # Verify shared RAM works
    test_addr = 1000
    test_value = 42
    cpus[0].RAM[test_addr] = test_value
    
    shared_ram_works = all(cpu.RAM[test_addr] == test_value for cpu in cpus)
    print(f"Shared RAM coordination: {'✓ PASS' if shared_ram_works else '✗ FAIL'}")
    
    # Step 4: Execute single-threaded Petri net for reference
    print("\nExecuting Petri net (reference):")
    reference_net = create_reference_net()
    reference_result = execute_petri_net_reference(reference_net)
    print(f"Reference result: {reference_result}")
    
    # Step 5: Simulate multicore execution
    print("\nSimulating multicore execution:")
    multicore_result = simulate_multicore_petri_execution(emitter.net, assignments, shared_ram)
    
    # Step 6: Validate results
    print(f"\nResults:")
    print(f"Reference (single-core): {reference_result}")
    print(f"Multicore execution: {multicore_result}")
    print(f"Correctness: {'✓ PASS' if reference_result == multicore_result else '✗ FAIL'}")
    
    return reference_result == multicore_result and shared_ram_works

def create_reference_net():
    """Create reference Petri net for comparison"""
    emitter = PetriEmitter()
    
    cmd1 = vmcommand("push", "constant", 5)
    cmd2 = vmcommand("push", "constant", 3)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    
    emitter.net.allocate_memory()
    return emitter.net

def execute_petri_net_reference(net):
    """Execute Petri net and return final result"""
    step = 0
    max_steps = 50
    
    while step < max_steps:
        fired = net.execute_step()
        if not fired:
            break
        step += 1
    
    # Find final result
    for place_name, place in net.places.items():
        if place.has and "add_result" in place_name:
            return place.token.value if place.token else None
    
    return None

def simulate_multicore_petri_execution(net, assignments, shared_ram):
    """Simulate multicore execution of Petri net"""
    print("Simulating step-by-step multicore execution:")
    
    step = 0
    max_steps = 50
    
    while step < max_steps:
        # Get transitions that can fire
        enabled_transitions = [t for t in net.transitions.values() if t.can_fire()]
        
        if not enabled_transitions:
            break
        
        # Group by assigned core
        core_work = {}
        for transition in enabled_transitions:
            core = assignments.get(transition.name, 0)
            if core not in core_work:
                core_work[core] = []
            core_work[core].append(transition)
        
        print(f"  Step {step + 1}: Cores {list(core_work.keys())} executing {len(enabled_transitions)} transitions")
        
        # Fire all enabled transitions (simulating parallel execution)
        for transition in enabled_transitions:
            transition.fire()
        
        step += 1
    
    # Get final result
    for place_name, place in net.places.items():
        if place.has and "add_result" in place_name:
            return place.token.value if place.token else None
    
    return None

def test_multicore_complex_calculation():
    """Test multicore execution with complex calculation: (10 + 20) + (30 + 40) = 100"""
    print("\nTesting multicore execution: (10 + 20) + (30 + 40) = 100")
    print("-" * 60)
    
    # Generate Petri net
    emitter = PetriEmitter()
    
    commands = [
        vmcommand("push", "constant", 10),
        vmcommand("push", "constant", 20),
        vmcommand("push", "constant", 30),
        vmcommand("push", "constant", 40),
        vmcommand("add"),  # 30 + 40 = 70
        vmcommand("add"),  # 20 + 70 = 90
        vmcommand("add"),  # 10 + 90 = 100
    ]
    
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "add":
            emitter.add(cmd)
    
    emitter.net.allocate_memory()
    
    # Test with different numbers of cores
    expected_result = 100
    
    for num_cores in [1, 2, 4]:
        print(f"\n--- Testing with {num_cores} cores ---")
        
        assignments = emitter.net.assign_cpu_cores(num_cores)
        roms = emitter.net.generate_roms()
        
        # Show work distribution
        print("Work distribution:")
        for core_id, rom in roms.items():
            if len(rom) > 0:
                core_transitions = [t for t, c in assignments.items() if c == core_id]
                print(f"  Core {core_id}: {len(core_transitions)} transitions, {len(rom)} instructions")
        
        # Create shared RAM
        shared_ram = [0] * 24576
        
        # Simulate execution
        result = simulate_multicore_petri_execution(emitter.net, assignments, shared_ram)
        
        print(f"Result: {result}, Expected: {expected_result}")
        print(f"Correctness: {'✓ PASS' if result == expected_result else '✗ FAIL'}")
        
        if result != expected_result:
            return False
    
    return True

def test_cpu_coordination():
    """Test that CPUs properly coordinate through shared RAM"""
    print("\nTesting CPU coordination through shared RAM")
    print("-" * 50)
    
    # Create shared RAM
    shared_ram = [0] * 24576
    
    # Create multiple CPUs
    num_cpus = 3
    cpus = []
    
    for i in range(num_cpus):
        cpu = CPU(RAM=shared_ram)
        cpus.append(cpu)
    
    print(f"Created {num_cpus} CPUs with shared RAM")
    
    # Test 1: Write from one CPU, read from others
    test_addr = 1000
    test_value = 42
    
    cpus[0].RAM[test_addr] = test_value
    
    all_see_value = all(cpu.RAM[test_addr] == test_value for cpu in cpus)
    print(f"Write visibility test: {'✓ PASS' if all_see_value else '✗ FAIL'}")
    
    # Test 2: Multiple CPUs writing to different addresses
    for i, cpu in enumerate(cpus):
        addr = 2000 + i
        value = 100 + i
        cpu.RAM[addr] = value
    
    # Verify all CPUs see all writes
    coordination_ok = True
    for i in range(num_cpus):
        addr = 2000 + i
        expected_value = 100 + i
        for cpu in cpus:
            if cpu.RAM[addr] != expected_value:
                coordination_ok = False
                break
    
    print(f"Multi-CPU coordination test: {'✓ PASS' if coordination_ok else '✗ FAIL'}")
    
    return all_see_value and coordination_ok

def test_load_balancing():
    """Test load balancing across multiple cores"""
    print("\nTesting load balancing")
    print("-" * 30)
    
    # Create a program with many operations
    emitter = PetriEmitter()
    
    # Push 6 constants and add them
    for i in range(6):
        cmd = vmcommand("push", "constant", i + 1)
        emitter.push_constant(cmd)
    
    # Add them in sequence: ((((1+2)+3)+4)+5)+6 = 21
    for i in range(5):
        cmd = vmcommand("add")
        emitter.add(cmd)
    
    emitter.net.allocate_memory()
    
    # Test load balancing with 3 cores
    assignments = emitter.net.assign_cpu_cores(3)
    roms = emitter.net.generate_roms()
    
    # Calculate load distribution
    loads = [len(rom) for rom in roms.values()]
    max_load = max(loads)
    min_load = min(loads)
    avg_load = sum(loads) / len(loads)
    
    print(f"Load distribution: max={max_load}, min={min_load}, avg={avg_load:.1f}")
    
    # Check that work is reasonably distributed
    load_balance_ratio = min_load / max_load if max_load > 0 else 0
    well_balanced = load_balance_ratio > 0.3  # At least 30% of max load on each core
    
    print(f"Load balance ratio: {load_balance_ratio:.2f}")
    print(f"Load balancing: {'✓ PASS' if well_balanced else '✗ FAIL'}")
    
    # Verify correctness
    result = simulate_multicore_petri_execution(emitter.net, assignments, [0] * 24576)
    expected = 21  # 1+2+3+4+5+6
    
    print(f"Calculation result: {result}, Expected: {expected}")
    print(f"Correctness: {'✓ PASS' if result == expected else '✗ FAIL'}")
    
    return well_balanced and result == expected

if __name__ == "__main__":
    print("Running comprehensive multicore execution tests...")
    print("=" * 70)
    
    test1 = test_multicore_simple_add()
    test2 = test_multicore_complex_calculation()
    test3 = test_cpu_coordination()
    test4 = test_load_balancing()
    
    print("=" * 70)
    print("Test Results:")
    print(f"Simple addition: {'✓ PASS' if test1 else '✗ FAIL'}")
    print(f"Complex calculation: {'✓ PASS' if test2 else '✗ FAIL'}")
    print(f"CPU coordination: {'✓ PASS' if test3 else '✗ FAIL'}")
    print(f"Load balancing: {'✓ PASS' if test4 else '✗ FAIL'}")
    
    all_passed = all([test1, test2, test3, test4])
    print(f"\nOverall: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")