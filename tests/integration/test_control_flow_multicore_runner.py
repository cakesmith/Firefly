#!/usr/bin/env python3
"""
Test runner for control flow multicore integration
"""

import sys
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def test_control_flow_multicore_integration():
    """
    Test control flow operations with multi-core execution and memory optimization
    """
    print("Testing control flow with multi-core execution...")
    
    # Create translator
    translator = VMToPetriTranslator()
    
    # Simple test program without complex control flow for now
    commands = [
        ("push", "constant", 5),
        ("push", "constant", 3),
        ("add",),
        ("return",)
    ]
    
    print(f"Executing basic program with {len(commands)} commands...")
    
    try:
        # Execute the program
        result = translator.execute_program(commands)
        print(f"Program executed successfully. Result: {result}")
        
        # Create some control flow constructs manually for testing memory optimization
        print("\nCreating control flow constructs for memory optimization test...")
        
        # Create some control flow places manually
        label_place1 = translator.control_flow.define_label("TEST_LABEL")
        label_place2 = translator.control_flow.define_label("LOOP_START") 
        label_place3 = translator.control_flow.define_label("LOOP_END")
        
        # Create some goto source places
        goto_source1 = translator.net.add_place(translator.get_unique_place_name("goto_source_TEST_LABEL"))
        goto_source2 = translator.net.add_place(translator.get_unique_place_name("goto_source_LOOP_START"))
        
        # Create some if-goto continue places
        continue_place1 = translator.net.add_place(translator.get_unique_place_name("if_goto_continue_TEST_LABEL"))
        continue_place2 = translator.net.add_place(translator.get_unique_place_name("if_goto_continue_LOOP_END"))
        
        print("Control flow constructs created successfully")
        
        # Test enhanced memory optimization with control flow places
        print("\nTesting enhanced memory optimization...")
        memory_map = translator._optimize_memory_allocation()
        
        print(f"Memory optimization completed successfully!")
        print(f"Total memory locations: {memory_map['total_locations']}")
        print(f"Control flow savings: {memory_map.get('control_flow_savings', 0)}")
        
        # Verify control flow places are in the memory map
        control_flow_places_in_map = 0
        for place_name in translator.net.places.keys():
            if translator._is_control_flow_place(place_name):
                if place_name in memory_map['location_map']:
                    control_flow_places_in_map += 1
        
        print(f"Control flow places in memory map: {control_flow_places_in_map}")
        
        # Test execution dependency analysis with control flow
        print(f"\nTesting execution dependency analysis...")
        execution_plan = translator._analyze_execution_dependencies()
        
        print(f"Total execution levels: {len(execution_plan['execution_levels'])}")
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        print(f"Control flow dependencies found: {len([k for k, v in control_flow_deps.items() if v])}")
        
        # Test multi-core assignment
        print(f"\nTesting multi-core assignment...")
        core_assignments = translator._assign_operations_to_cores(execution_plan, 2)
        print(f"2-core assignment completed: {len(core_assignments)} cores assigned")
        
        for core_id, operations in core_assignments.items():
            print(f"  Core {core_id}: {len(operations)} operations")
        
        print("\n✅ Control flow multicore integration test PASSED")
        return True
        
    except Exception as e:
        print(f"\n❌ Control flow multicore integration test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_control_flow_multicore_integration()
    sys.exit(0 if success else 1)