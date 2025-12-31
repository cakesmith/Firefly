#!/usr/bin/env python3
"""
Debug the memory allocation algorithm to understand the high reduction rates
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition

def debug_simple_case():
    """Debug a simple case that should NOT allow slot reuse"""
    print("🔍 DEBUGGING MEMORY ALLOCATION")
    print("="*50)
    
    # Create a simple diamond pattern: A -> T1 -> {B, C} -> T2 -> D
    # B and C should be alive simultaneously, so they need different slots
    net = PetriNet()
    
    # Create places
    net.add_place(Place("A"))
    net.add_place(Place("B"))
    net.add_place(Place("C"))
    net.add_place(Place("D"))
    
    # Create transitions
    net.add_transition(Transition("T1"))  # Fork: A -> {B, C}
    net.add_transition(Transition("T2"))  # Join: {B, C} -> D
    
    # Connect the diamond with proper arcs
    net.add_arc(net.places["A"], net.transitions["T1"])
    net.add_arc(net.transitions["T1"], net.places["B"])
    net.add_arc(net.transitions["T1"], net.places["C"])
    net.add_arc(net.places["B"], net.transitions["T2"])
    net.add_arc(net.places["C"], net.transitions["T2"])
    net.add_arc(net.transitions["T2"], net.places["D"])
    
    print("Network structure:")
    print("A -> T1 -> {B, C} -> T2 -> D")
    print("\nB and C are alive simultaneously after T1 fires!")
    print("They CANNOT share the same memory slot.")
    
    # Allocate memory
    slots = net.allocate_memory()
    
    print(f"\nMemory allocation results:")
    for place_name, place in net.places.items():
        print(f"  {place_name} -> R{place.memory_address}")
    
    print(f"\nTotal slots used: {slots}")
    
    # Check if B and C have the same slot (this would be WRONG!)
    b_slot = net.places["B"].memory_address
    c_slot = net.places["C"].memory_address
    
    if b_slot == c_slot:
        print("❌ ERROR: B and C share the same slot - this is incorrect!")
        print("   They can be alive simultaneously, causing data corruption.")
    else:
        print("✅ CORRECT: B and C have different slots")
    
    return b_slot == c_slot

def debug_linear_chain():
    """Debug why linear chains get such extreme reduction"""
    print("\n🔍 DEBUGGING LINEAR CHAIN")
    print("="*50)
    
    # Create: A -> T1 -> B -> T2 -> C -> T3 -> D
    net = PetriNet()
    
    places = ["A", "B", "C", "D"]
    for p in places:
        net.add_place(Place(p))
    
    transitions = ["T1", "T2", "T3"]
    for t in transitions:
        net.add_transition(Transition(t))
    
    # Connect linearly with proper arcs
    connections = [("A", "T1", "B"), ("B", "T2", "C"), ("C", "T3", "D")]
    for source, trans, target in connections:
        net.add_arc(net.places[source], net.transitions[trans])
        net.add_arc(net.transitions[trans], net.places[target])
    
    print("Network structure:")
    print("A -> T1 -> B -> T2 -> C -> T3 -> D")
    print("\nIn a linear chain, only adjacent places can be alive simultaneously.")
    print("So we need at most 2 slots (current + next).")
    
    # Allocate memory
    slots = net.allocate_memory()
    
    print(f"\nMemory allocation results:")
    for place_name in places:
        place = net.places[place_name]
        print(f"  {place_name} -> R{place.memory_address}")
    
    print(f"\nTotal slots used: {slots}")
    
    # Check if all places got the same slot (this might be wrong)
    all_slots = [net.places[p].memory_address for p in places]
    if len(set(all_slots)) == 1:
        print("❌ SUSPICIOUS: All places share one slot")
        print("   This assumes perfect sequential execution with no overlap.")
    else:
        print("✅ REASONABLE: Multiple slots used for safety")


if __name__ == "__main__":
    # Test the algorithm on simple cases
    has_error = debug_simple_case()
    debug_linear_chain()
    
    if has_error:
        print("\n❌ CONCLUSION: The memory allocation algorithm is flawed!")
        print("   The high reduction rates are due to incorrect slot sharing.")
    else:
        print("\n🤔 The algorithm might be more sophisticated than it appears...")