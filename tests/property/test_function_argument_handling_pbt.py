#!/usr/bin/env python3
"""
Property-Based Tests for Function Argument Handling
**Feature: petri-vm-improvements, Property 3: Function argument preservation**
**Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5**
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from hypothesis import given, strategies as st, settings
from Petri.VMToPetri import VMToPetriTranslator

class FunctionArgumentHandlingPBT:
    """Property-based tests for function argument handling"""
    
    @given(
        arg_values=st.lists(st.integers(min_value=-100, max_value=100), min_size=1, max_size=4)
    )
    @settings(max_examples=100)
    def test_argument_mapping_preservation(self, arg_values):
        """
        Property 3: Function argument preservation
        For any function arguments, they should be correctly mapped and accessible within function scope
        **Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5**
        """
        translator = VMToPetriTranslator()
        
        num_args = len(arg_values)
        
        commands = [
            # Define function that sums all its arguments
            ("function", "sum_args", 1),  # 1 local for accumulator
            ("push", "constant", 0),      # Initialize accumulator
            ("pop", "local", 0),
        ]
        
        # Add each argument to the accumulator
        for i in range(num_args):
            commands.extend([
                ("push", "argument", i),   # Push argument i
                ("push", "local", 0),      # Push current accumulator
                ("add",),                  # Add them
                ("pop", "local", 0),       # Store back to accumulator
            ])
        
        commands.extend([
            ("push", "local", 0),          # Return the sum
            ("return",),
        ])
        
        # Main program: push arguments and call function
        for value in arg_values:
            commands.append(("push", "constant", value))
        
        commands.append(("call", "sum_args", num_args))
        
        try:
            result = translator.execute_program(commands)
            
            # Result should be the sum of all arguments
            expected_sum = sum(arg_values)
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected_sum, f"Argument mapping failed: expected {expected_sum}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Argument mapping test failed for args={arg_values}: {e}")
    
    @given(
        arg1=st.integers(min_value=-50, max_value=50),
        arg2=st.integers(min_value=-50, max_value=50),
        arg_index=st.integers(min_value=0, max_value=1)
    )
    @settings(max_examples=100)
    def test_argument_order_preservation(self, arg1, arg2, arg_index):
        """
        Property: Function arguments maintain correct order
        For any two arguments, they should be accessible in the correct order
        **Validates: Requirements 2.2, 2.3**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            # Define function that returns a specific argument
            ("function", "get_arg", 0),
            ("push", "argument", arg_index),  # Return the specified argument
            ("return",),
            
            # Main program
            ("push", "constant", arg1),       # First argument
            ("push", "constant", arg2),       # Second argument
            ("call", "get_arg", 2),
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Result should be the argument at the specified index
            expected = arg1 if arg_index == 0 else arg2
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Argument order failed: expected {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Argument order test failed for arg1={arg1}, arg2={arg2}, index={arg_index}: {e}")
    
    @given(
        original_value=st.integers(min_value=-100, max_value=100),
        new_value=st.integers(min_value=-100, max_value=100),
        arg_index=st.integers(min_value=0, max_value=2)
    )
    @settings(max_examples=100)
    def test_argument_modification_during_execution(self, original_value, new_value, arg_index):
        """
        Property: Arguments preserve values during function execution
        For any argument modification within a function, the original caller's data should be preserved
        **Validates: Requirements 2.4, 2.5**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            # Define function that modifies an argument and returns it
            ("function", "modify_arg", 1),
            ("push", "constant", new_value),
            ("pop", "argument", arg_index),    # Modify the argument
            ("push", "argument", arg_index),   # Return the modified value
            ("return",),
            
            # Define caller function that checks argument preservation
            ("function", "caller", 1),
            ("push", "constant", original_value),
            ("pop", "local", 0),               # Store original in local
            ("push", "local", 0),              # Push as argument
            ("push", "local", 0),              # Push as argument (duplicate for safety)
            ("push", "local", 0),              # Push as argument (triplicate for safety)
            ("call", "modify_arg", 3),         # Call function that modifies argument
            ("pop",),                          # Discard return value
            ("push", "local", 0),              # Return original local value
            ("return",),
            
            # Main program
            ("call", "caller", 0),
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Caller's local variable should preserve the original value
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == original_value, f"Argument preservation failed: expected {original_value}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Argument preservation test failed for original={original_value}, new={new_value}: {e}")
    
    @given(
        values=st.lists(st.integers(min_value=-20, max_value=20), min_size=2, max_size=3),
        call_depth=st.integers(min_value=1, max_value=2)
    )
    @settings(max_examples=50)
    def test_nested_function_argument_isolation(self, values, call_depth):
        """
        Property: Nested function calls maintain argument isolation
        For any nested function calls, each function should have access to its own arguments
        **Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5**
        """
        translator = VMToPetriTranslator()
        
        # Use different values for different call levels
        outer_value = values[0]
        inner_value = values[1] if len(values) > 1 else values[0] + 10
        
        commands = [
            # Define inner function
            ("function", "inner_func", 1),
            ("push", "argument", 0),           # Get inner argument
            ("pop", "local", 0),               # Store in local
            ("push", "local", 0),              # Return inner argument
            ("return",),
            
            # Define outer function
            ("function", "outer_func", 1),
            ("push", "argument", 0),           # Get outer argument
            ("pop", "local", 0),               # Store in local
            ("push", "constant", inner_value), # Push inner function argument
            ("call", "inner_func", 1),         # Call inner function
            ("push", "local", 0),              # Push outer function's argument
            ("add",),                          # Add inner result + outer argument
            ("return",),
            
            # Main program
            ("push", "constant", outer_value),
            ("call", "outer_func", 1),
        ]
        
        try:
            result = translator.execute_program(commands)
            
            # Result should be inner_value + outer_value
            expected = inner_value + outer_value
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Nested argument isolation failed: expected {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Nested argument isolation failed for outer={outer_value}, inner={inner_value}: {e}")
    
    @given(
        arg_value=st.integers(min_value=-50, max_value=50),
        num_calls=st.integers(min_value=1, max_value=3)
    )
    @settings(max_examples=50)
    def test_argument_consistency_across_calls(self, arg_value, num_calls):
        """
        Property: Arguments remain consistent across multiple function calls
        For any argument value, multiple calls to the same function should see the same argument
        **Validates: Requirements 2.1, 2.2, 2.3**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            # Define function that returns its argument
            ("function", "echo_arg", 0),
            ("push", "argument", 0),
            ("return",),
            
            # Define coordinator that calls echo_arg multiple times
            ("function", "coordinator", 1),
            ("push", "constant", 0),           # Initialize accumulator
            ("pop", "local", 0),
        ]
        
        # Call echo_arg multiple times and sum results
        for i in range(num_calls):
            commands.extend([
                ("push", "argument", 0),       # Pass the coordinator's argument
                ("call", "echo_arg", 1),       # Call echo function
                ("push", "local", 0),          # Get current sum
                ("add",),                      # Add to sum
                ("pop", "local", 0),           # Store sum
            ])
        
        commands.extend([
            ("push", "local", 0),              # Return final sum
            ("return",),
            
            # Main program
            ("push", "constant", arg_value),
            ("call", "coordinator", 1),
        ])
        
        try:
            result = translator.execute_program(commands)
            
            # Result should be arg_value * num_calls
            expected = arg_value * num_calls
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == expected, f"Argument consistency failed: expected {expected}, got {result[0]}"
            
        except Exception as e:
            raise AssertionError(f"Argument consistency test failed for value={arg_value}, calls={num_calls}: {e}")

def run_property_tests():
    """Run all property-based tests for function argument handling"""
    print("Running Property-Based Tests for Function Argument Handling")
    print("=" * 70)
    
    pbt = FunctionArgumentHandlingPBT()
    
    try:
        print("Testing Property 3: Argument mapping preservation...")
        pbt.test_argument_mapping_preservation()
        print("✅ Argument mapping preservation PASSED")
        
        print("\nTesting Property: Argument order preservation...")
        pbt.test_argument_order_preservation()
        print("✅ Argument order preservation PASSED")
        
        print("\nTesting Property: Argument modification during execution...")
        pbt.test_argument_modification_during_execution()
        print("✅ Argument modification preservation PASSED")
        
        print("\nTesting Property: Nested function argument isolation...")
        pbt.test_nested_function_argument_isolation()
        print("✅ Nested argument isolation PASSED")
        
        print("\nTesting Property: Argument consistency across calls...")
        pbt.test_argument_consistency_across_calls()
        print("✅ Argument consistency PASSED")
        
        print("\n🎉 ALL FUNCTION ARGUMENT HANDLING TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ PROPERTY TEST FAILED: {e}")
        return False

if __name__ == "__main__":
    success = run_property_tests()
    sys.exit(0 if success else 1)