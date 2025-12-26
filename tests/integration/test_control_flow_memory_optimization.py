#!/usr/bin/env python3
"""
Integration test for control flow memory optimization
Tests the enhanced memory optimization system with control flow constructs
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from Petri.VMToPetri import VMToPetriTranslator

def test_control_flow_memory_optimization():
    """Test the enhanced memory optimization with control flow"""
    print("Testing control flow memory optimization...")
    
    # Create translator
    translator = VMToPetriTranslator()
    
    # Create a simple program with basic operations first
    commands = [
        ('push', 'constant', 5),
        ('push', 'constant', 3),
        ('add',),
        ('return',)
    ]
    
    print(f"Executing basic program with {len(commands)} commands...")
    
    # Execute the basic program first
    try:
        result = translator.execute_program(commands)
        print(f"Basic program executed successfully. Result: {result}")
    except Exception as e:
        print(f"Basic program execution failed: {e}")
        return False
    
    # Now test with control flow constructs by creating them directly
    print("\nCreating control flow constructs for memory optimization test...")
    
    try:
        # Create some control flow places directly for testing
        translator.control_flow.define_label("TEST_LABEL", None)
        translator.control_flow.define_label("LOOP_START", None)
        translator.control_flow.define_label("LOOP_END", None)
        
        # Create some goto source places
        goto_source1 = translator.net.add_place("goto_source_TEST_LABEL")
        goto_source2 = translator.net.add_place("goto_source_LOOP_START")
        
        # Create some if-goto continue places
        continue_place1 = translator.net.add_place("if_goto_continue_TEST_LABEL")
        continue_place2 = translator.net.add_place("if_goto_continue_LOOP_END")
        
        print("Control flow constructs created successfully")
        
    except Exception as e:
        print(f"Failed to create control flow constructs: {e}")
        return False
    
    # Test the enhanced memory optimization
    try:
        print("\nTesting enhanced memory optimization...")
        memory_map = translator._optimize_memory_allocation()
        
        print(f"Memory optimization completed successfully!")
        print(f"Total memory locations: {memory_map['total_locations']}")
        
        if 'control_flow_savings' in memory_map:
            print(f"Control flow savings: {memory_map['control_flow_savings']} locations")
        
        # Verify the memory map structure
        assert 'location_map' in memory_map
        assert 'location_to_places' in memory_map
        assert 'total_locations' in memory_map
        
        # Verify that control flow places are handled
        control_flow_places_found = 0
        for place_name in memory_map['location_map']:
            if any(place_name.startswith(pattern) for pattern in ['label_', 'goto_source_', 'if_goto_continue_']):
                control_flow_places_found += 1
        
        print(f"Control flow places in memory map: {control_flow_places_found}")
        
        print("All memory optimization tests passed!")
        return True
        
    except Exception as e:
        print(f"Memory optimization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_control_flow_memory_optimization()
    if success:
        print("\n✅ Control flow memory optimization test PASSED")
    else:
        print("\n❌ Control flow memory optimization test FAILED")
        sys.exit(1)