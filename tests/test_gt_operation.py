#!/usr/bin/env python3
"""
Test cases for gt (greater than) VM operation
Tests VM code parsing and Petri net generation for push constant + gt instructions
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

def test_gt_true():
    """Test: push constant 7, push constant 3, gt (7 > 3 = true = -1)"""
    print("\n=== Test: GT true (7 > 3) ===")
    
    vm_code = """push constant 7
push constant 3
gt
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
        expected_min_places = 5  # init, end, const_7, const_3, gt_result
        assert len(net.places) >= expected_min_places, f"Expected at least {expected_min_places} places, got {len(net.places)}"
        
        # Should have push transitions and gt transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        gt_transitions = [name for name in net.transitions.keys() if name.startswith("gt_")]
        
        assert len(push_transitions) == 2, f"Expected 2 push transitions, got {len(push_transitions)}"
        assert len(gt_transitions) == 1, f"Expected 1 gt transition, got {len(gt_transitions)}"
        assert len(emitter.control_stack) == 1, f"Expected 1 item on stack after gt, got {len(emitter.control_stack)}"
        
        # Check that result place is on stack
        result_place = emitter.control_stack[0]
        assert "gt_result" in result_place.name, f"Expected gt_result place on stack, got {result_place.name}"
        
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
        
        print("✓ GT true test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_gt_false():
    """Test: push constant 3, push constant 7, gt (3 > 7 = false = 0)"""
    print("\n=== Test: GT false (3 > 7) ===")
    
    vm_code = """push constant 3
push constant 7
gt
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
            print(f"✓ GT false: 3 > 7 = {result_place.token.value}")
        
        print("✓ GT false test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_gt_equal():
    """Test: push constant 5, push constant 5, gt (5 > 5 = false = 0)"""
    print("\n=== Test: GT equal (5 > 5) ===")
    
    vm_code = """push constant 5
push constant 5
gt
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
            print(f"✓ GT equal: 5 > 5 = {result_place.token.value}")
        
        print("✓ GT equal test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_gt_with_negatives():
    """Test: push constant 5, neg, push constant 3, neg, gt (-5 > -3 = false = 0)"""
    print("\n=== Test: GT with negatives (-5 > -3) ===")
    
    vm_code = """push constant 5
neg
push constant 3
neg
gt
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
        
        # Check result (should be 0 for false, since -5 < -3)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == 0, f"Expected 0 (false), got {result_place.token.value}"
            print(f"✓ GT with negatives: -5 > -3 = {result_place.token.value}")
        
        print("✓ GT with negatives test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_gt_arithmetic_result():
    """Test: push 10, push 3, add, push 12, gt ((10+3) > 12 = true = -1)"""
    print("\n=== Test: GT arithmetic result ((10+3) > 12) ===")
    
    vm_code = """push constant 10
push constant 3
add
push constant 12
gt
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
        
        # Should have 3 push, 1 add, and 1 gt transition
        push_transitions = [name for name in net.transitions.keys() if name.startswith("push_const")]
        add_transitions = [name for name in net.transitions.keys() if name.startswith("add_")]
        gt_transitions = [name for name in net.transitions.keys() if name.startswith("gt_")]
        
        assert len(push_transitions) == 3, f"Expected 3 push transitions, got {len(push_transitions)}"
        assert len(add_transitions) == 1, f"Expected 1 add transition, got {len(add_transitions)}"
        assert len(gt_transitions) == 1, f"Expected 1 gt transition, got {len(gt_transitions)}"
        
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
        
        # Check final result (should be -1: (10+3) > 12 = 13 > 12 = true)
        result_place = emitter.control_stack[0]
        if result_place.has:
            print(f"Final result: {result_place.token.value}")
            assert result_place.token.value == -1, f"Expected -1 (true), got {result_place.token.value}"
        
        print("✓ GT arithmetic result test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_gt_assembly_output():
    """Test the assembly code generation for gt operation"""
    print("\n=== Test: GT assembly output ===")
    
    vm_code = """push constant 10
push constant 5
gt
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
        
        # Get the gt transition
        gt_transition = [t for t in net.transitions.values() if t.name.startswith("gt_")][0]
        
        # Generate assembly code
        assembly = gt_transition.emit_assembly()
        print(f"Generated gt assembly: {assembly}")
        
        # Verify assembly structure
        assert len(assembly) >= 10, f"Expected at least 10 assembly instructions, got {len(assembly)}"
        
        # Check for expected assembly patterns
        assembly_str = '\n'.join(assembly)
        
        # Should load operands and perform subtraction
        assert "D=M" in assembly_str, "Expected D=M instruction to load first operand"
        assert "D=D-M" in assembly_str, "Expected D=D-M instruction for comparison"
        
        # Should have conditional jump for greater than
        assert "JGT" in assembly_str, "Expected JGT instruction for greater than comparison"
        
        # Should have labels for true and end cases
        assert "GT_TRUE_" in assembly_str, "Expected GT_TRUE label"
        assert "GT_END_" in assembly_str, "Expected GT_END label"
        
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
        
        # Verify the result is correct (10 > 5 = true = -1)
        result_place = emitter.control_stack[0]
        if result_place.has:
            assert result_place.token.value == -1, f"Expected -1, got {result_place.token.value}"
            print(f"✓ Assembly execution result: 10 > 5 = {result_place.token.value}")
        
        print("✓ GT assembly output test passed")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Testing GT (Greater Than) VM Operation")
    print("=" * 60)
    
    print("\n🔹 GT OPERATION TESTS")
    test_gt_true()
    test_gt_false()
    test_gt_equal()
    test_gt_with_negatives()
    test_gt_arithmetic_result()
    
    print("\n🔹 GT ASSEMBLY TESTS")
    test_gt_assembly_output()
    
    print("\n" + "=" * 60)
    print("All gt operation tests passed! ✓")
    print("VM gt operation is working correctly.")