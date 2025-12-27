#!/usr/bin/env python3
"""
Comprehensive Tests for Recursive Functions with Control Flow
Tests recursive functions combined with local variables, arithmetic, and control flow
**Validates: Requirements US-4.1, US-3.1, US-3.2, US-3.3, US-1.1, US-1.2**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Petri.VMToPetri import VMToPetriTranslator

def test_recursive_gcd_with_control_flow():
    """Test recursive Greatest Common Divisor using control flow"""
    print("=== Testing Recursive GCD with Control Flow ===")
    
    # Euclidean algorithm for GCD using recursion and control flow
    commands = [
        ("function", "gcd", 0),
        # Base case: if b == 0, return a
        ("push", "argument", 1),            # Get b
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # b == 0?
        ("if-goto", "BASE_CASE"),           # If b == 0, return a
        
        # Recursive case: gcd(b, a % b)
        # Since we don't have modulo, we'll use: gcd(b, a - (a/b)*b)
        ("push", "argument", 1),            # Push b (new a)
        ("push", "argument", 0),            # Push a
        ("push", "argument", 0),            # Push a
        ("push", "argument", 1),            # Push b
        ("div",),                           # a / b (integer division)
        ("push", "argument", 1),            # Push b
        ("mul",),                           # (a/b) * b
        ("sub",),                           # a - (a/b)*b = a % b (new b)
        ("call", "gcd", 2),                 # Recursive call
        ("return",),
        
        ("label", "BASE_CASE"),
        ("push", "argument", 0),            # Return a
        ("return",),
        
        # Test gcd(48, 18) = 6
        ("push", "constant", 48),
        ("push", "constant", 18),
        ("call", "gcd", 2)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for gcd(48, 18): {result}")
        print(f"Expected: [6]")
        
        if result and len(result) >= 1 and result[-1] == 6:
            print("✅ Recursive GCD with control flow PASSED")
            return True
        else:
            print("❌ Recursive GCD with control flow FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in recursive GCD test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_recursive_power_with_locals():
    """Test recursive power function using local variables"""
    print("\n=== Testing Recursive Power with Locals ===")
    
    # Power function: base^exponent using recursion and locals
    commands = [
        ("function", "power", 2),           # 2 locals for intermediate calculations
        # Base case: if exponent == 0, return 1
        ("push", "argument", 1),            # Get exponent
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # exponent == 0?
        ("if-goto", "BASE_CASE"),           # If exponent == 0, return 1
        
        # Base case: if exponent == 1, return base
        ("push", "argument", 1),            # Get exponent
        ("push", "constant", 1),            # Push 1
        ("eq",),                            # exponent == 1?
        ("if-goto", "RETURN_BASE"),         # If exponent == 1, return base
        
        # Recursive case: base * power(base, exponent - 1)
        ("push", "argument", 0),            # Push base
        ("pop", "local", 0),                # Store base in local 0
        
        ("push", "argument", 0),            # Push base (for multiplication)
        ("push", "argument", 0),            # Push base (for recursive call)
        ("push", "argument", 1),            # Push exponent
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # exponent - 1
        ("call", "power", 2),               # power(base, exponent - 1)
        ("mul",),                           # base * power(base, exponent - 1)
        ("return",),
        
        ("label", "BASE_CASE"),
        ("push", "constant", 1),            # Return 1
        ("return",),
        
        ("label", "RETURN_BASE"),
        ("push", "argument", 0),            # Return base
        ("return",),
        
        # Test power(3, 4) = 81
        ("push", "constant", 3),            # base
        ("push", "constant", 4),            # exponent
        ("call", "power", 2)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for power(3, 4): {result}")
        print(f"Expected: [81]")
        
        if result and len(result) >= 1 and result[-1] == 81:
            print("✅ Recursive power with locals PASSED")
            return True
        else:
            print("❌ Recursive power with locals FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in recursive power test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_recursive_sum_with_control_flow():
    """Test recursive sum function with multiple control flow paths"""
    print("\n=== Testing Recursive Sum with Control Flow ===")
    
    # Sum from 1 to n, but with special cases for even/odd numbers
    commands = [
        ("function", "special_sum", 1),     # 1 local for intermediate result
        # Base case: if n <= 0, return 0
        ("push", "argument", 0),            # Get n
        ("push", "constant", 0),            # Push 0
        ("gt",),                            # n > 0?
        ("if-goto", "POSITIVE_CASE"),       # If n > 0, continue
        
        # Return 0 for n <= 0
        ("push", "constant", 0),
        ("return",),
        
        ("label", "POSITIVE_CASE"),
        # Check if n is even or odd
        ("push", "argument", 0),            # Get n
        ("push", "constant", 2),            # Push 2
        ("div",),                           # n / 2
        ("push", "constant", 2),            # Push 2
        ("mul",),                           # (n / 2) * 2
        ("pop", "local", 0),                # Store (n/2)*2 in local
        
        ("push", "argument", 0),            # Get n
        ("push", "local", 0),               # Get (n/2)*2
        ("eq",),                            # n == (n/2)*2? (i.e., n is even)
        ("if-goto", "EVEN_CASE"),           # If even, go to even case
        
        # Odd case: n + special_sum(n-1)
        ("push", "argument", 0),            # Push n
        ("push", "argument", 0),            # Push n
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # n - 1
        ("call", "special_sum", 1),         # special_sum(n-1)
        ("add",),                           # n + special_sum(n-1)
        ("return",),
        
        ("label", "EVEN_CASE"),
        # Even case: n + special_sum(n-1)
        ("push", "argument", 0),            # Push n
        ("push", "argument", 0),            # Push n
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # n - 1
        ("call", "special_sum", 1),         # special_sum(n-1)
        ("add",),                           # n + special_sum(n-1)
        ("return",),
        
        # Test special_sum(5) = 5+4+3+2+1 = 15
        ("push", "constant", 5),
        ("call", "special_sum", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for special_sum(5): {result}")
        print(f"Expected: [15] (1+2+3+4+5)")
        
        if result and len(result) >= 1 and result[-1] == 15:
            print("✅ Recursive sum with control flow PASSED")
            return True
        else:
            print("❌ Recursive sum with control flow FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in recursive sum test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_mutual_recursion_with_locals():
    """Test mutually recursive functions with local variables"""
    print("\n=== Testing Mutual Recursion with Locals ===")
    
    # Even/odd checker using mutual recursion
    commands = [
        # Function to check if a number is even
        ("function", "is_even", 1),
        ("push", "argument", 0),            # Get n
        ("pop", "local", 0),                # Store n in local
        
        # Base case: if n == 0, return 1 (true)
        ("push", "local", 0),               # Get n
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # n == 0?
        ("if-goto", "EVEN_TRUE"),           # If n == 0, return true
        
        # Recursive case: is_odd(n-1)
        ("push", "local", 0),               # Get n
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # n - 1
        ("call", "is_odd", 1),              # is_odd(n-1)
        ("return",),
        
        ("label", "EVEN_TRUE"),
        ("push", "constant", 1),            # Return true
        ("return",),
        
        # Function to check if a number is odd
        ("function", "is_odd", 1),
        ("push", "argument", 0),            # Get n
        ("pop", "local", 0),                # Store n in local
        
        # Base case: if n == 0, return 0 (false)
        ("push", "local", 0),               # Get n
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # n == 0?
        ("if-goto", "ODD_FALSE"),           # If n == 0, return false
        
        # Recursive case: is_even(n-1)
        ("push", "local", 0),               # Get n
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # n - 1
        ("call", "is_even", 1),             # is_even(n-1)
        ("return",),
        
        ("label", "ODD_FALSE"),
        ("push", "constant", 0),            # Return false
        ("return",),
        
        # Test is_even(6) = 1 (true)
        ("push", "constant", 6),
        ("call", "is_even", 1)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for is_even(6): {result}")
        print(f"Expected: [1] (true)")
        
        if result and len(result) >= 1 and result[-1] == 1:
            print("✅ Mutual recursion with locals PASSED")
            return True
        else:
            print("❌ Mutual recursion with locals FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in mutual recursion test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_recursive_tree_traversal():
    """Test recursive tree-like computation with all features"""
    print("\n=== Testing Recursive Tree Traversal ===")
    
    # Simulate tree traversal: compute sum of binary tree
    # Tree structure encoded as: node_value, left_exists, right_exists
    commands = [
        ("function", "tree_sum", 3),        # 3 locals for tree processing
        # Get node value
        ("push", "argument", 0),            # node_value
        ("pop", "local", 0),                # Store in local 0
        
        # Initialize sum with node value
        ("push", "local", 0),               # Get node_value
        ("pop", "local", 2),                # sum = node_value
        
        # Check if left child exists
        ("push", "argument", 1),            # left_exists
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # left_exists == 0?
        ("if-goto", "CHECK_RIGHT"),         # If no left child, check right
        
        # Process left child (simulate with node_value - 1)
        ("push", "local", 0),               # Get node_value
        ("push", "constant", 1),            # Push 1
        ("sub",),                           # node_value - 1 (left child value)
        ("push", "constant", 0),            # left_exists = 0 (leaf)
        ("push", "constant", 0),            # right_exists = 0 (leaf)
        ("call", "tree_sum", 3),            # Recursive call for left
        ("push", "local", 2),               # Get current sum
        ("add",),                           # sum += left_sum
        ("pop", "local", 2),                # Store back to sum
        
        ("label", "CHECK_RIGHT"),
        # Check if right child exists
        ("push", "argument", 2),            # right_exists
        ("push", "constant", 0),            # Push 0
        ("eq",),                            # right_exists == 0?
        ("if-goto", "RETURN_SUM"),          # If no right child, return sum
        
        # Process right child (simulate with node_value - 2)
        ("push", "local", 0),               # Get node_value
        ("push", "constant", 2),            # Push 2
        ("sub",),                           # node_value - 2 (right child value)
        ("push", "constant", 0),            # left_exists = 0 (leaf)
        ("push", "constant", 0),            # right_exists = 0 (leaf)
        ("call", "tree_sum", 3),            # Recursive call for right
        ("push", "local", 2),               # Get current sum
        ("add",),                           # sum += right_sum
        ("pop", "local", 2),                # Store back to sum
        
        ("label", "RETURN_SUM"),
        ("push", "local", 2),               # Return sum
        ("return",),
        
        # Test with root node: value=5, has left child, has right child
        # Tree: 5 with left child 4 and right child 3 (both leaves)
        # Expected sum: 5 + 4 + 3 = 12
        ("push", "constant", 5),            # node_value
        ("push", "constant", 1),            # left_exists
        ("push", "constant", 1),            # right_exists
        ("call", "tree_sum", 3)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result for tree_sum(5, 1, 1): {result}")
        print(f"Expected: [12] (5 + 4 + 3)")
        
        if result and len(result) >= 1 and result[-1] == 12:
            print("✅ Recursive tree traversal PASSED")
            return True
        else:
            print("❌ Recursive tree traversal FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in recursive tree traversal test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Recursive Functions with Control Flow")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run recursive tests
    total_tests += 1
    if test_recursive_gcd_with_control_flow():
        tests_passed += 1
    
    total_tests += 1
    if test_recursive_power_with_locals():
        tests_passed += 1
        
    total_tests += 1
    if test_recursive_sum_with_control_flow():
        tests_passed += 1
        
    total_tests += 1
    if test_mutual_recursion_with_locals():
        tests_passed += 1
        
    total_tests += 1
    if test_recursive_tree_traversal():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Recursive Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All recursive function tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some recursive tests failed")
        sys.exit(1)