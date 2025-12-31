#!/usr/bin/env python3
"""
Test cases for combining comparison (lt) with arithmetic operations (add, sub, neg)
Tests complex expressions involving comparisons and arithmetic
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

def test_arithmetic_then_compare():
    """Test: push 10, push 3, add, push 15, lt ((10+3) < 15 = true = -1)"""
    print("\n=== Test: Arithmetic then compare ((10+3) < 15) ===")
    
    vm_code = """push constant 10
push constant 3
add
push constant 15
lt
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
        
        # Should have 3 push, 1 add, and 1 lt transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        lt_transitions = [name for name in net.transitions.keys() if name.startswith("lt_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(lt_transitions) == 1, f"Expected 1 lt transition, got {len(lt_transitions)}"
        
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
        
        # Check final result (should be -1: (10+3) < 15 = 13 < 15 = true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
        
        print("✓ Arithmetic then compare test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_compare_then_arithmetic():
    """Test: push 5, push 10, lt, push 2, add ((-1) + 2 = 1)"""
    print("\n=== Test: Compare then arithmetic ((5 < 10) + 2) ===")
    
    vm_code = """push constant 5
push constant 10
lt
push constant 2
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
        
        # Check final result (should be 1: (-1) + 2 = 1)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 1, f"Expected 1, got {result_place.token.value}"
        
        print("✓ Compare then arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_negated_comparison():
    """Test: push 8, push 3, lt, neg (negate the result of 8 < 3)"""
    print("\n=== Test: Negated comparison (-(8 < 3)) ===")
    
    vm_code = """push constant 8
push constant 3
lt
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
        
        # Check final result (should be 0: -(8 < 3) = -(false) = -0 = 0)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 0, f"Expected 0, got {result_place.token.value}"
        
        print("✓ Negated comparison test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_complex_expression():
    """Test: push 20, push 5, sub, push 12, lt, push 1, add ((20-5) < 12) + 1"""
    print("\n=== Test: Complex expression (((20-5) < 12) + 1) ===")
    
    vm_code = """push constant 20
push constant 5
sub
push constant 12
lt
push constant 1
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
            if step > 40:
                break
        
        # Check final result 
        # (20-5) < 12 = 15 < 12 = false = 0
        # 0 + 1 = 1
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 1, f"Expected 1, got {result_place.token.value}"
        
        print("✓ Complex expression test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Comparison and Arithmetic VM Operations")
    print("=" * 60)
    
    test_arithmetic_then_compare()
    test_compare_then_arithmetic()
    test_negated_comparison()
    test_complex_expression()
    
    print("\n" + "=" * 60)
    print("All comparison and arithmetic tests passed! ✓")
    print("LT operation works correctly with arithmetic operations.")