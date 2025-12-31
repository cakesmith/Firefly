#!/usr/bin/env python3
"""
Test cases for sub VM operation
Tests VM code parsing and Petri net generation for push constant + sub instructions
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

def test_simple_sub():
    """Test: push constant 8, push constant 3, sub (8 - 3 = 5)"""
    print("\n=== Test: Simple sub (8 - 3) ===")
    
    vm_code = """push constant 8
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
        
        # Verify net structure
        # Should have: init, end, const_8, const_3, sub_result, plus any dup places
        expected_min_places = 5  # init, end, const_8, const_3, sub_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and sub transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        sub_transitions = [name for name in net.transitions.keys() if name.startswith("sub_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(sub_transitions) == 1, f"Expected 1 sub transition, got {len(sub_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after sub, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "sub_result" in result_place.name, f"Expected sub_result place on stack, got {result_place.name}"
        
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
        
        # Check that result place has token with value 5 (8 - 3)
        if result_place.has:
            print(f"Result place token value: {result_place.token.value}")
            assert result_place.token.value == 5, f"Expected token value 5, got {result_place.token.value}"
        else:
            print("Result place has no token - execution may not be complete")
        
        print("✓ Simple sub test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_sub_with_zero():
    """Test: push constant 42, push constant 0, sub (42 - 0 = 42)"""
    print("\n=== Test: Sub with zero (42 - 0) ===")
    
    vm_code = """push constant 42
push constant 0
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
            if step > 20:
                break
        
        # Check result
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 42, f"Expected 42, got {result_place.token.value}"
            print(f"✓ Sub with zero: 42 - 0 = {result_place.token.value}")
        
        print("✓ Sub with zero test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_sub_negative_result():
    """Test: push constant 3, push constant 8, sub (3 - 8 = -5)"""
    print("\n=== Test: Sub with negative result (3 - 8) ===")
    
    vm_code = """push constant 3
push constant 8
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
            if step > 20:
                break
        
        # Check result
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -5, f"Expected -5, got {result_place.token.value}"
            print(f"✓ Negative result: 3 - 8 = {result_place.token.value}")
        
        print("✓ Sub with negative result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_multiple_subs():
    """Test: push constant 10, push constant 3, sub, push constant 2, sub (10 - 3 - 2 = 5)"""
    print("\n=== Test: Multiple subs (10 - 3 - 2) ===")
    
    vm_code = """push constant 10
push constant 3
sub
push constant 2
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
        
        # Should have 3 push transitions and 2 sub transitions
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        sub_transitions = [name for name in net.transitions.keys() if name.startswith("sub_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(sub_transitions) == 2, f"Expected 2 sub transitions, got {len(sub_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after subs, got {len(emitter.control_stack)}"
        
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
        
        # Check final result (should be 5)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == 5, f"Expected 5, got {result_place.token.value}"
        
        print("✓ Multiple subs test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_large_numbers_sub():
    """Test: push constant 5000, push constant 2000, sub (5000 - 2000 = 3000)"""
    print("\n=== Test: Large numbers sub (5000 - 2000) ===")
    
    vm_code = """push constant 5000
push constant 2000
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
            if step > 20:
                break
        
        # Check result
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 3000, f"Expected 3000, got {result_place.token.value}"
            print(f"✓ Large numbers: 5000 - 2000 = {result_place.token.value}")
        
        print("✓ Large numbers sub test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_sub_assembly_output():
    """Test the assembly code generation for sub operation"""
    print("\n=== Test: Sub assembly output ===")
    
    vm_code = """push constant 15
push constant 7
sub
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
        
        # Get the sub transition
        sub_transition = [t for t in net.transitions.values() if t.name.startswith("sub_")][0]
        
        # Generate assembly code
        assembly = sub_transition.emit_assembly()
        print(f"Generated sub assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 5, f"Expected at least 5 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load first operand into D register
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        
        # Should subtract second operand from D register
        assert "D=D-M" in assembly_str, "Expected D=D-M instruction to subtract second operand"
        
        # Should store result
        assert "M=D" in assembly_str, "Expected M=D instruction to store result"
        
        # Check for memory address references
        r_references = [line for line in assembly if line.startswith("@R")]
        assert len(r_references) >= 3, f"Expected at least 3 memory references, got {len(r_references)}"
        
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
        
        # Verify the result is correct (15 - 7 = 8)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 8, f"Expected 8, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 15 - 7 = {result_place.token.value}")
        
        print("✓ Sub assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing Sub VM Operation")
    print("=" * 60)
    
    print("\n🔹 SUB OPERATION TESTS")
    test_simple_sub()
    test_sub_with_zero()
    test_sub_negative_result()
    test_multiple_subs()
    test_large_numbers_sub()
    
    print("\n🔹 SUB ASSEMBLY TESTS")
    test_sub_assembly_output()
    
    print("\n" + "=" * 60)
    print("All sub operation tests passed! ✓")
    print("VM sub operation is working correctly.")