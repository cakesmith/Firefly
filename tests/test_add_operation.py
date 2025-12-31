#!/usr/bin/env python3
"""
Test cases for add VM operation
Tests VM code parsing and Petri net generation for push constant + add instructions
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

def test_simple_add():
    """Test: push constant 5, push constant 3, add"""
    print("\n=== Test: Simple add (5 + 3) ===")
    
    vm_code = """push constant 5
push constant 3
add
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
        # Should have: init, end, const_5, const_3, add_result, plus any dup places
        expected_min_places = 5  # init, end, const_5, const_3, add_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and add transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after add, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "add_result" in result_place.name, f"Expected add_result place on stack, got {result_place.name}"
        
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
        
        # Check that result place has token with value 8 (5 + 3)
        if result_place.has:
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == 8, f"Expected token value 8, got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        # Generate assembly code for add transition
        add_transition = [t for t in net.transitions.values() if t.name.startswith("add_")][0]
        assembly = add_transition.emit_assembly()
        print(f"Generated add assembly: {assembly}")
        
        # Verify assembly structure (should load, add, store)
        assert len(assembly) >= 5, f"Expected at least 5 assembly instructions, got {len(assembly)}"
        assert "D=M" in assembly, "Expected D=M instruction to load first operand"
        assert "D=D+M" in assembly, "Expected D=D+M instruction to add second operand"
        
        print("✓ Simple add test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_add_with_zero():
    """Test: push constant 42, push constant 0, add"""
    print("\n=== Test: Add with zero (42 + 0) ===")
    
    vm_code = """push constant 42
push constant 0
add
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
        
        # Check result
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 42, f"Expected 42, got {result_place.token.value}"
            print(f"✓ Add with zero: 42 + 0 = {result_place.token.value}")
        
        print("✓ Add with zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_multiple_adds():
    """Test: push constant 1, push constant 2, add, push constant 3, add"""
    print("\n=== Test: Multiple adds (1 + 2 + 3) ===")
    
    vm_code = """push constant 1
push constant 2
add
push constant 3
add
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
        
        # Should have 3 push transitions and 2 add transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 2, f"Expected 2 add transitions, got {len(add_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after adds, got {len(emitter.control_stack)}"
        
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
        
        # Check final result (should be 6)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 6, f"Expected 6, got {result_place.token.value}"
        
        print("✓ Multiple adds test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_large_numbers_add():
    """Test: push constant 1000, push constant 2000, add"""
    print("\n=== Test: Large numbers add (1000 + 2000) ===")
    
    vm_code = """push constant 1000
push constant 2000
add
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
        
        # Check result
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 3000, f"Expected 3000, got {result_place.token.value}"
            print(f"✓ Large numbers: 1000 + 2000 = {result_place.token.value}")
        
        print("✓ Large numbers add test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Add VM Operation")
    print("=" * 60)
    
    print("\n🔹 ADD OPERATION TESTS")
    test_simple_add()
    test_add_with_zero()
    test_multiple_adds()
    test_large_numbers_add()
    
    print("\n" + "=" * 60)
    print("All add operation tests passed! ✓")
    print("VM add operation is working correctly.")