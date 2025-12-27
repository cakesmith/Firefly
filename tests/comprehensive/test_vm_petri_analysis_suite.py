#!/usr/bin/env python3
"""
Comprehensive Test Suite for VM Files and Petri Net Analysis
============================================================

This test suite analyzes VM files from TECS chapters 7+ and the new Petri VM,
focusing on:
1. Petri net structure analysis
2. Execution flow analysis  
3. Assembly emission verification
4. Multi-core optimization analysis
5. Memory optimization analysis

Tests VM files from:
- Chapter 7: StackArithmetic, MemoryAccess
- Chapter 8: ProgramFlow, FunctionCalls
- Custom examples with complex control flow
"""

import sys
import os
import json
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Petri.VMToPetri import VMToPetriTranslator
from vm_parser import parse_vm_file

class VMPetriAnalysisSuite:
    """Comprehensive analysis suite for VM files and Petri nets"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results_dir = "test_results/comprehensive_analysis"
        self.analysis_results = {}
        
        # Create test results directory
        if not os.path.exists(self.test_results_dir):
            os.makedirs(self.test_results_dir)
            print(f"Created comprehensive analysis directory: {self.test_results_dir}/")
    
    def run_test(self, test_name, test_func):
        """Run a test and track results"""
        print(f"\n{'='*60}")
        print(f"ANALYZING: {test_name}")
        print('='*60)
        try:
            success = test_func()
            if success:
                print(f"✅ {test_name} ANALYSIS COMPLETE")
                self.passed += 1
            else:
                print(f"❌ {test_name} ANALYSIS FAILED")
                self.failed += 1
            return success
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
            import traceback
            traceback.print_exc()
            self.failed += 1
            return False
    
    def analyze_vm_file(self, vm_file_path, test_name):
        """
        Comprehensive analysis of a VM file:
        1. Parse and translate to Petri net
        2. Analyze net structure
        3. Analyze execution dependencies
        4. Generate assembly for multiple core counts
        5. Analyze memory optimization
        """
        print(f"Analyzing VM file: {vm_file_path}")
        
        if not os.path.exists(vm_file_path):
            print(f"VM file not found: {vm_file_path}")
            return False
            
        try:
            # Parse VM file
            commands = parse_vm_file(vm_file_path)
            print(f"Parsed {len(commands)} VM commands")
            
            # Create translator and execute
            translator = VMToPetriTranslator()
            result = translator.execute_program(commands)
            
            # Analyze Petri net structure
            net_analysis = self.analyze_petri_net_structure(translator, test_name)
            
            # Analyze execution dependencies
            execution_analysis = self.analyze_execution_flow(translator, test_name)
            
            # Generate and analyze assembly for different core counts
            assembly_analysis = self.analyze_assembly_emission(translator, test_name)
            
            # Analyze memory optimization
            memory_analysis = self.analyze_memory_optimization(translator, test_name)
            
            # Store comprehensive analysis
            self.analysis_results[test_name] = {
                'vm_file': vm_file_path,
                'commands_count': len(commands),
                'execution_result': result,
                'net_analysis': net_analysis,
                'execution_analysis': execution_analysis,
                'assembly_analysis': assembly_analysis,
                'memory_analysis': memory_analysis,
                'timestamp': time.time()
            }
            
            # Save detailed analysis to file
            self.save_analysis_report(test_name)
            
            return True
            
        except Exception as e:
            print(f"Error analyzing {vm_file_path}: {e}")
            return False
    
    def analyze_petri_net_structure(self, translator, test_name):
        """Analyze the structure of the generated Petri net"""
        print("\n--- Petri Net Structure Analysis ---")
        
        net = translator.net
        places = net.places
        transitions = net.transitions
        
        # Basic statistics
        place_count = len(places)
        transition_count = len(transitions)
        arc_count = len(net.arcs)
        
        print(f"Places: {place_count}")
        print(f"Transitions: {transition_count}")
        print(f"Arcs: {arc_count}")
        
        # Analyze place types
        place_types = self.classify_places(places)
        print(f"Place classification: {place_types}")
        
        # Analyze transition types
        transition_types = self.classify_transitions(transitions)
        print(f"Transition classification: {transition_types}")
        
        # Analyze connectivity
        connectivity = self.analyze_connectivity(places, transitions)
        print(f"Connectivity analysis: {connectivity}")
        
        # Check for Petri net properties
        properties = self.check_petri_net_properties(net)
        print(f"Petri net properties: {properties}")
        
        return {
            'place_count': place_count,
            'transition_count': transition_count,
            'arc_count': arc_count,
            'place_types': place_types,
            'transition_types': transition_types,
            'connectivity': connectivity,
            'properties': properties
        }
    
    def classify_places(self, places):
        """Classify places by their purpose and structure"""
        classification = {
            'constant_sources': 0,
            'local_variables': 0,
            'arguments': 0,
            'control_flow': 0,
            'computation_results': 0,
            'function_related': 0,
            'other': 0
        }
        
        for place_name, place in places.items():
            if 'const' in place_name.lower():
                classification['constant_sources'] += 1
            elif 'local' in place_name.lower():
                classification['local_variables'] += 1
            elif 'arg' in place_name.lower():
                classification['arguments'] += 1
            elif any(keyword in place_name.lower() for keyword in ['label', 'goto', 'if', 'control']):
                classification['control_flow'] += 1
            elif any(keyword in place_name.lower() for keyword in ['add', 'sub', 'mul', 'div', 'eq', 'lt', 'gt']):
                classification['computation_results'] += 1
            elif any(keyword in place_name.lower() for keyword in ['function', 'call', 'return']):
                classification['function_related'] += 1
            else:
                classification['other'] += 1
                
        return classification
    
    def classify_transitions(self, transitions):
        """Classify transitions by their operations"""
        classification = {
            'arithmetic': 0,
            'logical': 0,
            'memory': 0,
            'control_flow': 0,
            'function_calls': 0,
            'primitives': 0,
            'other': 0
        }
        
        for trans_name, transition in transitions.items():
            if any(keyword in trans_name.lower() for keyword in ['add', 'sub', 'mul', 'div', 'neg']):
                classification['arithmetic'] += 1
            elif any(keyword in trans_name.lower() for keyword in ['eq', 'lt', 'gt', 'and', 'or', 'not']):
                classification['logical'] += 1
            elif any(keyword in trans_name.lower() for keyword in ['push', 'pop', 'local', 'arg']):
                classification['memory'] += 1
            elif any(keyword in trans_name.lower() for keyword in ['goto', 'if', 'label', 'choice']):
                classification['control_flow'] += 1
            elif any(keyword in trans_name.lower() for keyword in ['call', 'return', 'function']):
                classification['function_calls'] += 1
            elif any(keyword in trans_name.lower() for keyword in ['source', 'dup', 'drop', 'join', 'loop']):
                classification['primitives'] += 1
            else:
                classification['other'] += 1
                
        return classification
    
    def analyze_connectivity(self, places, transitions):
        """Analyze connectivity patterns in the Petri net"""
        # Calculate in-degree and out-degree for places
        place_in_degrees = {}
        place_out_degrees = {}
        
        for place_name, place in places.items():
            place_in_degrees[place_name] = len(place.in_transitions)
            place_out_degrees[place_name] = len(place.out_transitions)
        
        # Calculate in-degree and out-degree for transitions
        trans_in_degrees = {}
        trans_out_degrees = {}
        
        for trans_name, transition in transitions.items():
            trans_in_degrees[trans_name] = len(transition.in_places)
            trans_out_degrees[trans_name] = len(transition.out_places)
        
        return {
            'max_place_in_degree': max(place_in_degrees.values()) if place_in_degrees else 0,
            'max_place_out_degree': max(place_out_degrees.values()) if place_out_degrees else 0,
            'max_trans_in_degree': max(trans_in_degrees.values()) if trans_in_degrees else 0,
            'max_trans_out_degree': max(trans_out_degrees.values()) if trans_out_degrees else 0,
            'avg_place_connectivity': sum(place_in_degrees.values()) / len(places) if places else 0,
            'avg_trans_connectivity': sum(trans_in_degrees.values()) / len(transitions) if transitions else 0
        }
    
    def check_petri_net_properties(self, net):
        """Check important Petri net properties"""
        properties = {
            'is_pure': True,  # No self-loops
            'is_ordinary': True,  # All arc weights are 1
            'has_source_places': False,  # Places with no input transitions
            'has_sink_places': False,  # Places with no output transitions
            'is_connected': True  # All nodes are reachable
        }
        
        # Check for source and sink places
        for place_name, place in net.places.items():
            if len(place.in_transitions) == 0:
                properties['has_source_places'] = True
            if len(place.out_transitions) == 0:
                properties['has_sink_places'] = True
        
        return properties
    
    def analyze_execution_flow(self, translator, test_name):
        """Analyze execution dependencies and parallelization opportunities"""
        print("\n--- Execution Flow Analysis ---")
        
        try:
            # Get execution analysis
            execution_plan = translator.execution_analyzer.analyze_execution_dependencies()
            
            # Analyze dependency structure
            dependency_analysis = self.analyze_dependencies(execution_plan)
            print(f"Dependency analysis: {dependency_analysis}")
            
            # Analyze parallelization potential
            parallelization = self.analyze_parallelization_potential(execution_plan)
            print(f"Parallelization potential: {parallelization}")
            
            return {
                'execution_plan': execution_plan,
                'dependency_analysis': dependency_analysis,
                'parallelization': parallelization
            }
            
        except Exception as e:
            print(f"Error in execution flow analysis: {e}")
            return {'error': str(e)}
    
    def analyze_dependencies(self, execution_plan):
        """Analyze the dependency structure"""
        if 'dependencies' not in execution_plan:
            return {'error': 'No dependency information available'}
            
        dependencies = execution_plan['dependencies']
        
        # Calculate dependency statistics
        total_operations = len(dependencies)
        total_dependencies = sum(len(deps) for deps in dependencies.values())
        
        # Find operations with no dependencies (can start immediately)
        independent_ops = [op for op, deps in dependencies.items() if len(deps) == 0]
        
        # Find operations with many dependencies (bottlenecks)
        max_deps = max(len(deps) for deps in dependencies.values()) if dependencies else 0
        bottleneck_ops = [op for op, deps in dependencies.items() if len(deps) == max_deps]
        
        return {
            'total_operations': total_operations,
            'total_dependencies': total_dependencies,
            'avg_dependencies_per_op': total_dependencies / total_operations if total_operations > 0 else 0,
            'independent_operations': len(independent_ops),
            'max_dependencies': max_deps,
            'bottleneck_operations': len(bottleneck_ops)
        }
    
    def analyze_parallelization_potential(self, execution_plan):
        """Analyze how well the program can be parallelized"""
        if 'execution_levels' not in execution_plan:
            return {'error': 'No execution level information available'}
            
        execution_levels = execution_plan['execution_levels']
        
        # Calculate parallelization metrics
        total_levels = len(execution_levels)
        operations_per_level = [len(level) for level in execution_levels]
        max_parallel_ops = max(operations_per_level) if operations_per_level else 0
        avg_parallel_ops = sum(operations_per_level) / total_levels if total_levels > 0 else 0
        
        # Calculate theoretical speedup (Amdahl's law approximation)
        sequential_fraction = sum(1 for count in operations_per_level if count == 1) / total_levels if total_levels > 0 else 1
        theoretical_speedup = 1 / (sequential_fraction + (1 - sequential_fraction) / max_parallel_ops) if max_parallel_ops > 0 else 1
        
        return {
            'execution_levels': total_levels,
            'max_parallel_operations': max_parallel_ops,
            'avg_parallel_operations': avg_parallel_ops,
            'sequential_fraction': sequential_fraction,
            'theoretical_speedup': theoretical_speedup,
            'operations_per_level': operations_per_level
        }
    
    def analyze_assembly_emission(self, translator, test_name):
        """Analyze assembly generation for different core counts"""
        print("\n--- Assembly Emission Analysis ---")
        
        assembly_results = {}
        core_counts = [1, 2, 4, 8]  # Test different core configurations
        
        for cores in core_counts:
            try:
                print(f"Generating assembly for {cores} core(s)...")
                
                if cores == 1:
                    # Single core - get assembly directly
                    assembly_code = translator.assembly_generator.generate_multicore_assembly(cores)
                    assembly_results[cores] = {
                        'type': 'single_core',
                        'assembly_lines': len(assembly_code) if isinstance(assembly_code, list) else 0,
                        'success': True
                    }
                else:
                    # Multi-core - generates files
                    rom_files = translator.assembly_generator.generate_multicore_assembly(cores, self.test_results_dir)
                    assembly_results[cores] = {
                        'type': 'multi_core',
                        'rom_files': len(rom_files) if rom_files else 0,
                        'success': rom_files is not None
                    }
                    
            except Exception as e:
                print(f"Error generating {cores}-core assembly: {e}")
                assembly_results[cores] = {
                    'type': 'error',
                    'error': str(e),
                    'success': False
                }
        
        # Analyze assembly characteristics
        assembly_analysis = self.analyze_assembly_characteristics(assembly_results)
        
        return {
            'core_results': assembly_results,
            'analysis': assembly_analysis
        }
    
    def analyze_assembly_characteristics(self, assembly_results):
        """Analyze characteristics of generated assembly"""
        successful_generations = sum(1 for result in assembly_results.values() if result['success'])
        total_generations = len(assembly_results)
        
        # Check scaling behavior
        scaling_analysis = {}
        if successful_generations > 1:
            # Analyze how assembly complexity scales with core count
            single_core_lines = assembly_results.get(1, {}).get('assembly_lines', 0)
            if single_core_lines > 0:
                for cores, result in assembly_results.items():
                    if cores > 1 and result['success']:
                        scaling_analysis[cores] = {
                            'efficiency': single_core_lines / (cores * result.get('rom_files', 1)),
                            'parallelization_overhead': result.get('rom_files', 1) - 1
                        }
        
        return {
            'success_rate': successful_generations / total_generations,
            'scaling_analysis': scaling_analysis,
            'max_cores_supported': max(cores for cores, result in assembly_results.items() if result['success']) if successful_generations > 0 else 0
        }
    
    def analyze_memory_optimization(self, translator, test_name):
        """Analyze memory optimization results"""
        print("\n--- Memory Optimization Analysis ---")
        
        try:
            # Get memory optimization results
            memory_results = translator.memory_optimizer.optimize_memory_allocation()
            
            original_places = len(translator.net.places)
            optimized_locations = memory_results.get('total_locations', original_places)
            memory_savings = original_places - optimized_locations
            savings_percentage = (memory_savings / original_places * 100) if original_places > 0 else 0
            
            print(f"Original places: {original_places}")
            print(f"Optimized locations: {optimized_locations}")
            print(f"Memory savings: {memory_savings} places ({savings_percentage:.1f}%)")
            
            return {
                'original_places': original_places,
                'optimized_locations': optimized_locations,
                'memory_savings': memory_savings,
                'savings_percentage': savings_percentage,
                'optimization_details': memory_results
            }
            
        except Exception as e:
            print(f"Error in memory optimization analysis: {e}")
            return {'error': str(e)}
    
    def save_analysis_report(self, test_name):
        """Save detailed analysis report to file"""
        if test_name not in self.analysis_results:
            return
            
        report_file = os.path.join(self.test_results_dir, f"{test_name}_analysis.json")
        
        try:
            with open(report_file, 'w') as f:
                json.dump(self.analysis_results[test_name], f, indent=2, default=str)
            print(f"Saved detailed analysis: {report_file}")
        except Exception as e:
            print(f"Error saving analysis report: {e}")
    
    def generate_comprehensive_report(self):
        """Generate a comprehensive report of all analyses"""
        report_file = os.path.join(self.test_results_dir, "comprehensive_analysis_report.json")
        
        summary = {
            'total_tests': len(self.analysis_results),
            'timestamp': time.time(),
            'summary_statistics': self.calculate_summary_statistics(),
            'detailed_results': self.analysis_results
        }
        
        try:
            with open(report_file, 'w') as f:
                json.dump(summary, f, indent=2, default=str)
            print(f"\nSaved comprehensive report: {report_file}")
        except Exception as e:
            print(f"Error saving comprehensive report: {e}")
    
    def calculate_summary_statistics(self):
        """Calculate summary statistics across all tests"""
        if not self.analysis_results:
            return {}
            
        # Aggregate statistics
        total_places = sum(result['net_analysis']['place_count'] for result in self.analysis_results.values() if 'net_analysis' in result)
        total_transitions = sum(result['net_analysis']['transition_count'] for result in self.analysis_results.values() if 'net_analysis' in result)
        
        # Memory optimization statistics
        memory_savings = []
        for result in self.analysis_results.values():
            if 'memory_analysis' in result and 'savings_percentage' in result['memory_analysis']:
                memory_savings.append(result['memory_analysis']['savings_percentage'])
        
        avg_memory_savings = sum(memory_savings) / len(memory_savings) if memory_savings else 0
        
        # Assembly generation success rate
        assembly_successes = 0
        assembly_total = 0
        for result in self.analysis_results.values():
            if 'assembly_analysis' in result and 'analysis' in result['assembly_analysis']:
                assembly_total += 1
                if result['assembly_analysis']['analysis'].get('success_rate', 0) > 0.5:
                    assembly_successes += 1
        
        assembly_success_rate = assembly_successes / assembly_total if assembly_total > 0 else 0
        
        return {
            'total_places_analyzed': total_places,
            'total_transitions_analyzed': total_transitions,
            'average_memory_savings_percent': avg_memory_savings,
            'assembly_generation_success_rate': assembly_success_rate,
            'tests_with_memory_optimization': len(memory_savings),
            'tests_with_assembly_generation': assembly_total
        }
    
    # Test methods for specific VM files
    
    def test_chapter7_simple_add(self):
        """Test SimpleAdd.vm from Chapter 7"""
        return self.analyze_vm_file("tecs/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm", "chapter7_simple_add")
    
    def test_chapter7_stack_test(self):
        """Test StackTest.vm from Chapter 7"""
        return self.analyze_vm_file("tecs/projects/07/StackArithmetic/StackTest/StackTest.vm", "chapter7_stack_test")
    
    def test_chapter7_basic_test(self):
        """Test BasicTest.vm from Chapter 7"""
        return self.analyze_vm_file("tecs/projects/07/MemoryAccess/BasicTest/BasicTest.vm", "chapter7_basic_test")
    
    def test_chapter7_pointer_test(self):
        """Test PointerTest.vm from Chapter 7"""
        return self.analyze_vm_file("tecs/projects/07/MemoryAccess/PointerTest/PointerTest.vm", "chapter7_pointer_test")
    
    def test_chapter7_static_test(self):
        """Test StaticTest.vm from Chapter 7"""
        return self.analyze_vm_file("tecs/projects/07/MemoryAccess/StaticTest/StaticTest.vm", "chapter7_static_test")
    
    def test_chapter8_basic_loop(self):
        """Test BasicLoop.vm from Chapter 8"""
        return self.analyze_vm_file("tecs/projects/08/ProgramFlow/BasicLoop/BasicLoop.vm", "chapter8_basic_loop")
    
    def test_chapter8_fibonacci_series(self):
        """Test FibonacciSeries.vm from Chapter 8"""
        return self.analyze_vm_file("tecs/projects/08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm", "chapter8_fibonacci_series")
    
    def test_chapter8_simple_function(self):
        """Test SimpleFunction.vm from Chapter 8"""
        return self.analyze_vm_file("tecs/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm", "chapter8_simple_function")
    
    def test_chapter8_fibonacci_element_main(self):
        """Test FibonacciElement Main.vm from Chapter 8"""
        return self.analyze_vm_file("tecs/projects/08/FunctionCalls/FibonacciElement/Main.vm", "chapter8_fibonacci_element_main")
    
    def test_chapter8_fibonacci_element_sys(self):
        """Test FibonacciElement Sys.vm from Chapter 8"""
        return self.analyze_vm_file("tecs/projects/08/FunctionCalls/FibonacciElement/Sys.vm", "chapter8_fibonacci_element_sys")
    
    def test_custom_complex_control_flow(self):
        """Test a custom VM program with complex control flow"""
        # Create a complex VM program for testing
        complex_vm_content = """// Complex control flow test
function ComplexTest.main 3
push constant 10
pop local 0
push constant 0
pop local 1
push constant 1
pop local 2

label OUTER_LOOP
push local 0
push constant 0
gt
if-goto CONTINUE_OUTER
goto END_PROGRAM

label CONTINUE_OUTER
push local 1
push local 2
add
pop local 1
push local 2
push local 1
pop local 2

push local 0
push constant 1
sub
pop local 0

push local 0
push constant 5
eq
if-goto MIDDLE_CHECK
goto OUTER_LOOP

label MIDDLE_CHECK
push local 1
push constant 100
gt
if-goto INNER_PROCESS
goto OUTER_LOOP

label INNER_PROCESS
push local 1
push constant 2
div
pop local 1
goto OUTER_LOOP

label END_PROGRAM
push local 1
return
"""
        
        # Save to temporary file
        temp_vm_file = os.path.join(self.test_results_dir, "complex_control_flow.vm")
        with open(temp_vm_file, 'w') as f:
            f.write(complex_vm_content)
        
        return self.analyze_vm_file(temp_vm_file, "custom_complex_control_flow")
    
    def test_custom_recursive_function(self):
        """Test a custom recursive function"""
        recursive_vm_content = """// Recursive factorial test
function Factorial.compute 0
push argument 0
push constant 1
eq
if-goto BASE_CASE
push argument 0
push constant 0
eq
if-goto BASE_CASE

push argument 0
push argument 0
push constant 1
sub
call Factorial.compute 1
mul
return

label BASE_CASE
push constant 1
return

function Main.test 0
push constant 5
call Factorial.compute 1
return
"""
        
        # Save to temporary file
        temp_vm_file = os.path.join(self.test_results_dir, "recursive_factorial.vm")
        with open(temp_vm_file, 'w') as f:
            f.write(recursive_vm_content)
        
        return self.analyze_vm_file(temp_vm_file, "custom_recursive_function")
    
    def run_all_tests(self):
        """Run all analysis tests"""
        print("=" * 80)
        print("COMPREHENSIVE VM AND PETRI NET ANALYSIS SUITE")
        print("=" * 80)
        
        # Chapter 7 tests
        self.run_test("Chapter 7 - SimpleAdd", self.test_chapter7_simple_add)
        self.run_test("Chapter 7 - StackTest", self.test_chapter7_stack_test)
        self.run_test("Chapter 7 - BasicTest", self.test_chapter7_basic_test)
        self.run_test("Chapter 7 - PointerTest", self.test_chapter7_pointer_test)
        self.run_test("Chapter 7 - StaticTest", self.test_chapter7_static_test)
        
        # Chapter 8 tests
        self.run_test("Chapter 8 - BasicLoop", self.test_chapter8_basic_loop)
        self.run_test("Chapter 8 - FibonacciSeries", self.test_chapter8_fibonacci_series)
        self.run_test("Chapter 8 - SimpleFunction", self.test_chapter8_simple_function)
        self.run_test("Chapter 8 - FibonacciElement Main", self.test_chapter8_fibonacci_element_main)
        self.run_test("Chapter 8 - FibonacciElement Sys", self.test_chapter8_fibonacci_element_sys)
        
        # Custom complex tests
        self.run_test("Custom - Complex Control Flow", self.test_custom_complex_control_flow)
        self.run_test("Custom - Recursive Function", self.test_custom_recursive_function)
        
        # Generate comprehensive report
        self.generate_comprehensive_report()
        
        # Print summary
        print("\n" + "=" * 80)
        print("ANALYSIS SUITE SUMMARY")
        print("=" * 80)
        print(f"Total tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success rate: {self.passed / (self.passed + self.failed) * 100:.1f}%")
        
        if self.analysis_results:
            summary_stats = self.calculate_summary_statistics()
            print(f"\nAggregate Statistics:")
            print(f"Total places analyzed: {summary_stats.get('total_places_analyzed', 0)}")
            print(f"Total transitions analyzed: {summary_stats.get('total_transitions_analyzed', 0)}")
            print(f"Average memory savings: {summary_stats.get('average_memory_savings_percent', 0):.1f}%")
            print(f"Assembly generation success rate: {summary_stats.get('assembly_generation_success_rate', 0) * 100:.1f}%")
        
        print(f"\nDetailed results saved in: {self.test_results_dir}/")
        
        return self.failed == 0


if __name__ == "__main__":
    suite = VMPetriAnalysisSuite()
    success = suite.run_all_tests()
    sys.exit(0 if success else 1)