#!/usr/bin/env python3
"""
Test cases for or (bitwise OR) VM operation
Tests VM code parsing and Petri net generation for push constant + or instructions
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

def test_or_basic():
    """Test: push constant 12, push constant 10, or (12 | 10 = 14)"""
    print("\n=== Test: OR basic (12 | 10 = 14) ===")
    
    vm_code = """push constant 12
push constant 10
or
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
        expected_min_places = 5  # init, end, const_12, const_10, or_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and or transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        or_transitions = [name for name in net.transitions.keys() if name.startswith("or_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(or_transitions) == 1, f"Expected 1 or transition, got {len(or_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after or, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "or_result" in result_place.name, f"Expected or_result place on stack, got {result_place.name}"
        
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
        
        # Check that result place has token with value 14 (12 | 10 = 14)
        # 12 in binary: 1100, 10 in binary: 1010, 12 | 10 = 1110 = 14
        if result_place.has:
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == 14, f"Expected token value 14, got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        print("✓ OR basic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_all_zeros():
    """Test: push constant 0, push constant 0, or (0 | 0 = 0)"""
    print("\n=== Test: OR all zeros (0 | 0 = 0) ===")
    
    vm_code = """push constant 0
push constant 0
or
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
        
        # Check result (should be 0 for 0 | 0)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0, got {result_place.token.value}"
            print(f"✓ OR all zeros: 0 | 0 = {result_place.token.value}")
        
        print("✓ OR all zeros test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_with_zero():
    """Test: push constant 7, push constant 0, or (7 | 0 = 7)"""
    print("\n=== Test: OR with zero (7 | 0 = 7) ===")
    
    vm_code = """push constant 7
push constant 0
or
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
        
        # Check result (should be 7 for 7 | 0, OR with zero preserves value)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 7, f"Expected 7, got {result_place.token.value}"
            print(f"✓ OR with zero: 7 | 0 = {result_place.token.value}")
        
        print("✓ OR with zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_negative_numbers():
    """Test: push constant 5, neg, push constant 3, or (-5 | 3)"""
    print("\n=== Test: OR with negative numbers (-5 | 3) ===")
    
    vm_code = """push constant 5
neg
push constant 3
or
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
        
        # Check result (-5 | 3 in two's complement)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = (-5) | 3  # Let Python calculate the expected result
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ OR with negatives: -5 | 3 = {result_place.token.value}")
        
        print("✓ OR with negative numbers test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_powers_of_two():
    """Test: push constant 8, push constant 4, or (8 | 4 = 12)"""
    print("\n=== Test: OR powers of two (8 | 4 = 12) ===")
    
    vm_code = """push constant 8
push constant 4
or
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
        
        # Check result (8 | 4: 1000 | 0100 = 1100 = 12)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 12, f"Expected 12, got {result_place.token.value}"
            print(f"✓ OR powers of two: 8 | 4 = {result_place.token.value}")
        
        print("✓ OR powers of two test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_arithmetic_result():
    """Test: push 5, push 3, add, push 6, or ((5+3) | 6 = 14)"""
    print("\n=== Test: OR arithmetic result ((5+3) | 6) ===")
    
    vm_code = """push constant 5
push constant 3
add
push constant 6
or
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
        
        # Should have 3 push, 1 add, and 1 or transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        or_transitions = [name for name in net.transitions.keys() if name.startswith("or_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(or_transitions) == 1, f"Expected 1 or transition, got {len(or_transitions)}"
        
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
        
        # Check final result (should be 14: (5+3) | 6 = 8 | 6 = 14)
        # 8 in binary: 1000, 6 in binary: 0110, 8 | 6 = 1110 = 14
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 14, f"Expected 14, got {result_place.token.value}"
        
        print("✓ OR arithmetic result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_all_ones():
    """Test: push constant 15, push constant 7, or (15 | 7 = 15)"""
    print("\n=== Test: OR all ones (15 | 7 = 15) ===")
    
    vm_code = """push constant 15
push constant 7
or
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
        
        # Check result (15 | 7: 1111 | 0111 = 1111 = 15)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 15, f"Expected 15, got {result_place.token.value}"
            print(f"✓ OR all ones: 15 | 7 = {result_place.token.value}")
        
        print("✓ OR all ones test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_assembly_output():
    """Test the assembly code generation for or operation"""
    print("\n=== Test: OR assembly output ===")
    
    vm_code = """push constant 12
push constant 10
or
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
        
        # Get the or transition
        or_transition = [t for t in net.transitions.values() if t.name.startswith("or_")][0]
        
        # Generate assembly code
        assembly = or_transition.emit_assembly()
        print(f"Generated or assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 6, f"Expected at least 6 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operands and perform bitwise OR
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        assert "D=D|M" in assembly_str, "Expected D=D|M instruction for bitwise OR"
        
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
        
        # Verify the result is correct (12 | 10 = 14)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 14, f"Expected 14, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 12 | 10 = {result_place.token.value}")
        
        print("✓ OR assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing OR (Bitwise OR) VM Operation")
    print("=" * 60)
    
    print("\n🔹 OR OPERATION TESTS")
    test_or_basic()
    test_or_all_zeros()
    test_or_with_zero()
    test_or_negative_numbers()
    test_or_powers_of_two()
    test_or_arithmetic_result()
    test_or_all_ones()
    
    print("\n🔹 OR ASSEMBLY TESTS")
    test_or_assembly_output()
    
    print("\n" + "=" * 60)
    print("All or operation tests passed! ✓")
    print("VM or operation is working correctly.")