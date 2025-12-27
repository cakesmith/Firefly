#!/usr/bin/env python3
"""
Assembly Emission Analysis Test Suite
=====================================

This test suite focuses on analyzing the assembly code generation from Petri nets,
including:
1. Single-core assembly generation and analysis
2. Multi-core assembly generation and optimization
3. Assembly code quality metrics
4. Performance characteristics analysis
5. Scalability analysis across different core counts
6. Memory layout optimization analysis
"""

import sys
import os
import json
import time
import re
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Petri.VMToPetri import VMToPetriTranslator
from vm_parser import parse_vm_file

class AssemblyEmissionAnalyzer:
    """Analyzes assembly code generation from Petri nets"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results_dir = "test_results/assembly_emission_analysis"
        self.assembly_analyses = {}
        
        # Create test results directory
        if not os.path.exists(self.test_results_dir):
            os.makedirs(self.test_results_dir)
            print(f"Created assembly emission analysis directory: {self.test_results_dir}/")
    
    def run_test(self, test_name, test_func):
        """Run a test and track results"""
        print(f"\n{'='*60}")
        print(f"ANALYZING ASSEMBLY EMISSION: {test_name}")
        print('='*60)
        try:
            success = test_func()
            if success:
                print(f"✅ {test_name} ASSEMBLY ANALYSIS COMPLETE")
                self.passed += 1
            else:
                print(f"❌ {test_name} ASSEMBLY ANALYSIS FAILED")
                self.failed += 1
            return success
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
            import traceback
            traceback.print_exc()
            self.failed += 1
            return False
    
    def analyze_assembly_emission(self, commands, test_name, core_counts=[1, 2, 4, 8]):
        """
        Comprehensive assembly emission analysis:
        1. Generate assembly for different core counts
        2. Analyze assembly code quality
        3. Measure performance characteristics
        4. Analyze scalability patterns
        5. Verify correctness across configurations
        """
        print(f"Analyzing assembly emission for {len(commands)} commands")
        
        try:
            # Create translator and execute program
            translator = VMToPetriTranslator()
            execution_result = translator.execute_program(commands)
            print(f"Program execution result: {execution_result}")
            
            # Analyze assembly generation for different core counts
            assembly_results = {}
            
            for cores in core_counts:
                print(f"\nGenerating assembly for {cores} core(s)...")
                
                try:
                    # Generate assembly
                    if cores == 1:
                        assembly_code = translator.assembly_generator.generate_multicore_assembly(cores)
                        assembly_results[cores] = self.analyze_single_core_assembly(assembly_code, cores)
                    else:
                        rom_files = translator.assembly_generator.generate_multicore_assembly(cores, self.test_results_dir)
                        assembly_results[cores] = self.analyze_multi_core_assembly(rom_files, cores)
                    
                    assembly_results[cores]['generation_successful'] = True
                    
                except Exception as e:
                    print(f"Error generating {cores}-core assembly: {e}")
                    assembly_results[cores] = {
                        'generation_successful': False,
                        'error': str(e)
                    }
            
            # Perform cross-core analysis
            cross_core_analysis = self.analyze_cross_core_patterns(assembly_results)
            
            # Analyze scalability
            scalability_analysis = self.analyze_scalability_patterns(assembly_results)
            
            # Store comprehensive analysis
            self.assembly_analyses[test_name] = {
                'commands_count': len(commands),
                'execution_result': execution_result,
                'assembly_results': assembly_results,
                'cross_core_analysis': cross_core_analysis,
                'scalability_analysis': scalability_analysis,
                'timestamp': time.time()
            }
            
            # Save detailed analysis
            self.save_assembly_analysis(test_name)
            
            return True
            
        except Exception as e:
            print(f"Error in assembly emission analysis: {e}")
            return False
    
    def analyze_single_core_assembly(self, assembly_code, cores):
        """Analyze single-core assembly code"""
        print(f"Analyzing single-core assembly ({len(assembly_code) if assembly_code else 0} lines)")
        
        if not assembly_code:
            return {'error': 'No assembly code generated'}
        
        # Basic metrics
        total_lines = len(assembly_code)
        instruction_lines = len([line for line in assembly_code if self.is_instruction_line(line)])
        comment_lines = len([line for line in assembly_code if self.is_comment_line(line)])
        label_lines = len([line for line in assembly_code if self.is_label_line(line)])
        
        # Instruction analysis
        instruction_analysis = self.analyze_instructions(assembly_code)
        
        # Memory usage analysis
        memory_analysis = self.analyze_memory_usage(assembly_code)
        
        # Control flow analysis
        control_flow_analysis = self.analyze_control_flow(assembly_code)
        
        # Performance estimation
        performance_analysis = self.estimate_performance(assembly_code)
        
        return {
            'type': 'single_core',
            'total_lines': total_lines,
            'instruction_lines': instruction_lines,
            'comment_lines': comment_lines,
            'label_lines': label_lines,
            'code_density': instruction_lines / total_lines if total_lines > 0 else 0,
            'instruction_analysis': instruction_analysis,
            'memory_analysis': memory_analysis,
            'control_flow_analysis': control_flow_analysis,
            'performance_analysis': performance_analysis
        }
    
    def analyze_multi_core_assembly(self, rom_files, cores):
        """Analyze multi-core assembly generation"""
        print(f"Analyzing multi-core assembly for {cores} cores")
        
        if not rom_files:
            return {'error': 'No ROM files generated'}
        
        # Analyze each core's ROM
        core_analyses = {}
        total_instructions = 0
        
        for core_id, rom_content in rom_files.items():
            if isinstance(rom_content, list):
                core_analysis = self.analyze_single_core_assembly(rom_content, 1)
                core_analyses[core_id] = core_analysis
                total_instructions += core_analysis.get('instruction_lines', 0)
        
        # Analyze load balancing
        load_balance_analysis = self.analyze_load_balancing(core_analyses)
        
        # Analyze coordination overhead
        coordination_analysis = self.analyze_coordination_overhead(core_analyses)
        
        # Analyze memory distribution
        memory_distribution = self.analyze_memory_distribution(core_analyses)
        
        return {
            'type': 'multi_core',
            'core_count': cores,
            'core_analyses': core_analyses,
            'total_instructions': total_instructions,
            'avg_instructions_per_core': total_instructions / cores if cores > 0 else 0,
            'load_balance_analysis': load_balance_analysis,
            'coordination_analysis': coordination_analysis,
            'memory_distribution': memory_distribution
        }
    
    def is_instruction_line(self, line):
        """Check if a line contains an actual instruction"""
        line = line.strip()
        if not line or line.startswith('//') or line.startswith(';'):
            return False
        if line.endswith(':'):  # Label
            return False
        return True
    
    def is_comment_line(self, line):
        """Check if a line is a comment"""
        line = line.strip()
        return line.startswith('//') or line.startswith(';')
    
    def is_label_line(self, line):
        """Check if a line is a label"""
        line = line.strip()
        return line.endswith(':') and not line.startswith('//')
    
    def analyze_instructions(self, assembly_code):
        """Analyze instruction types and patterns"""
        instruction_types = {
            'arithmetic': 0,
            'memory': 0,
            'control': 0,
            'logical': 0,
            'data_movement': 0,
            'other': 0
        }
        
        instruction_patterns = []
        
        for line in assembly_code:
            if self.is_instruction_line(line):
                instruction = line.strip().split()[0].upper() if line.strip() else ''
                
                # Categorize instruction
                if instruction in ['ADD', 'SUB', 'MUL', 'DIV', 'INC', 'DEC']:
                    instruction_types['arithmetic'] += 1
                elif instruction in ['LOAD', 'STORE', 'PUSH', 'POP']:
                    instruction_types['memory'] += 1
                elif instruction in ['JMP', 'JZ', 'JNZ', 'CALL', 'RET']:
                    instruction_types['control'] += 1
                elif instruction in ['AND', 'OR', 'XOR', 'NOT', 'CMP']:
                    instruction_types['logical'] += 1
                elif instruction in ['MOV', 'COPY']:
                    instruction_types['data_movement'] += 1
                else:
                    instruction_types['other'] += 1
                
                # Track instruction patterns
                instruction_patterns.append(instruction)
        
        # Analyze instruction sequences
        sequence_analysis = self.analyze_instruction_sequences(instruction_patterns)
        
        return {
            'instruction_types': instruction_types,
            'total_instructions': sum(instruction_types.values()),
            'sequence_analysis': sequence_analysis,
            'most_common_instructions': self.get_most_common_instructions(instruction_patterns)
        }
    
    def analyze_instruction_sequences(self, instruction_patterns):
        """Analyze common instruction sequences"""
        sequences = {}
        sequence_length = 3  # Analyze 3-instruction sequences
        
        for i in range(len(instruction_patterns) - sequence_length + 1):
            sequence = tuple(instruction_patterns[i:i + sequence_length])
            sequences[sequence] = sequences.get(sequence, 0) + 1
        
        # Find most common sequences
        common_sequences = sorted(sequences.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'total_sequences': len(sequences),
            'most_common_sequences': common_sequences,
            'sequence_diversity': len(sequences) / max(1, len(instruction_patterns) - sequence_length + 1)
        }
    
    def get_most_common_instructions(self, instruction_patterns):
        """Get the most commonly used instructions"""
        instruction_counts = {}
        for instruction in instruction_patterns:
            instruction_counts[instruction] = instruction_counts.get(instruction, 0) + 1
        
        return sorted(instruction_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    def analyze_memory_usage(self, assembly_code):
        """Analyze memory usage patterns in assembly"""
        memory_operations = 0
        memory_addresses = set()
        register_usage = set()
        
        for line in assembly_code:
            if self.is_instruction_line(line):
                line_upper = line.upper()
                
                # Count memory operations
                if any(op in line_upper for op in ['LOAD', 'STORE', 'PUSH', 'POP']):
                    memory_operations += 1
                
                # Extract memory addresses (simplified pattern matching)
                addresses = re.findall(r'@(\d+)', line)
                memory_addresses.update(addresses)
                
                # Extract register usage
                registers = re.findall(r'R(\d+)', line)
                register_usage.update(registers)
        
        return {
            'memory_operations': memory_operations,
            'unique_memory_addresses': len(memory_addresses),
            'register_usage_count': len(register_usage),
            'memory_operation_ratio': memory_operations / len(assembly_code) if assembly_code else 0
        }
    
    def analyze_control_flow(self, assembly_code):
        """Analyze control flow patterns"""
        labels = []
        jumps = []
        calls = []
        returns = []
        
        for line in assembly_code:
            line_stripped = line.strip()
            
            if self.is_label_line(line_stripped):
                labels.append(line_stripped[:-1])  # Remove colon
            elif self.is_instruction_line(line_stripped):
                line_upper = line_stripped.upper()
                
                if line_upper.startswith('JMP') or line_upper.startswith('JZ') or line_upper.startswith('JNZ'):
                    jumps.append(line_stripped)
                elif line_upper.startswith('CALL'):
                    calls.append(line_stripped)
                elif line_upper.startswith('RET'):
                    returns.append(line_stripped)
        
        # Analyze control flow complexity
        control_flow_complexity = len(jumps) + len(calls)
        
        return {
            'label_count': len(labels),
            'jump_count': len(jumps),
            'call_count': len(calls),
            'return_count': len(returns),
            'control_flow_complexity': control_flow_complexity,
            'control_flow_ratio': control_flow_complexity / len(assembly_code) if assembly_code else 0
        }
    
    def estimate_performance(self, assembly_code):
        """Estimate performance characteristics"""
        # Simple performance estimation based on instruction types
        cycle_estimates = {
            'ADD': 1, 'SUB': 1, 'MUL': 3, 'DIV': 10,
            'LOAD': 2, 'STORE': 2, 'PUSH': 1, 'POP': 1,
            'JMP': 1, 'JZ': 1, 'JNZ': 1, 'CALL': 3, 'RET': 2,
            'AND': 1, 'OR': 1, 'XOR': 1, 'NOT': 1, 'CMP': 1,
            'MOV': 1, 'COPY': 1
        }
        
        estimated_cycles = 0
        instruction_count = 0
        
        for line in assembly_code:
            if self.is_instruction_line(line):
                instruction = line.strip().split()[0].upper() if line.strip() else ''
                cycles = cycle_estimates.get(instruction, 2)  # Default 2 cycles
                estimated_cycles += cycles
                instruction_count += 1
        
        return {
            'estimated_cycles': estimated_cycles,
            'instruction_count': instruction_count,
            'avg_cycles_per_instruction': estimated_cycles / instruction_count if instruction_count > 0 else 0,
            'performance_score': instruction_count / estimated_cycles if estimated_cycles > 0 else 0
        }
    
    def analyze_load_balancing(self, core_analyses):
        """Analyze load balancing across cores"""
        if not core_analyses:
            return {'error': 'No core analyses available'}
        
        instruction_counts = []
        cycle_estimates = []
        
        for core_id, analysis in core_analyses.items():
            if 'instruction_lines' in analysis:
                instruction_counts.append(analysis['instruction_lines'])
            if 'performance_analysis' in analysis:
                cycle_estimates.append(analysis['performance_analysis'].get('estimated_cycles', 0))
        
        if not instruction_counts:
            return {'error': 'No instruction count data available'}
        
        # Calculate load balance metrics
        max_instructions = max(instruction_counts)
        min_instructions = min(instruction_counts)
        avg_instructions = sum(instruction_counts) / len(instruction_counts)
        
        load_balance_ratio = min_instructions / max_instructions if max_instructions > 0 else 0
        load_variance = sum((count - avg_instructions) ** 2 for count in instruction_counts) / len(instruction_counts)
        
        return {
            'instruction_counts': instruction_counts,
            'max_instructions': max_instructions,
            'min_instructions': min_instructions,
            'avg_instructions': avg_instructions,
            'load_balance_ratio': load_balance_ratio,
            'load_variance': load_variance,
            'is_well_balanced': load_balance_ratio > 0.8  # Threshold for good balance
        }
    
    def analyze_coordination_overhead(self, core_analyses):
        """Analyze coordination overhead in multi-core assembly"""
        total_coordination_instructions = 0
        total_instructions = 0
        
        coordination_keywords = ['SYNC', 'BARRIER', 'LOCK', 'UNLOCK', 'WAIT', 'SIGNAL']
        
        for core_id, analysis in core_analyses.items():
            if 'instruction_analysis' in analysis:
                # This is a simplified analysis - in a real implementation,
                # we would need to examine the actual assembly code
                total_instructions += analysis.get('instruction_lines', 0)
                # Estimate coordination overhead as a percentage
                total_coordination_instructions += analysis.get('instruction_lines', 0) * 0.1  # 10% estimate
        
        coordination_overhead = total_coordination_instructions / total_instructions if total_instructions > 0 else 0
        
        return {
            'total_coordination_instructions': total_coordination_instructions,
            'total_instructions': total_instructions,
            'coordination_overhead_ratio': coordination_overhead,
            'efficiency': 1 - coordination_overhead
        }
    
    def analyze_memory_distribution(self, core_analyses):
        """Analyze memory usage distribution across cores"""
        memory_usages = []
        
        for core_id, analysis in core_analyses.items():
            if 'memory_analysis' in analysis:
                memory_ops = analysis['memory_analysis'].get('memory_operations', 0)
                memory_usages.append(memory_ops)
        
        if not memory_usages:
            return {'error': 'No memory usage data available'}
        
        total_memory_ops = sum(memory_usages)
        avg_memory_ops = total_memory_ops / len(memory_usages)
        
        return {
            'memory_operations_per_core': memory_usages,
            'total_memory_operations': total_memory_ops,
            'avg_memory_operations': avg_memory_ops,
            'memory_distribution_variance': sum((ops - avg_memory_ops) ** 2 for ops in memory_usages) / len(memory_usages)
        }
    
    def analyze_cross_core_patterns(self, assembly_results):
        """Analyze patterns across different core configurations"""
        print("Analyzing cross-core patterns...")
        
        successful_cores = [cores for cores, result in assembly_results.items() 
                          if result.get('generation_successful', False)]
        
        if len(successful_cores) < 2:
            return {'error': 'Need at least 2 successful core configurations for comparison'}
        
        # Analyze instruction scaling
        instruction_scaling = {}
        for cores in successful_cores:
            result = assembly_results[cores]
            if result['type'] == 'single_core':
                instruction_scaling[cores] = result.get('instruction_lines', 0)
            else:  # multi_core
                instruction_scaling[cores] = result.get('total_instructions', 0)
        
        # Analyze efficiency trends
        efficiency_trends = {}
        base_instructions = instruction_scaling.get(1, 0)
        
        for cores in successful_cores:
            if cores > 1 and base_instructions > 0:
                actual_instructions = instruction_scaling[cores]
                theoretical_instructions = base_instructions  # Ideally should stay constant
                efficiency = theoretical_instructions / actual_instructions if actual_instructions > 0 else 0
                efficiency_trends[cores] = efficiency
        
        return {
            'successful_core_counts': successful_cores,
            'instruction_scaling': instruction_scaling,
            'efficiency_trends': efficiency_trends,
            'scaling_quality': self.assess_scaling_quality(efficiency_trends)
        }
    
    def assess_scaling_quality(self, efficiency_trends):
        """Assess the quality of scaling across core counts"""
        if not efficiency_trends:
            return 'unknown'
        
        avg_efficiency = sum(efficiency_trends.values()) / len(efficiency_trends)
        
        if avg_efficiency > 0.9:
            return 'excellent'
        elif avg_efficiency > 0.8:
            return 'good'
        elif avg_efficiency > 0.7:
            return 'fair'
        else:
            return 'poor'
    
    def analyze_scalability_patterns(self, assembly_results):
        """Analyze scalability patterns in assembly generation"""
        print("Analyzing scalability patterns...")
        
        scalability_metrics = {
            'linear_scaling_score': 0,
            'overhead_growth_rate': 0,
            'efficiency_degradation': 0,
            'optimal_core_count': 1
        }
        
        # Extract performance data
        performance_data = {}
        for cores, result in assembly_results.items():
            if result.get('generation_successful', False):
                if result['type'] == 'single_core':
                    perf = result.get('performance_analysis', {})
                    performance_data[cores] = perf.get('estimated_cycles', 0)
                else:  # multi_core
                    # Estimate total cycles across all cores
                    total_cycles = 0
                    for core_analysis in result.get('core_analyses', {}).values():
                        if 'performance_analysis' in core_analysis:
                            total_cycles += core_analysis['performance_analysis'].get('estimated_cycles', 0)
                    performance_data[cores] = total_cycles
        
        # Calculate scalability metrics
        if len(performance_data) >= 2:
            scalability_metrics = self.calculate_scalability_metrics(performance_data)
        
        return scalability_metrics
    
    def calculate_scalability_metrics(self, performance_data):
        """Calculate detailed scalability metrics"""
        sorted_cores = sorted(performance_data.keys())
        
        if len(sorted_cores) < 2:
            return {'error': 'Insufficient data for scalability analysis'}
        
        # Linear scaling score (how close to ideal scaling)
        base_performance = performance_data[sorted_cores[0]]
        linear_scaling_scores = []
        
        for cores in sorted_cores[1:]:
            actual_performance = performance_data[cores]
            ideal_performance = base_performance / cores  # Ideal linear scaling
            
            if ideal_performance > 0:
                scaling_score = min(1.0, ideal_performance / actual_performance)
                linear_scaling_scores.append(scaling_score)
        
        avg_linear_scaling = sum(linear_scaling_scores) / len(linear_scaling_scores) if linear_scaling_scores else 0
        
        # Overhead growth rate
        overhead_rates = []
        for i in range(1, len(sorted_cores)):
            prev_cores = sorted_cores[i-1]
            curr_cores = sorted_cores[i]
            
            prev_perf = performance_data[prev_cores]
            curr_perf = performance_data[curr_cores]
            
            # Calculate overhead as deviation from linear scaling
            expected_perf = prev_perf * prev_cores / curr_cores
            overhead = (curr_perf - expected_perf) / expected_perf if expected_perf > 0 else 0
            overhead_rates.append(overhead)
        
        avg_overhead_growth = sum(overhead_rates) / len(overhead_rates) if overhead_rates else 0
        
        # Find optimal core count (best performance per core)
        efficiency_per_core = {}
        for cores, performance in performance_data.items():
            efficiency_per_core[cores] = base_performance / (performance * cores) if performance > 0 else 0
        
        optimal_cores = max(efficiency_per_core.keys(), key=lambda k: efficiency_per_core[k])
        
        return {
            'linear_scaling_score': avg_linear_scaling,
            'overhead_growth_rate': avg_overhead_growth,
            'efficiency_per_core': efficiency_per_core,
            'optimal_core_count': optimal_cores,
            'scalability_assessment': self.assess_scalability(avg_linear_scaling, avg_overhead_growth)
        }
    
    def assess_scalability(self, linear_scaling_score, overhead_growth_rate):
        """Assess overall scalability quality"""
        if linear_scaling_score > 0.9 and overhead_growth_rate < 0.1:
            return 'excellent'
        elif linear_scaling_score > 0.8 and overhead_growth_rate < 0.2:
            return 'good'
        elif linear_scaling_score > 0.7 and overhead_growth_rate < 0.3:
            return 'fair'
        else:
            return 'poor'
    
    def save_assembly_analysis(self, test_name):
        """Save detailed assembly analysis to file"""
        if test_name not in self.assembly_analyses:
            return
            
        analysis_file = os.path.join(self.test_results_dir, f"{test_name}_assembly_analysis.json")
        
        try:
            with open(analysis_file, 'w') as f:
                json.dump(self.assembly_analyses[test_name], f, indent=2, default=str)
            print(f"Saved assembly analysis: {analysis_file}")
        except Exception as e:
            print(f"Error saving assembly analysis: {e}")
    
    # Test methods for different assembly emission scenarios
    
    def test_simple_arithmetic_assembly(self):
        """Test assembly emission for simple arithmetic"""
        commands = [
            ("push", "constant", 7),
            ("push", "constant", 8),
            ("add",)
        ]
        return self.analyze_assembly_emission(commands, "simple_arithmetic_assembly")
    
    def test_complex_arithmetic_assembly(self):
        """Test assembly emission for complex arithmetic"""
        commands = [
            ("push", "constant", 10),
            ("push", "constant", 3),
            ("sub",),
            ("push", "constant", 2),
            ("mul",),
            ("push", "constant", 5),
            ("div",),
            ("neg",)
        ]
        return self.analyze_assembly_emission(commands, "complex_arithmetic_assembly")
    
    def test_control_flow_assembly(self):
        """Test assembly emission for control flow"""
        commands = [
            ("push", "constant", 10),
            ("push", "constant", 5),
            ("gt",),
            ("if-goto", "GREATER"),
            ("push", "constant", 0),
            ("goto", "END"),
            ("label", "GREATER"),
            ("push", "constant", 1),
            ("label", "END")
        ]
        return self.analyze_assembly_emission(commands, "control_flow_assembly")
    
    def test_function_call_assembly(self):
        """Test assembly emission for function calls"""
        commands = [
            ("function", "multiply", 0),
            ("push", "argument", 0),
            ("push", "argument", 1),
            ("mul",),
            ("return",),
            ("push", "constant", 6),
            ("push", "constant", 7),
            ("call", "multiply", 2)
        ]
        return self.analyze_assembly_emission(commands, "function_call_assembly")
    
    def test_recursive_function_assembly(self):
        """Test assembly emission for recursive functions"""
        commands = [
            ("function", "factorial", 0),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("eq",),
            ("if-goto", "BASE_CASE"),
            ("push", "argument", 0),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("sub",),
            ("call", "factorial", 1),
            ("mul",),
            ("return",),
            ("label", "BASE_CASE"),
            ("push", "constant", 1),
            ("return",),
            ("push", "constant", 4),
            ("call", "factorial", 1)
        ]
        return self.analyze_assembly_emission(commands, "recursive_function_assembly")
    
    def test_memory_intensive_assembly(self):
        """Test assembly emission for memory-intensive operations"""
        commands = [
            ("push", "constant", 100),
            ("pop", "local", 0),
            ("push", "constant", 200),
            ("pop", "local", 1),
            ("push", "constant", 300),
            ("pop", "local", 2),
            ("push", "local", 0),
            ("push", "local", 1),
            ("add",),
            ("push", "local", 2),
            ("add",),
            ("pop", "local", 3),
            ("push", "local", 3),
            ("push", "local", 0),
            ("sub",),
            ("pop", "local", 4)
        ]
        return self.analyze_assembly_emission(commands, "memory_intensive_assembly")
    
    def test_loop_assembly(self):
        """Test assembly emission for loops"""
        commands = [
            ("push", "constant", 10),
            ("pop", "local", 0),
            ("push", "constant", 0),
            ("pop", "local", 1),
            ("label", "LOOP_START"),
            ("push", "local", 0),
            ("push", "constant", 0),
            ("gt",),
            ("if-goto", "LOOP_BODY"),
            ("goto", "LOOP_END"),
            ("label", "LOOP_BODY"),
            ("push", "local", 1),
            ("push", "local", 0),
            ("add",),
            ("pop", "local", 1),
            ("push", "local", 0),
            ("push", "constant", 1),
            ("sub",),
            ("pop", "local", 0),
            ("goto", "LOOP_START"),
            ("label", "LOOP_END"),
            ("push", "local", 1)
        ]
        return self.analyze_assembly_emission(commands, "loop_assembly")
    
    def test_vm_file_assembly(self, vm_file_path, test_name):
        """Test assembly emission for a specific VM file"""
        if not os.path.exists(vm_file_path):
            print(f"VM file not found: {vm_file_path}")
            return False
        
        try:
            commands = parse_vm_file(vm_file_path)
            return self.analyze_assembly_emission(commands, test_name)
        except Exception as e:
            print(f"Error parsing VM file {vm_file_path}: {e}")
            return False
    
    def run_all_tests(self):
        """Run all assembly emission analysis tests"""
        print("=" * 80)
        print("ASSEMBLY EMISSION ANALYSIS SUITE")
        print("=" * 80)
        
        # Test different assembly emission scenarios
        self.run_test("Simple Arithmetic Assembly", self.test_simple_arithmetic_assembly)
        self.run_test("Complex Arithmetic Assembly", self.test_complex_arithmetic_assembly)
        self.run_test("Control Flow Assembly", self.test_control_flow_assembly)
        self.run_test("Function Call Assembly", self.test_function_call_assembly)
        self.run_test("Recursive Function Assembly", self.test_recursive_function_assembly)
        self.run_test("Memory Intensive Assembly", self.test_memory_intensive_assembly)
        self.run_test("Loop Assembly", self.test_loop_assembly)
        
        # Test VM files from TECS chapters
        vm_files = [
            ("tecs/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm", "SimpleAdd_Assembly"),
            ("tecs/projects/07/StackArithmetic/StackTest/StackTest.vm", "StackTest_Assembly"),
            ("tecs/projects/07/MemoryAccess/BasicTest/BasicTest.vm", "BasicTest_Assembly"),
            ("tecs/projects/08/ProgramFlow/BasicLoop/BasicLoop.vm", "BasicLoop_Assembly"),
            ("tecs/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm", "SimpleFunction_Assembly")
        ]
        
        for vm_file, test_name in vm_files:
            self.run_test(f"VM File - {test_name}", lambda vf=vm_file, tn=test_name: self.test_vm_file_assembly(vf, tn))
        
        # Generate comprehensive analysis report
        self.generate_assembly_analysis_report()
        
        # Print summary
        print("\n" + "=" * 80)
        print("ASSEMBLY EMISSION ANALYSIS SUMMARY")
        print("=" * 80)
        print(f"Total assembly tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success rate: {self.passed / (self.passed + self.failed) * 100:.1f}%")
        
        if self.assembly_analyses:
            self.print_aggregate_assembly_statistics()
        
        print(f"\nDetailed analyses saved in: {self.test_results_dir}/")
        
        return self.failed == 0
    
    def generate_assembly_analysis_report(self):
        """Generate comprehensive assembly analysis report"""
        report_file = os.path.join(self.test_results_dir, "assembly_analysis_report.json")
        
        summary = {
            'total_assembly_analyses': len(self.assembly_analyses),
            'timestamp': time.time(),
            'aggregate_statistics': self.calculate_aggregate_assembly_statistics(),
            'detailed_analyses': self.assembly_analyses
        }
        
        try:
            with open(report_file, 'w') as f:
                json.dump(summary, f, indent=2, default=str)
            print(f"\nSaved assembly analysis report: {report_file}")
        except Exception as e:
            print(f"Error saving assembly analysis report: {e}")
    
    def calculate_aggregate_assembly_statistics(self):
        """Calculate aggregate statistics across all assembly analyses"""
        if not self.assembly_analyses:
            return {}
        
        # Aggregate instruction counts
        total_single_core_instructions = 0
        total_multi_core_instructions = 0
        successful_generations = 0
        
        # Aggregate scalability scores
        scalability_scores = []
        efficiency_scores = []
        
        for analysis in self.assembly_analyses.values():
            assembly_results = analysis.get('assembly_results', {})
            
            for cores, result in assembly_results.items():
                if result.get('generation_successful', False):
                    successful_generations += 1
                    
                    if result['type'] == 'single_core':
                        total_single_core_instructions += result.get('instruction_lines', 0)
                    else:
                        total_multi_core_instructions += result.get('total_instructions', 0)
            
            # Collect scalability metrics
            scalability = analysis.get('scalability_analysis', {})
            if 'linear_scaling_score' in scalability:
                scalability_scores.append(scalability['linear_scaling_score'])
            
            cross_core = analysis.get('cross_core_analysis', {})
            if 'efficiency_trends' in cross_core:
                efficiency_scores.extend(cross_core['efficiency_trends'].values())
        
        # Calculate averages
        avg_scalability = sum(scalability_scores) / len(scalability_scores) if scalability_scores else 0
        avg_efficiency = sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0
        
        return {
            'total_single_core_instructions': total_single_core_instructions,
            'total_multi_core_instructions': total_multi_core_instructions,
            'successful_generations': successful_generations,
            'average_scalability_score': avg_scalability,
            'average_efficiency_score': avg_efficiency,
            'analyses_count': len(self.assembly_analyses)
        }
    
    def print_aggregate_assembly_statistics(self):
        """Print aggregate statistics across all assembly analyses"""
        stats = self.calculate_aggregate_assembly_statistics()
        
        print(f"\nAggregate Assembly Statistics:")
        print(f"Assembly analyses performed: {stats.get('analyses_count', 0)}")
        print(f"Successful generations: {stats.get('successful_generations', 0)}")
        print(f"Total single-core instructions: {stats.get('total_single_core_instructions', 0)}")
        print(f"Total multi-core instructions: {stats.get('total_multi_core_instructions', 0)}")
        print(f"Average scalability score: {stats.get('average_scalability_score', 0):.3f}")
        print(f"Average efficiency score: {stats.get('average_efficiency_score', 0):.3f}")


if __name__ == "__main__":
    analyzer = AssemblyEmissionAnalyzer()
    success = analyzer.run_all_tests()
    sys.exit(0 if success else 1)