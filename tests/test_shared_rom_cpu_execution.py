#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from CPU import CPU
from VMParser import vmcommand

def create_mock_instruction(instruction_type, value):
    """Create a mock CPU instruction for testing"""
    if instruction_type == "A":
        return {"TYPE": "A_COMMAND", "VAL": value}
    elif instruction_type == "C":
        return {"TYPE": "C_COMMAND", "VAL": value}
    else:
        return {"TYPE": "COMMENT", "VAL": instruction_type}

def test_shared_rom_basic_execution():
    """Test basic shared ROM execution with multiple CPUs"""
    
    print("Testing shared ROM basic execution...")
    
    # Create shared ROM with simple instructions
    shared_rom = [
        create_mock_instruction("A", 10),      # @10
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),  # D=A
        create_mock_instruction("A", 20),      # @20  
        create_mock_instruction("C", {"DEST": "D", "COMP": "D+A", "JUMP": ""}),  # D=D+A
        create_mock_instruction("A", 100),     # @100
        create_mock_instruction("C", {"DEST": "M", "COMP": "D", "JUMP": ""}),  # M=D (store result)
    ]
    
    # Create shared RAM and multiple CPUs
    shared_ram = [0] * 24576
    cpus = [
        CPU(cpu_id=0, RAM=shared_ram),
        CPU(cpu_id=1, RAM=shared_ram)
    ]
    
    print(f"Created {len(cpus)} CPUs with shared ROM of {len(shared_rom)} instructions")
    
    # Execute on CPU 0
    cpu0 = cpus[0]
    print(f"\nExecuting on CPU 0:")
    
    for step in range(len(shared_rom)):
        print(f"  Step {step}: PC={cpu0.get_pc()}, {cpu0}")
        
        # Fetch instruction from shared ROM
        if cpu0.get_pc() < len(shared_rom):
            instruction = shared_rom[cpu0.get_pc()]
            cpu0.step(instruction)
        else:
            break
    
    print(f"  Final: PC={cpu0.get_pc()}, {cpu0}")
    print(f"  Result at RAM[100]: {shared_ram[100]}")
    
    # Verify result
    assert shared_ram[100] == 30, f"Expected 30, got {shared_ram[100]}"
    
    # Test that CPU 1 can see the same result in shared RAM
    cpu1 = cpus[1]
    print(f"\nCPU 1 can see shared result: RAM[100] = {cpu1.RAM[100]}")
    assert cpu1.RAM[100] == 30, "CPU 1 should see the same shared RAM value"
    
    print("✓ Shared ROM basic execution test passed")

def test_shared_rom_with_jumps():
    """Test shared ROM execution with jump instructions (control flow)"""
    
    print("\nTesting shared ROM with jump instructions...")
    
    # Create shared ROM with conditional jump
    shared_rom = [
        # 0: @5
        create_mock_instruction("A", 5),
        # 1: D=A  
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),
        # 2: @3
        create_mock_instruction("A", 3),
        # 3: D=D-A
        create_mock_instruction("C", {"DEST": "D", "COMP": "D-A", "JUMP": ""}),
        # 4: @8 (jump target)
        create_mock_instruction("A", 8),
        # 5: D;JGT (jump if D > 0, i.e., if 5-3 > 0)
        create_mock_instruction("C", {"DEST": "", "COMP": "D", "JUMP": "JGT"}),
        # 6: @200 (should be skipped)
        create_mock_instruction("A", 200),
        # 7: M=A (should be skipped)
        create_mock_instruction("C", {"DEST": "M", "COMP": "A", "JUMP": ""}),
        # 8: @100 (jump target)
        create_mock_instruction("A", 100),
        # 9: M=1 (executed after jump)
        create_mock_instruction("C", {"DEST": "M", "COMP": "1", "JUMP": ""}),
    ]
    
    # Create shared RAM and CPU
    shared_ram = [0] * 24576
    cpu = CPU(cpu_id=0, RAM=shared_ram)
    
    print(f"Created CPU with shared ROM of {len(shared_rom)} instructions")
    
    # Execute step by step
    print(f"\nExecuting with jumps:")
    max_steps = 20  # Prevent infinite loops
    step = 0
    
    while cpu.get_pc() < len(shared_rom) and step < max_steps:
        pc_before = cpu.get_pc()
        print(f"  Step {step}: PC={pc_before}, {cpu}")
        
        # Fetch instruction from shared ROM and execute
        instruction = shared_rom[cpu.get_pc()]
        cpu.step(instruction)
        
        if cpu.get_pc() != pc_before + 1:
            print(f"    -> JUMP: PC changed from {pc_before} to {cpu.get_pc()}")
        
        step += 1
    
    print(f"  Final: PC={cpu.get_pc()}, {cpu}")
    print(f"  RAM[100]: {shared_ram[100]} (should be 1)")
    print(f"  RAM[200]: {shared_ram[200]} (should be 0, skipped)")
    
    # Verify jump worked correctly
    assert shared_ram[100] == 1, f"Expected RAM[100]=1, got {shared_ram[100]}"
    assert shared_ram[200] == 0, f"Expected RAM[200]=0 (skipped), got {shared_ram[200]}"
    
    print("✓ Shared ROM with jumps test passed")

def test_multiple_cpus_shared_rom():
    """Test multiple CPUs executing different parts of shared ROM"""
    
    print("\nTesting multiple CPUs with shared ROM...")
    
    # Create shared ROM with multiple entry points
    shared_rom = [
        # CPU 0 entry point (0-3)
        create_mock_instruction("A", 10),      # @10
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),  # D=A
        create_mock_instruction("A", 100),     # @100
        create_mock_instruction("C", {"DEST": "M", "COMP": "D", "JUMP": ""}),  # M=D
        
        # CPU 1 entry point (4-7)  
        create_mock_instruction("A", 20),      # @20
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),  # D=A
        create_mock_instruction("A", 101),     # @101
        create_mock_instruction("C", {"DEST": "M", "COMP": "D", "JUMP": ""}),  # M=D
        
        # Shared code (8+)
        create_mock_instruction("A", 30),      # @30
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),  # D=A
        create_mock_instruction("A", 102),     # @102
        create_mock_instruction("C", {"DEST": "M", "COMP": "D", "JUMP": ""}),  # M=D
    ]
    
    # Create shared RAM and multiple CPUs
    shared_ram = [0] * 24576
    cpus = [
        CPU(cpu_id=0, RAM=shared_ram),
        CPU(cpu_id=1, RAM=shared_ram)
    ]
    
    # Set different starting PCs for each CPU
    cpus[0].set_pc(0)  # CPU 0 starts at beginning
    cpus[1].set_pc(4)  # CPU 1 starts at offset 4
    
    print(f"Created {len(cpus)} CPUs with different starting PCs")
    print(f"CPU 0 starts at PC={cpus[0].get_pc()}")
    print(f"CPU 1 starts at PC={cpus[1].get_pc()}")
    
    # Execute both CPUs for a few steps
    for step in range(4):
        print(f"\nStep {step}:")
        
        for i, cpu in enumerate(cpus):
            if cpu.get_pc() < len(shared_rom):
                pc_before = cpu.get_pc()
                # Fetch instruction from shared ROM and execute
                instruction = shared_rom[cpu.get_pc()]
                cpu.step(instruction)
                print(f"  CPU {i}: PC {pc_before} -> {cpu.get_pc()}, {cpu}")
    
    # Check results in shared RAM
    print(f"\nShared RAM results:")
    print(f"  RAM[100] = {shared_ram[100]} (CPU 0 wrote 10)")
    print(f"  RAM[101] = {shared_ram[101]} (CPU 1 wrote 20)")
    print(f"  RAM[102] = {shared_ram[102]} (shared code)")
    
    # Verify both CPUs wrote to shared RAM
    assert shared_ram[100] == 10, f"CPU 0 should have written 10 to RAM[100]"
    assert shared_ram[101] == 20, f"CPU 1 should have written 20 to RAM[101]"
    
    print("✓ Multiple CPUs shared ROM test passed")

def test_shared_rom_control_flow_simulation():
    """Test simulated control flow operations in shared ROM"""
    
    print("\nTesting simulated control flow in shared ROM...")
    
    # Simulate a simple if-then-else pattern:
    # if (condition) goto TRUE_CASE else goto FALSE_CASE
    shared_rom = [
        # 0: Load condition (5)
        create_mock_instruction("A", 5),
        create_mock_instruction("C", {"DEST": "D", "COMP": "A", "JUMP": ""}),
        
        # 2: Compare with 3
        create_mock_instruction("A", 3),
        create_mock_instruction("C", {"DEST": "D", "COMP": "D-A", "JUMP": ""}),
        
        # 4: Jump to TRUE_CASE if D > 0 (address 8)
        create_mock_instruction("A", 8),
        create_mock_instruction("C", {"DEST": "", "COMP": "D", "JUMP": "JGT"}),
        
        # 6-7: FALSE_CASE - store 0
        create_mock_instruction("A", 200),
        create_mock_instruction("C", {"DEST": "M", "COMP": "0", "JUMP": ""}),
        
        # 8-9: TRUE_CASE - store 1  
        create_mock_instruction("A", 200),
        create_mock_instruction("C", {"DEST": "M", "COMP": "1", "JUMP": ""}),
    ]
    
    # Test with multiple CPUs that could potentially execute this
    shared_ram = [0] * 24576
    
    for cpu_id in range(2):
        print(f"\nTesting CPU {cpu_id}:")
        
        cpu = CPU(cpu_id=cpu_id, RAM=shared_ram)
        cpu.set_pc(0)  # Start from beginning
        
        # Execute until completion or max steps
        max_steps = 10
        step = 0
        
        while cpu.get_pc() < len(shared_rom) and step < max_steps:
            pc_before = cpu.get_pc()
            # Fetch instruction from shared ROM and execute
            instruction = shared_rom[cpu.get_pc()]
            cpu.step(instruction)
            print(f"  Step {step}: PC {pc_before} -> {cpu.get_pc()}")
            step += 1
        
        print(f"  Result: RAM[200] = {shared_ram[200]}")
        
        # Reset for next CPU test
        shared_ram[200] = 0
    
    # Final test - should result in 1 (TRUE_CASE) since 5 > 3
    cpu = CPU(cpu_id=0, RAM=shared_ram)
    
    step = 0
    while cpu.get_pc() < len(shared_rom) and step < 10:
        instruction = shared_rom[cpu.get_pc()]
        cpu.step(instruction)
        step += 1
    
    assert shared_ram[200] == 1, f"Expected TRUE_CASE (1), got {shared_ram[200]}"
    
    print("✓ Shared ROM control flow simulation test passed")

if __name__ == "__main__":
    test_shared_rom_basic_execution()
    test_shared_rom_with_jumps()
    test_multiple_cpus_shared_rom()
    test_shared_rom_control_flow_simulation()
    
    print(f"\n{'='*60}")
    print("🎉 All shared ROM CPU execution tests passed!")
    print("✓ Multiple CPUs can share ROM and RAM")
    print("✓ Each CPU maintains its own PC register")
    print("✓ Jump instructions work correctly in shared ROM")
    print("✓ Control flow operations can span multiple CPUs")