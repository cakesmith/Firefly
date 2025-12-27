#!/usr/bin/env python3
"""
Enhanced VM parser to convert .vm files to command tuples for our Petri-net VM
Supports complete VM command set including control flow and function operations
"""

import re
import os
from Petri.VMToPetri import VMToPetriTranslator

class VMParseError(Exception):
    """Exception raised for VM parsing errors"""
    def __init__(self, message, line_number, line_content):
        self.message = message
        self.line_number = line_number
        self.line_content = line_content
        super().__init__(f"Line {line_number}: {message} in '{line_content}'")

def parse_vm_file(filename):
    """
    Parse a .vm file and return list of command tuples
    Enhanced to support all VM commands with proper error handling
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"VM file not found: {filename}")
        
    commands = []
    supported_segments = {
        'constant', 'local', 'argument', 'static', 'temp', 
        'pointer', 'this', 'that'
    }
    
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    # Remove comments and whitespace
                    original_line = line
                    line = re.sub(r'//.*', '', line).strip()
                    if not line:
                        continue
                        
                    parts = line.split()
                    if not parts:
                        continue
                        
                    cmd = parts[0].lower()
                    
                    # Memory operations
                    if cmd == "push":
                        if len(parts) != 3:
                            raise VMParseError(f"push command requires 2 arguments, got {len(parts)-1}", line_num, original_line.strip())
                        segment = parts[1]
                        if segment not in supported_segments:
                            raise VMParseError(f"Unsupported memory segment: {segment}", line_num, original_line.strip())
                        try:
                            index = int(parts[2])
                        except ValueError:
                            raise VMParseError(f"push index must be integer, got '{parts[2]}'", line_num, original_line.strip())
                        _validate_segment_index(segment, index, line_num, original_line.strip())
                        commands.append(("push", segment, index))
                        
                    elif cmd == "pop":
                        if len(parts) != 3:
                            raise VMParseError(f"pop command requires 2 arguments, got {len(parts)-1}", line_num, original_line.strip())
                        segment = parts[1]
                        if segment not in supported_segments:
                            raise VMParseError(f"Unsupported memory segment: {segment}", line_num, original_line.strip())
                        if segment == 'constant':
                            raise VMParseError("Cannot pop to constant segment", line_num, original_line.strip())
                        try:
                            index = int(parts[2])
                        except ValueError:
                            raise VMParseError(f"pop index must be integer, got '{parts[2]}'", line_num, original_line.strip())
                        _validate_segment_index(segment, index, line_num, original_line.strip())
                        commands.append(("pop", segment, index))
                        
                    # Arithmetic operations (enhanced to include mul, div)
                    elif cmd in ["add", "sub", "mul", "div", "neg"]:
                        if len(parts) != 1:
                            raise VMParseError(f"{cmd} command takes no arguments, got {len(parts)-1}", line_num, original_line.strip())
                        commands.append((cmd,))
                        
                    # Logical operations
                    elif cmd in ["eq", "lt", "gt", "and", "or", "not"]:
                        if len(parts) != 1:
                            raise VMParseError(f"{cmd} command takes no arguments, got {len(parts)-1}", line_num, original_line.strip())
                        commands.append((cmd,))
                        
                    # Control flow operations (NEW)
                    elif cmd == "label":
                        if len(parts) != 2:
                            raise VMParseError(f"label command requires 1 argument, got {len(parts)-1}", line_num, original_line.strip())
                        label_name = parts[1]
                        if not _is_valid_identifier(label_name):
                            raise VMParseError(f"Invalid label name: {label_name}", line_num, original_line.strip())
                        commands.append(("label", label_name))
                        
                    elif cmd == "goto":
                        if len(parts) != 2:
                            raise VMParseError(f"goto command requires 1 argument, got {len(parts)-1}", line_num, original_line.strip())
                        label_name = parts[1]
                        if not _is_valid_identifier(label_name):
                            raise VMParseError(f"Invalid label name: {label_name}", line_num, original_line.strip())
                        commands.append(("goto", label_name))
                        
                    elif cmd == "if-goto":
                        if len(parts) != 2:
                            raise VMParseError(f"if-goto command requires 1 argument, got {len(parts)-1}", line_num, original_line.strip())
                        label_name = parts[1]
                        if not _is_valid_identifier(label_name):
                            raise VMParseError(f"Invalid label name: {label_name}", line_num, original_line.strip())
                        commands.append(("if-goto", label_name))
                        
                    # Function operations (NEW)
                    elif cmd == "function":
                        if len(parts) != 3:
                            raise VMParseError(f"function command requires 2 arguments, got {len(parts)-1}", line_num, original_line.strip())
                        function_name = parts[1]
                        if not _is_valid_identifier(function_name):
                            raise VMParseError(f"Invalid function name: {function_name}", line_num, original_line.strip())
                        try:
                            num_locals = int(parts[2])
                        except ValueError:
                            raise VMParseError(f"function numLocals must be integer, got '{parts[2]}'", line_num, original_line.strip())
                        if num_locals < 0:
                            raise VMParseError(f"function numLocals must be non-negative, got {num_locals}", line_num, original_line.strip())
                        commands.append(("function", function_name, num_locals))
                        
                    elif cmd == "call":
                        if len(parts) != 3:
                            raise VMParseError(f"call command requires 2 arguments, got {len(parts)-1}", line_num, original_line.strip())
                        function_name = parts[1]
                        if not _is_valid_identifier(function_name):
                            raise VMParseError(f"Invalid function name: {function_name}", line_num, original_line.strip())
                        try:
                            num_args = int(parts[2])
                        except ValueError:
                            raise VMParseError(f"call numArgs must be integer, got '{parts[2]}'", line_num, original_line.strip())
                        if num_args < 0:
                            raise VMParseError(f"call numArgs must be non-negative, got {num_args}", line_num, original_line.strip())
                        commands.append(("call", function_name, num_args))
                        
                    elif cmd == "return":
                        if len(parts) != 1:
                            raise VMParseError(f"return command takes no arguments, got {len(parts)-1}", line_num, original_line.strip())
                        commands.append(("return",))
                        
                    else:
                        raise VMParseError(f"Unsupported command: {cmd}", line_num, original_line.strip())
                        
                except VMParseError:
                    raise
                except Exception as e:
                    raise VMParseError(f"Parse error: {str(e)}", line_num, original_line.strip())
                    
    except IOError as e:
        raise VMParseError(f"File I/O error: {str(e)}", 0, filename)
        
    return commands

def _validate_segment_index(segment, index, line_num, line):
    """Validate segment-specific index constraints"""
    if index < 0:
        raise VMParseError(f"Segment index must be non-negative, got {index}", line_num, line)
        
    # Segment-specific validation
    if segment == 'temp' and index > 7:
        raise VMParseError(f"temp segment index must be 0-7, got {index}", line_num, line)
    elif segment == 'pointer' and index > 1:
        raise VMParseError(f"pointer segment index must be 0-1, got {index}", line_num, line)
    elif segment == 'static' and index > 239:
        raise VMParseError(f"static segment index must be 0-239, got {index}", line_num, line)

def _is_valid_identifier(name):
    """Check if a name is a valid identifier"""
    if not name:
        return False
    # Allow alphanumeric, underscore, dot (for class.method), and hyphen
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_.-]*$', name) is not None

def get_supported_commands():
    """Get list of all supported commands"""
    return [
        'push', 'pop', 'add', 'sub', 'mul', 'div', 'neg',
        'eq', 'lt', 'gt', 'and', 'or', 'not',
        'label', 'goto', 'if-goto', 'function', 'call', 'return'
    ]

def get_supported_segments():
    """Get list of all supported memory segments"""
    return ['constant', 'local', 'argument', 'static', 'temp', 'pointer', 'this', 'that']

def validate_vm_file(filename):
    """
    Validate a VM file and return validation results
    
    Args:
        filename: Path to the VM file
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    try:
        commands = parse_vm_file(filename)
        # If we get here, parsing succeeded
        return True, []
    except VMParseError as e:
        errors.append(str(e))
    except Exception as e:
        errors.append(f"Unexpected error: {str(e)}")
        
    return False, errors

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