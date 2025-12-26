#!/usr/bin/env python3
"""
Simple VM parser to convert .vm files to command tuples for our Petri-net VM
"""

import re
from Petri.VMToPetri import VMToPetriTranslator

def parse_vm_file(filename):
    """Parse a .vm file and return list of command tuples"""
    commands = []
    
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            # Remove comments and whitespace
            line = re.sub(r'//.*', '', line).strip()
            if not line:
                continue
                
            parts = line.split()
            if not parts:
                continue
                
            cmd = parts[0]
            
            if cmd == "push" and len(parts) == 3:
                segment = parts[1]
                index = int(parts[2])
                commands.append(("push", segment, index))
            elif cmd in ["add", "sub", "neg", "and", "or", "not", "eq", "lt", "gt"]:
                commands.append((cmd,))
            elif cmd == "pop" and len(parts) == 3:
                segment = parts[1]
                index = int(parts[2])
                commands.append(("pop", segment, index))
            else:
                print(f"Warning: Unsupported command '{line}' at line {line_num}")
                
    return commands

def test_simple_add_vm():
    """Test with the actual SimpleAdd.vm file"""
    print("=== Testing with SimpleAdd.vm ===")
    
    vm_file = "tecs/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm"
    commands = parse_vm_file(vm_file)
    
    print(f"Parsed commands: {commands}")
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Final result: {result}")
    print(f"Expected: [15]")
    print(f"Success: {result == [15]}")

    # Print comprehensive statistics about the translated Petri net
    translator.print_net_statistics()
    
    return result == [15]

def test_stack_test_vm():
    """Test with the more complex StackTest.vm file"""
    print("\n=== Testing with StackTest.vm ===")
    
    vm_file = "tecs/projects/07/StackArithmetic/StackTest/StackTest.vm"
    commands = parse_vm_file(vm_file)
    
    print(f"Parsed {len(commands)} commands")
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Final result: {result}")
    
    # Print comprehensive statistics about the translated Petri net
    translator.print_net_statistics()
    
    return len(result) >= 1  # Should have at least one result on stack

if __name__ == "__main__":
    test_simple_add_vm()
    test_stack_test_vm()