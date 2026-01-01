#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_basic_loop_pattern():
    """Test a basic loop pattern using label, if-goto, and goto operations"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Simulate a simple loop pattern:
    # push constant 3      // counter
    # label LOOP_START
    # push constant 1
    # sub                  // counter--
    # dup                  // duplicate for both condition check and next iteration
    # if-goto LOOP_START   // continue if counter > 0
    # goto END
    # label END
    
    # Push initial counter value
    push_cmd1 = vmcommand("push", "constant", 3, None)
    emitter.push_constant(push_cmd1)
    
    # Create loop start label
    label_cmd = vmcommand("label", None, "LOOP_START", None)
    emitter.label(label_cmd)
    
    # Push 1 for subtraction
    push_cmd2 = vmcommand("push", "constant", 1, None)
    emitter.push_constant(push_cmd2)
    
    # Subtract 1 from counter
    sub_cmd = vmcommand("sub", None, None, None)
    emitter.sub(sub_cmd)
    
    # Check if we should continue loop (if-goto consumes the value)
    ifgoto_cmd = vmcommand("if-goto", None, "LOOP_START", None)
    emitter.ifgoto(ifgoto_cmd)
    
    # Unconditional jump to end
    goto_cmd = vmcommand("goto", None, "END", None)
    emitter.goto(goto_cmd)
    
    # End label
    end_label_cmd = vmcommand("label", None, "END", None)
    emitter.label(end_label_cmd)
    
    # Allocate memory and generate assembly
    emitter.net.allocate_memory()
    
    # Debug: Check memory allocation
    print("Memory allocation:")
    for place_name, place in emitter.net.places.items():
        if place.memory_address is not None:
            print(f"  {place_name}: R{place.memory_address}")
    
    # Generate assembly from transitions
    assembly_lines = []
    for transition_name, transition in emitter.net.transitions.items():
        assembly_code = transition.emit_assembly()
        if isinstance(assembly_code, list):
            assembly_lines.extend(assembly_code)
        else:
            assembly_lines.append(assembly_code)
    
    # Add label assembly
    label_assembly = emitter._generate_label_assembly()
    assembly_lines.extend(label_assembly)
    
    # Verify assembly contains all expected elements
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Check for labels
    assert "(LOOP_START)" in assembly_text, f"Label (LOOP_START) not found"
    assert "(END)" in assembly_text, f"Label (END) not found"
    
    # Check for jumps
    assert "@LOOP_START" in assembly_text, f"@LOOP_START not found"
    assert "D;JNE" in assembly_text, f"D;JNE (if-goto) not found"
    assert "@END" in assembly_text, f"@END not found"
    assert "0;JMP" in assembly_text, f"0;JMP (goto) not found"
    
    # Check for constants and arithmetic
    assert "@3" in assembly_text, f"@3 (initial counter) not found"
    assert "@1" in assembly_text, f"@1 (decrement) not found"
    assert "D=D-M" in assembly_text, f"D=D-M (subtraction) not found"
    
    print("✓ Basic loop pattern test passed")

def test_simple_conditional():
    """Test a simple conditional jump pattern"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Simple pattern:
    # push constant 0
    # if-goto SKIP
    # push constant 42    // This should be skipped
    # label SKIP
    
    # Push condition (0 = false)
    push_cmd1 = vmcommand("push", "constant", 0, None)
    emitter.push_constant(push_cmd1)
    
    # Conditional jump
    ifgoto_cmd = vmcommand("if-goto", None, "SKIP", None)
    emitter.ifgoto(ifgoto_cmd)
    
    # This should be skipped when condition is false
    push_cmd2 = vmcommand("push", "constant", 42, None)
    emitter.push_constant(push_cmd2)
    
    # Skip label
    label_cmd = vmcommand("label", None, "SKIP", None)
    emitter.label(label_cmd)
    
    # Allocate memory and generate assembly
    emitter.net.allocate_memory()
    
    # Generate assembly from transitions
    assembly_lines = []
    for transition_name, transition in emitter.net.transitions.items():
        assembly_code = transition.emit_assembly()
        if isinstance(assembly_code, list):
            assembly_lines.extend(assembly_code)
        else:
            assembly_lines.append(assembly_code)
    
    # Add label assembly
    label_assembly = emitter._generate_label_assembly()
    assembly_lines.extend(label_assembly)
    
    # Verify assembly
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly for conditional:")
    print(assembly_text)
    
    # Check basic structure
    assert "(SKIP)" in assembly_text, f"Label (SKIP) not found"
    assert "@SKIP" in assembly_text, f"@SKIP not found"
    assert "D;JNE" in assembly_text, f"D;JNE not found"
    assert "@0" in assembly_text, f"@0 (condition) not found"
    assert "@42" in assembly_text, f"@42 (skipped value) not found"
    
    print("✓ Simple conditional test passed")

if __name__ == "__main__":
    test_basic_loop_pattern()
    test_simple_conditional()