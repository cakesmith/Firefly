#!/usr/bin/env python3
"""
Integration Tests for Control Flow Operations
Tests simple loops using goto/if-goto, conditional execution patterns, and nested control structures
**Validates: Requirements US-3.1, US-3.2, US-3.3**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Petri.VMToPetri import VMToPetriTranslator

def test_simple_conditional_execution():
    """Test simple if-goto conditional execution pattern"""
    print("=== Testing Simple Conditional Execution ===")
    
    # Test conditional execution: if condition then return 100 else return 200
    commands = [
        ("function", "test_conditional", 0),
        ("push", "argument", 0),        # Get condition argument
        ("if-goto", "TRUE_BRANCH"),     # If non-zero, goto TRUE_BRANCH
        # False branch
        ("push", "constant", 200),      # Return 200 for false
        ("goto", "END"),                # Skip true branch
        ("label", "TRUE_BRANCH"),       # True branch label
        ("push", "constant", 100),      # Return 100 for true
        ("label", "END"),               # End label
        ("return",),
        
        # Test with true condition (non-zero)
        ("push", "constant", 5),        # Non-zero condition
        ("call", "test_conditional", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for condition=5: {result}")
        
        if result and len(result) >= 1 and result[-1] == 100:
            print("✅ True condition test PASSED")
        else:
            print("❌ True condition test FAILED")
            return False
            
        # Test with false condition (zero)
        commands_false = [
            ("function", "test_conditional", 0),
            ("push", "argument", 0),        # Get condition argument
            ("if-goto", "TRUE_BRANCH"),     # If non-zero, goto TRUE_BRANCH
            # False branch
            ("push", "constant", 200),      # Return 200 for false
            ("goto", "END"),                # Skip true branch
            ("label", "TRUE_BRANCH"),       # True branch label
            ("push", "constant", 100),      # Return 100 for true
            ("label", "END"),               # End label
            ("return",),
            
            # Test with false condition (zero)
            ("push", "constant", 0),        # Zero condition
            ("call", "test_conditional", 1)
        ]
        
        translator_false = VMToPetriTranslator()
        result_false = translator_false.execute_program(commands_false)
        print(f"Result for condition=0: {result_false}")
        
        if result_false and len(result_false) >= 1 and result_false[-1] == 200:
            print("✅ False condition test PASSED")
            return True
        else:
            print("❌ False condition test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in conditional execution test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_simple_loop_pattern():
    """Test simple loop using goto/if-goto pattern"""
    print("\n=== Testing Simple Loop Pattern ===")
    
    # Simple counting loop: count from 0 to N-1, return sum
    commands = [
        ("function", "count_loop", 2),      # 2 locals: counter, sum
        # Initialize locals
        ("push", "constant", 0),
        ("pop", "local", 0),                # counter = 0
        ("push", "constant", 0),
        ("pop", "local", 1),                # sum = 0
        
        ("label", "LOOP_START"),            # Loop start label
        # Check if counter < N (argument 0)
        ("push", "local", 0),               # Push counter
        ("push", "argument", 0),            # Push N
        ("lt",),                            # counter < N?
        ("if-goto", "LOOP_BODY"),           # If true, continue loop
        ("goto", "LOOP_END"),               # Else exit loop
        
        ("label", "LOOP_BODY"),             # Loop body
        # sum += counter
        ("push", "local", 1),               # Push sum
        ("push", "local", 0),               # Push counter
        ("add",),                           # sum + counter
        ("pop", "local", 1),                # Store back to sum
        # counter++
        ("push", "local", 0),               # Push counter
        ("push", "constant", 1),            # Push 1
        ("add",),                           # counter + 1
        ("pop", "local", 0),                # Store back to counter
        ("goto", "LOOP_START"),             # Go back to loop start
        
        ("label", "LOOP_END"),              # Loop end
        ("push", "local", 1),               # Return sum
        ("return",),
        
        # Test: count from 0 to 4 (sum should be 0+1+2+3+4 = 10)
        ("push", "constant", 5),            # N = 5
        ("call", "count_loop", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for N=5: {result}")
        print(f"Expected: [10] (sum of 0+1+2+3+4)")
        
        if result and len(result) >= 1 and result[-1] == 10:
            print("✅ Simple loop test PASSED")
            return True
        else:
            print("❌ Simple loop test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in loop test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_nested_control_structures():
    """Test nested if-goto and goto structures"""
    print("\n=== Testing Nested Control Structures ===")
    
    # Nested conditional: if x > 0 then (if x > 10 then return 1 else return 2) else return 3
    commands = [
        ("function", "nested_test", 0),
        ("push", "argument", 0),            # Get x
        ("push", "constant", 0),            # Push 0
        ("gt",),                            # x > 0?
        ("if-goto", "POSITIVE"),            # If positive, check further
        # x <= 0 case
        ("push", "constant", 3),            # Return 3
        ("goto", "END"),
        
        ("label", "POSITIVE"),              # x > 0 case
        ("push", "argument", 0),            # Get x again
        ("push", "constant", 10),           # Push 10
        ("gt",),                            # x > 10?
        ("if-goto", "LARGE"),               # If large, return 1
        # 0 < x <= 10 case
        ("push", "constant", 2),            # Return 2
        ("goto", "END"),
        
        ("label", "LARGE"),                 # x > 10 case
        ("push", "constant", 1),            # Return 1
        
        ("label", "END"),
        ("return",),
        
        # Test with x = 15 (should return 1)
        ("push", "constant", 15),
        ("call", "nested_test", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for x=15: {result}")
        print(f"Expected: [1] (x > 10)")
        
        if result and len(result) >= 1 and result[-1] == 1:
            print("✅ Nested control test (x=15) PASSED")
        else:
            print("❌ Nested control test (x=15) FAILED")
            return False
            
        # Test with x = 5 (should return 2)
        commands_mid = [
            ("function", "nested_test", 0),
            ("push", "argument", 0),            # Get x
            ("push", "constant", 0),            # Push 0
            ("gt",),                            # x > 0?
            ("if-goto", "POSITIVE"),            # If positive, check further
            # x <= 0 case
            ("push", "constant", 3),            # Return 3
            ("goto", "END"),
            
            ("label", "POSITIVE"),              # x > 0 case
            ("push", "argument", 0),            # Get x again
            ("push", "constant", 10),           # Push 10
            ("gt",),                            # x > 10?
            ("if-goto", "LARGE"),               # If large, return 1
            # 0 < x <= 10 case
            ("push", "constant", 2),            # Return 2
            ("goto", "END"),
            
            ("label", "LARGE"),                 # x > 10 case
            ("push", "constant", 1),            # Return 1
            
            ("label", "END"),
            ("return",),
            
            # Test with x = 5 (should return 2)
            ("push", "constant", 5),
            ("call", "nested_test", 1)
        ]
        
        translator_mid = VMToPetriTranslator()
        result_mid = translator_mid.execute_program(commands_mid)
        print(f"Result for x=5: {result_mid}")
        print(f"Expected: [2] (0 < x <= 10)")
        
        if result_mid and len(result_mid) >= 1 and result_mid[-1] == 2:
            print("✅ Nested control test (x=5) PASSED")
        else:
            print("❌ Nested control test (x=5) FAILED")
            return False
            
        # Test with x = -3 (should return 3)
        commands_neg = [
            ("function", "nested_test", 0),
            ("push", "argument", 0),            # Get x
            ("push", "constant", 0),            # Push 0
            ("gt",),                            # x > 0?
            ("if-goto", "POSITIVE"),            # If positive, check further
            # x <= 0 case
            ("push", "constant", 3),            # Return 3
            ("goto", "END"),
            
            ("label", "POSITIVE"),              # x > 0 case
            ("push", "argument", 0),            # Get x again
            ("push", "constant", 10),           # Push 10
            ("gt",),                            # x > 10?
            ("if-goto", "LARGE"),               # If large, return 1
            # 0 < x <= 10 case
            ("push", "constant", 2),            # Return 2
            ("goto", "END"),
            
            ("label", "LARGE"),                 # x > 10 case
            ("push", "constant", 1),            # Return 1
            
            ("label", "END"),
            ("return",),
            
            # Test with x = -3 (should return 3)
            ("push", "constant", -3),
            ("call", "nested_test", 1)
        ]
        
        translator_neg = VMToPetriTranslator()
        result_neg = translator_neg.execute_program(commands_neg)
        print(f"Result for x=-3: {result_neg}")
        print(f"Expected: [3] (x <= 0)")
        
        if result_neg and len(result_neg) >= 1 and result_neg[-1] == 3:
            print("✅ Nested control test (x=-3) PASSED")
            return True
        else:
            print("❌ Nested control test (x=-3) FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in nested control structures test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_label_and_goto_basic():
    """Test basic label definition and goto functionality"""
    print("\n=== Testing Basic Label and Goto ===")
    
    # Simple goto test: skip some code using goto
    commands = [
        ("function", "goto_test", 0),
        ("goto", "SKIP_CODE"),              # Jump over the next instruction
        ("push", "constant", 999),          # This should be skipped
        ("return",),                        # This should also be skipped
        ("label", "SKIP_CODE"),             # Jump target
        ("push", "constant", 42),           # This should execute
        ("return",),
        
        ("call", "goto_test", 0)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [42] (should skip 999)")
        
        if result and len(result) >= 1 and result[-1] == 42:
            print("✅ Basic goto test PASSED")
            return True
        else:
            print("❌ Basic goto test FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in basic goto test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Petri Net VM Control Flow Integration")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run tests
    total_tests += 1
    if test_simple_conditional_execution():
        tests_passed += 1
    
    total_tests += 1
    if test_simple_loop_pattern():
        tests_passed += 1
        
    total_tests += 1
    if test_nested_control_structures():
        tests_passed += 1
        
    total_tests += 1
    if test_label_and_goto_basic():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All control flow integration tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some control flow tests failed")
        sys.exit(1)