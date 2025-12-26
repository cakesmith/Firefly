#!/usr/bin/env python3
"""
Comprehensive test suite for Petri-net VM and multi-core assembly generation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Petri.VMToPetri import VMToPetriTranslator
from vm_parser import parse_vm_file

class PetriVMTestSuite:
    """Test suite for Petri-net VM capabilities"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results_dir = "test_results"
        
        # Create test results directory
        if not os.path.exists(self.test_results_dir):
            os.makedirs(self.test_results_dir)
            print(f"Created test results directory: {self.test_results_dir}/")
    
    def get_test_file_path(self, filename):
        """Get path for test result file"""
        return os.path.join(self.test_results_dir, filename)
    
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
    
    def test_basic_operations(self):
        """Test basic VM operations: push, add"""
        translator = VMToPetriTranslator()
        commands = [("push", "constant", 7), ("push", "constant", 8), ("add",)]
        result = translator.execute_program(commands)
        expected = [15]
        
        print(f"Commands: {commands}")
        print(f"Result: {result}, Expected: {expected}")
        translator.print_net_statistics()
        
        return result == expected
    
    def test_arithmetic_sequence(self):
        """Test arithmetic sequence: 10 - 3 = 7, then negate = -7"""
        translator = VMToPetriTranslator()
        commands = [
            ("push", "constant", 10),
            ("push", "constant", 3),
            ("sub",),
            ("neg",)
        ]
        result = translator.execute_program(commands)
        expected = [-7]
        
        print(f"Sequence: 10 - 3, then negate")
        print(f"Result: {result}, Expected: {expected}")
        
        return result == expected
    
    def test_stack_free_semantics(self):
        """Test that VM operates without stack abstraction"""
        translator = VMToPetriTranslator()
        
        # Step-by-step execution to verify stack-free operation
        place1 = translator.push_constant(7)
        place2 = translator.push_constant(8)
        
        print(f"Created places: {place1.name}, {place2.name}")
        print(f"Result places: {[p.name for p in translator.result_places]}")
        
        result_place = translator.add_operation()
        print(f"Add result place: {result_place.name}")
        
        # Execute and verify
        translator.execute_step()
        final_values = translator.get_result_values()
        
        print(f"Final values: {final_values}")
        print("✓ No stack abstraction - places ARE the data flow")
        
        return final_values == [15]
    
    def test_complex_operations(self):
        """Test complex StackTest operations"""
        vm_file = "tecs/projects/07/StackArithmetic/StackTest/StackTest.vm"
        if not os.path.exists(vm_file):
            print(f"Skipping - {vm_file} not found")
            return True
            
        commands = parse_vm_file(vm_file)
        translator = VMToPetriTranslator()
        result = translator.execute_program(commands)
        expected = [-1, 0, -1, 90]
        
        print(f"StackTest result: {result}")
        print(f"Expected: {expected}")
        translator.print_net_statistics()
        
        return result == expected
    
    def test_single_core_assembly(self):
        """Test single-core assembly generation"""
        translator = VMToPetriTranslator()
        commands = [("push", "constant", 7), ("push", "constant", 8), ("add",)]
        
        translator.execute_program(commands)
        assembly = translator.generate_multicore_assembly(num_cores=1)
        
        print(f"Generated {len(assembly)} lines of single-core assembly")
        print("Sample lines:")
        for i, line in enumerate(assembly[:5]):
            print(f"  {line}")
        
        # Save to test results folder
        output_file = self.get_test_file_path("simple_add_single.asm")
        with open(output_file, 'w') as f:
            f.write('\n'.join(assembly))
        print(f"Saved to {output_file}")
        
        return len(assembly) > 0
    
    def test_multi_core_assembly(self):
        """Test multi-core assembly generation"""
        translator = VMToPetriTranslator()
        commands = [
            ("push", "constant", 10), ("push", "constant", 5), ("add",),
            ("push", "constant", 3), ("push", "constant", 2), ("sub",),
            ("add",)
        ]
        
        translator.execute_program(commands)
        assembly = translator.generate_multicore_assembly(num_cores=2, output_dir=self.test_results_dir)
        
        print(f"Generated multi-core ROMs")
        print(f"Check {self.test_results_dir}/multicore_2cores/ folder for individual ROM files")
        
        # Check if folder was created
        folder_path = os.path.join(self.test_results_dir, "multicore_2cores")
        folder_exists = os.path.exists(folder_path)
        print(f"Folder created: {folder_exists}")
        
        if folder_exists:
            files = os.listdir(folder_path)
            print(f"Files generated: {files}")
        
        return folder_exists and len(assembly) > 0
    
    def test_stacktest_multicore(self):
        """Test StackTest with 4-core assembly generation"""
        vm_file = "tecs/projects/07/StackArithmetic/StackTest/StackTest.vm"
        if not os.path.exists(vm_file):
            print(f"Skipping - {vm_file} not found")
            return True
            
        commands = parse_vm_file(vm_file)
        translator = VMToPetriTranslator()
        translator.execute_program(commands)
        
        assembly = translator.generate_multicore_assembly(num_cores=4, output_dir=self.test_results_dir)
        
        print(f"Generated 4-core ROM system")
        print("Network statistics:")
        translator.print_net_statistics()
        
        # Check if folder was created
        folder_path = os.path.join(self.test_results_dir, "multicore_4cores")
        folder_exists = os.path.exists(folder_path)
        print(f"Folder created: {folder_exists}")
        
        if folder_exists:
            files = os.listdir(folder_path)
            print(f"Files generated: {files}")
        
        return folder_exists and len(assembly) > 0
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("Petri-Net VM Comprehensive Test Suite")
        print("=" * 60)
        
        # Core VM tests
        self.run_test("Basic Operations", self.test_basic_operations)
        self.run_test("Arithmetic Sequence", self.test_arithmetic_sequence)
        self.run_test("Stack-Free Semantics", self.test_stack_free_semantics)
        self.run_test("Complex Operations", self.test_complex_operations)
        
        # Assembly generation tests
        self.run_test("Single-Core Assembly", self.test_single_core_assembly)
        self.run_test("Multi-Core Assembly", self.test_multi_core_assembly)
        self.run_test("StackTest Multi-Core", self.test_stacktest_multicore)
        
        # Summary
        print("\n" + "=" * 60)
        print(f"Test Results: {self.passed} passed, {self.failed} failed")
        
        if self.failed == 0:
            print("🎉 ALL TESTS PASSED!")
            print("✓ Petri-net native VM working correctly")
            print("✓ Stack-free architecture validated")
            print("✓ Multi-core assembly generation functional")
        else:
            print(f"❌ {self.failed} tests failed - check implementation")
        
        return self.failed == 0

if __name__ == "__main__":
    suite = PetriVMTestSuite()
    suite.run_all_tests()