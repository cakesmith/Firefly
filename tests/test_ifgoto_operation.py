#!/usr/bin/env python3
"""
Test if-goto operation with Petri net semantics.

In the Petri net model, if-goto creates a conditional branch:
- If condition is true (non-zero): token goes to target label place
- If condition is false (zero): token goes to fallthrough place

This is implemented via the transition's operation function, not assembly jumps.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand
from Petri.Token import Token

def test_ifgoto_operation():
    """Test that if-goto operation creates proper Petri net structure"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # First push a constant to have something on the stack for if-goto to consume
    push_cmd = vmcommand("push", "constant", 5, None)
    emitter.push_constant(push_cmd)
    
    # Create if-goto command
    ifgoto_cmd = vmcommand("if-goto", "LOOP_START", None, None)
    
    # Execute if-goto operation
    emitter.ifgoto(ifgoto_cmd)
    
    # Verify Petri net structure
    # 1. Label place should exist
    assert hasattr(emitter.net, 'labels'), "Labels registry not created"
    assert "LOOP_START" in emitter.net.labels, "LOOP_START not in labels registry"
    
    # 2. An ifgoto transition should exist
    ifgoto_transitions = [t for t in emitter.net.transitions.values() 
                         if t.name.startswith("ifgoto_")]
    assert len(ifgoto_transitions) == 1, f"Expected 1 ifgoto transition, found {len(ifgoto_transitions)}"
    
    ifgoto_trans = ifgoto_transitions[0]
    
    # 3. The ifgoto transition should have 2 output places (label and fallthrough)
    assert len(ifgoto_trans.out_places) == 2, \
        f"ifgoto should have 2 outputs, found {len(ifgoto_trans.out_places)}"
    
    # 4. One output should be the label place
    label_place = emitter.net.labels["LOOP_START"]
    assert label_place in ifgoto_trans.out_places, "Label place should be an output"
    
    # 5. The other output should be a fallthrough place
    fallthrough_places = [p for p in ifgoto_trans.out_places if p != label_place]
    assert len(fallthrough_places) == 1, "Should have exactly one fallthrough place"
    fallthrough = fallthrough_places[0]
    assert "fallthrough" in fallthrough.name, f"Fallthrough place name: {fallthrough.name}"
    
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
    
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Should contain the push constant setup
    assert "@5" in assembly_text, f"@5 (constant) not found in assembly: {assembly_text}"
    
    # Should contain indication of condition check
    assert "if-goto" in assembly_text.lower() or "condition" in assembly_text.lower(), \
        f"Assembly should indicate conditional: {assembly_text}"
    
    print("✓ If-goto operation test passed (Petri net semantics)")

def test_ifgoto_operation_semantics():
    """Test that ifgoto operation function correctly routes tokens"""
    
    emitter = PetriEmitter()
    
    # Push a value
    push_cmd = vmcommand("push", "constant", 5, None)
    emitter.push_constant(push_cmd)
    
    # Create if-goto
    ifgoto_cmd = vmcommand("if-goto", "TARGET", None, None)
    emitter.ifgoto(ifgoto_cmd)
    
    # Get the ifgoto transition
    ifgoto_trans = [t for t in emitter.net.transitions.values() 
                   if t.name.startswith("ifgoto_")][0]
    
    # Test the operation function with true condition (non-zero)
    true_result = ifgoto_trans.operation([Token(5)])  # 5 is truthy
    assert true_result[0] is not None, "True condition should produce token for label"
    assert true_result[1] is None, "True condition should NOT produce token for fallthrough"
    
    # Test with false condition (zero)
    false_result = ifgoto_trans.operation([Token(0)])  # 0 is falsy
    assert false_result[0] is None, "False condition should NOT produce token for label"
    assert false_result[1] is not None, "False condition should produce token for fallthrough"
    
    print("✓ If-goto operation semantics test passed")

if __name__ == "__main__":
    test_ifgoto_operation()
    test_ifgoto_operation_semantics()
