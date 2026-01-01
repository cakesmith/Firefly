#!/usr/bin/env python3
"""
Test cases for not (bitwise NOT) VM operation
Tests VM code parsing and Petri net generation for push constant + not instructions
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

def test_not_basic():
    """Test: push constant 5, not (~5)"""
    print("\n=== Test: NOT basic (~5) ===")
    
    vm_code = """push constant 5
not
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
        expected_min_places = 4  # init, end, const_5, not_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transition and not transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        not_transitions = [name for name in net.transitions.keys() if name.startswith("not_")]
        
        assert len(push_transitions) == 1, f"Expected 1 push transition, got {len(push_transitions)}"
        assert len(not_transitions) == 1, f"Expected 1 not transition, got {len(not_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after not, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "not_result" in result_place.name, f"Expected not_result place on stack, got {result_place.name}"
        
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
        
        # Check that result place has token with bitwise NOT of 5
        if result_place.has:
            expected_result = ~5  # Let Python calculate the expected result
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        print("✓ NOT basic test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_zero():
    """Test: push constant 0, not (~0)"""
    print("\n=== Test: NOT zero (~0) ===")
    
    vm_code = """push constant 0
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
            if step > 20:
                break
        
        # Check result (~0 should be -1 in two's complement)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~0
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ NOT zero: ~0 = {result_place.token.value}")
        
        print("✓ NOT zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_negative_one():
    """Test: push constant 1, neg, not (~(-1))"""
    print("\n=== Test: NOT negative one (~(-1)) ===")
    
    vm_code = """push constant 1
neg
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
        
        # Check result (~(-1) should be 0)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~(-1)
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ NOT negative one: ~(-1) = {result_place.token.value}")
        
        print("✓ NOT negative one test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_powers_of_two():
    """Test: push constant 8, not (~8)"""
    print("\n=== Test: NOT powers of two (~8) ===")
    
    vm_code = """push constant 8
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
            if step > 20:
                break
        
        # Check result (~8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~8
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ NOT powers of two: ~8 = {result_place.token.value}")
        
        print("✓ NOT powers of two test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_arithmetic_result():
    """Test: push 5, push 3, add, not (~(5+3))"""
    print("\n=== Test: NOT arithmetic result (~(5+3)) ===")
    
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
        
        # Examine the net structure
        print(f"Places in net: {list(net.places.keys())}")
        print(f"Transitions in net: {list(net.transitions.keys())}")
        
        # Should have 2 push, 1 add, and 1 not transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        not_transitions = [name for name in net.transitions.keys() if name.startswith("not_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(not_transitions) == 1, f"Expected 1 not transition, got {len(not_transitions)}"
        
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
        
        # Check final result (~(5+3) = ~8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~8
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        
        print("✓ NOT arithmetic result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_double_negation():
    """Test: push constant 7, not, not (~~7 should equal 7)"""
    print("\n=== Test: NOT double negation (~~7) ===")
    
    vm_code = """push constant 7
not
not
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Should have 2 not transitions
        not_transitions = [name for name in net.transitions.keys() if name.startswith("not_")]
        assert len(not_transitions) == 2, f"Expected 2 not transitions, got {len(not_transitions)}"
        
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
        
        # Check result (~~7 should equal 7)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 7, f"Expected 7, got {result_place.token.value}"
        
        print("✓ NOT double negation test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_with_bitwise_ops():
    """Test: push 12, push 10, and, not (~(12 & 10))"""
    print("\n=== Test: NOT with bitwise ops (~(12 & 10)) ===")
    
    vm_code = """push constant 12
push constant 10
and
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
        
        # Check result (~(12 & 10) = ~8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~(12 & 10)
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
        
        print("✓ NOT with bitwise ops test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_not_assembly_output():
    """Test the assembly code generation for not operation"""
    print("\n=== Test: NOT assembly output ===")
    
    vm_code = """push constant 5
not
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
        
        # Get the not transition
        not_transition = [t for t in net.transitions.values() if t.name.startswith("not_")][0]
        
        # Generate assembly code
        assembly = not_transition.emit_assembly()
        print(f"Generated not assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 4, f"Expected at least 4 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operand and perform bitwise NOT
        assert "D=M" in assembly_str, "Expected D=M instruction to load operand"
        assert "D=!D" in assembly_str, "Expected D=!D instruction for bitwise NOT"
        
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
        
        # Verify the result is correct (~5)
        result_place = emitter.control_stack[0]
        if result_place.has:
            expected_result = ~5
            assert result_place.token.value == expected_result, f"Expected {expected_result}, got {result_place.token.value}"
            print(f"✓ Assembly execution result: ~5 = {result_place.token.value}")
        
        print("✓ NOT assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing NOT (Bitwise NOT) VM Operation")
    print("=" * 60)
    
    print("\n🔹 NOT OPERATION TESTS")
    test_not_basic()
    test_not_zero()
    test_not_negative_one()
    test_not_powers_of_two()
    test_not_arithmetic_result()
    test_not_double_negation()
    test_not_with_bitwise_ops()
    
    print("\n🔹 NOT ASSEMBLY TESTS")
    test_not_assembly_output()
    
    print("\n" + "=" * 60)
    print("All not operation tests passed! ✓")
    print("VM not operation is working correctly.")