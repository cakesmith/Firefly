#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_ifgoto_operation():
    """Test that if-goto operation creates proper conditional jump"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # First push a constant to have something on the stack for if-goto to consume
    push_cmd = vmcommand("push", "constant", 5, None)
    emitter.push_constant(push_cmd)
    
    # Create if-goto command
    ifgoto_cmd = vmcommand("if-goto", None, "LOOP_START", None)
    
    # Execute if-goto operation
    emitter.ifgoto(ifgoto_cmd)
    
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
    
    # Verify assembly contains the if-goto
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Check that if-goto is created with proper conditional jump
    assert "@LOOP_START" in assembly_text, f"@LOOP_START not found in assembly: {assembly_text}"
    assert "D;JNE" in assembly_text, f"D;JNE not found in assembly: {assembly_text}"
    
    # Should also contain the push constant setup
    assert "@5" in assembly_text, f"@5 (constant) not found in assembly: {assembly_text}"
    
    print("✓ If-goto operation test passed")

if __name__ == "__main__":
    test_ifgoto_operation()