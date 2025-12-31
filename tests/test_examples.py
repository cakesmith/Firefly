#!/usr/bin/env python3
"""
Test runner for VM examples - demonstrates both single file and multi-file parsing
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser
import tempfile
import shutil

def test_single_vm_file(vm_file_path, expected_result=None):
    """Test a single VM file by creating an isolated temporary directory"""
    print(f"\n=== Testing Single File: {os.path.basename(vm_file_path)} ===")
    
    # Read the VM file content
    with open(vm_file_path, 'r') as f:
        vm_content = f.read()
    
    # Create a temporary directory with just this VM file
    temp_dir = tempfile.mkdtemp()
    temp_vm_file = os.path.join(temp_dir, "test.vm")
    
    try:
        # Write the VM content to the temporary file
        with open(temp_vm_file, 'w') as f:
            f.write(vm_content)
        
        # Parse VM code
        parser = VMParser(temp_dir)
        emitter = parser.emitter
        net = emitter.net
        
        print(f"Commands parsed: {len(parser.results)}")
        print(f"Control stack size: {len(emitter.control_stack)}")
        
        # Execute the net
        net.allocate_memory()
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 50:
                break
        
        # Show result
        if emitter.control_stack:
            result_place = emitter.control_stack[-1]
            if result_place.has:
                result = result_place.token.value
                print(f"Result: {result}")
                
                if expected_result is not None:
                    if result == expected_result:
                        print(f"✓ Expected {expected_result}, got {result}")
                    else:
                        print(f"✗ Expected {expected_result}, got {result}")
                else:
                    print("✓ Execution completed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_multi_file_directory(directory_path):
    """Test parsing all VM files in a directory (the normal use case)"""
    print(f"\n=== Testing Multi-File Directory: {directory_path} ===")
    
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist")
        return
    
    try:
        # Parse all VM files in the directory
        parser = VMParser(directory_path)
        emitter = parser.emitter
        net = emitter.net
        
        vm_files = [f for f in os.listdir(directory_path) if f.endswith('.vm')]
        print(f"VM files found: {vm_files}")
        print(f"Total commands parsed: {len(parser.results)}")
        print(f"Places in net: {len(net.places)}")
        print(f"Transitions in net: {len(net.transitions)}")
        print(f"Final control stack size: {len(emitter.control_stack)}")
        
        # Execute the net
        net.allocate_memory()
        step = 1
        while True:
            fired = net.execute_step()
            if not fired:
                break
            step += 1
            if step > 100:  # Higher limit for multi-file programs
                print("Execution stopped (max steps reached)")
                break
        
        # Show all results on the stack
        print(f"\nFinal results:")
        if emitter.control_stack:
            for i, place in enumerate(emitter.control_stack):
                if place.has:
                    print(f"  Stack[{i}]: {place.token.value} (from {place.name})")
        else:
            print("  No results on stack")
        
        print("✓ Multi-file directory parsing completed")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("VM Examples Test Runner")
    print("Demonstrates single-file vs multi-file VM parsing")
    print("=" * 60)
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    examples_dir = os.path.join(project_root, "examples")
    
    print("\n🔹 SINGLE FILE TESTS (Isolated)")
    # Test individual files in isolation
    simple_add_path = os.path.join(examples_dir, "simple_add.vm")
    if os.path.exists(simple_add_path):
        test_single_vm_file(simple_add_path, expected_result=20)
    
    multiple_adds_path = os.path.join(examples_dir, "multiple_adds.vm")
    if os.path.exists(multiple_adds_path):
        test_single_vm_file(multiple_adds_path, expected_result=50)
    
    print("\n🔹 MULTI-FILE DIRECTORY TEST (Normal Use Case)")
    # Test parsing the entire examples directory (all VM files together)
    test_multi_file_directory(examples_dir)
    
    print("\n" + "=" * 60)
    print("Testing complete!")
    print("Note: Single-file tests show isolated behavior.")
    print("Multi-file test shows how VMParser normally works - parsing ALL .vm files in a directory.")