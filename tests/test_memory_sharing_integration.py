#!/usr/bin/env python3
"""
Test for memory sharing integration between PetriEmitter and memory sharing analysis.

This tests how VM instructions are analyzed for memory sharing
and placed on a 2D mesh of cores.
"""

import sys
import os
import unittest

# Add the parent directory to Python path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter
from petri_memory_integration import integrate_petri_memory_sharing, PetriMemoryIntegrator


class MockVMCommand:
    """Mock VM command for testing"""
    def __init__(self, command_type, index=None):
        self.command_type = command_type
        self.index = index


class TestMemorySharingIntegration(unittest.TestCase):
    """Test cases for memory sharing integration"""
    
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def create_simple_vm_program(self):
        """Create a simple VM program using PetriEmitter"""
        emitter = PetriEmitter()
        
        # Simple program: push 5, push 10, add
        emitter.push_constant(MockVMCommand("push", 5))
        emitter.push_constant(MockVMCommand("push", 10))
        emitter.add(MockVMCommand("add"))
        
        return emitter
    
    def create_complex_vm_program(self):
        """Create a more complex VM program with control flow"""
        emitter = PetriEmitter()
        
        # More complex program with arithmetic and comparisons
        emitter.push_constant(MockVMCommand("push", 5))
        emitter.push_constant(MockVMCommand("push", 3))
        emitter.sub(MockVMCommand("sub"))  # 5 - 3 = 2
        
        emitter.push_constant(MockVMCommand("push", 10))
        emitter.push_constant(MockVMCommand("push", 7))
        emitter.add(MockVMCommand("add"))  # 10 + 7 = 17
        
        emitter.lt(MockVMCommand("lt"))    # 2 < 17 = true (-1)
        
        # Add some labels and control flow
        emitter.label(MockVMCommand("label", "LOOP"))
        emitter.push_constant(MockVMCommand("push", 1))
        emitter.neg(MockVMCommand("neg"))  # -1
        
        # Conditional jump
        emitter.ifgoto(MockVMCommand("if-goto", "END"))
        
        # More operations
        emitter.push_constant(MockVMCommand("push", 42))
        emitter.push_constant(MockVMCommand("push", 8))
        emitter.and_op(MockVMCommand("and"))
        
        emitter.label(MockVMCommand("label", "END"))
        emitter.push_constant(MockVMCommand("push", 0))
        
        return emitter
    
    def test_simple_program_integration(self):
        """Test memory sharing analysis on a simple VM program"""
        emitter = self.create_simple_vm_program()
        
        # Perform memory sharing analysis
        report = integrate_petri_memory_sharing(emitter, 4)
        
        # Verify the report contains expected sections
        self.assertIn("PETRI NET MEMORY SHARING & PLACEMENT REPORT", report)
        self.assertIn("SUMMARY:", report)
        self.assertIn("TRANSITION PLACEMENT:", report)
        self.assertIn("MEMORY PLACEMENT:", report)
        
        # Verify we have the expected number of transitions and places
        self.assertIn("Transitions: 4", report)  # push_5, push_10, add, dup
        self.assertIn("Places: 7", report)       # init, end, const_5, const_10, dup_outs, add_result
    
    def test_complex_program_integration(self):
        """Test memory sharing analysis on a complex VM program"""
        emitter = self.create_complex_vm_program()
        
        # Perform memory sharing analysis
        report = integrate_petri_memory_sharing(emitter, 9)
        
        # Verify the report contains expected sections
        self.assertIn("PETRI NET MEMORY SHARING & PLACEMENT REPORT", report)
        self.assertIn("SUMMARY:", report)
        self.assertIn("TRANSITION PLACEMENT:", report)
        self.assertIn("MEMORY PLACEMENT:", report)
        
        # Verify we have a reasonable number of transitions and places
        lines = report.split('\n')
        transitions_line = [line for line in lines if "Transitions:" in line and "SUMMARY:" in report][0]
        places_line = [line for line in lines if "Places:" in line and "SUMMARY:" in report][0]
        
        # Extract numbers
        transitions_count = int(transitions_line.split("Transitions: ")[1])
        places_count = int(places_line.split("Places: ")[1])
        
        # Should have more than the simple case
        self.assertGreater(transitions_count, 10)
        self.assertGreater(places_count, 15)
    
    def test_integrator_extraction(self):
        """Test the PetriMemoryIntegrator's data extraction methods"""
        emitter = self.create_simple_vm_program()
        integrator = PetriMemoryIntegrator(emitter)
        
        # Test transition extraction
        mem_transitions = integrator.extract_memory_transitions()
        self.assertGreater(len(mem_transitions), 0)
        
        # Verify transitions have reads and writes
        for trans in mem_transitions:
            self.assertIsInstance(trans.reads, set)
            self.assertIsInstance(trans.writes, set)
            self.assertIsInstance(trans.id, str)
        
        # Test place extraction
        mem_places = integrator.extract_memory_places()
        self.assertGreater(len(mem_places), 0)
        
        # Verify places have types
        for place in mem_places:
            self.assertIn(place.type.value, ["ROM", "RAM"])
            self.assertIsInstance(place.id, str)
        
        # Test concurrency inference
        concurrency = integrator.infer_concurrency()
        self.assertIsInstance(concurrency.concurrent, set)
    
    def test_place_classification(self):
        """Test that places are correctly classified as ROM or RAM"""
        emitter = self.create_complex_vm_program()
        integrator = PetriMemoryIntegrator(emitter)
        
        mem_places = integrator.extract_memory_places()
        place_types = {place.id: place.type.value for place in mem_places}
        
        # Constants should be ROM
        const_places = [pid for pid in place_types.keys() if pid.startswith("const_")]
        for const_place in const_places:
            self.assertEqual(place_types[const_place], "ROM", 
                           f"Constant place {const_place} should be ROM")
        
        # Labels should be ROM
        label_places = [pid for pid in place_types.keys() if pid.startswith("label_")]
        for label_place in label_places:
            self.assertEqual(place_types[label_place], "ROM", 
                           f"Label place {label_place} should be ROM")
        
        # Control places should be ROM
        if "init" in place_types:
            self.assertEqual(place_types["init"], "ROM")
        if "end" in place_types:
            self.assertEqual(place_types["end"], "ROM")
        
        # Result places should be RAM
        result_places = [pid for pid in place_types.keys() if "result" in pid]
        for result_place in result_places:
            self.assertEqual(place_types[result_place], "RAM", 
                           f"Result place {result_place} should be RAM")
    
    def test_mesh_creation(self):
        """Test mesh topology creation"""
        integrator = PetriMemoryIntegrator(PetriEmitter())
        
        # Test 2x2 mesh
        mesh_4 = integrator.create_default_mesh(4)
        self.assertEqual(len(mesh_4), 4)
        for core in mesh_4:
            self.assertIsInstance(core.neighbors, list)
            self.assertGreater(len(core.neighbors), 0)  # Each core should have neighbors
        
        # Test 3x3 mesh
        mesh_9 = integrator.create_default_mesh(9)
        self.assertEqual(len(mesh_9), 9)
        
        # Test linear topology
        mesh_6 = integrator.create_default_mesh(6)
        self.assertEqual(len(mesh_6), 6)
    
    def test_memory_address_assignment(self):
        """Test that memory addresses are assigned to places"""
        emitter = self.create_simple_vm_program()
        integrator = PetriMemoryIntegrator(emitter)
        
        # Perform analysis
        transition_placement, memory_placement = integrator.analyze_and_place_memory(4)
        
        # Apply memory addresses
        integrator.apply_memory_addresses(memory_placement)
        
        # Check that places have memory addresses assigned
        addressed_places = 0
        for place_id, place in emitter.net.places.items():
            if hasattr(place, 'memory_address') and place.memory_address is not None:
                addressed_places += 1
                self.assertIsInstance(place.memory_address, int)
                self.assertGreaterEqual(place.memory_address, 0)
        
        # Should have assigned addresses to most places
        self.assertGreater(addressed_places, 0)
    
    def test_different_mesh_sizes(self):
        """Test that the system works with different mesh sizes"""
        emitter = self.create_simple_vm_program()
        
        for num_cores in [1, 4, 9, 16]:
            with self.subTest(num_cores=num_cores):
                report = integrate_petri_memory_sharing(emitter, num_cores)
                self.assertIn("PETRI NET MEMORY SHARING & PLACEMENT REPORT", report)
                self.assertIn("TRANSITION PLACEMENT:", report)


def run_memory_sharing_tests():
    """Run the memory sharing integration tests and return results"""
    print("Running Memory Sharing Integration Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMemorySharingIntegration)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_memory_sharing_tests()
    sys.exit(0 if success else 1)