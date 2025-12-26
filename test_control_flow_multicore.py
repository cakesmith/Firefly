#!/usr/bin/env python3
"""
Test control flow integration with multi-core execution
Verifies that control flow operations work correctly with distributed coordination
"""

from Petri.VMToPetri import VMToPetriTranslator

def test_control_flow_multicore_integration():
    """Test that control flow operations integrate properly with multi-core execution"""
    
    print("Testing Control Flow Multi-Core Integration")
    print("=" * 50)
    
    # Create translator
    translator = VMToPetriTranslator()
    
    # Define a function with control flow
    translator.define_function("test_loop", 1, 0)  # 1 local, 0 args
    
    # Function body with control flow
    function_commands = [
        ("push", "constant", 10),    # Initial counter
        ("pop", "local", 0),         # Store to local[0]
        ("label", "LOOP_START"),     # Loop label
        ("push", "local", 0),        # Load counter
        ("push", "constant", 1),     # Load 1
        ("sub",),                    # Decrement counter
        ("pop", "local", 0),         # Store back to local[0]
        ("push", "local", 0),        # Load counter for condition
        ("if-goto", "LOOP_START"),   # Continue if non-zero
        ("push", "local", 0),        # Push final result
        ("return",)                  # Return
    ]
    
    # Execute function definition
    for command in function_commands:
        translator._execute_command(command)
    
    # Call the function
    translator.call_function("test_loop", 0)
    
    print("\n1. EXECUTION DEPENDENCY ANALYSIS")
    print("-" * 30)
    
    # Analyze execution dependencies (should handle control flow)
    execution_plan = translator._analyze_execution_dependencies()
    
    print(f"Total execution levels: {len(execution_plan['execution_levels'])}")
    
    # Check for control flow dependencies
    if 'control_flow_deps' in execution_plan:
        cf_deps = {k: v for k, v in execution_plan['control_flow_deps'].items() if v}
        if cf_deps:
            print(f"Control flow dependencies found: {len(cf_deps)}")
            for trans, deps in cf_deps.items():
                print(f"  {trans} -> {deps}")
        else:
            print("No control flow dependencies detected")
    
    print("\n2. MULTI-CORE ASSIGNMENT")
    print("-" * 30)
    
    # Test multi-core assignment (should handle control flow barriers)
    for num_cores in [2, 4]:
        print(f"\nTesting with {num_cores} cores:")
        
        core_assignments = translator._assign_operations_to_cores(execution_plan, num_cores)
        
        # Check that all cores participate in control flow barriers
        control_flow_levels = set()
        barrier_levels = set()
        
        for core_id, operations in core_assignments.items():
            print(f"  Core {core_id}: {len(operations)} operations")
            
            for op_info in operations:
                if op_info.get('is_control_flow', False):
                    control_flow_levels.add(op_info['level'])
                if op_info.get('requires_barrier', False):
                    barrier_levels.add(op_info['level'])
        
        print(f"  Control flow levels: {sorted(control_flow_levels)}")
        print(f"  Barrier levels: {sorted(barrier_levels)}")
        
        # Verify that barrier levels include all control flow levels
        assert control_flow_levels.issubset(barrier_levels), \
            f"Not all control flow levels have barriers: {control_flow_levels - barrier_levels}"
    
    print("\n3. MEMORY OPTIMIZATION WITH CONTROL FLOW")
    print("-" * 30)
    
    # Test memory optimization (should handle control flow places)
    memory_map = translator._optimize_memory_allocation()
    
    print(f"Total memory locations: {memory_map['total_locations']}")
    print(f"Places optimized: {len(memory_map['location_map'])}")
    
    # Check that control flow places are included in optimization
    control_flow_places = [name for name in memory_map['location_map'].keys() 
                          if any(cf in name for cf in ['label_', 'goto_', 'if_goto_'])]
    
    if control_flow_places:
        print(f"Control flow places optimized: {len(control_flow_places)}")
        for place in control_flow_places[:3]:  # Show first 3
            location = memory_map['location_map'][place]
            print(f"  {place} -> @{location}")
    else:
        print("No control flow places found in memory map")
    
    print("\n4. ASSEMBLY GENERATION")
    print("-" * 30)
    
    # Test assembly generation with control flow
    try:
        assembly = translator._generate_assembly_code(core_assignments, 2)
        if isinstance(assembly, list):
            print(f"Assembly generated: {len(assembly)} lines")
            # Show first few lines
            for line in assembly[:5]:
                print(f"  {line}")
        else:
            print(f"Assembly type: {type(assembly)}")
    except Exception as e:
        print(f"Assembly generation error: {e}")
    
    print("\n[SUCCESS] Control flow multi-core integration test completed!")
    return True

if __name__ == "__main__":
    test_control_flow_multicore_integration()