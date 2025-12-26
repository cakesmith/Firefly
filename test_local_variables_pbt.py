#!/usr/bin/env python3
"""
Property-Based Tests for Local Variable Operations
**Feature: petri-vm-extensions, Property 1: Local variable round trip**
**Validates: Requirements US-1.1, US-1.2**
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hypothesis import given, strategies as st, settings
from Petri.VMToPetri import VMToPetriTranslator

class LocalVariablePBT:
    """Property-based tests for local variable operations"""
    
    @given(
        value=st.integers(min_value=-32768, max_value=32767),
        local_index=st.integers(min_value=0, max_value=7),
        num_locals=st.integers(min_value=1, max_value=8)
    )
    @settings(max_examples=100)
    def test_local_variable_round_trip(self, value, local_index, num_locals):
        """
        Property 1: Local variable round trip
        For any value and valid local index, storing then loading should preserve the value
        **Validates: Requirements US-1.1, US-1.2**
        """
        # Ensure local_index is within bounds
        if local_index >= num_locals:
            local_index = local_index % num_locals
        
        translator = VMToPetriTranslator()
        
        # Create a function context with local variables
        commands = [
            ("function", "test_func", num_locals),
            ("push", "constant", value),
            ("pop", "local", local_index),
            ("push", "local", local_index),
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # The result should contain the original value
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == value, f"Round trip failed: {value} -> {result[0]}"
            
        except Exception as e:
            # Property should hold for all valid inputs
            raise AssertionError(f"Local variable round trip failed for value={value}, index={local_index}: {e}")
    
    @given(
        values=st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1, max_size=5),
        num_locals=st.integers(min_value=1, max_value=8)
    )
    @settings(max_examples=100)
    def test_multiple_local_variables(self, values, num_locals):
        """
        Property: Multiple local variables maintain independence
        For any list of values, storing to different locals should preserve all values
        **Validates: Requirements US-1.1, US-1.2**
        """
        translator = VMToPetriTranslator()
        
        # Limit to available locals
        values = values[:num_locals]
        
        # Build commands to store values to different locals
        commands = [("function", "test_func", num_locals)]
        
        # Store values to locals
        for i, value in enumerate(values):
            commands.extend([
                ("push", "constant", value),
                ("pop", "local", i)
            ])
        
        # Retrieve values from locals and sum them (since functions return one value)
        if len(values) > 0:
            commands.append(("push", "local", 0))
            for i in range(1, len(values)):
                commands.extend([
                    ("push", "local", i),
                    ("add",)
                ])
        
        commands.extend([
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ])
        
        try:
            result = translator.execute_program(commands)
            
            # Results should be the sum of all values
            expected_sum = sum(values)
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected_sum, f"Sum failed: expected {expected_sum}, got {result[0]}"
                
        except Exception as e:
            raise AssertionError(f"Multiple locals test failed for values={values}: {e}")
    
    @given(
        initial_value=st.integers(min_value=-100, max_value=100),
        new_value=st.integers(min_value=-100, max_value=100),
        local_index=st.integers(min_value=0, max_value=3)
    )
    @settings(max_examples=100)
    def test_local_variable_overwrite(self, initial_value, new_value, local_index):
        """
        Property: Local variable overwrite preserves latest value
        For any two values, the second store should overwrite the first
        **Validates: Requirements US-1.1, US-1.2**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 4),
            # Store initial value
            ("push", "constant", initial_value),
            ("pop", "local", local_index),
            # Store new value (overwrite)
            ("push", "constant", new_value),
            ("pop", "local", local_index),
            # Retrieve final value
            ("push", "local", local_index),
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == new_value, f"Overwrite failed: expected {new_value}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Local overwrite test failed: initial={initial_value}, new={new_value}, index={local_index}: {e}")

def run_property_tests():
    """Run all property-based tests"""
    print("Running Property-Based Tests for Local Variable Operations")
    print("=" * 60)
    
    pbt = LocalVariablePBT()
    
    try:
        print("Testing Property 1: Local variable round trip...")
        pbt.test_local_variable_round_trip()
        print("✅ Property 1 PASSED")
        
        print("\nTesting Property: Multiple local variables independence...")
        pbt.test_multiple_local_variables()
        print("✅ Multiple locals property PASSED")
        
        print("\nTesting Property: Local variable overwrite...")
        pbt.test_local_variable_overwrite()
        print("✅ Overwrite property PASSED")
        
        print("\n🎉 ALL PROPERTY TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ PROPERTY TEST FAILED: {e}")
        return False

if __name__ == "__main__":
    success = run_property_tests()
    sys.exit(0 if success else 1)