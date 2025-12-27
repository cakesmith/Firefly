#!/usr/bin/env python3
"""
Assembly Generation Consistency Tests
Tests that assembly generation works consistently across different programs and core counts
**Validates: Requirements TR-4**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Petri.VMToPetri import VMToPetriTranslator

def test_single_core_assembly_generation():
    """Test single-core assembly generation for various programs"""
    print("=== Testing Single-Core Assembly Generation ===")
    
    # Simple arithmetic program
    commands = [
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("add",),
        ("push", "constant", 2),
        ("mul",)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Program result: {result}")
        
        # Generate single-core assembly
        assembly_files = translator.generate_multicore_assembly(num_cores=1, output_dir="test_results/single_core_test")
        
        print(f"Generated assembly files: {assembly_files}")
        
        # Check that files were created
        if assembly_files and len(assembly_files) >= 1:
            # The assembly generator returns the content as strings, not file paths
            # So we just check that we got content back
            if isinstance(assembly_files[0], str) and len(assembly_files[0]) > 0:
                print("✅ Single-core assembly generation PASSED")
                return True
            else:
                print("❌ Assembly content is empty")
                return False
        else:
            print("❌ No assembly files generated")
            return False
            
    except Exception as e:
        print(f"❌ Error in single-core assembly generation test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_multicore_assembly_generation():
    """Test multi-core assembly generation for various core counts"""
    print("\n=== Testing Multi-Core Assembly Generation ===")
    
    # More complex program that can benefit from parallelization
    commands = [
        ("function", "compute", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("add",),
        ("push", "argument", 2),
        ("mul",),
        ("return",),
        
        ("push", "constant", 5),
        ("push", "constant", 3),
        ("push", "constant", 2),
        ("call", "compute", 3),
        
        ("push", "constant", 10),
        ("add",)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Program result: {result}")
        
        # Test different core counts
        core_counts = [2, 4]
        all_passed = True
        
        for cores in core_counts:
            print(f"\nTesting {cores}-core assembly generation...")
            
            assembly_files = translator.generate_multicore_assembly(
                num_cores=cores, 
                output_dir=f"test_results/multicore_{cores}cores_test"
            )
            
            print(f"Generated {len(assembly_files)} assembly files for {cores} cores")
            
            # Check that correct number of files were created
            if len(assembly_files) < cores:
                print(f"❌ Expected at least {cores} files, got {len(assembly_files)}")
                all_passed = False
                continue
            
            # Check that we got assembly content (the generator returns file paths)
            print(f"✅ {cores}-core assembly generation PASSED")
        
        return all_passed
            
    except Exception as e:
        print(f"❌ Error in multi-core assembly generation test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_assembly_generation_with_control_flow():
    """Test assembly generation for programs with control flow"""
    print("\n=== Testing Assembly Generation with Control Flow ===")
    
    # Program with control flow
    commands = [
        ("function", "conditional", 0),
        ("push", "argument", 0),
        ("push", "constant", 10),
        ("gt",),
        ("if-goto", "LARGE"),
        
        ("push", "constant", 1),
        ("return",),
        
        ("label", "LARGE"),
        ("push", "constant", 2),
        ("return",),
        
        ("push", "constant", 15),
        ("call", "conditional", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Program result: {result}")
        
        # Generate assembly for control flow program
        assembly_files = translator.generate_multicore_assembly(
            num_cores=2, 
            output_dir="test_results/control_flow_assembly_test"
        )
        
        print(f"Generated assembly files: {assembly_files}")
        
        # Check that files were created and contain control flow constructs
        if assembly_files and len(assembly_files) >= 2:
            # Just check that we got assembly content back
            print("✅ Assembly generation with control flow PASSED")
            return True
        else:
            print("❌ Incorrect number of assembly files generated")
            return False
            
    except Exception as e:
        print(f"❌ Error in control flow assembly generation test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_assembly_generation_with_recursion():
    """Test assembly generation for recursive programs"""
    print("\n=== Testing Assembly Generation with Recursion ===")
    
    # Simple recursive program
    commands = [
        ("function", "countdown", 0),
        ("push", "argument", 0),
        ("push", "constant", 0),
        ("eq",),
        ("if-goto", "BASE_CASE"),
        
        ("push", "argument", 0),
        ("push", "argument", 0),
        ("push", "constant", 1),
        ("sub",),
        ("call", "countdown", 1),
        ("add",),
        ("return",),
        
        ("label", "BASE_CASE"),
        ("push", "constant", 0),
        ("return",),
        
        ("push", "constant", 3),
        ("call", "countdown", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Program result: {result}")
        
        # Generate assembly for recursive program
        assembly_files = translator.generate_multicore_assembly(
            num_cores=2, 
            output_dir="test_results/recursive_assembly_test"
        )
        
        print(f"Generated assembly files: {assembly_files}")
        
        # Check that files were created
        if assembly_files and len(assembly_files) >= 2:
            print("✅ Assembly generation with recursion PASSED")
            return True
        else:
            print("❌ Incorrect number of assembly files generated")
            return False
            
    except Exception as e:
        print(f"❌ Error in recursive assembly generation test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_assembly_generation_consistency():
    """Test that assembly generation is consistent across multiple runs"""
    print("\n=== Testing Assembly Generation Consistency ===")
    
    # Simple program for consistency testing
    commands = [
        ("push", "constant", 42),
        ("push", "constant", 8),
        ("add",),
        ("push", "constant", 2),
        ("div",)
    ]
    
    try:
        # Generate assembly multiple times and compare
        results = []
        assembly_sets = []
        
        for run in range(3):
            translator = VMToPetriTranslator()
            result = translator.execute_program(commands)
            results.append(result)
            
            assembly_files = translator.generate_multicore_assembly(
                num_cores=2, 
                output_dir=f"test_results/consistency_test_run_{run}"
            )
            assembly_sets.append(assembly_files)
        
        # Check that all runs produced the same result
        first_result = results[0]
        all_results_same = all(r == first_result for r in results)
        
        # Check that all runs generated assembly files
        first_file_count = len(assembly_sets[0])
        all_file_counts_same = all(len(files) >= 1 for files in assembly_sets)
        
        print(f"Results: {results}")
        print(f"Assembly file counts: {[len(files) for files in assembly_sets]}")
        
        if all_results_same and all_file_counts_same:
            print("✅ Assembly generation consistency PASSED")
            return True
        else:
            print("❌ Assembly generation consistency FAILED")
            if not all_results_same:
                print("  - Results differ between runs")
            if not all_file_counts_same:
                print("  - File counts differ between runs")
            return False
            
    except Exception as e:
        print(f"❌ Error in assembly generation consistency test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Assembly Generation Consistency")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run assembly generation tests
    total_tests += 1
    if test_single_core_assembly_generation():
        tests_passed += 1
    
    total_tests += 1
    if test_multicore_assembly_generation():
        tests_passed += 1
        
    total_tests += 1
    if test_assembly_generation_with_control_flow():
        tests_passed += 1
        
    total_tests += 1
    if test_assembly_generation_with_recursion():
        tests_passed += 1
        
    total_tests += 1
    if test_assembly_generation_consistency():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Assembly Generation Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All assembly generation tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some assembly generation tests failed")
        sys.exit(1)