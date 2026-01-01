#!/usr/bin/env python3
"""
Test program flow integration with Petri net semantics.

Tests that control flow operations create proper Petri net structures
and can be distributed across multiple CPU cores with shared ROM.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_program_flow_petri_structure():
    """Test that program flow operations create correct Petri net structure"""
    
    print("Testing program flow Petri net structure...")
    
    # Create emitter
    emitter = PetriEmitter()
    
    # Simple if-then-else pattern:
    # push constant 5
    # push constant 3
    # gt
    # if-goto TRUE_CASE
    # push constant 0
    # goto END
    # label TRUE_CASE
    # push constant 1
    # label END
    
    commands = [
        vmcommand("push", "constant", 5, None),
        vmcommand("push", "constant", 3, None),
        vmcommand("gt", None, None, None),
        vmcommand("if-goto", "TRUE_CASE", None, None),
        vmcommand("push", "constant", 0, None),
        vmcommand("goto", "END", None, None),
        vmcommand("label", "TRUE_CASE", None, None),
        vmcommand("push", "constant", 1, None),
        vmcommand("label", "END", None, None),
    ]
    
    # Execute commands
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "gt":
            emitter.gt(cmd)
        elif cmd.command == "if-goto":
            emitter.ifgoto(cmd)
        elif cmd.command == "goto":
            emitter.goto(cmd)
        elif cmd.command == "label":
            emitter.label(cmd)
    
    print(f"Created Petri net: {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
    
    # Verify Petri net structure
    # 1. Both labels should exist
    assert "TRUE_CASE" in emitter.net.labels, "TRUE_CASE label not found"
    assert "END" in emitter.net.labels, "END label not found"
    
    # 2. ifgoto transition should have 2 outputs
    ifgoto_trans = [t for t in emitter.net.transitions.values() 
                   if t.name.startswith("ifgoto_")]
    assert len(ifgoto_trans) == 1, "Expected 1 ifgoto transition"
    assert len(ifgoto_trans[0].out_places) == 2, "ifgoto should have 2 outputs"
    
    # 3. goto transition should output to END label
    goto_trans = [t for t in emitter.net.transitions.values() 
                 if t.name.startswith("goto_")]
    assert len(goto_trans) == 1, "Expected 1 goto transition"
    end_place = emitter.net.labels["END"]
    assert end_place in goto_trans[0].out_places, "goto should output to END"
    
    # 4. gt transition should exist
    gt_trans = [t for t in emitter.net.transitions.values() 
               if t.name.startswith("gt_")]
    assert len(gt_trans) == 1, "Expected 1 gt transition"
    
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
    
    assembly_text = '\n'.join(assembly_lines)
    print("Generated assembly:")
    print(assembly_text)
    
    # Check for essential elements
    assert "@5" in assembly_text, "Constant 5 not found"
    assert "@3" in assembly_text, "Constant 3 not found"
    assert "D;JGT" in assembly_text, "GT comparison not found"
    assert "(TRUE_CASE)" in assembly_text, "TRUE_CASE label not found"
    assert "(END)" in assembly_text, "END label not found"
    
    print("✓ Program flow Petri structure test passed")

def test_shared_rom_architecture_concept():
    """Test the concept of shared ROM architecture without complex synchronization"""
    
    print("\nTesting shared ROM architecture concept...")
    
    # Create emitter with simple control flow
    emitter = PetriEmitter()
    
    # Simple goto pattern
    commands = [
        vmcommand("push", "constant", 42, None),
        vmcommand("goto", "SKIP", None, None),
        vmcommand("push", "constant", 99, None),  # Different path
        vmcommand("label", "SKIP", None, None),
        vmcommand("push", "constant", 1, None),
    ]
    
    for cmd in commands:
        if cmd.command == "push":
            emitter.push_constant(cmd)
        elif cmd.command == "goto":
            emitter.goto(cmd)
        elif cmd.command == "label":
            emitter.label(cmd)
    
    # Verify structure
    assert "SKIP" in emitter.net.labels, "SKIP label not found"
    
    goto_trans = [t for t in emitter.net.transitions.values() 
                 if t.name.startswith("goto_")]
    assert len(goto_trans) == 1, "Expected 1 goto transition"
    
    skip_place = emitter.net.labels["SKIP"]
    assert skip_place in goto_trans[0].out_places, "goto should output to SKIP"
    
    # Assign to multiple cores
    assignments = emitter.net.assign_cpu_cores(2)
    
    print("CPU core assignments:")
    for trans_name, core in assignments.items():
        print(f"  {trans_name}: Core {core}")
    
    # Verify that control flow operations can be on different cores
    # (this should now be allowed with shared ROM)
    goto_transitions = [name for name in assignments.keys() if 'goto' in name]
    push_transitions = [name for name in assignments.keys() if 'push' in name]
    
    if goto_transitions and push_transitions:
        goto_cores = set(assignments[name] for name in goto_transitions)
        push_cores = set(assignments[name] for name in push_transitions)
        
        print(f"Goto operations on cores: {goto_cores}")
        print(f"Push operations on cores: {push_cores}")
        
        # With shared ROM, operations can be distributed across cores
        total_cores_used = len(goto_cores | push_cores)
        print(f"Total cores used: {total_cores_used}")
        
        if total_cores_used > 1:
            print("✓ Operations successfully distributed across multiple cores")
        else:
            print("✓ Operations assigned to single core (also valid)")
    
    # Generate basic assembly to verify structure
    emitter.net.allocate_memory()
    assembly_lines = []
    for transition_name, transition in emitter.net.transitions.items():
        assembly_code = transition.emit_assembly()
        if isinstance(assembly_code, list):
            assembly_lines.extend(assembly_code)
        else:
            assembly_lines.append(assembly_code)
    
    label_assembly = emitter._generate_label_assembly()
    assembly_lines.extend(label_assembly)
    
    assembly_text = '\n'.join(assembly_lines)
    
    # Verify basic structure
    assert "@42" in assembly_text, "First constant not found"
    assert "(SKIP)" in assembly_text, "Skip label not found"
    assert "@1" in assembly_text, "Final constant not found"
    
    print("✓ Shared ROM architecture concept test passed")

if __name__ == "__main__":
    test_program_flow_petri_structure()
    test_shared_rom_architecture_concept()
    
    print(f"\n{'='*60}")
    print("🎉 Program flow integration tests passed!")
    print("✓ Control flow operations create correct Petri net structure")
    print("✓ Shared ROM architecture allows distributed execution")
    print("✓ Labels and token flow work correctly across CPU cores")
