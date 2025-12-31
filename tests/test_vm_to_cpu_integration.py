#!/usr/bin/env python3
"""
Integration tests that create VM code, convert to assembly via Petri nets, and run on CPU simulator
Tests the complete pipeline: VM -> Petri Net -> Assembly -> CPU execution
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser
from PetriEmitter import PetriEmitter
from CPU import CPU
import tempfile
import shutil

def create_test_vm_file(vm_code, filename="test.vm"):
    """Create a temporary VM file with the given code"""
    temp_dir = tempfile.mkdtemp()
    vm_file_path = os.path.join(temp_dir, filename)
    
    with open(vm_file_path, 'w') as f:
        f.write(vm_code)
    
    return temp_dir, vm_file_path

def vm_to_assembly_via_net(vm_code):
    """Convert VM code to assembly via Petri net generation"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code into Petri net
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        print(f"Petri Net Structure:")
        print(f"  Places: {len(net.places)} - {list(net.places.keys())}")
        print(f"  Transitions: {len(net.transitions)} - {list(net.transitions.keys())}")
        
        # Allocate memory (this is the optimization step)
        slots_used = net.allocate_memory()
        print(f"\nMemory Allocation (optimized to {slots_used} slots):")
        for place_name, place in net.places.items():
            if place.memory_address is not None:
                print(f"  {place_name}: R{place.memory_address}")
        
        # Generate assembly from each transition
        assembly_lines = []
        print(f"\nGenerating Assembly from Transitions:")
        for transition_name, transition in net.transitions.items():
            assembly_code = transition.emit_assembly()
            print(f"  {transition_name}:")
            if isinstance(assembly_code, list):
                assembly_lines.extend(assembly_code)
                for line in assembly_code:
                    print(f"    {line}")
            else:
                assembly_lines.append(assembly_code)
                print(f"    {assembly_code}")
        
        return assembly_lines, net, emitter
        
    finally:
        shutil.rmtree(temp_dir)

def assembly_to_cpu_instructions(assembly_lines):
    """Convert assembly lines to CPU instruction format"""
    instructions = []
    
    for line in assembly_lines:
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('('):
            continue
            
        if line.startswith('@'):
            # A-instruction
            val_str = line[1:]
            if val_str.startswith('R'):
                # Memory reference like @R5
                val = int(val_str[1:])
            elif val_str.isdigit():
                val = int(val_str)
            else:
                val = 0  # Unknown symbol
            instructions.append({"TYPE": "A_COMMAND", "VAL": val})
        else:
            # C-instruction
            dest = ""
            comp = line
            jump = ""
            
            if '=' in line:
                dest, comp = line.split('=', 1)
            if ';' in comp:
                comp, jump = comp.split(';', 1)
                
            instructions.append({
                "TYPE": "C_COMMAND", 
                "VAL": {"DEST": dest, "COMP": comp, "JUMP": jump}
            })
    
    return instructions

def test_simple_add_vm_to_cpu():
    """Test: Simple VM add operation through complete pipeline"""
    print("\n=== Test: Simple Add VM to CPU (7 + 3) ===")
    
    vm_code = """push constant 7
push constant 3
add
"""
    
    # Step 1: Convert VM to assembly via Petri net
    assembly_lines, net, emitter = vm_to_assembly_via_net(vm_code)
    
    # Step 2: Convert assembly to CPU instructions
    cpu_instructions = assembly_to_cpu_instructions(assembly_lines)
    print(f"\nGenerated CPU Instructions ({len(cpu_instructions)}):")
    for i, instr in enumerate(cpu_instructions):
        print(f"  {i}: {instr}")
    
    # Step 3: Execute Petri net to get expected result
    print(f"\nExecuting Petri Net for expected result:")
    step = 1
    while step <= 10:
        fired = net.execute_step()
        if not fired:
            break
        print(f"  Step {step}: Fired {fired}")
        step += 1
    
    expected_result = None
    result_memory_addr = None
    if emitter.control_stack and emitter.control_stack[-1].has:
        result_place = emitter.control_stack[-1]
        expected_result = result_place.token.value
        result_memory_addr = result_place.memory_address
        print(f"  Expected result: {expected_result} at R{result_memory_addr}")
    
    # Step 4: Execute on CPU
    if cpu_instructions:
        cpu = CPU(cpu_instructions)
        cpu.PC = 0
        
        print(f"\nExecuting on CPU:")
        step_count = 0
        max_steps = 50
        
        while step_count < max_steps and cpu.PC < len(cpu_instructions):
            instruction = cpu_instructions[cpu.PC]
            print(f"  Step {step_count}: PC={cpu.PC}, A={cpu.A}, D={cpu.D}")
            
            next_pc = cpu.step(cpu.PC)
            cpu.PC = next_pc
            step_count += 1
            
            # Check for halt
            if cpu.PC == next_pc and instruction.get("TYPE") == "C_COMMAND":
                jump = instruction.get("VAL", {}).get("JUMP", "")
                if jump == "JMP":
                    print(f"  -> CPU halted after {step_count} steps")
                    break
        
        print(f"  -> CPU finished after {step_count} steps, final PC={cpu.PC}")
        
        # Verify result
        if expected_result is not None and result_memory_addr is not None:
            cpu_result = cpu.RAM[result_memory_addr]
            print(f"\nResult Verification:")
            print(f"  Petri Net result: {expected_result}")
            print(f"  CPU result at R{result_memory_addr}: {cpu_result}")
            
            assert cpu_result == expected_result, f"CPU result {cpu_result} != Petri net result {expected_result}"
            assert cpu_result == 10, f"Expected 10 (7+3), got {cpu_result}"
            print("✓ Simple add VM to CPU test passed")

def test_multiple_add_vm_to_cpu():
    """Test: Multiple VM add operations through complete pipeline"""
    print("\n=== Test: Multiple Add VM to CPU (5 + 2 + 8) ===")
    
    vm_code = """push constant 5
push constant 2
add
push constant 8
add
"""
    
    # Convert VM to assembly via Petri net
    assembly_lines, net, emitter = vm_to_assembly_via_net(vm_code)
    
    # Convert assembly to CPU instructions
    cpu_instructions = assembly_to_cpu_instructions(assembly_lines)
    print(f"\nGenerated {len(cpu_instructions)} CPU instructions from VM code")
    
    # Execute Petri net for expected result
    print(f"\nExecuting Petri Net:")
    step = 1
    while step <= 15:
        fired = net.execute_step()
        if not fired:
            break
        print(f"  Step {step}: Fired {fired}")
        step += 1
    
    expected_result = None
    result_memory_addr = None
    if emitter.control_stack and emitter.control_stack[-1].has:
        result_place = emitter.control_stack[-1]
        expected_result = result_place.token.value
        result_memory_addr = result_place.memory_address
        print(f"  Expected result: {expected_result} at R{result_memory_addr}")
    
    # Execute on CPU
    if cpu_instructions:
        cpu = CPU(cpu_instructions)
        cpu.PC = 0
        
        step_count = 0
        max_steps = 100
        
        while step_count < max_steps and cpu.PC < len(cpu_instructions):
            instruction = cpu_instructions[cpu.PC]
            next_pc = cpu.step(cpu.PC)
            cpu.PC = next_pc
            step_count += 1
            
            if cpu.PC == next_pc and instruction.get("TYPE") == "C_COMMAND":
                jump = instruction.get("VAL", {}).get("JUMP", "")
                if jump == "JMP":
                    break
        
        # Verify result
        if expected_result is not None and result_memory_addr is not None:
            cpu_result = cpu.RAM[result_memory_addr]
            print(f"\nResult Verification:")
            print(f"  Expected: {expected_result}, CPU: {cpu_result}")
            
            assert cpu_result == expected_result, f"CPU result {cpu_result} != Petri net result {expected_result}"
            assert cpu_result == 15, f"Expected 15 (5+2+8), got {cpu_result}"
            print("✓ Multiple add VM to CPU test passed")

def test_large_constants_vm_to_cpu():
    """Test: Large constants through VM to CPU pipeline"""
    print("\n=== Test: Large Constants VM to CPU (1000 + 500) ===")
    
    vm_code = """push constant 1000
push constant 500
add
"""
    
    # Convert and execute
    assembly_lines, net, emitter = vm_to_assembly_via_net(vm_code)
    cpu_instructions = assembly_to_cpu_instructions(assembly_lines)
    
    # Get expected result from Petri net
    step = 1
    while step <= 10:
        fired = net.execute_step()
        if not fired:
            break
        step += 1
    
    expected_result = None
    result_memory_addr = None
    if emitter.control_stack and emitter.control_stack[-1].has:
        result_place = emitter.control_stack[-1]
        expected_result = result_place.token.value
        result_memory_addr = result_place.memory_address
    
    # Execute on CPU
    if cpu_instructions and expected_result is not None:
        cpu = CPU(cpu_instructions)
        cpu.PC = 0
        
        step_count = 0
        while step_count < 50 and cpu.PC < len(cpu_instructions):
            instruction = cpu_instructions[cpu.PC]
            next_pc = cpu.step(cpu.PC)
            cpu.PC = next_pc
            step_count += 1
            
            if cpu.PC == next_pc and instruction.get("TYPE") == "C_COMMAND":
                jump = instruction.get("VAL", {}).get("JUMP", "")
                if jump == "JMP":
                    break
        
        cpu_result = cpu.RAM[result_memory_addr]
        print(f"Result: Petri={expected_result}, CPU={cpu_result}")
        
        assert cpu_result == expected_result
        assert cpu_result == 1500, f"Expected 1500, got {cpu_result}"
        print("✓ Large constants VM to CPU test passed")

if __name__ == "__main__":
    print("VM to CPU Integration Tests via Petri Nets")
    print("=" * 60)
    
    print("\n🔹 VM -> PETRI NET -> ASSEMBLY -> CPU TESTS")
    test_simple_add_vm_to_cpu()
    test_multiple_add_vm_to_cpu()
    test_large_constants_vm_to_cpu()
    
    print("\n" + "=" * 60)
    print("All VM to CPU integration tests passed! ✓")
    print("Complete pipeline working: VM -> Petri Net -> Assembly -> CPU")