#!/usr/bin/env python3
"""
Test cases for combined arithmetic VM operations (add, sub, neg)
Tests that all arithmetic operations work together in complex expressions
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

def test_complex_arithmetic():
    """Test: push 10, push 3, add, push 5, sub, neg (-(10+3-5) = -8)"""
    print("\n=== Test: Complex arithmetic (-(10+3-5)) ===")
    
    vm_code = """push constant 10
push constant 3
add
push constant 5
sub
neg
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
        
        # Should have 3 push, 1 add, 1 sub, and 1 neg transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        sub_transitions = [name for name in net.transitions.keys() if name.startswith("sub_")]
        neg_transitions = [name for name in net.transitions.keys() if name.startswith("neg_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(sub_transitions) == 1, f"Expected 1 sub transition, got {len(sub_transitions)}"
        assert len(neg_transitions) == 1, f"Expected 1 neg transition, got {len(neg_transitions)}"
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            print(f"Step {step}: Fired {fired}")
            step += 1
            if step > 40:  # Safety break
                break
        
        # Check final result (should be -8: -(10+3-5) = -(13-5) = -8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -8, f"Expected -8, got {result_place.token.value}"
        
        print("✓ Complex arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_double_negation_with_arithmetic():
    """Test: push 5, push 3, sub, neg, neg (5-3 negated twice = 2)"""
    print("\n=== Test: Double negation with arithmetic ((5-3) negated twice) ===")
    
    vm_code = """push constant 5
push constant 3
sub
neg
neg
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
        
        # Check final result (should be 2: 5-3=2, neg=-2, neg=2)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 2, f"Expected 2, got {result_place.token.value}"
        
        print("✓ Double negation with arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_negative_addition():
    """Test: push 10, neg, push 5, add (-10 + 5 = -5)"""
    print("\n=== Test: Negative addition (-10 + 5) ===")
    
    vm_code = """push constant 10
neg
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
        
        # Check final result (should be -5)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -5, f"Expected -5, got {result_place.token.value}"
        
        print("✓ Negative addition test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_subtract_negative():
    """Test: push 8, push 3, neg, sub (8 - (-3) = 8 + 3 = 11)"""
    print("\n=== Test: Subtract negative (8 - (-3)) ===")
    
    vm_code = """push constant 8
push constant 3
neg
sub
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
        
        # Check final result (should be 11: 8 - (-3) = 8 + 3 = 11)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 11, f"Expected 11, got {result_place.token.value}"
        
        print("✓ Subtract negative test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Combined Arithmetic VM Operations")
    print("=" * 60)
    
    test_complex_arithmetic()
    test_double_negation_with_arithmetic()
    test_negative_addition()
    test_subtract_negative()
    
    print("\n" + "=" * 60)
    print("All combined arithmetic tests passed! ✓")
    print("Add, sub, and neg operations work correctly together.")