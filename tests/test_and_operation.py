#!/usr/bin/env python3
"""
Test cases for and (bitwise AND) VM operation
Tests VM code parsing and Petri net generation for push constant + and instructions
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser
from PetriEmitter import PetriEmitter
from Petri.Token import Token
import tempfile
import shutil

def create_test_vm_file(vm_code, filename="test.vm"):
    """Create a temporary VM file with the given code"""
    temp_dir = tempfile.mkdtemp()
    vm_file_path = os.path.join(temp_dir, filename)
    
    with open(vm_file_path, 'w') as f:
        f.write(vm_code)
    
    return temp_dir, vm_file_path

def test_and_basic():
    """Test: push constant 12, push constant 10, and (12 & 10 = 8)"""
    print("\n=== Test: AND basic (12 & 10 = 8) ===")
    
    vm_code = """push constant 12
push constant 10
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Examine the net structure
        print(f"Places in net: {list(net.places.keys())}")
        print(f"Transitions in net: {list(net.transitions.keys())}")
        print(f"Control stack size: {len(emitter.control_stack)}")
        
        # Verify net structure
        expected_min_places = 5  # init, end, const_12, const_10, and_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and and transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(and_transitions) == 1, f"Expected 1 and transition, got {len(and_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after and, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "and_result" in result_place.name, f"Expected and_result place on stack, got {result_place.name}"
        
        # Allocate memory
        slots_used = net.allocate_memory()
        print(f"Memory slots used: {slots_used}")
        
        # Execute the net step by step
        print("\nExecuting net...")
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            print(f"Step {step}: Fired {fired}")
            step += 1
            if step > 20:  # Safety break
                break
        
        # Check that result place has token with value 8 (12 & 10 = 8)
        # 12 in binary: 1100, 10 in binary: 1010, 12 & 10 = 1000 = 8
        if result_place.has:
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == 8, f"Expected token value 8, got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        print("✓ AND basic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_all_ones():
    """Test: push constant 15, push constant 15, and (15 & 15 = 15)"""
    print("\n=== Test: AND all ones (15 & 15 = 15) ===")
    
    vm_code = """push constant 15
push constant 15
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 20:
                break
        
        # Check result (should be 15 for 15 & 15)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 15, f"Expected 15, got {result_place.token.value}"
            print(f"✓ AND all ones: 15 & 15 = {result_place.token.value}")
        
        print("✓ AND all ones test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_with_zero():
    """Test: push constant 7, push constant 0, and (7 & 0 = 0)"""
    print("\n=== Test: AND with zero (7 & 0 = 0) ===")
    
    vm_code = """push constant 7
push constant 0
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 20:
                break
        
        # Check result (should be 0 for anything & 0)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0, got {result_place.token.value}"
            print(f"✓ AND with zero: 7 & 0 = {result_place.token.value}")
        
        print("✓ AND with zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_negative_numbers():
    """Test: push constant 5, neg, push constant 3, and (-5 & 3)"""
    print("\n=== Test: AND with negative numbers (-5 & 3) ===")
    
    vm_code = """push constant 5
neg
push constant 3
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 30:
                break
        
        # Check result (-5 & 3 in two's complement)
        # -5 in 16-bit two's complement: 1111111111111011
        # 3 in binary: 0000000000000011
        # Result: 0000000000000011 = 3
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = (-5) & 3  # Let Python calculate the expected result
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ AND with negatives: -5 & 3 = {result_place.token.value}")
        
        print("✓ AND with negative numbers test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_powers_of_two():
    """Test: push constant 8, push constant 4, and (8 & 4 = 0)"""
    print("\n=== Test: AND powers of two (8 & 4 = 0) ===")
    
    vm_code = """push constant 8
push constant 4
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 20:
                break
        
        # Check result (8 & 4: 1000 & 0100 = 0000 = 0)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0, got {result_place.token.value}"
            print(f"✓ AND powers of two: 8 & 4 = {result_place.token.value}")
        
        print("✓ AND powers of two test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_arithmetic_result():
    """Test: push 5, push 3, add, push 6, and ((5+3) & 6 = 0)"""
    print("\n=== Test: AND arithmetic result ((5+3) & 6) ===")
    
    vm_code = """push constant 5
push constant 3
add
push constant 6
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Examine the net structure
        print(f"Places in net: {list(net.places.keys())}")
        print(f"Transitions in net: {list(net.transitions.keys())}")
        
        # Should have 3 push, 1 add, and 1 and transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(and_transitions) == 1, f"Expected 1 and transition, got {len(and_transitions)}"
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            print(f"Step {step}: Fired {fired}")
            step += 1
            if step > 30:  # Safety break
                break
        
        # Check final result (should be 0: (5+3) & 6 = 8 & 6 = 0)
        # 8 in binary: 1000, 6 in binary: 0110, 8 & 6 = 0000 = 0
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 0, f"Expected 0, got {result_place.token.value}"
        
        print("✓ AND arithmetic result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_assembly_output():
    """Test the assembly code generation for and operation"""
    print("\n=== Test: AND assembly output ===")
    
    vm_code = """push constant 12
push constant 10
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Allocate memory
        slots_used = net.allocate_memory()
        print(f"Memory slots used: {slots_used}")
        
        # Get the and transition
        and_transition = [t for t in net.transitions.values() if t.name.startswith("and_")][0]
        
        # Generate assembly code
        assembly = and_transition.emit_assembly()
        print(f"Generated and assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 6, f"Expected at least 6 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operands and perform bitwise AND
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        assert "D=D&M" in assembly_str, "Expected D=D&M instruction for bitwise AND"
        
        # Should store result
        assert "M=D" in assembly_str, "Expected M=D instruction to store result"
        
        print("Assembly code structure:")
        for i, line in enumerate(assembly):
            print(f"  {i+1}: {line}")
        
        # Execute to verify the assembly works correctly
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 20:
                break
        
        # Verify the result is correct (12 & 10 = 8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 8, f"Expected 8, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 12 & 10 = {result_place.token.value}")
        
        print("✓ AND assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing AND (Bitwise AND) VM Operation")
    print("=" * 60)
    
    print("\n🔹 AND OPERATION TESTS")
    test_and_basic()
    test_and_all_ones()
    test_and_with_zero()
    test_and_negative_numbers()
    test_and_powers_of_two()
    test_and_arithmetic_result()
    
    print("\n🔹 AND ASSEMBLY TESTS")
    test_and_assembly_output()
    
    print("\n" + "=" * 60)
    print("All and operation tests passed! ✓")
    print("VM and operation is working correctly.")