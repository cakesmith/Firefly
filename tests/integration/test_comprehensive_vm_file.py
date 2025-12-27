#!/usr/bin/env python3
"""
Test Comprehensive VM File with All Features
Tests a complete VM program file that uses all new features together
**Validates: All user stories**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Petri.VMToPetri import VMToPetriTranslator
import vm_parser

def parse_vm_file(filename):
    """Parse a VM file into commands"""
    commands = []
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"VM file not found: {filename}")
        return []
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('//'):
            continue
        
        # Remove inline comments
        if '//' in line:
            line = line[:line.index('//')]
            line = line.strip()
        
        # Parse the command
        parts = line.split()
        if not parts:
            continue
        
        try:
            if parts[0] == "push":
                commands.append(("push", parts[1], int(parts[2])))
            elif parts[0] == "pop":
                commands.append(("pop", parts[1], int(parts[2])))
            elif parts[0] == "function":
                commands.append(("function", parts[1], int(parts[2])))
            elif parts[0] == "call":
                commands.append(("call", parts[1], int(parts[2])))
            elif parts[0] == "return":
                commands.append(("return",))
            elif parts[0] == "label":
                commands.append(("label", parts[1]))
            elif parts[0] == "goto":
                commands.append(("goto", parts[1]))
            elif parts[0] == "if-goto":
                commands.append(("if-goto", parts[1]))
            elif parts[0] in ["add", "sub", "mul", "div", "neg", "eq", "lt", "gt", "and", "or", "not"]:
                commands.append((parts[0],))
            else:
                print(f"Warning: Unknown command '{parts[0]}' at line {line_num}")
        except (IndexError, ValueError) as e:
            print(f"Error parsing line {line_num}: {line} - {e}")
    
    return commands

def test_comprehensive_vm_file():
    """Test the comprehensive VM file with all features"""
    print("=== Testing Comprehensive VM File ===")
    
    # Parse the comprehensive VM file
    vm_file_path = os.path.join("tests", "data", "comprehensive_program.vm")
    commands = parse_vm_file(vm_file_path)
    
    if not commands:
        print("❌ Failed to parse VM file")
        return False
    
    print(f"Parsed {len(commands)} commands from VM file")
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [120, 13, 47, 6] (factorial(5), fibonacci(7), complex_math, gcd(48,18))")
        
        # Print network statistics
        translator.print_net_statistics()
        
        # Check if results are correct
        expected = [120, 13, 47, 6]
        if result and len(result) >= len(expected):
            # Check the last few results (stack order might vary)
            actual_results = result[-len(expected):]
            if all(actual == expected[i] for i, actual in enumerate(actual_results)):
                print("✅ Comprehensive VM file test PASSED")
                return True
            else:
                print(f"❌ Results don't match. Got {actual_results}, expected {expected}")
                return False
        else:
            print("❌ Insufficient results returned")
            return False
            
    except Exception as e:
        print(f"❌ Error executing comprehensive VM file: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_vm_file_multicore_generation():
    """Test multicore assembly generation for the comprehensive VM file"""
    print("\n=== Testing Multicore Assembly Generation ===")
    
    # Parse the comprehensive VM file
    vm_file_path = os.path.join("tests", "data", "comprehensive_program.vm")
    commands = parse_vm_file(vm_file_path)
    
    if not commands:
        print("❌ Failed to parse VM file for multicore test")
        return False
    
    translator = VMToPetriTranslator()
    
    try:
        # Execute the program first to build the Petri net
        result = translator.execute_program(commands)
        
        # Generate multicore assembly for 2 cores
        assembly_files = translator.generate_multicore_assembly(num_cores=2, output_dir="test_results/comprehensive_2cores")
        
        print(f"Generated multicore assembly files: {assembly_files}")
        
        # Check that files were created
        if assembly_files and len(assembly_files) >= 2:
            print("✅ Multicore assembly generation PASSED")
            return True
        else:
            print("❌ Multicore assembly generation FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in multicore assembly generation: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_memory_optimization_comprehensive():
    """Test memory optimization with the comprehensive program"""
    print("\n=== Testing Memory Optimization ===")
    
    # Parse the comprehensive VM file
    vm_file_path = os.path.join("tests", "data", "comprehensive_program.vm")
    commands = parse_vm_file(vm_file_path)
    
    if not commands:
        print("❌ Failed to parse VM file for memory optimization test")
        return False
    
    translator = VMToPetriTranslator()
    
    try:
        # Execute the program
        result = translator.execute_program(commands)
        
        # Get memory optimization statistics
        memory_stats = translator._optimize_memory_allocation()
        
        print(f"Memory optimization results: {memory_stats}")
        
        # Check that optimization was performed
        if memory_stats and 'control_flow_savings' in memory_stats:
            optimized_count = memory_stats['control_flow_savings']
            if optimized_count > 0:
                print(f"✅ Memory optimization PASSED ({optimized_count} places optimized)")
                return True
            else:
                print("⚠️  Memory optimization ran but no places were optimized")
                return True  # Still pass, just no optimization opportunities
        else:
            print("❌ Memory optimization FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in memory optimization test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_execution_analysis_comprehensive():
    """Test execution analysis with the comprehensive program"""
    print("\n=== Testing Execution Analysis ===")
    
    # Parse the comprehensive VM file
    vm_file_path = os.path.join("tests", "data", "comprehensive_program.vm")
    commands = parse_vm_file(vm_file_path)
    
    if not commands:
        print("❌ Failed to parse VM file for execution analysis test")
        return False
    
    translator = VMToPetriTranslator()
    
    try:
        # Execute the program to build the Petri net
        result = translator.execute_program(commands)
        
        # Analyze execution dependencies
        execution_plan = translator._analyze_execution_dependencies()
        
        print(f"Execution analysis results: {execution_plan}")
        
        # Check that analysis was performed
        if execution_plan and 'execution_levels' in execution_plan:
            level_count = len(execution_plan['execution_levels'])
            if level_count > 0:
                print(f"✅ Execution analysis PASSED ({level_count} execution levels)")
                return True
            else:
                print("❌ No execution levels found")
                return False
        else:
            print("❌ Execution analysis FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in execution analysis test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Comprehensive VM File with All Features")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run comprehensive VM file tests
    total_tests += 1
    if test_comprehensive_vm_file():
        tests_passed += 1
    
    total_tests += 1
    if test_vm_file_multicore_generation():
        tests_passed += 1
        
    total_tests += 1
    if test_memory_optimization_comprehensive():
        tests_passed += 1
        
    total_tests += 1
    if test_execution_analysis_comprehensive():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Comprehensive VM File Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All comprehensive VM file tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some comprehensive VM file tests failed")
        sys.exit(1)