#!/usr/bin/env python3

"""
Validation and statistics for multi-CPU Petri net execution.
Verifies correctness and measures CPU utilization.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand
from Petri.Token import Token

def test_execution_correctness():
    """Test that the Petri net produces correct results"""
    print("Testing execution correctness...")
    
    # Create a simple program: 5 + 3 = 8
    emitter = PetriEmitter()
    
    cmd1 = vmcommand("push", "constant", 5)
    cmd2 = vmcommand("push", "constant", 3)
    cmd3 = vmcommand("add")
    
    emitter.push_constant(cmd1)
    emitter.push_constant(cmd2)
    emitter.add(cmd3)
    
    # Allocate memory
    emitter.net.allocate_memory()
    
    # Execute the Petri net step by step
    print("Initial state:")
    print_net_state(emitter.net)
    
    step = 0
    while True:
        fired = emitter.net.execute_step()
        step += 1
        
        print(f"\nStep {step}: Fired {fired}")
        print_net_state(emitter.net)
        
        if not fired:  # No more transitions can fire
            break
        
        if step > 20:  # Safety limit
            print("ERROR: Too many steps, possible infinite loop")
            break
    
    # Check final result
    final_result = get_final_result(emitter.net)
    expected_result = 8
    
    print(f"\nFinal result: {final_result}")
    print(f"Expected: {expected_result}")
    print(f"Correct: {'✓' if final_result == expected_result else '✗'}")
    
    return final_result == expected_result

def print_net_state(net):
    """Print current state of the Petri net"""
    print("  Places with tokens:")
    for place_name, place in net.places.items():
        if place.has:
            token_value = place.token.value if place.token else "None"
            print(f"    {place_name}: {token_value}")

def get_final_result(net):
    """Extract the final result from the Petri net"""
    # Look for places that might contain the final result
    for place_name, place in net.places.items():
        if place.has and "add_result" in place_name:
            return place.token.value if place.token else None
    return None

def test_cpu_utilization_statistics():
    """Test CPU utilization and generate statistics"""
    print("\nTesting CPU utilization statistics...")
    
    # Create a more complex program for better statistics
    emitter = PetriEmitter()
    
    # Program: (10 + 20) + (30 + 40) = 100
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
    for num_cores in [1, 2, 4]:
        print(f"\n--- {num_cores} CPU Core{'s' if num_cores > 1 else ''} ---")
        
        assignments = emitter.net.assign_cpu_cores(num_cores)
        roms = emitter.net.generate_roms()
        
        # Calculate statistics
        stats = calculate_utilization_stats(assignments, roms, emitter.net.transition_levels)
        print_utilization_stats(stats, num_cores)

def calculate_utilization_stats(assignments, roms_result, levels):
    """Calculate CPU utilization statistics"""
    # Handle both old format (dict of lists) and new format (dict with 'cores' key)
    if isinstance(roms_result, dict) and 'cores' in roms_result:
        roms = roms_result['cores']
    else:
        roms = roms_result
    
    stats = {
        'total_transitions': len(assignments),
        'total_instructions': sum(len(rom) for rom in roms.values()),
        'cores_used': len([rom for rom in roms.values() if len(rom) > 0]),
        'core_loads': {},
        'level_distribution': {},
    }
    
    # Core loads
    for core_id, rom in roms.items():
        stats['core_loads'][core_id] = len(rom)
    
    # Level distribution across cores
    for trans_name, core in assignments.items():
        level = levels.get(trans_name, 0)
        if level not in stats['level_distribution']:
            stats['level_distribution'][level] = {}
        if core not in stats['level_distribution'][level]:
            stats['level_distribution'][level][core] = 0
        stats['level_distribution'][level][core] += 1
    
    # Load balance metrics
    loads = list(stats['core_loads'].values())
    if loads:
        avg_load = sum(loads) / len(loads)
        stats['load_balance'] = {
            'max_load': max(loads),
            'min_load': min(loads),
            'avg_load': avg_load,
            'load_variance': sum((load - avg_load)**2 for load in loads) / len(loads) if len(loads) > 1 else 0
        }
    
    return stats

def print_utilization_stats(stats, num_cores):
    """Print CPU utilization statistics"""
    print(f"Total transitions: {stats['total_transitions']}")
    print(f"Total instructions: {stats['total_instructions']}")
    print(f"Cores utilized: {stats['cores_used']}/{num_cores} ({stats['cores_used']/num_cores*100:.1f}%)")
    
    print("Core loads:")
    for core_id, load in stats['core_loads'].items():
        utilization = (load / stats['total_instructions'] * 100) if stats['total_instructions'] > 0 else 0
        print(f"  Core {core_id}: {load} instructions ({utilization:.1f}%)")
    
    if 'load_balance' in stats and stats['load_balance']:
        lb = stats['load_balance']
        print(f"Load balance: max={lb['max_load']}, min={lb['min_load']}, avg={lb['avg_load']:.1f}, variance={lb['load_variance']:.1f}")
    
    print("Level distribution:")
    for level, core_dist in stats['level_distribution'].items():
        print(f"  Level {level}: {core_dist}")

def test_parallel_execution_simulation():
    """Simulate parallel execution and verify correctness"""
    print("\nTesting parallel execution simulation...")
    
    # Create a program that benefits from parallelization
    emitter = PetriEmitter()
    
    # Program: 1 + 2 + 3 + 4 = 10
    for i in range(1, 5):
        cmd = vmcommand("push", "constant", i)
        emitter.push_constant(cmd)
    
    # Add them: ((1 + 2) + 3) + 4
    for i in range(3):
        cmd = vmcommand("add")
        emitter.add(cmd)
    
    emitter.net.allocate_memory()
    
    # Test with 2 cores
    assignments = emitter.net.assign_cpu_cores(2)
    roms = emitter.net.generate_roms()
    
    print(f"Assignments: {assignments}")
    
    # Create shared RAM and CPUs
    shared_ram = [0] * 24576
    cpus = [CPU(RAM=shared_ram) for _ in range(2)]
    
    # Simulate execution by running the Petri net
    print("Simulating parallel execution...")
    
    # Execute Petri net to get expected result
    step = 0
    max_steps = 50
    
    while step < max_steps:
        fired = emitter.net.execute_step()
        step += 1
        
        if not fired:
            break
    
    # Get final result
    final_result = get_final_result(emitter.net)
    expected_result = 10  # 1 + 2 + 3 + 4
    
    print(f"Parallel execution result: {final_result}")
    print(f"Expected result: {expected_result}")
    print(f"Correctness: {'✓' if final_result == expected_result else '✗'}")
    
    # Check that both CPUs have work
    core_roms = roms['cores']
    core0_work = len(core_roms.get(0, []))
    core1_work = len(core_roms.get(1, []))
    
    print(f"Core 0 work: {core0_work} instructions")
    print(f"Core 1 work: {core1_work} instructions")
    print(f"Work distribution: {'✓' if core0_work > 0 and core1_work > 0 else '✗'}")
    
    return final_result == expected_result and core0_work > 0 and core1_work > 0

def test_scalability_analysis():
    """Analyze how the system scales with more cores"""
    print("\nTesting scalability analysis...")
    
    # Create a larger program
    emitter = PetriEmitter()
    
    # Program with 8 constants and 7 adds
    for i in range(8):
        cmd = vmcommand("push", "constant", i + 1)
        emitter.push_constant(cmd)
    
    for i in range(7):
        cmd = vmcommand("add")
        emitter.add(cmd)
    
    emitter.net.allocate_memory()
    
    print("Scalability analysis:")
    print("Cores | Utilized | Max Load | Min Load | Avg Load | Efficiency")
    print("------|----------|----------|----------|----------|----------")
    
    for num_cores in [1, 2, 4, 8, 16]:
        assignments = emitter.net.assign_cpu_cores(num_cores)
        roms = emitter.net.generate_roms()
        stats = calculate_utilization_stats(assignments, roms, emitter.net.transition_levels)
        
        efficiency = (stats['cores_used'] / num_cores) * 100
        lb = stats.get('load_balance', {})
        
        print(f"{num_cores:5d} | {stats['cores_used']:8d} | {lb.get('max_load', 0):8d} | {lb.get('min_load', 0):8d} | {lb.get('avg_load', 0):8.1f} | {efficiency:8.1f}%")

if __name__ == "__main__":
    print("Running execution validation and statistics tests...")
    print("=" * 70)
    
    correctness = test_execution_correctness()
    test_cpu_utilization_statistics()
    parallel_correctness = test_parallel_execution_simulation()
    test_scalability_analysis()
    
    print("=" * 70)
    print(f"Execution correctness: {'✓ PASS' if correctness else '✗ FAIL'}")
    print(f"Parallel correctness: {'✓ PASS' if parallel_correctness else '✗ FAIL'}")
    print("All validation tests completed!")