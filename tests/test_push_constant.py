#!/usr/bin/env python3
"""
Test cases for push_constant VM operation
Tests VM code parsing and Petri net generation for push constant instructions
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

def test_single_push_constant():
    """Test: push constant 42"""
    print("\n=== Test: Single push constant 42 ===")
    
    vm_code = "push constant 42\n"
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
        assert len(net.places) == 3, f"Expected 3 places (init, end, const_42_*), got {len(net.places)}"
        assert len(net.transitions) == 1, f"Expected 1 transition, got {len(net.transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack, got {len(emitter.control_stack)}"
        
        # Check that constant place is on stack
        const_place = emitter.control_stack[0]
        assert "const_42" in const_place.name, f"Expected const_42 place on stack, got {const_place.name}"
        
        # Allocate memory and check
        slots_used = net.allocate_memory()
        print(f"Memory slots used: {slots_used}")
        
        # Execute the net
        print("\nExecuting net...")
        fired_transitions = net.execute_step()
        print(f"Fired transitions: {fired_transitions}")
        
        # Check that constant place has token with value 42
        if const_place.has:
            print(f"Constant place token value: {const_place.token.value}")
            assert const_place.token.value == 42, f"Expected token value 42, got {const_place.token.value}"
        
        # Generate assembly code
        transition = list(net.transitions.values())[0]
        assembly = transition.emit_assembly()
        print(f"Generated assembly: {assembly}")
        
        expected_assembly = ["@42", "D=A", f"@R{const_place.memory_address}", "M=D"]
        assert assembly == expected_assembly, f"Expected {expected_assembly}, got {assembly}"
        
        print("✓ Single push constant test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_multiple_push_constants():
    """Test: push constant 5, push constant 10, push constant 15"""
    print("\n=== Test: Multiple push constants (5, 10, 15) ===")
    
    vm_code = """push constant 5
push constant 10
push constant 15
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
        assert len(net.places) == 5, f"Expected 5 places (init, end, 3 constants), got {len(net.places)}"
        assert len(net.transitions) == 3, f"Expected 3 transitions, got {len(net.transitions)}"
        assert len(emitter.control_stack) == 3, f"Expected 3 items on stack, got {len(emitter.control_stack)}"
        
        # Check stack order (should be [const_5, const_10, const_15] with 15 on top)
        stack_values = []
        for place in emitter.control_stack:
            if "const_5" in place.name:
                stack_values.append(5)
            elif "const_10" in place.name:
                stack_values.append(10)
            elif "const_15" in place.name:
                stack_values.append(15)
        
        print(f"Stack values (bottom to top): {stack_values}")
        assert stack_values == [5, 10, 15], f"Expected [5, 10, 15], got {stack_values}"
        
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
        
        # Check final token values
        print("\nFinal token values:")
        for place_name, place in net.places.items():
            if place.has and "const_" in place_name:
                print(f"  {place_name}: {place.token.value}")
        
        # Generate assembly for all transitions
        print("\nGenerated assembly:")
        for trans_name, transition in net.transitions.items():
            assembly = transition.emit_assembly()
            print(f"  {trans_name}: {assembly}")
        
        print("✓ Multiple push constants test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_push_constant_zero():
    """Test: push constant 0 (edge case)"""
    print("\n=== Test: Push constant 0 (edge case) ===")
    
    vm_code = "push constant 0\n"
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Execute and check
        net.allocate_memory()
        net.execute_step()
        
        const_place = emitter.control_stack[0]
        assert const_place.token.value == 0, f"Expected token value 0, got {const_place.token.value}"
        
        # Check assembly generation for zero
        transition = list(net.transitions.values())[0]
        assembly = transition.emit_assembly()
        assert assembly[0] == "@0", f"Expected @0, got {assembly[0]}"
        
        print("✓ Push constant 0 test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Push Constant VM Operation")
    print("=" * 60)
    
    print("\n🔹 PUSH CONSTANT TESTS")
    test_single_push_constant()
    test_multiple_push_constants()
    test_push_constant_zero()
    
    print("\n" + "=" * 60)
    print("All push constant tests passed! ✓")
    print("VM push_constant operation is working correctly.")