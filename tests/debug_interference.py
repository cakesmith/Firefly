#!/usr/bin/env python3
"""
Debug interference detection to understand why we're getting fewer slots than expected
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Petri.net import PetriNet
from Petri.Place import Place
from Petri.Transition import Transition

def debug_binary_tree():
    """Debug the binary tree case that's using fewer slots than expected"""
    print("🔍 DEBUGGING BINARY TREE INTERFERENCE")
    print("="*60)
    
    net = PetriNet()
    
    # Create a small binary tree for easier analysis
    def create_binary_tree(node_name, depth, max_depth):
        net.add_place(Place(node_name))
        
        if depth < max_depth:
            left_child = f"{node_name}_L"
            right_child = f"{node_name}_R"
            
            # Fork transition
            fork_trans = f"Fork_{node_name}"
            net.add_transition(Transition(fork_trans))
            net.add_arc(net.places[node_name], net.transitions[fork_trans])
            
            # Create children
            create_binary_tree(left_child, depth + 1, max_depth)
            create_binary_tree(right_child, depth + 1, max_depth)
            
            # Connect to children
            net.add_arc(net.transitions[fork_trans], net.places[left_child])
            net.add_arc(net.transitions[fork_trans], net.places[right_child])
    
    # Create depth 3 tree (15 nodes) for easier analysis
    create_binary_tree("Root", 0, 3)
    
    print(f"Created binary tree with {len(net.places)} places")
    
    # Analyze interference
    interference = net._build_interference_graph()
    
    print("\nInterference analysis:")
    for place_name, neighbors in interference.items():
        if neighbors:
            print(f"  {place_name} interferes with: {sorted(neighbors)}")
        else:
            print(f"  {place_name} has no interference")
    
    # Check what we expect vs what we get
    print(f"\nExpected: At each level, sibling nodes should interfere")
    print(f"Level 1: Root_L and Root_R should interfere")
    print(f"Level 2: Root_L_L, Root_L_R should interfere; Root_R_L, Root_R_R should interfere")
    
    # Allocate memory
    slots = net.allocate_memory()
    print(f"\nMemory allocation:")
    for place_name, place in net.places.items():
        print(f"  {place_name} -> R{place.memory_address}")
    
    print(f"\nTotal slots used: {slots}")
    
    # Check if siblings got different slots
    root_l_slot = net.places["Root_L"].memory_address if "Root_L" in net.places else None
    root_r_slot = net.places["Root_R"].memory_address if "Root_R" in net.places else None
    
    if root_l_slot == root_r_slot:
        print("❌ ERROR: Root_L and Root_R share the same slot!")
    else:
        print("✅ CORRECT: Root_L and Root_R have different slots")

def debug_cyclic_case():
    """Debug the cyclic dependencies case"""
    print("\n🔍 DEBUGGING CYCLIC DEPENDENCIES")
    print("="*60)
    
    net = PetriNet()
    
    # Create a cycle: A -> B -> C -> D -> A
    cycle_places = ["A", "B", "C", "D"]
    for p in cycle_places:
        net.add_place(Place(p))
    
    # Create cycle transitions
    for i in range(len(cycle_places)):
        current = cycle_places[i]
        next_place = cycle_places[(i + 1) % len(cycle_places)]
        
        transition_name = f"T_{current}_to_{next_place}"
        net.add_transition(Transition(transition_name))
        net.add_arc(net.places[current], net.transitions[transition_name])
        net.add_arc(net.transitions[transition_name], net.places[next_place])
    
    # Add external connections
    net.add_place(Place("External_In"))
    net.add_place(Place("External_Out"))
    
    net.add_transition(Transition("Feed_Cycle"))
    net.add_arc(net.places["External_In"], net.transitions["Feed_Cycle"])
    net.add_arc(net.transitions["Feed_Cycle"], net.places["A"])
    
    net.add_transition(Transition("Drain_Cycle"))
    net.add_arc(net.places["C"], net.transitions["Drain_Cycle"])
    net.add_arc(net.transitions["Drain_Cycle"], net.places["External_Out"])
    
    print(f"Created cyclic network with {len(net.places)} places")
    
    # Analyze interference
    interference = net._build_interference_graph()
    
    print("\nInterference analysis:")
    for place_name, neighbors in interference.items():
        if neighbors:
            print(f"  {place_name} interferes with: {sorted(neighbors)}")
        else:
            print(f"  {place_name} has no interference")
    
    print(f"\nExpected: In a cycle, places could potentially all be active")
    print(f"But our algorithm might not detect this correctly...")
    
    # Allocate memory
    slots = net.allocate_memory()
    print(f"\nMemory allocation:")
    for place_name, place in net.places.items():
        print(f"  {place_name} -> R{place.memory_address}")
    
    print(f"\nTotal slots used: {slots}")

def analyze_interference_algorithm():
    """Analyze potential issues with the interference detection algorithm"""
    print("\n🔍 ANALYZING INTERFERENCE ALGORITHM")
    print("="*60)
    
    print("Potential issues with current algorithm:")
    print("1. Only detects interference through shared transitions")
    print("2. Doesn't consider temporal relationships (what can be alive simultaneously)")
    print("3. Missing reachability analysis for parallel paths")
    print("4. Pipeline overlap detection might be incomplete")
    
    print("\nFor binary trees:")
    print("- Sibling nodes (same parent) can be alive simultaneously")
    print("- Current algorithm only detects this if they share a transition")
    print("- Fork transitions create the interference, but algorithm might miss it")
    
    print("\nFor cycles:")
    print("- In a cycle, multiple places can hold tokens simultaneously")
    print("- Current algorithm might not detect this temporal overlap")
    print("- Need better liveness analysis")

if __name__ == "__main__":
    debug_binary_tree()
    debug_cyclic_case()
    analyze_interference_algorithm()