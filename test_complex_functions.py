#!/usr/bin/env python3
"""
Test more complex function scenarios in Petri net VM
"""

import sys
import os
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def test_multiple_functions():
    """Test multiple function definitions and calls"""
    print("=== Testing Multiple Functions ===")
    
    commands = [
        # Define first function: square a number (x * x)
        ("function", "Math.square", 0),
        ("push", "argument", 0),
        ("push", "argument", 0),
        ("mul",),  # Not implemented yet, but structure is there
        ("return",),
        
        # Define second function: add two numbers
        ("function", "Math.add", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("add",),
        ("return",),
        
        # Define third function: subtract two numbers  
        ("function", "Math.sub", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("sub",),
        ("return",),
        
        # Main program: test all functions
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("call", "Math.add", 2),      # 10 + 5 = 15
        
        ("push", "constant", 3),
        ("call", "Math.sub", 2),      # 15 - 3 = 12
        
        # Result should be 12
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [12]")
        
        # Print network statistics
        translator.print_net_statistics()
        
        # Check if result is correct
        if result and len(result) >= 1 and result[-1] == 12:
            print("✅ Multiple functions test PASSED")
            return True
        else:
            print("❌ Multiple functions test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in multiple functions test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_function_composition():
    """Test calling one function from another"""
    print("\n=== Testing Function Composition ===")
    
    commands = [
        # Define helper function: increment by 1
        ("function", "Math.inc", 0),
        ("push", "argument", 0),
        ("push", "constant", 1),
        ("add",),
        ("return",),
        
        # Define main function: increment twice
        ("function", "Math.incTwice", 0),
        ("push", "argument", 0),
        ("call", "Math.inc", 1),      # First increment
        ("call", "Math.inc", 1),      # Second increment  
        ("return",),
        
        # Main program
        ("push", "constant", 5),
        ("call", "Math.incTwice", 1), # Should be 5 + 1 + 1 = 7
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [7]")
        
        # Print network statistics
        translator.print_net_statistics()
        
        # Check if result is correct
        if result and len(result) >= 1 and result[-1] == 7:
            print("✅ Function composition test PASSED")
            return True
        else:
            print("❌ Function composition test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in function composition test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_function_with_no_args():
    """Test function with no arguments"""
    print("\n=== Testing Function with No Arguments ===")
    
    commands = [
        # Define function that returns a constant
        ("function", "Constants.pi", 0),
        ("push", "constant", 314),  # Approximation of pi * 100
        ("return",),
        
        # Define function that returns another constant
        ("function", "Constants.e", 0),
        ("push", "constant", 271),   # Approximation of e * 100
        ("return",),
        
        # Main program: add pi and e
        ("call", "Constants.pi", 0),
        ("call", "Constants.e", 0),
        ("add",),  # Should be 314 + 271 = 585
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [585]")
        
        # Print network statistics
        translator.print_net_statistics()
        
        # Check if result is correct
        if result and len(result) >= 1 and result[-1] == 585:
            print("✅ Function with no arguments test PASSED")
            return True
        else:
            print("❌ Function with no arguments test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in function with no arguments test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Complex Petri Net VM Function Scenarios")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run tests
    total_tests += 1
    if test_multiple_functions():
        tests_passed += 1
    
    total_tests += 1
    if test_function_composition():
        tests_passed += 1
        
    total_tests += 1
    if test_function_with_no_args():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed or were skipped")