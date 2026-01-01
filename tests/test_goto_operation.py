#!/usr/bin/env python3
"""
Test goto operation with Petri net semantics.

In the Petri net model, goto doesn't generate assembly jump instructions.
Instead, it creates a transition that outputs a token to the target label's place,
enabling whatever transition follows that label.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_goto_operation():
    """Test that goto operation creates proper Petri net structure for control transfer"""
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Create goto command
    goto_cmd = vmcommand("goto", "LOOP_START", None, None)
    
    # Execute goto operation
    emitter.goto(goto_cmd)
    
    # Verify Petri net structure
    # 1. Label place should exist in the labels registry
    assert hasattr(emitter.net, 'labels'), "Labels registry not created"
    assert "LOOP_START" in emitter.net.labels, "LOOP_START not in labels registry"
    
    # 2. A goto transition should exist
    goto_transitions = [t for t in emitter.net.transitions.values() 
                       if t.name.startswith("goto_")]
    assert len(goto_transitions) == 1, f"Expected 1 goto transition, found {len(goto_transitions)}"
    
    goto_trans = goto_transitions[0]
    
    # 3. The goto transition should output to the label place
    label_place = emitter.net.labels["LOOP_START"]
    assert label_place in goto_trans.out_places, "Goto transition should output to label place"
    
    # 4. The label place should be marked as a label
    assert getattr(label_place, 'is_label', False), "Label place should have is_label=True"
    
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
    
    # With Petri net semantics, goto doesn't generate @LABEL/JMP
    # Instead, it generates a comment indicating control transfer via token
    assert "goto" in assembly_text.lower() or "control" in assembly_text.lower(), \
        f"Assembly should indicate control transfer: {assembly_text}"
    
    print("✓ Goto operation test passed (Petri net semantics)")

def test_goto_creates_forward_reference():
    """Test that goto to undefined label creates forward reference"""
    
    emitter = PetriEmitter()
    
    # Goto to a label that doesn't exist yet
    goto_cmd = vmcommand("goto", "FUTURE_LABEL", None, None)
    emitter.goto(goto_cmd)
    
    # The label place should be created as a forward reference
    assert "FUTURE_LABEL" in emitter.net.labels, "Forward reference label not created"
    
    # Now define the label
    label_cmd = vmcommand("label", "FUTURE_LABEL", None, None)
    emitter.label(label_cmd)
    
    # Should reuse the same place (not create a duplicate)
    label_places = [p for p in emitter.net.places.values() 
                   if getattr(p, 'label_name', None) == "FUTURE_LABEL"]
    assert len(label_places) == 1, f"Expected 1 label place, found {len(label_places)}"
    
    print("✓ Goto forward reference test passed")

if __name__ == "__main__":
    test_goto_operation()
    test_goto_creates_forward_reference()
