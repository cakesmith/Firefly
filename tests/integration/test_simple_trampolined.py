#!/usr/bin/env python3
"""
Simple Test for Trampolined Recursion
Tests basic trampolined recursion functionality
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from Petri.VMToPetri import VMToPetriTranslator

def test_simple_factorial():
    """
    Test simple factorial function with trampolined recursion
    """
    print("=== Testing Simple Factorial with Trampolined Recursion ===")
    
    # Simple factorial function
    commands = [
        # function factorial 0
        ("function", "factorial", 0),
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("eq",),                        # n == 1?
        ("if-goto", "BASE_CASE"),       # if n == 1, goto BASE_CASE
        
        # Recursive case: n * factorial(n-1)
        ("push", "argument", 0),        # push n
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("sub",),                       # n - 1
        ("call", "factorial", 1),       # factorial(n-1)
        ("mul",),                       # n * factorial(n-1)
        ("return",),
        
        # Base case: return 1
        ("label", "BASE_CASE"),
        ("push", "constant", 1),        # return 1
        ("return",),
        
        # Main program: compute factorial(3)
        ("push", "constant", 3),        # push 3
        ("call", "factorial", 1),       # factorial(3)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        
        # Check result correctness (3! = 6)
        if result and len(result) >= 1 and result[-1] == 6:
            print("[PASS] Trampolined factorial result correct: factorial(3) = 6")
            return True
        else:
            print(f"[FAIL] Incorrect result: {result}, expected [6]")
            return False
        
    except Exception as e:
        print(f"[FAIL] Error in simple factorial test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_simple_countdown():
    """
    Test simple countdown function
    """
    print("\n=== Testing Simple Countdown ===")
    
    # Simple countdown function
    commands = [
        # function countdown 0
        ("function", "countdown", 0),
        ("push", "argument", 0),        # push n
        ("push", "constant", 0),        # push 0
        ("eq",),                        # n == 0?
        ("if-goto", "BASE_CASE"),       # if n == 0, goto BASE_CASE
        
        # Recursive case: countdown(n-1)
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("sub",),                       # n - 1
        ("call", "countdown", 1),       # countdown(n-1)
        ("return",),
        
        # Base case: return 42
        ("label", "BASE_CASE"),
        ("push", "constant", 42),       # return 42
        ("return",),
        
        # Main program: compute countdown(3) - small number to avoid infinite loop
        ("push", "constant", 3),        # push 3
        ("call", "countdown", 1),       # countdown(3)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        
        # Check result correctness
        if result and len(result) >= 1 and result[-1] == 42:
            print("[PASS] Trampolined countdown result correct: countdown(3) = 42")
            return True
        else:
            print(f"[FAIL] Incorrect result: {result}, expected [42]")
            return False
        
    except Exception as e:
        print(f"[FAIL] Error in simple countdown test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Simple Trampolined Recursion")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Run tests
    total_tests += 1
    if test_simple_factorial():
        tests_passed += 1
    
    total_tests += 1
    if test_simple_countdown():
        tests_passed += 1
    
    print(f"\n" + "=" * 50)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("SUCCESS: All simple trampolined recursion tests passed!")
        sys.exit(0)
    else:
        print("WARNING: Some tests failed")
        sys.exit(1)