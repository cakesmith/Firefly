#!/usr/bin/env python3
"""
Test cases for bitwise operations (and, or, not) combined with arithmetic and comparison operations
Tests complex expressions involving bitwise logic
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

def test_and_with_arithmetic():
    """Test: push 5, push 3, add, push 6, and, push 2, add ((5+3) & 6) + 2"""
    print("\n=== Test: AND with arithmetic (((5+3) & 6) + 2) ===")
    
    vm_code = """push constant 5
push constant 3
add
push constant 6
and
push constant 2
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
        
        # Should have push, add, and, add transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        
        print(f"Push transitions: {len(push_transitions)}")
        print(f"Add transitions: {len(add_transitions)}")
        print(f"AND transitions: {len(and_transitions)}")
        
        assert len(push_transitions) == 4, f"Expected 4 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 2, f"Expected 2 add transitions, got {len(add_transitions)}"
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
            if step > 40:  # Safety break
                break
        
        # Check final result 
        # (5+3) = 8, 8 & 6 = 0 (1000 & 0110 = 0000), 0 + 2 = 2
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 2, f"Expected 2, got {result_place.token.value}"
        
        print("✓ AND with arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_with_comparisons():
    """Test: push 12, push 10, and, push 8, eq ((12 & 10) == 8)"""
    print("\n=== Test: AND with comparisons ((12 & 10) == 8) ===")
    
    vm_code = """push constant 12
push constant 10
and
push constant 8
eq
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
        
        # Check result (12 & 10 = 8, 8 == 8 = true = -1)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
        
        print("✓ AND with comparisons test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_multiple_and_operations():
    """Test: push 15, push 12, and, push 8, and ((15 & 12) & 8)"""
    print("\n=== Test: Multiple AND operations ((15 & 12) & 8) ===")
    
    vm_code = """push constant 15
push constant 12
and
push constant 8
and
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Should have 2 and transitions
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        assert len(and_transitions) == 2, f"Expected 2 and transitions, got {len(and_transitions)}"
        
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
        
        # Check result 
        # 15 & 12: 1111 & 1100 = 1100 = 12
        # 12 & 8: 1100 & 1000 = 1000 = 8
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 8, f"Expected 8, got {result_place.token.value}"
        
        print("✓ Multiple AND operations test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_with_negation():
    """Test: push 7, push 3, neg, and (7 & (-3))"""
    print("\n=== Test: AND with negation (7 & (-3)) ===")
    
    vm_code = """push constant 7
push constant 3
neg
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
        
        # Check result (7 & (-3) in two's complement)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = 7 & (-3)  # Let Python calculate the expected result
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        
        print("✓ AND with negation test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_or_combined():
    """Test: push 12, push 10, and, push 3, or ((12 & 10) | 3)"""
    print("\n=== Test: AND and OR combined ((12 & 10) | 3) ===")
    
    vm_code = """push constant 12
push constant 10
and
push constant 3
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
        
        # Should have push, and, or transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        or_transitions = [name for name in net.transitions.keys() if name.startswith("or_")]
        
        print(f"Push transitions: {len(push_transitions)}")
        print(f"AND transitions: {len(and_transitions)}")
        print(f"OR transitions: {len(or_transitions)}")
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(and_transitions) == 1, f"Expected 1 and transition, got {len(and_transitions)}"
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
        
        # Check final result 
        # (12 & 10) = 8 (1100 & 1010 = 1000), 8 | 3 = 11 (1000 | 0011 = 1011)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 11, f"Expected 11, got {result_place.token.value}"
        
        print("✓ AND and OR combined test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_with_arithmetic():
    """Test: push 5, push 3, add, push 2, or ((5+3) | 2)"""
    print("\n=== Test: OR with arithmetic ((5+3) | 2) ===")
    
    vm_code = """push constant 5
push constant 3
add
push constant 2
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
        
        # Check result (5+3 = 8, 8 | 2 = 10: 1000 | 0010 = 1010)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 10, f"Expected 10, got {result_place.token.value}"
        
        print("✓ OR with arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_or_flag_setting():
    """Test: push 8, push 1, or (8 | 1 = 9) - common flag setting operation"""
    print("\n=== Test: OR flag setting (8 | 1 = 9) ===")
    
    vm_code = """push constant 8
push constant 1
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
        
        # Check result (8 | 1 = 9, common flag setting: 1000 | 0001 = 1001)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 9, f"Expected 9, got {result_place.token.value}"
        
        print("✓ OR flag setting test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_mask_operation():
    """Test: push 255, push 15, and (255 & 15 = 15) - common masking operation"""
    print("\n=== Test: AND mask operation (255 & 15 = 15) ===")
    
    vm_code = """push constant 255
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
        
        # Check result (255 & 15 = 15, common masking to get lower 4 bits)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 15, f"Expected 15, got {result_place.token.value}"
        
        print("✓ AND mask operation test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_with_arithmetic():
    """Test: push 5, push 3, add, not (~(5+3))"""
    print("\n=== Test: NOT with arithmetic (~(5+3)) ===")
    
    vm_code = """push constant 5
push constant 3
add
not
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
        
        # Check result (~(5+3) = ~8 = -9)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~8
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        
        print("✓ NOT with arithmetic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_all_bitwise_combined():
    """Test: push 12, push 10, and, not, push 3, or ((~(12 & 10)) | 3)"""
    print("\n=== Test: All bitwise combined ((~(12 & 10)) | 3) ===")
    
    vm_code = """push constant 12
push constant 10
and
not
push constant 3
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
        
        # Should have push, and, not, or transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        not_transitions = [name for name in net.transitions.keys() if name.startswith("not_")]
        or_transitions = [name for name in net.transitions.keys() if name.startswith("or_")]
        
        print(f"Push transitions: {len(push_transitions)}")
        print(f"AND transitions: {len(and_transitions)}")
        print(f"NOT transitions: {len(not_transitions)}")
        print(f"OR transitions: {len(or_transitions)}")
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(and_transitions) == 1, f"Expected 1 and transition, got {len(and_transitions)}"
        assert len(not_transitions) == 1, f"Expected 1 not transition, got {len(not_transitions)}"
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
            if step > 40:  # Safety break
                break
        
        # Check final result 
        # (12 & 10) = 8, ~8 = -9, (-9) | 3 = -9 (since -9 has all high bits set)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = (~(12 & 10)) | 3
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        
        print("✓ All bitwise combined test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_and_or_combined():
    """Test: push 12, push 10, and, push 3, or ((12 & 10) | 3)"""
    print("\n=== Test: AND and OR combined ((12 & 10) | 3) ===")
    
    vm_code = """push constant 12
push constant 10
and
push constant 3
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
        
        # Should have push, and, or transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        and_transitions = [name for name in net.transitions.keys() if name.startswith("and_")]
        or_transitions = [name for name in net.transitions.keys() if name.startswith("or_")]
        
        print(f"Push transitions: {len(push_transitions)}")
        print(f"AND transitions: {len(and_transitions)}")
        print(f"OR transitions: {len(or_transitions)}")
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(and_transitions) == 1, f"Expected 1 and transition, got {len(and_transitions)}"
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
        
        # Check final result 
        # (12 & 10) = 8 (1100 & 1010 = 1000), 8 | 3 = 11 (1000 | 0011 = 1011)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 11, f"Expected 11, got {result_place.token.value}"
        
        print("✓ AND and OR combined test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Bitwise Operations Combined with Other Operations")
    print("=" * 60)
    
    test_and_with_arithmetic()
    test_and_with_comparisons()
    test_multiple_and_operations()
    test_and_with_negation()
    test_and_or_combined()
    test_or_with_arithmetic()
    test_and_mask_operation()
    test_not_with_arithmetic()
    test_all_bitwise_combined()
    test_or_flag_setting()
    
    print("\n" + "=" * 60)
    print("All bitwise operation tests passed! ✓")
    print("AND, OR, and NOT operations work correctly with arithmetic and comparison operations.")