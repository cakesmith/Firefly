#!/usr/bin/env python3
"""
Unit Tests for Arithmetic Edge Cases
Tests specific examples and edge cases for arithmetic operations
**Validates: Requirements US-2.1, US-2.2**
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Petri.VMToPetri import VMToPetriTranslator

class ArithmeticEdgeCasesUnitTests:
    """Unit tests for arithmetic edge cases"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def run_test(self, test_name, test_func):
        """Run a test and track results"""
        print(f"\n=== {test_name} ===")
        try:
            success = test_func()
            if success:
                print(f"✅ {test_name} PASSED")
                self.passed += 1
            else:
                print(f"❌ {test_name} FAILED")
                self.failed += 1
            return success
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
            self.failed += 1
            return False
    
    def test_multiplication_overflow(self):
        """Test multiplication overflow handling"""
        translator = VMToPetriTranslator()
        
        # Test multiplication that causes 16-bit overflow
        commands = [
            ("push", "constant", 1000),
            ("push", "constant", 100),
            ("mul",)
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Multiplication overflow result: {result}")
            
            # 1000 * 100 = 100000, which overflows 16-bit signed (-32768 to 32767)
            # 100000 & 0xFFFF = 34464, but since > 32767, subtract 65536 = -31072
            expected_result = (100000 & 0xFFFF)
            if expected_result > 32767:
                expected_result = expected_result - 65536
            
            expected = [expected_result]
            return result == expected
            
        except Exception as e:
            print(f"Multiplication overflow test failed: {e}")
            return False
    
    def test_multiplication_with_zero(self):
        """Test multiplication with zero"""
        translator = VMToPetriTranslator()
        
        commands = [
            ("push", "constant", 42),
            ("push", "constant", 0),
            ("mul",)
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Multiplication with zero result: {result}")
            
            expected = [0]
            return result == expected
            
        except Exception as e:
            print(f"Multiplication with zero test failed: {e}")
            return False
    
    def test_multiplication_with_negative_numbers(self):
        """Test multiplication with negative numbers"""
        translator = VMToPetriTranslator()
        
        # Test negative * positive
        commands1 = [
            ("push", "constant", -5),
            ("push", "constant", 7),
            ("mul",)
        ]
        
        # Test negative * negative
        commands2 = [
            ("push", "constant", -3),
            ("push", "constant", -4),
            ("mul",)
        ]
        
        try:
            result1 = translator.execute_program(commands1)
            print(f"Negative * positive result: {result1}")
            
            translator2 = VMToPetriTranslator()
            result2 = translator2.execute_program(commands2)
            print(f"Negative * negative result: {result2}")
            
            expected1 = [-35]
            expected2 = [12]
            
            return result1 == expected1 and result2 == expected2
            
        except Exception as e:
            print(f"Multiplication with negative numbers test failed: {e}")
            return False
    
    def test_division_by_zero_handling(self):
        """Test division by zero handling"""
        translator = VMToPetriTranslator()
        
        commands = [
            ("push", "constant", 42),
            ("push", "constant", 0),
            ("div",)
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Division by zero result: {result}")
            
            # Should return 0 for graceful handling
            expected = [0]
            return result == expected
            
        except Exception as e:
            print(f"Division by zero test failed: {e}")
            return False
    
    def test_division_truncation_toward_zero(self):
        """Test division truncation toward zero"""
        translator1 = VMToPetriTranslator()
        translator2 = VMToPetriTranslator()
        translator3 = VMToPetriTranslator()
        translator4 = VMToPetriTranslator()
        
        # Test positive / positive
        commands1 = [
            ("push", "constant", 7),
            ("push", "constant", 3),
            ("div",)
        ]
        
        # Test negative / positive (should truncate toward zero)
        commands2 = [
            ("push", "constant", -7),
            ("push", "constant", 3),
            ("div",)
        ]
        
        # Test positive / negative (should truncate toward zero)
        commands3 = [
            ("push", "constant", 7),
            ("push", "constant", -3),
            ("div",)
        ]
        
        # Test negative / negative
        commands4 = [
            ("push", "constant", -7),
            ("push", "constant", -3),
            ("div",)
        ]
        
        try:
            result1 = translator1.execute_program(commands1)
            result2 = translator2.execute_program(commands2)
            result3 = translator3.execute_program(commands3)
            result4 = translator4.execute_program(commands4)
            
            print(f"7 / 3 = {result1}")
            print(f"-7 / 3 = {result2}")
            print(f"7 / -3 = {result3}")
            print(f"-7 / -3 = {result4}")
            
            # Expected results (truncated toward zero)
            expected1 = [2]    # 7 / 3 = 2.33... -> 2
            expected2 = [-2]   # -7 / 3 = -2.33... -> -2 (toward zero)
            expected3 = [-2]   # 7 / -3 = -2.33... -> -2 (toward zero)
            expected4 = [2]    # -7 / -3 = 2.33... -> 2
            
            return (result1 == expected1 and result2 == expected2 and 
                   result3 == expected3 and result4 == expected4)
            
        except Exception as e:
            print(f"Division truncation test failed: {e}")
            return False
    
    def test_division_with_negative_numbers(self):
        """Test division with various negative number combinations"""
        translator1 = VMToPetriTranslator()
        translator2 = VMToPetriTranslator()
        
        # Test cases that should result in exact division
        commands1 = [
            ("push", "constant", -12),
            ("push", "constant", 4),
            ("div",)
        ]
        
        commands2 = [
            ("push", "constant", 15),
            ("push", "constant", -5),
            ("div",)
        ]
        
        try:
            result1 = translator1.execute_program(commands1)
            result2 = translator2.execute_program(commands2)
            
            print(f"-12 / 4 = {result1}")
            print(f"15 / -5 = {result2}")
            
            expected1 = [-3]
            expected2 = [-3]
            
            return result1 == expected1 and result2 == expected2
            
        except Exception as e:
            print(f"Division with negative numbers test failed: {e}")
            return False
    
    def test_arithmetic_with_boundary_values(self):
        """Test arithmetic operations with 16-bit boundary values"""
        translator1 = VMToPetriTranslator()
        translator2 = VMToPetriTranslator()
        
        # Test with maximum positive 16-bit value
        commands1 = [
            ("push", "constant", 32767),
            ("push", "constant", 1),
            ("mul",)
        ]
        
        # Test with minimum negative 16-bit value
        commands2 = [
            ("push", "constant", -32768),
            ("push", "constant", 1),
            ("div",)
        ]
        
        try:
            result1 = translator1.execute_program(commands1)
            result2 = translator2.execute_program(commands2)
            
            print(f"32767 * 1 = {result1}")
            print(f"-32768 / 1 = {result2}")
            
            expected1 = [32767]
            expected2 = [-32768]
            
            return result1 == expected1 and result2 == expected2
            
        except Exception as e:
            print(f"Boundary values test failed: {e}")
            return False
    
    def test_chained_arithmetic_operations(self):
        """Test chaining multiple arithmetic operations"""
        translator = VMToPetriTranslator()
        
        # Test: (5 * 3) / 2 = 15 / 2 = 7 (truncated)
        commands = [
            ("push", "constant", 5),
            ("push", "constant", 3),
            ("mul",),
            ("push", "constant", 2),
            ("div",)
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"(5 * 3) / 2 = {result}")
            
            expected = [7]  # 15 / 2 = 7.5 -> 7 (truncated)
            return result == expected
            
        except Exception as e:
            print(f"Chained arithmetic operations test failed: {e}")
            return False
    
    def test_arithmetic_with_small_numbers(self):
        """Test arithmetic operations with small numbers"""
        translator1 = VMToPetriTranslator()
        translator2 = VMToPetriTranslator()
        
        # Test multiplication with small numbers
        commands1 = [
            ("push", "constant", 1),
            ("push", "constant", 1),
            ("mul",)
        ]
        
        # Test division with small numbers
        commands2 = [
            ("push", "constant", 1),
            ("push", "constant", 2),
            ("div",)
        ]
        
        try:
            result1 = translator1.execute_program(commands1)
            result2 = translator2.execute_program(commands2)
            
            print(f"1 * 1 = {result1}")
            print(f"1 / 2 = {result2}")
            
            expected1 = [1]
            expected2 = [0]  # 1 / 2 = 0.5 -> 0 (truncated)
            
            return result1 == expected1 and result2 == expected2
            
        except Exception as e:
            print(f"Small numbers test failed: {e}")
            return False

def run_unit_tests():
    """Run all unit tests for arithmetic edge cases"""
    print("Running Unit Tests for Arithmetic Edge Cases")
    print("=" * 60)
    
    tests = ArithmeticEdgeCasesUnitTests()
    
    # Run all tests
    tests.run_test("Multiplication Overflow", tests.test_multiplication_overflow)
    tests.run_test("Multiplication with Zero", tests.test_multiplication_with_zero)
    tests.run_test("Multiplication with Negative Numbers", tests.test_multiplication_with_negative_numbers)
    tests.run_test("Division by Zero Handling", tests.test_division_by_zero_handling)
    tests.run_test("Division Truncation Toward Zero", tests.test_division_truncation_toward_zero)
    tests.run_test("Division with Negative Numbers", tests.test_division_with_negative_numbers)
    tests.run_test("Arithmetic with Boundary Values", tests.test_arithmetic_with_boundary_values)
    tests.run_test("Chained Arithmetic Operations", tests.test_chained_arithmetic_operations)
    tests.run_test("Arithmetic with Small Numbers", tests.test_arithmetic_with_small_numbers)
    
    # Summary
    total_tests = tests.passed + tests.failed
    print(f"\n" + "=" * 60)
    print(f"ARITHMETIC EDGE CASES UNIT TEST SUMMARY")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {tests.passed}")
    print(f"Failed: {tests.failed}")
    
    if tests.failed == 0:
        print("🎉 ALL ARITHMETIC EDGE CASE TESTS PASSED!")
        return True
    else:
        print(f"❌ {tests.failed} tests failed - check implementation")
        return False

if __name__ == "__main__":
    success = run_unit_tests()
    sys.exit(0 if success else 1)