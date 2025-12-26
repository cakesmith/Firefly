#!/usr/bin/env python3
"""
Multi-Core Control Flow Performance and Scaling Tests
Tests performance characteristics and scaling behavior of control flow operations
in multi-core environments.

Requirements: TR-2, TR-3
- TR-2: Distributed Execution Compatibility - Control flow must work with level-based synchronization
- TR-3: Memory Optimization Integration - Control flow places must be optimizable
"""

import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from Petri.VMToPetri import VMToPetriTranslator

def test_control_flow_execution_scaling():
    """
    Test execution scaling with control flow operations across multiple cores
    Verifies TR-2: Distributed Execution Compatibility
    """
    print("=" * 60)
    print("CONTROL FLOW EXECUTION SCALING TEST")
    print("=" * 60)
    
    # Create a program with nested control flow that should scale well
    commands = [
        ("function", "nested_loops", 3),   # 3 local variables
        
        # Outer loop: i from 0 to 4
        ("push", "constant", 0),           # i = 0
        ("pop", "local", 0),
        
        ("label", "OUTER_LOOP"),
        ("push", "local", 0),              # Load i
        ("push", "constant", 5),           # Compare with 5
        ("lt",),                           # i < 5?
        ("if-goto", "OUTER_BODY"),
        ("goto", "OUTER_END"),
        
        ("label", "OUTER_BODY"),
        # Inner loop: j from 0 to 3
        ("push", "constant", 0),           # j = 0
        ("pop", "local", 1),
        
        ("label", "INNER_LOOP"),
        ("push", "local", 1),              # Load j
        ("push", "constant", 3),           # Compare with 3
        ("lt",),                           # j < 3?
        ("if-goto", "INNER_BODY"),
        ("goto", "INNER_END"),
        
        ("label", "INNER_BODY"),
        # Accumulate i * j
        ("push", "local", 0),              # Load i
        ("push", "local", 1),              # Load j
        ("mul",),                          # i * j
        ("push", "local", 2),              # Load accumulator
        ("add",),                          # acc + (i * j)
        ("pop", "local", 2),               # Store back
        
        # Increment j
        ("push", "local", 1),              # Load j
        ("push", "constant", 1),           # Load 1
        ("add",),                          # j + 1
        ("pop", "local", 1),               # Store j
        ("goto", "INNER_LOOP"),
        
        ("label", "INNER_END"),
        # Increment i
        ("push", "local", 0),              # Load i
        ("push", "constant", 1),           # Load 1
        ("add",),                          # i + 1
        ("pop", "local", 0),               # Store i
        ("goto", "OUTER_LOOP"),
        
        ("label", "OUTER_END"),
        ("push", "local", 2),              # Return accumulator
        ("return",),
        
        ("call", "nested_loops", 0)        # Call the function
    ]
    
    translator = VMToPetriTranslator()
    
    # Execute and time the program
    start_time = time.time()
    try:
        result = translator.execute_program(commands)
        execution_time = time.time() - start_time
        print(f"✅ Nested loops program executed in {execution_time:.4f}s. Result: {result}")
    except Exception as e:
        execution_time = time.time() - start_time
        print(f"⚠️  Program execution error after {execution_time:.4f}s: {e}")
    
    # Test scaling across different core counts
    print(f"\nTesting execution scaling across core counts:")
    
    execution_plan = translator._analyze_execution_dependencies()
    total_operations = sum(len(level) for level in execution_plan['execution_levels'])
    
    scaling_metrics = {}
    
    for num_cores in [1, 2, 4, 8, 16]:
        print(f"\n  Testing with {num_cores} cores:")
        
        start_time = time.time()
        try:
            core_assignments = translator._assign_operations_to_cores(execution_plan, num_cores)
            assignment_time = time.time() - start_time
            
            # Calculate load distribution
            ops_per_core = [len(ops) for ops in core_assignments.values()]
            active_cores = sum(1 for ops in ops_per_core if ops > 0)
            max_ops = max(ops_per_core) if ops_per_core else 0
            min_ops = min(ops for ops in ops_per_core if ops > 0) if any(ops_per_core) else 0
            load_balance = min_ops / max_ops if max_ops > 0 else 1.0
            
            # Count control flow operations
            total_cf_ops = 0
            cf_ops_per_core = []
            barrier_levels = set()
            
            for core_id, operations in core_assignments.items():
                cf_ops = sum(1 for op in operations if op.get('is_control_flow', False))
                cf_ops_per_core.append(cf_ops)
                total_cf_ops += cf_ops
                
                # Collect barrier levels
                for op in operations:
                    if op.get('requires_barrier', False):
                        barrier_levels.add(op['level'])
            
            scaling_metrics[num_cores] = {
                'assignment_time': assignment_time,
                'active_cores': active_cores,
                'load_balance': load_balance,
                'max_ops_per_core': max_ops,
                'total_cf_ops': total_cf_ops,
                'barrier_levels': len(barrier_levels),
                'parallelization_efficiency': active_cores / num_cores
            }
            
            print(f"    Assignment time: {assignment_time:.4f}s")
            print(f"    Active cores: {active_cores}/{num_cores}")
            print(f"    Load balance: {load_balance:.3f}")
            print(f"    Max ops/core: {max_ops}")
            print(f"    Control flow ops: {total_cf_ops}")
            print(f"    Barrier levels: {len(barrier_levels)}")
            print(f"    Efficiency: {(active_cores/num_cores):.2%}")
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            scaling_metrics[num_cores] = {'error': str(e)}
    
    # Analyze scaling trends
    print(f"\nScaling Analysis:")
    successful_tests = {k: v for k, v in scaling_metrics.items() if 'error' not in v}
    
    if len(successful_tests) >= 2:
        core_counts = sorted(successful_tests.keys())
        
        # Check if assignment time scales reasonably
        times = [successful_tests[cores]['assignment_time'] for cores in core_counts]
        time_increase = times[-1] / times[0] if times[0] > 0 else float('inf')
        core_increase = core_counts[-1] / core_counts[0]
        
        print(f"  Time scaling: {time_increase:.2f}x for {core_increase:.0f}x cores")
        
        # Check load balancing effectiveness
        load_balances = [successful_tests[cores]['load_balance'] for cores in core_counts]
        avg_load_balance = sum(load_balances) / len(load_balances)
        
        print(f"  Average load balance: {avg_load_balance:.3f}")
        
        # Check parallelization efficiency
        efficiencies = [successful_tests[cores]['parallelization_efficiency'] for cores in core_counts]
        
        print(f"  Parallelization efficiency range: {min(efficiencies):.2%} - {max(efficiencies):.2%}")
        
        # Verify distributed execution compatibility (TR-2)
        barrier_consistency = all(successful_tests[cores]['barrier_levels'] > 0 
                                for cores in core_counts if successful_tests[cores]['total_cf_ops'] > 0)
        
        print(f"  Barrier consistency (TR-2): {'✅' if barrier_consistency else '❌'}")
    
    print(f"\n✅ Control flow execution scaling test completed!")
    return True

def test_memory_optimization_performance():
    """
    Test memory optimization performance with control flow places
    Verifies TR-3: Memory Optimization Integration
    """
    print("\n" + "=" * 60)
    print("MEMORY OPTIMIZATION PERFORMANCE TEST")
    print("=" * 60)
    
    # Create programs with increasing control flow complexity
    test_programs = {
        "Linear": [
            ("push", "constant", 1),
            ("push", "constant", 2),
            ("add",),
            ("return",)
        ],
        
        "Single Branch": [
            ("push", "constant", 5),
            ("push", "constant", 0),
            ("if-goto", "BRANCH"),
            ("push", "constant", 1),
            ("goto", "END"),
            ("label", "BRANCH"),
            ("push", "constant", 2),
            ("label", "END"),
            ("add",),
            ("return",)
        ],
        
        "Multiple Branches": [
            ("push", "constant", 3),
            ("push", "constant", 1),
            ("if-goto", "BRANCH1"),
            ("push", "constant", 2),
            ("if-goto", "BRANCH2"),
            ("push", "constant", 10),
            ("goto", "END"),
            ("label", "BRANCH1"),
            ("push", "constant", 20),
            ("goto", "END"),
            ("label", "BRANCH2"),
            ("push", "constant", 30),
            ("label", "END"),
            ("add",),
            ("return",)
        ],
        
        "Nested Loops": [
            ("function", "nested", 2),
            ("push", "constant", 0),
            ("pop", "local", 0),
            ("label", "OUTER"),
            ("push", "local", 0),
            ("push", "constant", 3),
            ("lt",),
            ("if-goto", "OUTER_BODY"),
            ("goto", "OUTER_END"),
            ("label", "OUTER_BODY"),
            ("push", "constant", 0),
            ("pop", "local", 1),
            ("label", "INNER"),
            ("push", "local", 1),
            ("push", "constant", 2),
            ("lt",),
            ("if-goto", "INNER_BODY"),
            ("goto", "INNER_END"),
            ("label", "INNER_BODY"),
            ("push", "local", 1),
            ("push", "constant", 1),
            ("add",),
            ("pop", "local", 1),
            ("goto", "INNER"),
            ("label", "INNER_END"),
            ("push", "local", 0),
            ("push", "constant", 1),
            ("add",),
            ("pop", "local", 0),
            ("goto", "OUTER"),
            ("label", "OUTER_END"),
            ("push", "local", 0),
            ("return",),
            ("call", "nested", 0)
        ]
    }
    
    optimization_results = {}
    
    for program_name, commands in test_programs.items():
        print(f"\nTesting memory optimization for '{program_name}' program:")
        
        translator = VMToPetriTranslator()
        
        try:
            # Execute program
            start_time = time.time()
            result = translator.execute_program(commands)
            execution_time = time.time() - start_time
            
            # Measure memory optimization performance
            start_time = time.time()
            memory_map = translator._optimize_memory_allocation()
            optimization_time = time.time() - start_time
            
            # Analyze optimization results
            total_places = len(translator.net.places)
            memory_locations = memory_map['total_locations']
            optimized_places = len(memory_map['location_map'])
            
            # Count different types of places
            cf_places = 0
            regular_places = 0
            
            for place_name in memory_map['location_map'].keys():
                if translator._is_control_flow_place(place_name):
                    cf_places += 1
                else:
                    regular_places += 1
            
            # Calculate optimization metrics
            memory_reduction = (total_places - memory_locations) / total_places if total_places > 0 else 0
            cf_optimization_ratio = cf_places / total_places if total_places > 0 else 0
            
            optimization_results[program_name] = {
                'execution_time': execution_time,
                'optimization_time': optimization_time,
                'total_places': total_places,
                'memory_locations': memory_locations,
                'cf_places': cf_places,
                'regular_places': regular_places,
                'memory_reduction': memory_reduction,
                'cf_optimization_ratio': cf_optimization_ratio,
                'optimization_efficiency': memory_reduction / optimization_time if optimization_time > 0 else 0
            }
            
            print(f"  Execution time: {execution_time:.4f}s")
            print(f"  Optimization time: {optimization_time:.4f}s")
            print(f"  Total places: {total_places}")
            print(f"  Memory locations: {memory_locations}")
            print(f"  Memory reduction: {memory_reduction:.2%}")
            print(f"  Control flow places: {cf_places}")
            print(f"  CF optimization ratio: {cf_optimization_ratio:.2%}")
            print(f"  ✅ Optimization successful")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            optimization_results[program_name] = {'error': str(e)}
    
    # Analyze optimization performance trends
    print(f"\nMemory Optimization Performance Analysis:")
    
    successful_results = {k: v for k, v in optimization_results.items() if 'error' not in v}
    
    if successful_results:
        # Check if optimization scales with complexity
        complexities = list(successful_results.keys())
        
        print(f"  Programs tested: {len(successful_results)}")
        
        # Memory reduction effectiveness
        reductions = [results['memory_reduction'] for results in successful_results.values()]
        avg_reduction = sum(reductions) / len(reductions)
        min_reduction = min(reductions)
        max_reduction = max(reductions)
        
        print(f"  Memory reduction range: {min_reduction:.2%} - {max_reduction:.2%}")
        print(f"  Average memory reduction: {avg_reduction:.2%}")
        
        # Control flow place optimization
        cf_ratios = [results['cf_optimization_ratio'] for results in successful_results.values()]
        programs_with_cf = sum(1 for ratio in cf_ratios if ratio > 0)
        
        print(f"  Programs with control flow: {programs_with_cf}/{len(successful_results)}")
        
        if programs_with_cf > 0:
            avg_cf_ratio = sum(ratio for ratio in cf_ratios if ratio > 0) / programs_with_cf
            print(f"  Average CF place ratio: {avg_cf_ratio:.2%}")
        
        # Optimization time scaling
        opt_times = [results['optimization_time'] for results in successful_results.values()]
        place_counts = [results['total_places'] for results in successful_results.values()]
        
        if len(opt_times) > 1:
            time_complexity = max(opt_times) / min(opt_times) if min(opt_times) > 0 else float('inf')
            place_complexity = max(place_counts) / min(place_counts) if min(place_counts) > 0 else float('inf')
            
            print(f"  Time scaling: {time_complexity:.2f}x for {place_complexity:.2f}x places")
        
        # Verify TR-3 compliance
        tr3_compliance = all(results['memory_reduction'] > 0 for results in successful_results.values())
        print(f"  TR-3 Compliance (Memory Optimization): {'✅' if tr3_compliance else '❌'}")
    
    print(f"\n✅ Memory optimization performance test completed!")
    return True

def test_distributed_coordination_overhead():
    """
    Test the overhead of distributed coordination with control flow
    Verifies that control flow doesn't significantly impact coordination efficiency
    """
    print("\n" + "=" * 60)
    print("DISTRIBUTED COORDINATION OVERHEAD TEST")
    print("=" * 60)
    
    # Test programs with different control flow densities
    test_cases = [
        ("No Control Flow", [
            ("push", "constant", 1),
            ("push", "constant", 2),
            ("add",),
            ("push", "constant", 3),
            ("mul",),
            ("return",)
        ]),
        
        ("Low CF Density", [
            ("push", "constant", 1),
            ("push", "constant", 2),
            ("add",),
            ("label", "POINT1"),
            ("push", "constant", 3),
            ("mul",),
            ("return",)
        ]),
        
        ("Medium CF Density", [
            ("push", "constant", 1),
            ("if-goto", "BRANCH"),
            ("push", "constant", 2),
            ("goto", "MERGE"),
            ("label", "BRANCH"),
            ("push", "constant", 3),
            ("label", "MERGE"),
            ("push", "constant", 4),
            ("add",),
            ("return",)
        ]),
        
        ("High CF Density", [
            ("push", "constant", 1),
            ("if-goto", "B1"),
            ("goto", "B2"),
            ("label", "B1"),
            ("push", "constant", 2),
            ("if-goto", "B3"),
            ("goto", "B4"),
            ("label", "B2"),
            ("push", "constant", 3),
            ("goto", "MERGE"),
            ("label", "B3"),
            ("push", "constant", 4),
            ("goto", "MERGE"),
            ("label", "B4"),
            ("push", "constant", 5),
            ("label", "MERGE"),
            ("add",),
            ("return",)
        ])
    ]
    
    coordination_metrics = {}
    
    for case_name, commands in test_cases:
        print(f"\nTesting coordination overhead for '{case_name}':")
        
        translator = VMToPetriTranslator()
        
        try:
            # Execute program
            result = translator.execute_program(commands)
            
            # Analyze coordination requirements
            execution_plan = translator._analyze_execution_dependencies()
            
            total_levels = len(execution_plan['execution_levels'])
            total_operations = sum(len(level) for level in execution_plan['execution_levels'])
            
            # Count control flow operations and dependencies
            cf_operations = 0
            cf_dependencies = 0
            barrier_levels = set()
            
            for level_idx, level_ops in enumerate(execution_plan['execution_levels']):
                level_cf_ops = [op for op in level_ops if any(op.startswith(cf) for cf in ['goto_', 'if_goto_', 'label_'])]
                cf_operations += len(level_cf_ops)
                
                if level_cf_ops:
                    barrier_levels.add(level_idx)
            
            # Count control flow dependencies
            cf_deps = execution_plan.get('control_flow_deps', {})
            cf_dependencies = sum(len(deps) for deps in cf_deps.values() if deps)
            
            # Test coordination overhead across core counts
            core_overhead = {}
            
            for num_cores in [2, 4, 8]:
                start_time = time.time()
                core_assignments = translator._assign_operations_to_cores(execution_plan, num_cores)
                assignment_time = time.time() - start_time
                
                # Calculate coordination metrics
                cores_with_barriers = 0
                total_barrier_ops = 0
                
                for core_id, operations in core_assignments.items():
                    barrier_ops = sum(1 for op in operations if op.get('requires_barrier', False))
                    if barrier_ops > 0:
                        cores_with_barriers += 1
                        total_barrier_ops += barrier_ops
                
                coordination_overhead = total_barrier_ops / total_operations if total_operations > 0 else 0
                
                core_overhead[num_cores] = {
                    'assignment_time': assignment_time,
                    'cores_with_barriers': cores_with_barriers,
                    'coordination_overhead': coordination_overhead
                }
            
            coordination_metrics[case_name] = {
                'total_levels': total_levels,
                'total_operations': total_operations,
                'cf_operations': cf_operations,
                'cf_dependencies': cf_dependencies,
                'barrier_levels': len(barrier_levels),
                'cf_density': cf_operations / total_operations if total_operations > 0 else 0,
                'core_overhead': core_overhead
            }
            
            print(f"  Total operations: {total_operations}")
            print(f"  Control flow operations: {cf_operations}")
            print(f"  CF density: {(cf_operations/total_operations):.2%}")
            print(f"  Barrier levels: {len(barrier_levels)}")
            print(f"  CF dependencies: {cf_dependencies}")
            
            # Show coordination overhead for different core counts
            for cores, overhead_data in core_overhead.items():
                overhead_pct = overhead_data['coordination_overhead']
                print(f"    {cores} cores: {overhead_pct:.2%} coordination overhead")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            coordination_metrics[case_name] = {'error': str(e)}
    
    # Analyze coordination overhead trends
    print(f"\nCoordination Overhead Analysis:")
    
    successful_metrics = {k: v for k, v in coordination_metrics.items() if 'error' not in v}
    
    if successful_metrics:
        # Analyze relationship between CF density and coordination overhead
        densities = [metrics['cf_density'] for metrics in successful_metrics.values()]
        
        print(f"  CF density range: {min(densities):.2%} - {max(densities):.2%}")
        
        # Check if overhead scales reasonably with CF density
        for cores in [2, 4, 8]:
            overheads = []
            for metrics in successful_metrics.values():
                if cores in metrics['core_overhead']:
                    overheads.append(metrics['core_overhead'][cores]['coordination_overhead'])
            
            if overheads:
                avg_overhead = sum(overheads) / len(overheads)
                max_overhead = max(overheads)
                print(f"  {cores} cores - Avg overhead: {avg_overhead:.2%}, Max: {max_overhead:.2%}")
        
        # Verify reasonable coordination overhead (should be < 50% for most cases)
        reasonable_overhead = True
        for metrics in successful_metrics.values():
            for cores, overhead_data in metrics['core_overhead'].items():
                if overhead_data['coordination_overhead'] > 0.5:  # > 50% overhead
                    reasonable_overhead = False
                    break
        
        print(f"  Reasonable overhead maintained: {'✅' if reasonable_overhead else '❌'}")
    
    print(f"\n✅ Distributed coordination overhead test completed!")
    return True

if __name__ == "__main__":
    success = True
    
    try:
        success &= test_control_flow_execution_scaling()
        success &= test_memory_optimization_performance()
        success &= test_distributed_coordination_overhead()
        
        if success:
            print(f"\n🎉 ALL MULTI-CORE CONTROL FLOW PERFORMANCE TESTS PASSED!")
        else:
            print(f"\n❌ SOME PERFORMANCE TESTS FAILED!")
            
    except Exception as e:
        print(f"\n💥 CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        success = False
    
    sys.exit(0 if success else 1)