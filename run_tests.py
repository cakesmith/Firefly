#!/usr/bin/env python3
"""
Quick test runner for Petri-net VM
"""

import sys
from test_petri_net_vm import PetriVMTestSuite

def main():
    """Run tests with optional filtering"""
    if len(sys.argv) > 1:
        test_filter = sys.argv[1].lower()
        suite = PetriVMTestSuite()
        
        if test_filter == "basic":
            print("Running basic VM tests only...")
            suite.run_test("Basic Operations", suite.test_basic_operations)
            suite.run_test("Arithmetic Sequence", suite.test_arithmetic_sequence)
            suite.run_test("Stack-Free Semantics", suite.test_stack_free_semantics)
        
        elif test_filter == "assembly":
            print("Running assembly generation tests only...")
            suite.run_test("Single-Core Assembly", suite.test_single_core_assembly)
            suite.run_test("Multi-Core Assembly", suite.test_multi_core_assembly)
        
        elif test_filter == "complex":
            print("Running complex tests only...")
            suite.run_test("Complex Operations", suite.test_complex_operations)
            suite.run_test("StackTest Multi-Core", suite.test_stacktest_multicore)
        
        else:
            print(f"Unknown filter: {test_filter}")
            print("Available filters: basic, assembly, complex")
            return
        
        print(f"\nFiltered tests: {suite.passed} passed, {suite.failed} failed")
    
    else:
        # Run all tests
        suite = PetriVMTestSuite()
        suite.run_all_tests()

if __name__ == "__main__":
    main()