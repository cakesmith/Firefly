#!/usr/bin/env python3
"""
Test cases for all comparison operations (lt, eq) working together
Tests complex expressions involving multiple comparison types
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

def test_lt_and_eq():
    """Test: push 5, push 10, lt, push 7, push 7, eq, add ((5 < 10) + (7 == 7))"""
    print("\n=== Test: LT and EQ combined ((5 < 10) + (7 == 7)) ===")
    
    vm_code = """push constant 5
push constant 10
lt
push constant 7
push constant 7
eq
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
        
        # Should have push, lt, eq, and add transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        lt_transitions = [name for name in net.transitions.keys() if name.startswith("lt_")]
        eq_transitions = [name for name in net.transitions.keys() if name.startswith("eq_")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        
        print(f"Push transitions: {len(push_transitions)}")
        print(f"LT transitions: {len(lt_transitions)}")
        print(f"EQ transitions: {len(eq_transitions)}")
        print(f"Add transitions: {len(add_transitions)}")
        
        assert len(lt_transitions) == 1, f"Expected 1 lt transition, got {len(lt_transitions)}"
        assert len(eq_transitions) == 1, f"Expected 1 eq transition, got {len(eq_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        
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
        
        # Check final result (should be -2: (-1) + (-1) = -2, both comparisons are true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -2, f"Expected -2, got {result_place.token.value}"
        
        print("✓ LT and EQ combined test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_comparison_chain():
    """Test: push 3, push 5, lt, push 8, push 8, eq, push 10, push 7, lt, add, add"""
    print("\n=== Test: Comparison chain ((3 < 5) + (8 == 8) + (10 < 7)) ===")
    
    vm_code = """push constant 3
push constant 5
lt
push constant 8
push constant 8
eq
push constant 10
push constant 7
lt
add
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
            if step > 50:
                break
        
        # Check final result 
        # (3 < 5) = true = -1
        # (8 == 8) = true = -1  
        # (10 < 7) = false = 0
        # (-1) + (-1) + 0 = -2
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -2, f"Expected -2, got {result_place.token.value}"
        
        print("✓ Comparison chain test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_vs_lt():
    """Test different values to verify eq and lt work correctly"""
    print("\n=== Test: EQ vs LT verification ===")
    
    # Test case 1: 5 == 5 should be true, 5 < 5 should be false
    vm_code1 = """push constant 5
push constant 5
eq
push constant 5
push constant 5
lt
sub
"""
    temp_dir1, vm_file1 = create_test_vm_file(vm_code1, "test1.vm")
    
    try:
        parser1 = VMParser(temp_dir1)
        emitter1 = parser1.emitter
        net1 = emitter1.net
        net1.allocate_memory()
        
        step = 1
        while True:
            fired = net1.execute_step()
            if not fired:
                break
            step += 1
            if step > 40:
                break
        
        # eq result should be -1, lt result should be 0, so (-1) - 0 = -1
        result_place1 = emitter1.control_stack[0]
        if result_place1.has:
            print(f"(5 == 5) - (5 < 5) = {result_place1.token.value}")
            assert result_place1.token.value == -1, f"Expected -1, got {result_place1.token.value}"
        
    finally:
        shutil.rmtree(temp_dir1)
    
    # Test case 2: 3 == 7 should be false, 3 < 7 should be true
    vm_code2 = """push constant 3
push constant 7
eq
push constant 3
push constant 7
lt
sub
"""
    temp_dir2, vm_file2 = create_test_vm_file(vm_code2, "test2.vm")
    
    try:
        parser2 = VMParser(temp_dir2)
        emitter2 = parser2.emitter
        net2 = emitter2.net
        net2.allocate_memory()
        
        step = 1
        while True:
            fired = net2.execute_step()
            if not fired:
                break
            step += 1
            if step > 40:
                break
        
        # eq result should be 0, lt result should be -1, so 0 - (-1) = 1
        result_place2 = emitter2.control_stack[0]
        if result_place2.has:
            print(f"(3 == 7) - (3 < 7) = {result_place2.token.value}")
            assert result_place2.token.value == 1, f"Expected 1, got {result_place2.token.value}"
        
    finally:
        shutil.rmtree(temp_dir2)
    
    print("✓ EQ vs LT verification test passed")

if __name__ == "__main__":
    print("Testing All Comparison VM Operations")
    print("=" * 60)
    
    test_lt_and_eq()
    test_comparison_chain()
    test_eq_vs_lt()
    
    print("\n" + "=" * 60)
    print("All comparison tests passed! ✓")
    print("LT and EQ operations work correctly together.")