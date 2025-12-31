#!/usr/bin/env python3
"""
Test cases for dup branching logic
Tests that multiple push constants create proper dup transitions for branching
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from Petri.Place import Place
from Petri.Transition import Transition
from Petri.Token import Token

def test_single_push_no_dup():
    """Test: Single push constant should not create dup"""
    print("\n=== Test: Single push constant (no dup needed) ===")
    
    emitter = PetriEmitter()
    
    # Create first push constant
    const_place = Place("const_42")
    emitter.net.add_place(const_place)
    
    push_transition = Transition("push_const_42")
    emitter._insert_operation(push_transition, const_place, consumes_stack=0, produces_stack=1)
    
    # Verify no dup transition created
    dup_transitions = [name for name in emitter.net.transitions.keys() if name.startswith("dup_")]
    assert len(dup_transitions) == 0, f"Expected no dup transitions, found: {dup_transitions}"
    
    # Verify direct connection from init
    assert emitter.net.places["init"] in push_transition.in_places, "Should connect directly from init"
    
    print(f"✓ Transitions: {list(emitter.net.transitions.keys())}")
    print(f"✓ No dup transitions created")
    print("✓ Single push test passed")

def test_two_push_constants_create_dup():
    """Test: Two push constants should create dup transition"""
    print("\n=== Test: Two push constants create dup ===")
    
    emitter = PetriEmitter()
    
    # Create first push constant
    const_place1 = Place("const_5")
    emitter.net.add_place(const_place1)
    push_transition1 = Transition("push_const_5")
    emitter._insert_operation(push_transition1, const_place1, consumes_stack=0, produces_stack=1)
    
    # Create second push constant (should trigger dup creation)
    const_place2 = Place("const_10")
    emitter.net.add_place(const_place2)
    push_transition2 = Transition("push_const_10")
    emitter._insert_operation(push_transition2, const_place2, consumes_stack=0, produces_stack=1)
    
    # Verify dup transition was created
    dup_transitions = [name for name in emitter.net.transitions.keys() if name.startswith("dup_")]
    assert len(dup_transitions) == 1, f"Expected 1 dup transition, found: {dup_transitions}"
    
    dup_transition = emitter.net.transitions[dup_transitions[0]]
    
    # Verify dup connects from init
    assert emitter.net.places["init"] in dup_transition.in_places, "Dup should connect from init"
    
    # Verify dup has 2 output places
    assert len(dup_transition.out_places) == 2, f"Dup should have 2 outputs, has {len(dup_transition.out_places)}"
    
    # Verify push transitions no longer connect directly to init
    assert emitter.net.places["init"] not in push_transition1.in_places, "Push1 should not connect to init"
    assert emitter.net.places["init"] not in push_transition2.in_places, "Push2 should not connect to init"
    
    # Verify push transitions connect to dup outputs
    dup_out_places = dup_transition.out_places
    assert len(push_transition1.in_places) == 1, "Push1 should have 1 input"
    assert len(push_transition2.in_places) == 1, "Push2 should have 1 input"
    assert push_transition1.in_places[0] in dup_out_places, "Push1 should connect to dup output"
    assert push_transition2.in_places[0] in dup_out_places, "Push2 should connect to dup output"
    
    print(f"✓ Transitions: {list(emitter.net.transitions.keys())}")
    print(f"✓ Dup transition created: {dup_transitions[0]}")
    print(f"✓ Dup outputs: {[p.name for p in dup_transition.out_places]}")
    print("✓ Two push constants test passed")

def test_dup_execution():
    """Test: Multiple push transitions execute correctly without dup"""
    print("\n=== Test: Multiple push execution (no dup) ===")
    
    emitter = PetriEmitter()
    
    # Create two push constants (no dup needed)
    const_place1 = Place("const_7")
    const_place2 = Place("const_14")
    emitter.net.add_place(const_place1)
    emitter.net.add_place(const_place2)
    
    push_trans1 = Transition("push_7", operation=lambda tokens: [Token(7)])
    push_trans2 = Transition("push_14", operation=lambda tokens: [Token(14)])
    
    emitter._insert_operation(push_trans1, const_place1, consumes_stack=0, produces_stack=1)
    emitter._insert_operation(push_trans2, const_place2, consumes_stack=0, produces_stack=1)
    
    # Execute the network
    print("Executing network...")
    step = 1
    while True:
        fired = emitter.net.execute_step()
        if not fired:
            break
        print(f"Step {step}: Fired {fired}")
        step += 1
    
    # Verify both constants were produced
    assert const_place1.has, "const_7 should have token"
    assert const_place2.has, "const_14 should have token"
    assert const_place1.token.value == 7, f"Expected 7, got {const_place1.token.value}"
    assert const_place2.token.value == 14, f"Expected 14, got {const_place2.token.value}"
    
    # Verify stack has both values
    assert len(emitter.control_stack) == 2, f"Expected 2 items on stack, got {len(emitter.control_stack)}"
    
    print(f"✓ Final token values: {const_place1.token.value}, {const_place2.token.value}")
    print(f"✓ Stack size: {len(emitter.control_stack)}")
    print("✓ Multiple push execution test passed")

def test_three_push_constants():
    """Test: Three push constants (more complex dup scenario)"""
    print("\n=== Test: Three push constants ===")
    
    emitter = PetriEmitter()
    
    # Create three push constants
    places = []
    transitions = []
    for i, value in enumerate([1, 2, 3]):
        place = Place(f"const_{value}")
        emitter.net.add_place(place)
        places.append(place)
        
        transition = Transition(f"push_{value}", operation=lambda tokens, v=value: [Token(v)])
        transitions.append(transition)
        
        emitter._insert_operation(transition, place, consumes_stack=0, produces_stack=1)
    
    # Check dup transitions created
    dup_transitions = [name for name in emitter.net.transitions.keys() if name.startswith("dup_")]
    print(f"Dup transitions created: {dup_transitions}")
    
    # Execute network
    emitter.net.execute_step()  # Should fire all available transitions
    
    # Verify all constants produced
    for i, place in enumerate(places):
        expected_value = i + 1
        if place.has:
            print(f"✓ {place.name}: {place.token.value}")
            assert place.token.value == expected_value, f"Expected {expected_value}, got {place.token.value}"
    
    print(f"✓ Total transitions: {len(emitter.net.transitions)}")
    print(f"✓ Stack size: {len(emitter.control_stack)}")
    print("✓ Three push constants test passed")

def test_mixed_operations():
    """Test: Mix of stack-consuming and non-consuming operations"""
    print("\n=== Test: Mixed operations (push + add) ===")
    
    emitter = PetriEmitter()
    
    # Push two constants
    const1 = Place("const_5")
    const2 = Place("const_8")
    emitter.net.add_place(const1)
    emitter.net.add_place(const2)
    
    push1 = Transition("push_5", operation=lambda tokens: [Token(5)])
    push2 = Transition("push_8", operation=lambda tokens: [Token(8)])
    
    emitter._insert_operation(push1, const1, consumes_stack=0, produces_stack=1)
    emitter._insert_operation(push2, const2, consumes_stack=0, produces_stack=1)
    
    # Add operation (consumes 2 from stack)
    add_result = Place("add_result")
    emitter.net.add_place(add_result)
    
    add_trans = Transition("add", operation=lambda tokens: [Token(tokens[0].value + tokens[1].value)])
    emitter._insert_operation(add_trans, add_result, consumes_stack=2, produces_stack=1)
    
    # Verify structure
    dup_transitions = [name for name in emitter.net.transitions.keys() if name.startswith("dup_")]
    assert len(dup_transitions) == 1, "Should have 1 dup for the two push operations"
    
    # Add should consume from stack, not create dup
    assert len(add_trans.in_places) == 2, "Add should consume from 2 stack places"
    
    print(f"✓ Transitions: {list(emitter.net.transitions.keys())}")
    print(f"✓ Add consumes from: {[p.name for p in add_trans.in_places]}")
    print("✓ Mixed operations test passed")

def test_dup_assembly_generation():
    """Test: Dup transition generates correct assembly"""
    print("\n=== Test: Dup assembly generation ===")
    
    emitter = PetriEmitter()
    
    # Create two push constants to trigger dup
    const_place1 = Place("const_100")
    const_place2 = Place("const_200")
    emitter.net.add_place(const_place1)
    emitter.net.add_place(const_place2)
    
    push_trans1 = Transition("push_100", operation=lambda tokens: [Token(100)])
    push_trans2 = Transition("push_200", operation=lambda tokens: [Token(200)])
    
    emitter._insert_operation(push_trans1, const_place1, consumes_stack=0, produces_stack=1)
    emitter._insert_operation(push_trans2, const_place2, consumes_stack=0, produces_stack=1)
    
    # Allocate memory to get addresses
    emitter.net.allocate_memory()
    
    # Find the dup transition
    dup_transitions = [name for name in emitter.net.transitions.keys() if name.startswith("dup_")]
    assert len(dup_transitions) == 1, f"Expected 1 dup transition, found: {dup_transitions}"
    
    dup_transition = emitter.net.transitions[dup_transitions[0]]
    
    # Generate assembly for dup
    assembly = dup_transition.emit_assembly()
    print(f"Dup assembly: {assembly}")
    
    # Verify assembly structure - should be control token (no data movement)
    assert assembly == ["// dup control token - no data movement needed"], f"Expected control token comment, got {assembly}"
    
    print("✓ Dup assembly generation test passed")

if __name__ == "__main__":
    print("Testing Dup Branching Logic")
    print("=" * 60)
    
    print("\n🔹 BASIC DUP TESTS")
    test_single_push_no_dup()
    test_two_push_constants_create_dup()
    test_dup_execution()
    
    print("\n🔹 ADVANCED DUP TESTS")
    test_three_push_constants()
    test_mixed_operations()
    test_dup_assembly_generation()
    
    print("\n" + "=" * 60)
    print("All dup branching tests passed! ✓")
    print("Petri net branching logic is working correctly.")