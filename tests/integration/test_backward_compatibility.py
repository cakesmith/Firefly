#!/usr/bin/env python3
"""
Backward Compatibility Integration Tests
Tests that all existing functionality continues to work with new features
**Validates: Requirements TR-4**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Petri.VMToPetri import VMToPetriTranslator

def test_basic_arithmetic_compatibility():
    """Test that basic arithmetic operations still work correctly"""
    print("=== Testing Basic Arithmetic Compatibility ===")
    
    # Original basic arithmetic test
    commands = [
        ("push", "constant", 7),
        ("push", "constant", 8),
        ("add",),
        ("push", "constant", 3),
        ("sub",),
        ("push", "constant", 2),
        ("mul",),
        ("neg",)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [-24] ((7+8-3)*2 negated)")
        
        if result and len(result) >= 1 and result[-1] == -24:
            print("✅ Basic arithmetic compatibility PASSED")
            return True
        else:
            print("❌ Basic arithmetic compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in basic arithmetic compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_logical_operations_compatibility():
    """Test that logical operations still work correctly"""
    print("\n=== Testing Logical Operations Compatibility ===")
    
    # Original logical operations test
    commands = [
        ("push", "constant", 5),
        ("push", "constant", 5),
        ("eq",),                    # Should be -1 (true)
        ("push", "constant", 3),
        ("push", "constant", 7),
        ("lt",),                    # Should be -1 (true)
        ("and",),                   # -1 AND -1 = -1
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("gt",),                    # Should be -1 (true)
        ("or",),                    # -1 OR -1 = -1
        ("not",)                    # NOT -1 = 0
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [0] (NOT of true)")
        
        if result and len(result) >= 1 and result[-1] == 0:
            print("✅ Logical operations compatibility PASSED")
            return True
        else:
            print("❌ Logical operations compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in logical operations compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_simple_function_calls_compatibility():
    """Test that simple function calls still work correctly"""
    print("\n=== Testing Simple Function Calls Compatibility ===")
    
    # Original function call test
    commands = [
        ("function", "add_two", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("add",),
        ("return",),
        
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("call", "add_two", 2)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [15] (10 + 5)")
        
        if result and len(result) >= 1 and result[-1] == 15:
            print("✅ Simple function calls compatibility PASSED")
            return True
        else:
            print("❌ Simple function calls compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in function calls compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_nested_function_calls_compatibility():
    """Test that nested function calls still work correctly"""
    print("\n=== Testing Nested Function Calls Compatibility ===")
    
    # Original nested function call test
    commands = [
        ("function", "double", 0),
        ("push", "argument", 0),
        ("push", "constant", 2),
        ("mul",),
        ("return",),
        
        ("function", "add_and_double", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("add",),
        ("call", "double", 1),
        ("return",),
        
        ("push", "constant", 3),
        ("push", "constant", 4),
        ("call", "add_and_double", 2)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [14] ((3 + 4) * 2)")
        
        if result and len(result) >= 1 and result[-1] == 14:
            print("✅ Nested function calls compatibility PASSED")
            return True
        else:
            print("❌ Nested function calls compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in nested function calls compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_complex_program_compatibility():
    """Test that complex programs with multiple features still work"""
    print("\n=== Testing Complex Program Compatibility ===")
    
    # Complex program combining multiple features
    commands = [
        ("function", "calculate", 0),
        ("push", "argument", 0),    # x
        ("push", "argument", 1),    # y
        ("add",),                   # x + y
        ("push", "argument", 2),    # z
        ("mul",),                   # (x + y) * z
        ("push", "constant", 10),   # 10
        ("sub",),                   # (x + y) * z - 10
        ("return",),
        
        ("function", "process", 0),
        ("push", "argument", 0),    # a
        ("push", "argument", 1),    # b
        ("push", "argument", 2),    # c
        ("call", "calculate", 3),   # calculate(a, b, c)
        ("push", "constant", 2),    # 2
        ("div",),                   # result / 2
        ("return",),
        
        ("push", "constant", 5),    # a = 5
        ("push", "constant", 3),    # b = 3
        ("push", "constant", 4),    # c = 4
        ("call", "process", 3)      # process(5, 3, 4)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Result: {result}")
        print(f"Expected: [11] (((5+3)*4-10)/2 = (32-10)/2 = 22/2 = 11)")
        
        if result and len(result) >= 1 and result[-1] == 11:
            print("✅ Complex program compatibility PASSED")
            return True
        else:
            print("❌ Complex program compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in complex program compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_memory_optimization_compatibility():
    """Test that memory optimization still works with existing programs"""
    print("\n=== Testing Memory Optimization Compatibility ===")
    
    # Program that should benefit from memory optimization
    commands = [
        ("push", "constant", 1),
        ("push", "constant", 2),
        ("add",),
        ("push", "constant", 3),
        ("mul",),
        ("push", "constant", 4),
        ("sub",),
        ("push", "constant", 5),
        ("add",)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        
        # Test memory optimization
        memory_stats = translator._optimize_memory_allocation()
        
        print(f"Result: {result}")
        print(f"Memory optimization stats: {memory_stats}")
        
        # Check that result is correct and optimization ran
        # (1+2)*3-4+5 = 3*3-4+5 = 9-4+5 = 10
        expected = 10
        if result and len(result) >= 1 and result[-1] == expected:
            print("✅ Memory optimization compatibility PASSED")
            return True
        else:
            print("❌ Memory optimization compatibility FAILED")
            return False
            
    except Exception as e:
        print(f"❌ Error in memory optimization compatibility test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Backward Compatibility")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run compatibility tests
    total_tests += 1
    if test_basic_arithmetic_compatibility():
        tests_passed += 1
    
    total_tests += 1
    if test_logical_operations_compatibility():
        tests_passed += 1
        
    total_tests += 1
    if test_simple_function_calls_compatibility():
        tests_passed += 1
        
    total_tests += 1
    if test_nested_function_calls_compatibility():
        tests_passed += 1
        
    total_tests += 1
    if test_complex_program_compatibility():
        tests_passed += 1
        
    total_tests += 1
    if test_memory_optimization_compatibility():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Backward Compatibility Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All backward compatibility tests passed!")
        sys.exit(0)
    else:
        print("⚠️  Some backward compatibility tests failed")
        sys.exit(1)