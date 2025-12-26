"""
Unit tests for control flow operations (label, goto, if-goto)
Tests label definition, goto operations, and error handling for undefined labels
Requirements: US-3.2, US-3.3
"""

import unittest
import sys
import os

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from Petri.VMToPetri import VMToPetriTranslator
from Petri.Token import Token


class TestControlFlowUnit(unittest.TestCase):
    """Unit tests for control flow operations"""
    
    def setUp(self):
        """Set up a fresh translator for each test"""
        self.translator = VMToPetriTranslator()
        # Set up a function context for testing
        self.translator.current_function = "test_function"
        self.translator.function_locals["test_function"] = 0
        # Set up function definition for control flow operations
        self.translator.function_definitions["test_function"] = {
            'num_locals': 0,
            'body': []  # Empty body for unit tests
        }
        
    def test_label_definition(self):
        """Test basic label definition"""
        # Test label creation
        label_place = self.translator.label_operation("LOOP_START")
        
        # Verify label was created
        self.assertIsNotNone(label_place)
        self.assertTrue(label_place.has_token())
        self.assertEqual(label_place.tokens[0].value, "control")
        
        # Verify label is registered in control flow manager
        self.assertTrue(self.translator.control_flow.is_label_defined("LOOP_START", "test_function"))
        
    def test_label_function_scoping(self):
        """Test that labels are properly scoped to functions"""
        # Create label in current function
        self.translator.label_operation("LABEL1")
        
        # Switch to different function
        self.translator.current_function = "other_function"
        self.translator.function_locals["other_function"] = 0
        
        # Create same label name in different function
        self.translator.label_operation("LABEL1")
        
        # Both labels should exist in their respective scopes
        self.assertTrue(self.translator.control_flow.is_label_defined("LABEL1", "test_function"))
        self.assertTrue(self.translator.control_flow.is_label_defined("LABEL1", "other_function"))
        
        # Labels should be different places
        place1 = self.translator.control_flow.get_label_place("LABEL1", "test_function")
        place2 = self.translator.control_flow.get_label_place("LABEL1", "other_function")
        self.assertNotEqual(place1, place2)
        
    def test_goto_operation(self):
        """Test basic goto operation"""
        # First define a label
        self.translator.label_operation("TARGET")
        
        # Create goto to that label
        goto_transition = self.translator.goto_operation("TARGET")
        
        # Verify goto transition was created
        self.assertIsNotNone(goto_transition)
        self.assertIn("goto_TARGET", goto_transition.name)
        
        # Verify transition has correct connections
        self.assertEqual(len(goto_transition.in_places), 1)
        self.assertEqual(len(goto_transition.out_places), 1)
        
        # Verify it connects to the target label place
        target_place = self.translator.control_flow.get_label_place("TARGET", "test_function")
        self.assertIn(target_place, goto_transition.out_places)
        
    def test_goto_undefined_label(self):
        """Test error handling for goto to undefined label"""
        # Try to goto undefined label
        with self.assertRaises(RuntimeError) as context:
            self.translator.goto_operation("UNDEFINED_LABEL")
            
        self.assertIn("undefined label", str(context.exception).lower())
        
    def test_if_goto_operation(self):
        """Test basic if-goto operation"""
        # Set up condition on stack
        condition_place = self.translator.push_constant(1)  # Non-zero (true)
        
        # Define target label
        self.translator.label_operation("IF_TARGET")
        
        # Create if-goto
        if_goto_transition = self.translator.if_goto_operation("IF_TARGET")
        
        # Verify if-goto transition was created
        self.assertIsNotNone(if_goto_transition)
        self.assertIn("if_goto_IF_TARGET", if_goto_transition.name)
        
        # Verify transition has correct connections (condition input, two outputs)
        self.assertEqual(len(if_goto_transition.in_places), 1)
        self.assertEqual(len(if_goto_transition.out_places), 2)
        
        # Verify one output connects to target label
        target_place = self.translator.control_flow.get_label_place("IF_TARGET", "test_function")
        self.assertIn(target_place, if_goto_transition.out_places)
        
    def test_if_goto_no_condition(self):
        """Test error handling for if-goto with no condition on stack"""
        # Define target label
        self.translator.label_operation("IF_TARGET")
        
        # Try if-goto with empty stack
        with self.assertRaises(RuntimeError) as context:
            self.translator.if_goto_operation("IF_TARGET")
            
        self.assertIn("no condition", str(context.exception).lower())
        
    def test_if_goto_undefined_label(self):
        """Test error handling for if-goto to undefined label"""
        # Set up condition on stack
        self.translator.push_constant(1)
        
        # Try if-goto to undefined label
        with self.assertRaises(RuntimeError) as context:
            self.translator.if_goto_operation("UNDEFINED_LABEL")
            
        self.assertIn("undefined label", str(context.exception).lower())
        
    def test_control_flow_within_function_boundaries(self):
        """Test that control flow works correctly within function boundaries"""
        # Create a simple control flow pattern within a function
        self.translator.push_constant(5)  # Initial value
        
        # Define labels
        self.translator.label_operation("LOOP_START")
        self.translator.label_operation("LOOP_END")
        
        # Simulate a simple loop structure
        # push constant 1
        # sub (decrement counter)
        # dup (duplicate for condition check)
        # if-goto LOOP_END (exit if zero)
        # goto LOOP_START (continue loop)
        
        self.translator.push_constant(1)
        self.translator.sub_operation()
        self.translator.dup_operation()
        
        # Test if-goto (should work)
        if_goto_trans = self.translator.if_goto_operation("LOOP_END")
        self.assertIsNotNone(if_goto_trans)
        
        # Test goto (should work)
        goto_trans = self.translator.goto_operation("LOOP_START")
        self.assertIsNotNone(goto_trans)
        
        # Verify both labels exist in function scope
        self.assertTrue(self.translator.control_flow.is_label_defined("LOOP_START", "test_function"))
        self.assertTrue(self.translator.control_flow.is_label_defined("LOOP_END", "test_function"))
        
    def test_empty_label_name_error(self):
        """Test error handling for empty label names"""
        with self.assertRaises(RuntimeError) as context:
            self.translator.label_operation("")
            
        self.assertIn("cannot be empty", str(context.exception).lower())
        
        with self.assertRaises(RuntimeError) as context:
            self.translator.goto_operation("")
            
        self.assertIn("cannot be empty", str(context.exception).lower())
        
        # Set up condition for if-goto test
        self.translator.push_constant(1)
        with self.assertRaises(RuntimeError) as context:
            self.translator.if_goto_operation("")
            
        self.assertIn("cannot be empty", str(context.exception).lower())
        
    def test_control_flow_manager_integration(self):
        """Test integration with ControlFlowManager"""
        # Test that control flow manager is properly initialized
        self.assertIsNotNone(self.translator.control_flow)
        
        # Test label management through control flow manager
        self.translator.control_flow.define_label("DIRECT_LABEL", "test_function")
        self.assertTrue(self.translator.control_flow.is_label_defined("DIRECT_LABEL", "test_function"))
        
        # Test getting function labels
        function_labels = self.translator.control_flow.get_function_labels("test_function")
        self.assertIn("DIRECT_LABEL", function_labels)
        
    def test_multiple_labels_in_function(self):
        """Test multiple labels within the same function"""
        labels = ["START", "MIDDLE", "END", "ERROR_HANDLER"]
        
        # Define multiple labels
        for label in labels:
            self.translator.label_operation(label)
            
        # Verify all labels exist
        for label in labels:
            self.assertTrue(self.translator.control_flow.is_label_defined(label, "test_function"))
            
        # Verify we can goto all labels
        for label in labels:
            goto_trans = self.translator.goto_operation(label)
            self.assertIsNotNone(goto_trans)


if __name__ == '__main__':
    unittest.main()