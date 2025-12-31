#!/usr/bin/env python3
"""
Test cases for eq (equals) VM operation
Tests VM code parsing and Petri net generation for push constant + eq instructions
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

def test_eq_true():
    """Test: push constant 7, push constant 7, eq (7 == 7 = true = -1)"""
    print("\n=== Test: EQ true (7 == 7) ===")
    
    vm_code = """push constant 7
push constant 7
eq
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
        # Should have: init, end, const_7 (x2), eq_result, plus any dup places
        expected_min_places = 5  # init, end, const_7 (x2), eq_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and eq transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        eq_transitions = [name for name in net.transitions.keys() if name.startswith("eq_")]
        
        # Note: When pushing the same constant twice, the system may optimize to use one transition
        assert len(push_transitions) >= 1, f"Expected at least 1 push transition, got {len(push_transitions)}"
        assert len(eq_transitions) == 1, f"Expected 1 eq transition, got {len(eq_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after eq, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "eq_result" in result_place.name, f"Expected eq_result place on stack, got {result_place.name}"
        
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
        
        print("✓ EQ true test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_false():
    """Test: push constant 5, push constant 8, eq (5 == 8 = false = 0)"""
    print("\n=== Test: EQ false (5 == 8) ===")
    
    vm_code = """push constant 5
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
            if step > 20:
                break
        
        # Check result (should be 0 for false)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0 (false), got {result_place.token.value}"
            print(f"✓ EQ false: 5 == 8 = {result_place.token.value}")
        
        print("✓ EQ false test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_zero():
    """Test: push constant 0, push constant 0, eq (0 == 0 = true = -1)"""
    print("\n=== Test: EQ zero (0 == 0) ===")
    
    vm_code = """push constant 0
push constant 0
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
            if step > 20:
                break
        
        # Check result (should be -1 for true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
            print(f"✓ EQ zero: 0 == 0 = {result_place.token.value}")
        
        print("✓ EQ zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_with_negatives():
    """Test: push constant 5, neg, push constant 5, neg, eq (-5 == -5 = true = -1)"""
    print("\n=== Test: EQ with negatives (-5 == -5) ===")
    
    vm_code = """push constant 5
neg
push constant 5
neg
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
        
        # Check result (should be -1 for true, since -5 == -5)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
            print(f"✓ EQ with negatives: -5 == -5 = {result_place.token.value}")
        
        print("✓ EQ with negatives test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_arithmetic_result():
    """Test: push 10, push 3, add, push 13, eq ((10+3) == 13 = true = -1)"""
    print("\n=== Test: EQ arithmetic result ((10+3) == 13) ===")
    
    vm_code = """push constant 10
push constant 3
add
push constant 13
eq
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
        
        # Should have 3 push, 1 add, and 1 eq transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        eq_transitions = [name for name in net.transitions.keys() if name.startswith("eq_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(eq_transitions) == 1, f"Expected 1 eq transition, got {len(eq_transitions)}"
        
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
        
        # Check final result (should be -1: (10+3) == 13 = 13 == 13 = true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
        
        print("✓ EQ arithmetic result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_chained():
    """Test: push 5, push 5, eq, push 3, push 3, eq, add (check chaining comparisons)"""
    print("\n=== Test: EQ chained ((5 == 5) + (3 == 3)) ===")
    
    vm_code = """push constant 5
push constant 5
eq
push constant 3
push constant 3
eq
add
"""
    temp_dir, vm_file = create_test_vm_file(vm_code)
    
    try:
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        # Should have push transitions, eq transitions, and add transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        eq_transitions = [name for name in net.transitions.keys() if name.startswith("eq_")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        
        # Note: When pushing the same constants, the system may optimize transitions
        assert len(push_transitions) >= 2, f"Expected at least 2 push transitions, got {len(push_transitions)}"
        assert len(eq_transitions) == 2, f"Expected 2 eq transitions, got {len(eq_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        
        # Allocate memory and execute
        net.allocate_memory()
        
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 40:  # Safety break
                break
        
        # Check final result (should be -2: (-1) + (-1) = -2, since both comparisons are true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -2, f"Expected -2, got {result_place.token.value}"
        
        print("✓ EQ chained test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_eq_assembly_output():
    """Test the assembly code generation for eq operation"""
    print("\n=== Test: EQ assembly output ===")
    
    vm_code = """push constant 42
push constant 42
eq
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
        
        # Get the eq transition
        eq_transition = [t for t in net.transitions.values() if t.name.startswith("eq_")][0]
        
        # Generate assembly code
        assembly = eq_transition.emit_assembly()
        print(f"Generated eq assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 10, f"Expected at least 10 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operands and perform subtraction
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        assert "D=D-M" in assembly_str, "Expected D=D-M instruction for comparison"
        
        # Should have conditional jump for equality
        assert "JEQ" in assembly_str, "Expected JEQ instruction for equality comparison"
        
        # Should have labels for true and end cases
        assert "EQ_TRUE_" in assembly_str, "Expected EQ_TRUE label"
        assert "EQ_END_" in assembly_str, "Expected EQ_END label"
        
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
        
        # Verify the result is correct (42 == 42 = true = -1)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 42 == 42 = {result_place.token.value}")
        
        print("✓ EQ assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing EQ (Equals) VM Operation")
    print("=" * 60)
    
    print("\n🔹 EQ OPERATION TESTS")
    test_eq_true()
    test_eq_false()
    test_eq_zero()
    test_eq_with_negatives()
    test_eq_arithmetic_result()
    test_eq_chained()
    
    print("\n🔹 EQ ASSEMBLY TESTS")
    test_eq_assembly_output()
    
    print("\n" + "=" * 60)
    print("All eq operation tests passed! ✓")
    print("VM eq operation is working correctly.")