#!/usr/bin/env python3
"""
Unit Tests for Local Variable Edge Cases
Tests specific examples and edge cases for local variable operations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Petri.VMToPetri import VMToPetriTranslator

class LocalVariableUnitTests:
    """Unit tests for local variable edge cases"""
    
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
    
    def test_uninitialized_local_access(self):
        """Test accessing uninitialized local variables"""
        translator = VMToPetriTranslator()
        
        # Try to push from uninitialized local
        commands = [
            ("function", "test_func", 2),
            ("push", "local", 0),  # Should get default value (0)
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Uninitialized local access result: {result}")
            
            # Should get default value of 0
            expected = [0]
            return result == expected
            
        except Exception as e:
            print(f"Uninitialized local access failed: {e}")
            return False
    
    def test_local_out_of_bounds(self):
        """Test accessing local variables out of bounds"""
        translator = VMToPetriTranslator()
        
        # Try to access local beyond function's local count
        commands = [
            ("function", "test_func", 2),  # Only 2 locals (0, 1)
            ("push", "constant", 42),
            ("pop", "local", 5),  # Out of bounds
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Out of bounds access should have failed but got: {result}")
            return False  # Should have thrown an exception
            
        except RuntimeError as e:
            print(f"Correctly caught out of bounds error: {e}")
            return "out of bounds" in str(e).lower()
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    def test_local_without_function_context(self):
        """Test local operations without function context"""
        translator = VMToPetriTranslator()
        
        # Try to use local operations outside function
        commands = [
            ("push", "constant", 42),
            ("pop", "local", 0),  # No function context
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"No function context should have failed but got: {result}")
            return False  # Should have thrown an exception
            
        except RuntimeError as e:
            print(f"Correctly caught no function context error: {e}")
            return "function context" in str(e).lower()
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    def test_local_across_function_calls(self):
        """Test local variables across nested function calls"""
        translator = VMToPetriTranslator()
        
        commands = [
            # Define helper function
            ("function", "helper", 1),
            ("push", "constant", 100),
            ("pop", "local", 0),
            ("push", "local", 0),
            ("return",),
            
            # Define main function  
            ("function", "main", 2),
            ("push", "constant", 42),
            ("pop", "local", 0),
            ("call", "helper", 0),  # Call helper function
            ("pop", "local", 1),    # Store helper's result
            ("push", "local", 0),   # Push main's local (should still be 42)
            ("push", "local", 1),   # Push helper's result (should be 100)
            ("add",),               # Add them together: 42 + 100 = 142
            ("return",),
            
            # Call main function
            ("call", "main", 0)
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Nested function calls result: {result}")
            
            # Should have 42 + 100 = 142
            expected = [142]
            return result == expected
            
        except Exception as e:
            print(f"Nested function calls failed: {e}")
            return False
    
    def test_memory_optimization_with_locals(self):
        """Test that memory optimization works with local variables"""
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 3),
            ("push", "constant", 10),
            ("pop", "local", 0),
            ("push", "constant", 20),
            ("pop", "local", 1),
            ("push", "constant", 30),
            ("pop", "local", 2),
            ("push", "local", 0),
            ("push", "local", 1),
            ("add",),
            ("push", "local", 2),
            ("add",),
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Memory optimization test result: {result}")
            
            # Should compute 10 + 20 + 30 = 60
            expected = [60]
            success = result == expected
            
            if success:
                # Check memory optimization statistics
                translator.print_net_statistics()
            
            return success
            
        except Exception as e:
            print(f"Memory optimization test failed: {e}")
            return False
    
    def test_local_variable_persistence(self):
        """Test that local variables persist across operations within function"""
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 1),
            ("push", "constant", 5),
            ("pop", "local", 0),     # Store 5 in local 0
            ("push", "constant", 3),
            ("push", "local", 0),    # Push local 0 (should be 5)
            ("add",),                # 3 + 5 = 8
            ("pop", "local", 0),     # Store 8 back in local 0
            ("push", "local", 0),    # Push local 0 again (should be 8)
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Local persistence test result: {result}")
            
            # Should have 8 (the updated value)
            expected = [8]
            return result == expected
            
        except Exception as e:
            print(f"Local persistence test failed: {e}")
            return False
    
    def test_multiple_local_independence(self):
        """Test that multiple local variables are independent"""
        translator = VMToPetriTranslator()
        
        commands = [
            ("function", "test_func", 3),
            # Initialize locals with different values
            ("push", "constant", 10),
            ("pop", "local", 0),
            ("push", "constant", 20),
            ("pop", "local", 1),
            ("push", "constant", 30),
            ("pop", "local", 2),
            
            # Modify only local 1
            ("push", "local", 1),
            ("push", "constant", 5),
            ("add",),
            ("pop", "local", 1),
            
            # Check all locals by computing their sum
            ("push", "local", 0),  # Should still be 10
            ("push", "local", 1),  # Should be 25 (20 + 5)
            ("add",),              # 10 + 25 = 35
            ("push", "local", 2),  # Should still be 30
            ("add",),              # 35 + 30 = 65
            ("return",),
            ("call", "test_func", 0)  # Call the function
        ]
        
        try:
            result = translator.execute_program(commands)
            print(f"Local independence test result: {result}")
            
            # Should have 10 + 25 + 30 = 65
            expected = [65]
            return result == expected
            
        except Exception as e:
            print(f"Local independence test failed: {e}")
            return False
    
    def run_all_tests(self):
        """Run all unit tests"""
        print("Local Variable Unit Tests")
        print("=" * 50)
        
        self.run_test("Uninitialized Local Access", self.test_uninitialized_local_access)
        self.run_test("Local Out of Bounds", self.test_local_out_of_bounds)
        self.run_test("No Function Context", self.test_local_without_function_context)
        self.run_test("Locals Across Function Calls", self.test_local_across_function_calls)
        self.run_test("Memory Optimization with Locals", self.test_memory_optimization_with_locals)
        self.run_test("Local Variable Persistence", self.test_local_variable_persistence)
        self.run_test("Multiple Local Independence", self.test_multiple_local_independence)
        
        # Summary
        print("\n" + "=" * 50)
        print(f"Unit Test Results: {self.passed} passed, {self.failed} failed")
        
        if self.failed == 0:
            print("🎉 ALL UNIT TESTS PASSED!")
        else:
            print(f"❌ {self.failed} tests failed")
        
        return self.failed == 0

if __name__ == "__main__":
    suite = LocalVariableUnitTests()
    success = suite.run_all_tests()
    sys.exit(0 if success else 1)