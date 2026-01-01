#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_goto_operation():
    """Test that goto operation creates proper unconditional jump"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Create goto command
    goto_cmd = vmcommand("goto", None, "LOOP_START", None)
    
    # Execute goto operation
    emitter.goto(goto_cmd)
    
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
    
    # Verify assembly contains the goto
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Check that goto is created with proper jump
    assert "@LOOP_START" in assembly_text, f"@LOOP_START not found in assembly: {assembly_text}"
    assert "0;JMP" in assembly_text, f"0;JMP not found in assembly: {assembly_text}"
    
    print("✓ Goto operation test passed")

if __name__ == "__main__":
    test_goto_operation()