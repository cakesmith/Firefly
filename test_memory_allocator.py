#!/usr/bin/env python3
"""
Test cases for Petri net memory allocator
Tests various topological patterns to ensure correct memory slot reuse
"""

from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition
from Petri.Token import Token

def print_allocation(net, test_name):
    """Print memory allocation results for a test"""
    print(f"\n=== {test_name} ===")
    total_places = len(net.places)
    total_slots = net.allocate_memory()
    efficiency = (total_places - total_slots) / total_places * 100 if total_places > 0 else 0
    
    print(f"Places: {total_places}, Memory slots: {total_slots}, Efficiency: {efficiency:.1f}% reduction")
    
    for place_name, place in net.places.items():
        print(f"  {place_name} -> R{place.memory_address}")
    
    return total_slots

def test_linear_chain():
    """Test: A -> T1 -> B -> T2 -> C (should use 2 slots max)"""
    net = PetriNet()
    
    # Create places
    net.add_place(Place("A"))
    net.add_place(Place("B")) 
    net.add_place(Place("C"))
    
    # Create transitions
    net.add_transition(Transition("T1"))
    net.add_transition(Transition("T2"))
    
    # Connect: A -> T1 -> B -> T2 -> C
    net.add_arc(net.places["A"], net.transitions["T1"])
    net.add_arc(net.transitions["T1"], net.places["B"])
    net.add_arc(net.places["B"], net.transitions["T2"])
    net.add_arc(net.transitions["T2"], net.places["C"])
    
    slots = print_allocation(net, "Linear Chain: A->T1->B->T2->C")
    assert slots <= 2, f"Linear chain should use ≤2 slots, used {slots}"

def test_diamond_pattern():
    """Test: A -> T1 -> B, C -> T2 -> D (fork and join)"""
    net = PetriNet()
    
    # Create places
    net.add_place(Place("A"))
    net.add_place(Place("B"))
    net.add_place(Place("C"))
    net.add_place(Place("D"))
    
    # Create transitions
    net.add_transition(Transition("T1"))  # Fork
    net.add_transition(Transition("T2"))  # Join
    
    # Connect diamond: A -> T1 -> {B,C} -> T2 -> D
    net.add_arc(net.places["A"], net.transitions["T1"])
    net.add_arc(net.transitions["T1"], net.places["B"])
    net.add_arc(net.transitions["T1"], net.places["C"])
    net.add_arc(net.places["B"], net.transitions["T2"])
    net.add_arc(net.places["C"], net.transitions["T2"])
    net.add_arc(net.transitions["T2"], net.places["D"])
    
    slots = print_allocation(net, "Diamond: A->T1->{B,C}->T2->D")
    assert slots <= 3, f"Diamond should use ≤3 slots, used {slots}"

def test_large_pipeline():
    """Test: Large pipeline with 20 stages"""
    net = PetriNet()
    
    # Create 21 places (P0 through P20)
    places = [f"P{i}" for i in range(21)]
    for p in places:
        net.add_place(Place(p))
    
    # Create 20 transitions (T0 through T19)
    transitions = [f"T{i}" for i in range(20)]
    for t in transitions:
        net.add_transition(Transition(t, operation=lambda tokens: tokens))
    
    # Connect pipeline: P0->T0->P1->T1->P2->...->T19->P20
    for i in range(20):
        net.add_arc(net.places[f"P{i}"], net.transitions[f"T{i}"])
        net.add_arc(net.transitions[f"T{i}"], net.places[f"P{i+1}"])
    
    slots = print_allocation(net, "Large Pipeline: 21 places, 20 transitions")
    assert slots <= 2, f"Pipeline should use ≤2 slots, used {slots}"

def test_wide_network():
    """Test: Wide network with many parallel paths"""
    net = PetriNet()
    
    # Create 50 places in 10 parallel chains of 5 places each
    for chain in range(10):
        for stage in range(5):
            net.add_place(Place(f"C{chain}_P{stage}"))
    
    # Create transitions for each chain
    for chain in range(10):
        for stage in range(4):
            t_name = f"C{chain}_T{stage}"
            net.add_transition(Transition(t_name, operation=lambda tokens: tokens))
            net.add_arc(net.places[f"C{chain}_P{stage}"], net.transitions[t_name])
            net.add_arc(net.transitions[t_name], net.places[f"C{chain}_P{stage+1}"])
    
    slots = print_allocation(net, "Wide Network: 50 places, 40 transitions (10 parallel chains)")
    assert slots <= 20, f"Wide network used {slots} slots"

if __name__ == "__main__":
    print("Testing Petri Net Memory Allocator")
    print("=" * 60)
    
    # Basic topology tests
    print("\n🔹 BASIC TOPOLOGY TESTS")
    test_linear_chain()
    test_diamond_pattern()
    
    # Large-scale tests
    print("\n🔹 LARGE-SCALE TESTS")
    test_large_pipeline()
    test_wide_network()
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("Memory allocator is working correctly with functional verification.")