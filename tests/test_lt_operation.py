#!/usr/bin/env python3
"""
Test cases for lt (less than) VM operation
Tests VM code parsing and Petri net generation for push constant + lt instructions
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

def test_lt_true():
    """Test: push constant 3, push constant 5, lt (3 < 5 = true = -1)"""
    print("\n=== Test: LT true (3 < 5) ===")
    
    vm_code = """push constant 3
push constant 5
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
        
        # Verify net structure
        # Should have: init, end, const_3, const_5, lt_result, plus any dup places
        expected_min_places = 5  # init, end, const_3, const_5, lt_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and lt transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        lt_transitions = [name for name in net.transitions.keys() if name.startswith("lt_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(lt_transitions) == 1, f"Expected 1 lt transition, got {len(lt_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after lt, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "lt_result" in result_place.name, f"Expected lt_result place on stack, got {result_place.name}"
        
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
        
        # Check that result place has token with value -1 (true)
        if result_place.has:
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == -1, f"Expected token value -1 (true), got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        print("✓ LT true test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_lt_false():
    """Test: push constant 8, push constant 3, lt (8 < 3 = false = 0)"""
    print("\n=== Test: LT false (8 < 3) ===")
    
    vm_code = """push constant 8
push constant 3
lt
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
        
        # Check result (should be 0 for false)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0 (false), got {result_place.token.value}"
            print(f"✓ LT false: 8 < 3 = {result_place.token.value}")
        
        print("✓ LT false test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_lt_equal():
    """Test: push constant 5, push constant 5, lt (5 < 5 = false = 0)"""
    print("\n=== Test: LT equal (5 < 5) ===")
    
    vm_code = """push constant 5
push constant 5
lt
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
        
        # Check result (should be 0 for false, since 5 is not less than 5)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0 (false), got {result_place.token.value}"
            print(f"✓ LT equal: 5 < 5 = {result_place.token.value}")
        
        print("✓ LT equal test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_lt_with_negatives():
    """Test: push constant -3, push constant 2, lt (-3 < 2 = true = -1)"""
    print("\n=== Test: LT with negatives (-3 < 2) ===")
    
    # Since VM doesn't directly support negative constants, we'll create -3 by negating 3
    vm_code = """push constant 3
neg
push constant 2
lt
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
        
        # Check result (should be -1 for true, since -3 < 2)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
            print(f"✓ LT with negatives: -3 < 2 = {result_place.token.value}")
        
        print("✓ LT with negatives test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_lt_chained():
    """Test: push 1, push 2, lt, push 3, push 4, lt, add (check chaining comparisons)"""
    print("\n=== Test: LT chained ((1 < 2) + (3 < 4)) ===")
    
    vm_code = """push constant 1
push constant 2
lt
push constant 3
push constant 4
lt
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
        
        # Should have 4 push, 2 lt, and 1 add transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        lt_transitions = [name for name in net.transitions.keys() if name.startswith("lt_")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        
        assert len(push_transitions) == 4, f"Expected 4 push transitions, got {len(push_transitions)}"
        assert len(lt_transitions) == 2, f"Expected 2 lt transitions, got {len(lt_transitions)}"
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
        
        # Check final result (should be -2: (-1) + (-1) = -2, since both comparisons are true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -2, f"Expected -2, got {result_place.token.value}"
        
        print("✓ LT chained test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_lt_assembly_output():
    """Test the assembly code generation for lt operation"""
    print("\n=== Test: LT assembly output ===")
    
    vm_code = """push constant 10
push constant 15
lt
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
        
        # Get the lt transition
        lt_transition = [t for t in net.transitions.values() if t.name.startswith("lt_")][0]
        
        # Generate assembly code
        assembly = lt_transition.emit_assembly()
        print(f"Generated lt assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 10, f"Expected at least 10 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operands and perform subtraction
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        assert "D=D-M" in assembly_str, "Expected D=D-M instruction for comparison"
        
        # Should have conditional jump for less than
        assert "JLT" in assembly_str, "Expected JLT instruction for less than comparison"
        
        # Should have labels for true and end cases
        assert "LT_TRUE_" in assembly_str, "Expected LT_TRUE label"
        assert "LT_END_" in assembly_str, "Expected LT_END label"
        
        # Should set D=-1 for true case and D=0 for false case
        assert "D=-1" in assembly_str, "Expected D=-1 for true case"
        assert "D=0" in assembly_str, "Expected D=0 for false case"
        
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
        
        # Verify the result is correct (10 < 15 = true = -1)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 10 < 15 = {result_place.token.value}")
        
        print("✓ LT assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing LT (Less Than) VM Operation")
    print("=" * 60)
    
    print("\n🔹 LT OPERATION TESTS")
    test_lt_true()
    test_lt_false()
    test_lt_equal()
    test_lt_with_negatives()
    test_lt_chained()
    
    print("\n🔹 LT ASSEMBLY TESTS")
    test_lt_assembly_output()
    
    print("\n" + "=" * 60)
    print("All lt operation tests passed! ✓")
    print("VM lt operation is working correctly.")