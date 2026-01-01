#!/usr/bin/env python3
"""
Test label operation with Petri net semantics.

In the Petri net model, a label creates a place that serves as a merge point
for control flow. Control can arrive from:
1. Normal sequential flow (previous operation)
2. goto/if-goto jumps (token placement)

The next operation after the label takes this place as a control input.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_label_creates_place():
    """Test that label operation creates a place in the Petri net"""
    
    emitter = PetriEmitter()
    
    # Create label command
    label_cmd = vmcommand("label", "LOOP_START", None, None)
    emitter.label(label_cmd)
    
    # Verify label place exists
    assert hasattr(emitter.net, 'labels'), "Labels registry not created"
    assert "LOOP_START" in emitter.net.labels, "LOOP_START not in labels registry"
    
    label_place = emitter.net.labels["LOOP_START"]
    
    # Verify place properties
    assert getattr(label_place, 'is_label', False), "Label place should have is_label=True"
    assert label_place.label_name == "LOOP_START", "Label place should have correct label_name"
    
    # Verify pending control place is set
    assert emitter.pending_control_place == label_place, \
        "Label should set pending_control_place for next operation"
    
    print("✓ Label creates place test passed")

def test_label_with_goto():
    """Test that label and goto work together properly"""
    
    emitter = PetriEmitter()
    
    # Create label command
    label_cmd = vmcommand("label", "LOOP_START", None, None)
    emitter.label(label_cmd)
    
    # Create goto command that references the label
    goto_cmd = vmcommand("goto", "LOOP_START", None, None)
    emitter.goto(goto_cmd)
    
    # Verify Petri net structure
    # 1. Label place should exist
    assert "LOOP_START" in emitter.net.labels, "LOOP_START not in labels registry"
    label_place = emitter.net.labels["LOOP_START"]
    
    # 2. Goto transition should output to the label place
    goto_transitions = [t for t in emitter.net.transitions.values() 
                       if t.name.startswith("goto_")]
    assert len(goto_transitions) == 1, f"Expected 1 goto transition"
    
    goto_trans = goto_transitions[0]
    assert label_place in goto_trans.out_places, "Goto should output to label place"
    
    # 3. Only one label place should exist (not duplicated)
    label_places = [p for p in emitter.net.places.values() 
                   if getattr(p, 'label_name', None) == "LOOP_START"]
    assert len(label_places) == 1, f"Expected 1 label place, found {len(label_places)}"
    
    # Allocate memory
    emitter.net.allocate_memory()
    
    # Generate assembly
    assembly_lines = []
    for transition_name, transition in emitter.net.transitions.items():
        assembly_code = transition.emit_assembly()
        if isinstance(assembly_code, list):
            assembly_lines.extend(assembly_code)
        else:
            assembly_lines.append(assembly_code)
    
    # Add label assembly from the helper method
    label_assembly = emitter._generate_label_assembly()
    assembly_lines.extend(label_assembly)
    
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # With Petri net semantics, we should see the label in the generated assembly
    # The _generate_label_assembly method creates (LABEL_NAME) entries
    assert "(LOOP_START)" in assembly_text, f"Label (LOOP_START) not found in assembly: {assembly_text}"
    
    print("✓ Label with goto test passed (Petri net semantics)")

def test_forward_reference_label():
    """Test that goto before label creates forward reference that gets resolved"""
    
    emitter = PetriEmitter()
    
    # Goto to a label that doesn't exist yet (forward reference)
    goto_cmd = vmcommand("goto", "FUTURE", None, None)
    emitter.goto(goto_cmd)
    
    # Label place should be created as forward reference
    assert "FUTURE" in emitter.net.labels, "Forward reference should create label entry"
    forward_place = emitter.net.labels["FUTURE"]
    
    # Now define the label
    label_cmd = vmcommand("label", "FUTURE", None, None)
    emitter.label(label_cmd)
    
    # Should reuse the same place
    resolved_place = emitter.net.labels["FUTURE"]
    assert forward_place is resolved_place, "Label should reuse forward reference place"
    
    # Only one place with this label name should exist
    label_places = [p for p in emitter.net.places.values() 
                   if getattr(p, 'label_name', None) == "FUTURE"]
    assert len(label_places) == 1, f"Expected 1 label place, found {len(label_places)}"
    
    print("✓ Forward reference label test passed")

if __name__ == "__main__":
    test_label_creates_place()
    test_label_with_goto()
    test_forward_reference_label()
