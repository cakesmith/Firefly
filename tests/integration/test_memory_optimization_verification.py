#!/usr/bin/env python3
"""
Verification test for enhanced control flow memory optimization
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from Petri.VMToPetri import VMToPetriTranslator

def test_memory_optimization_verification():
    """
    Verify that the enhanced memory optimization correctly handles control flow places
    """
    print("Testing enhanced memory optimization verification...")
    
    # Create translator
    translator = VMToPetriTranslator()
    
    # Execute a simple program to create some basic places
    commands = [
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("add",),
        ("return",)
    ]
    
    print(f"Executing program to create basic places...")
    result = translator.execute_program(commands)
    print(f"Program result: {result}")
    
    # Create various types of control flow places to test optimization
    print("\nCreating diverse control flow constructs...")
    
    # Create multiple labels
    for i in range(5):
        translator.control_flow.define_label(f"LABEL_{i}")
    
    # Create goto source places
    for i in range(3):
        goto_place = translator.net.add_place(translator.get_unique_place_name(f"goto_source_LABEL_{i}"))
    
    # Create if-goto continue places
    for i in range(4):
        continue_place = translator.net.add_place(translator.get_unique_place_name(f"if_goto_continue_LABEL_{i}"))
    
    # Create some general control places
    for i in range(2):
        control_place = translator.net.add_place(translator.get_unique_place_name(f"control_{i}"))
    
    print(f"Created control flow constructs. Total places: {len(translator.net.places)}")
    
    # Test the enhanced memory optimization
    print("\nRunning enhanced memory optimization...")
    memory_map = translator._optimize_memory_allocation()
    
    # Verify results
    total_places = len(translator.net.places)
    memory_locations = memory_map['total_locations']
    control_flow_savings = memory_map.get('control_flow_savings', 0)
    
    print(f"\nMemory Optimization Results:")
    print(f"  Total places: {total_places}")
    print(f"  Memory locations used: {memory_locations}")
    print(f"  Total memory savings: {total_places - memory_locations}")
    print(f"  Control flow specific savings: {control_flow_savings}")
    
    # Calculate efficiency
    efficiency = (total_places - memory_locations) / total_places * 100 if total_places > 0 else 0
    print(f"  Memory efficiency: {efficiency:.1f}%")
    
    # Verify control flow places are properly handled
    control_flow_places = []
    for place_name in translator.net.places.keys():
        if translator._is_control_flow_place(place_name):
            control_flow_places.append(place_name)
    
    print(f"\nControl Flow Analysis:")
    print(f"  Control flow places found: {len(control_flow_places)}")
    
    # Check that control flow places are in the memory map
    cf_places_in_map = 0
    for place_name in control_flow_places:
        if place_name in memory_map['location_map']:
            cf_places_in_map += 1
    
    print(f"  Control flow places in memory map: {cf_places_in_map}")
    
    # Verify memory sharing for control flow places
    shared_locations = 0
    for location, places in memory_map['location_to_places'].items():
        if len(places) > 1:
            # Check if any control flow places are sharing this location
            cf_places_sharing = [p for p in places if translator._is_control_flow_place(p)]
            if cf_places_sharing:
                shared_locations += 1
                print(f"  Location @{location} shared by {len(places)} places ({len(cf_places_sharing)} control flow)")
    
    print(f"  Shared locations with control flow places: {shared_locations}")
    
    # Test success criteria
    success_criteria = [
        ("All places have memory locations", cf_places_in_map == len(control_flow_places)),
        ("Memory efficiency > 20%", efficiency > 20),
        ("Control flow savings > 0", control_flow_savings > 0),
        ("Some memory sharing occurs", shared_locations > 0)
    ]
    
    print(f"\nSuccess Criteria:")
    all_passed = True
    for criterion, passed in success_criteria:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {criterion}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print(f"\n✅ Enhanced memory optimization verification PASSED")
        return True
    else:
        print(f"\n❌ Enhanced memory optimization verification FAILED")
        return False

if __name__ == "__main__":
    success = test_memory_optimization_verification()
    sys.exit(0 if success else 1)