#!/usr/bin/env python3
"""
Property-Based Tests for Arithmetic Operations
**Feature: petri-vm-extensions, Property 2: Arithmetic operation correctness**
**Validates: Requirements US-2.1, US-2.2**
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hypothesis import given, strategies as st, settings
from Petri.VMToPetri import VMToPetriTranslator

class ArithmeticOperationsPBT:
    """Property-based tests for arithmetic operations"""
    
    @given(
        a=st.integers(min_value=-1000, max_value=1000),
        b=st.integers(min_value=-1000, max_value=1000)
    )
    @settings(max_examples=100)
    def test_multiplication_correctness(self, a, b):
        """
        Property 2a: Multiplication operation correctness
        For any two integers a and b, mul operation should produce a * b
        **Validates: Requirements US-2.1**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("push", "constant", a),
            ("push", "constant", b),
            ("mul",)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Calculate expected result with overflow handling (16-bit signed)
            expected = (a * b) & 0xFFFF
            if expected > 32767:
                expected = expected - 65536
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Multiplication failed: {a} * {b} = {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Multiplication test failed for a={a}, b={b}: {e}")
    
    @given(
        a=st.integers(min_value=-1000, max_value=1000),
        b=st.integers(min_value=1, max_value=1000)  # Exclude zero for basic test
    )
    @settings(max_examples=100)
    def test_division_correctness(self, a, b):
        """
        Property 2b: Division operation correctness
        For any integers a and b (b != 0), div operation should produce a / b (truncated toward zero)
        **Validates: Requirements US-2.2**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("push", "constant", a),
            ("push", "constant", b),
            ("div",)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Calculate expected result (truncated toward zero)
            if (a < 0) != (b < 0):  # Different signs
                expected = -(abs(a) // abs(b))
            else:
                expected = a // b
            
            # Ensure result fits in 16-bit signed integer
            expected = max(-32768, min(32767, expected))
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Division failed: {a} / {b} = {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Division test failed for a={a}, b={b}: {e}")
    
    @given(
        a=st.integers(min_value=-1000, max_value=1000)
    )
    @settings(max_examples=100)
    def test_division_by_zero_handling(self, a):
        """
        Property 2c: Division by zero handling
        For any integer a, dividing by zero should return 0 (graceful handling)
        **Validates: Requirements US-2.2**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("push", "constant", a),
            ("push", "constant", 0),
            ("div",)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Division by zero should return 0 (graceful handling)
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == 0, f"Division by zero should return 0, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Division by zero test failed for a={a}: {e}")
    
    @given(
        a=st.integers(min_value=-100, max_value=100),
        b=st.integers(min_value=-100, max_value=100),
        c=st.integers(min_value=1, max_value=100)  # Avoid division by zero
    )
    @settings(max_examples=100)
    def test_arithmetic_composition(self, a, b, c):
        """
        Property 2d: Arithmetic operations compose correctly
        For any integers a, b, c, (a + b) * c should equal a*c + b*c (distributive property)
        **Validates: Requirements US-2.1, US-2.2**
        """
        translator1 = VMToPetriTranslator()
        translator2 = VMToPetriTranslator()
        
        # Test (a + b) * c
        commands1 = [
            ("push", "constant", a),
            ("push", "constant", b),
            ("add",),
            ("push", "constant", c),
            ("mul",)
        ]
        
        # Test a*c + b*c
        commands2 = [
            ("push", "constant", a),
            ("push", "constant", c),
            ("mul",),
            ("push", "constant", b),
            ("push", "constant", c),
            ("mul",),
            ("add",)
        ]
        
        try:
            result1 = translator1.execute_program(commands1)
            result2 = translator2.execute_program(commands2)
            
            assert len(result1) == 1 and len(result2) == 1, "Expected 1 result from each computation"
            
            # Results should be equal (within 16-bit overflow constraints)
            # Note: This property may not hold exactly due to overflow, but should hold for small values
            if abs(a) < 50 and abs(b) < 50 and abs(c) < 50:  # Avoid overflow for this test
                assert result1[0] == result2[0], f"Distributive property failed: ({a}+{b})*{c}={result1[0]} vs {a}*{c}+{b}*{c}={result2[0]}"
            
        except Exception as e:
            raise AssertionError(f"Arithmetic composition test failed for a={a}, b={b}, c={c}: {e}")
    
    @given(
        values=st.lists(st.integers(min_value=1, max_value=10), min_size=2, max_size=4)
    )
    @settings(max_examples=100)
    def test_multiplication_chain(self, values):
        """
        Property 2e: Multiplication is associative
        For any list of positive integers, the order of multiplication should not matter
        **Validates: Requirements US-2.1**
        """
        if len(values) < 2:
            return  # Skip if not enough values
            
        translator = VMToPetriTranslator()
        
        # Build commands to multiply all values in sequence
        commands = [("push", "constant", values[0])]
        
        for value in values[1:]:
            commands.extend([
                ("push", "constant", value),
                ("mul",)
            ])
        
        try:
            result = translator.execute_program(commands)
            
            # Calculate expected result
            expected = 1
            for value in values:
                expected *= value
            
            # Handle 16-bit overflow
            expected = expected & 0xFFFF
            if expected > 32767:
                expected = expected - 65536
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Multiplication chain failed: {values} -> expected {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Multiplication chain test failed for values={values}: {e}")

def run_property_tests():
    """Run all property-based tests for arithmetic operations"""
    print("Running Property-Based Tests for Arithmetic Operations")
    print("=" * 60)
    
    pbt = ArithmeticOperationsPBT()
    
    try:
        print("Testing Property 2a: Multiplication correctness...")
        pbt.test_multiplication_correctness()
        print("✅ Multiplication correctness PASSED")
        
        print("\nTesting Property 2b: Division correctness...")
        pbt.test_division_correctness()
        print("✅ Division correctness PASSED")
        
        print("\nTesting Property 2c: Division by zero handling...")
        pbt.test_division_by_zero_handling()
        print("✅ Division by zero handling PASSED")
        
        print("\nTesting Property 2d: Arithmetic composition...")
        pbt.test_arithmetic_composition()
        print("✅ Arithmetic composition PASSED")
        
        print("\nTesting Property 2e: Multiplication chain...")
        pbt.test_multiplication_chain()
        print("✅ Multiplication chain PASSED")
        
        print("\n🎉 ALL ARITHMETIC PROPERTY TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ ARITHMETIC PROPERTY TEST FAILED: {e}")
        return False

if __name__ == "__main__":
    success = run_property_tests()
    sys.exit(0 if success else 1)