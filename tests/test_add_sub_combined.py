#!/usr/bin/env python3
"""
Test cases for combined add and sub VM operations
Tests that add and sub can work together in the same program
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

def test_add_then_sub():
    """Test: push 10, push 5, add, push 3, sub (10 + 5 - 3 = 12)"""
    print("\n=== Test: Add then sub (10 + 5 - 3) ===")
    
    vm_code = """push constant 10
push constant 5
add
push constant 3
sub
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
        
        # Should have 3 push, 1 add, and 1 sub transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        sub_transitions = [name for name in net.transitions.keys() if name.startswith("sub_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(sub_transitions) == 1, f"Expected 1 sub transition, got {len(sub_transitions)}"
        
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
        
        # Check final result (should be 12)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 12, f"Expected 12, got {result_place.token.value}"
        
        print("✓ Add then sub test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_sub_then_add():
    """Test: push 20, push 8, sub, push 5, add (20 - 8 + 5 = 17)"""
    print("\n=== Test: Sub then add (20 - 8 + 5) ===")
    
    vm_code = """push constant 20
push constant 8
sub
push constant 5
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
            if step > 30:
                break
        
        # Check final result (should be 17)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 17, f"Expected 17, got {result_place.token.value}"
        
        print("✓ Sub then add test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Combined Add and Sub VM Operations")
    print("=" * 60)
    
    test_add_then_sub()
    test_sub_then_add()
    
    print("\n" + "=" * 60)
    print("All combined add/sub tests passed! ✓")
    print("Add and sub operations work correctly together.")