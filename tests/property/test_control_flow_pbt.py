#!/usr/bin/env python3
"""
Property-Based Tests for Control Flow Operations
**Feature: petri-vm-extensions, Property 3: Control flow correctness**
**Validates: Requirements US-3.1, US-3.2, US-3.3**
"""

import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from hypothesis import given, strategies as st, settings
from Petri.VMToPetri import VMToPetriTranslator

class ControlFlowPBT:
    """Property-based tests for control flow operations"""
    
    @given(
        condition=st.integers(min_value=-100, max_value=100),
        true_value=st.integers(min_value=1, max_value=100),
        false_value=st.integers(min_value=1, max_value=100)
    )
    @settings(max_examples=100)
    def test_if_goto_conditional_execution(self, condition, true_value, false_value):
        """
        Property 3a: If-goto conditional execution correctness
        For any condition, if-goto should execute the correct branch
        **Validates: Requirements US-3.1**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 0),
            ("push", "constant", condition),
            ("if-goto", "TRUE_BRANCH"),
            # False branch
            ("push", "constant", false_value),
            ("goto", "END"),
            ("label", "TRUE_BRANCH"),
            # True branch
            ("push", "constant", true_value),
            ("label", "END"),
            ("return",),
            ("call", "test_func", 0)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            
            # Check that the correct branch was executed
            if condition != 0:  # Non-zero is true in VM semantics
                expected = true_value
                assert result[0] == expected, f"If-goto true branch failed: condition={condition}, expected={expected}, got={result[0]}"
            else:  # Zero is false
                expected = false_value
                assert result[0] == expected, f"If-goto false branch failed: condition={condition}, expected={expected}, got={result[0]}"
                
        except Exception as e:
            raise AssertionError(f"If-goto conditional execution failed for condition={condition}: {e}")
    
    @given(
        loop_count=st.integers(min_value=0, max_value=5),
        increment=st.integers(min_value=1, max_value=10)
    )
    @settings(max_examples=100)
    def test_goto_loop_correctness(self, loop_count, increment):
        """
        Property 3b: Goto loop execution correctness
        For any loop count, goto-based loops should execute the correct number of times
        **Validates: Requirements US-3.2, US-3.3**
        """
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 2),  # locals: counter, accumulator
            # Initialize counter and accumulator
            ("push", "constant", 0),
            ("pop", "local", 0),  # counter = 0
            ("push", "constant", 0),
            ("pop", "local", 1),  # accumulator = 0
            
            ("label", "LOOP_START"),
            # Check if counter < loop_count
            ("push", "local", 0),
            ("push", "constant", loop_count),
            ("lt",),
            ("if-goto", "LOOP_BODY"),
            ("goto", "LOOP_END"),
            
            ("label", "LOOP_BODY"),
            # accumulator += increment
            ("push", "local", 1),
            ("push", "constant", increment),
            ("add",),
            ("pop", "local", 1),
            # counter++
            ("push", "local", 0),
            ("push", "constant", 1),
            ("add",),
            ("pop", "local", 0),
            ("goto", "LOOP_START"),
            
            ("label", "LOOP_END"),
            # Return accumulator
            ("push", "local", 1),
            ("return",),
            ("call", "test_func", 0)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            
            expected = loop_count * increment
            assert result[0] == expected, f"Loop execution failed: loop_count={loop_count}, increment={increment}, expected={expected}, got={result[0]}"
                
        except Exception as e:
            raise AssertionError(f"Goto loop test failed for loop_count={loop_count}, increment={increment}: {e}")
    
    @given(
        values=st.lists(st.integers(min_value=1, max_value=50), min_size=1, max_size=5)
    )
    @settings(max_examples=100)
    def test_nested_control_structures(self, values):
        """
        Property 3c: Nested control structures correctness
        For any list of values, nested if-goto and goto should work correctly
        **Validates: Requirements US-3.1, US-3.2, US-3.3**
        """
        translator = VMToPetriTranslator()
        
        # Create a program that sums only positive values using nested control flow
        commands = [
            ("function", "test_func", 2),  # locals: sum, index
            ("push", "constant", 0),
            ("pop", "local", 0),  # sum = 0
            ("push", "constant", 0),
            ("pop", "local", 1),  # index = 0
        ]
        
        # Process each value with nested control flow
        for i, value in enumerate(values):
            commands.extend([
                # Check if we should process this value (index == i)
                ("push", "local", 1),
                ("push", "constant", i),
                ("eq",),
                ("if-goto", f"PROCESS_{i}"),
                ("goto", f"SKIP_{i}"),
                
                ("label", f"PROCESS_{i}"),
                # Check if value is positive
                ("push", "constant", value),
                ("push", "constant", 0),
                ("gt",),
                ("if-goto", f"ADD_{i}"),
                ("goto", f"NEXT_{i}"),
                
                ("label", f"ADD_{i}"),
                # Add positive value to sum
                ("push", "local", 0),
                ("push", "constant", value),
                ("add",),
                ("pop", "local", 0),
                
                ("label", f"NEXT_{i}"),
                # Increment index
                ("push", "local", 1),
                ("push", "constant", 1),
                ("add",),
                ("pop", "local", 1),
                
                ("label", f"SKIP_{i}")
            ])
        
        commands.extend([
            # Return sum
            ("push", "local", 0),
            ("return",),
            ("call", "test_func", 0)
        ])
        
        try:
            result = translator.execute_program(commands)
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            
            # Expected sum of positive values only
            expected = sum(v for v in values if v > 0)
            assert result[0] == expected, f"Nested control flow failed: values={values}, expected={expected}, got={result[0]}"
                
        except Exception as e:
            raise AssertionError(f"Nested control structures test failed for values={values}: {e}")
    
    @given(
        label_suffix=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=1, max_size=5),
        jump_value=st.integers(min_value=1, max_value=100)
    )
    @settings(max_examples=100)
    def test_label_definition_and_goto(self, label_suffix, jump_value):
        """
        Property 3d: Label definition and goto correctness
        For any label name, goto should correctly jump to the defined label
        **Validates: Requirements US-3.2, US-3.3**
        """
        translator = VMToPetriTranslator()
        
        label_name = f"LABEL_{label_suffix}"
        
        commands = [
            ("function", "test_func", 0),
            ("goto", label_name),
            # This should be skipped
            ("push", "constant", 999),
            ("return",),
            # Jump target
            ("label", label_name),
            ("push", "constant", jump_value),
            ("return",),
            ("call", "test_func", 0)
        ]
        
        try:
            result = translator.execute_program(commands)
            
            assert len(result) == 1, f"Expected 1 result, got {len(result)}"
            assert result[0] == jump_value, f"Goto failed: expected {jump_value}, got {result[0]} (should not be 999)"
                
        except Exception as e:
            raise AssertionError(f"Label and goto test failed for label={label_name}, value={jump_value}: {e}")

def run_property_tests():
    """Run all property-based tests"""
    print("Running Property-Based Tests for Control Flow Operations")
    print("=" * 60)
    
    pbt = ControlFlowPBT()
    
    try:
        print("Testing Property 3a: If-goto conditional execution...")
        pbt.test_if_goto_conditional_execution()
        print("✅ Property 3a PASSED")
        
        print("\nTesting Property 3b: Goto loop correctness...")
        pbt.test_goto_loop_correctness()
        print("✅ Property 3b PASSED")
        
        print("\nTesting Property 3c: Nested control structures...")
        pbt.test_nested_control_structures()
        print("✅ Property 3c PASSED")
        
        print("\nTesting Property 3d: Label definition and goto...")
        pbt.test_label_definition_and_goto()
        print("✅ Property 3d PASSED")
        
        print("\n🎉 ALL CONTROL FLOW PROPERTY TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ CONTROL FLOW PROPERTY TEST FAILED: {e}")
        return False

if __name__ == "__main__":
    success = run_property_tests()
    sys.exit(0 if success else 1)