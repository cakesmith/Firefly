#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_label_with_goto():
    """Test that label and goto work together properly"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Create label command
    label_cmd = vmcommand("label", None, "LOOP_START", None)
    emitter.label(label_cmd)
    
    # Create goto command that references the label
    goto_cmd = vmcommand("goto", None, "LOOP_START", None)
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
    
    # Add label assembly
    label_assembly = emitter._generate_label_assembly()
    assembly_lines.extend(label_assembly)
    
    # Verify assembly contains both the label and goto
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Check that label is created
    assert "(LOOP_START)" in assembly_text, f"Label (LOOP_START) not found in assembly: {assembly_text}"
    
    # Check that goto references the label
    assert "@LOOP_START" in assembly_text, f"@LOOP_START not found in assembly: {assembly_text}"
    assert "0;JMP" in assembly_text, f"0;JMP not found in assembly: {assembly_text}"
    
    # Check that label place exists in the net
    assert hasattr(emitter.net, 'labels'), "Labels registry not created"
    assert "LOOP_START" in emitter.net.labels, "LOOP_START not in labels registry"
    
    print("✓ Label with goto test passed")

if __name__ == "__main__":
    test_label_with_goto()