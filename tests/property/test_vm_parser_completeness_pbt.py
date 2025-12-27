#!/usr/bin/env python3
"""
Property-Based Tests for VM Parser Completeness
**Feature: petri-vm-improvements, Property 1: Complete command parsing**
**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
"""

import sys
import os
import tempfile
# Add the root directory to the path to import vm_parser
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from hypothesis import given, strategies as st, settings, assume
import vm_parser
from vm_parser import VMParseError

class VMParserCompletenessPBT:
    """Property-based tests for VM parser completeness"""
    
    @given(
        segment=st.sampled_from(['constant', 'local', 'argument', 'static', 'temp', 'pointer', 'this', 'that']),
        index=st.integers(min_value=0, max_value=100)
    )
    @settings(max_examples=100)
    def test_push_command_parsing(self, segment, index):
        """
        Property 1a: Push command parsing completeness
        For any valid segment and index, push commands should parse correctly
        **Validates: Requirements 3.1, 4.1, 4.2, 4.3**
        """
        # Apply segment-specific constraints
        if segment == 'temp' and index > 7:
            assume(False)  # Skip invalid temp indices
        if segment == 'pointer' and index > 1:
            assume(False)  # Skip invalid pointer indices
        if segment == 'static' and index > 239:
            assume(False)  # Skip invalid static indices
            
        # Create temporary VM file with push command
        vm_content = f"push {segment} {index}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == ("push", segment, index), f"Expected ('push', '{segment}', {index}), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Push command parsing failed for segment={segment}, index={index}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        segment=st.sampled_from(['local', 'argument', 'static', 'temp', 'pointer', 'this', 'that']),
        index=st.integers(min_value=0, max_value=100)
    )
    @settings(max_examples=100)
    def test_pop_command_parsing(self, segment, index):
        """
        Property 1b: Pop command parsing completeness
        For any valid segment and index (except constant), pop commands should parse correctly
        **Validates: Requirements 3.1, 4.1, 4.2, 4.3**
        """
        # Apply segment-specific constraints
        if segment == 'temp' and index > 7:
            assume(False)  # Skip invalid temp indices
        if segment == 'pointer' and index > 1:
            assume(False)  # Skip invalid pointer indices
        if segment == 'static' and index > 239:
            assume(False)  # Skip invalid static indices
            
        # Create temporary VM file with pop command
        vm_content = f"pop {segment} {index}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == ("pop", segment, index), f"Expected ('pop', '{segment}', {index}), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Pop command parsing failed for segment={segment}, index={index}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        arithmetic_cmd=st.sampled_from(['add', 'sub', 'mul', 'div', 'neg'])
    )
    @settings(max_examples=100)
    def test_arithmetic_command_parsing(self, arithmetic_cmd):
        """
        Property 1c: Arithmetic command parsing completeness
        For any arithmetic command, parsing should succeed
        **Validates: Requirements 3.1**
        """
        # Create temporary VM file with arithmetic command
        vm_content = f"{arithmetic_cmd}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == (arithmetic_cmd,), f"Expected ('{arithmetic_cmd}',), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Arithmetic command parsing failed for {arithmetic_cmd}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        logical_cmd=st.sampled_from(['eq', 'lt', 'gt', 'and', 'or', 'not'])
    )
    @settings(max_examples=100)
    def test_logical_command_parsing(self, logical_cmd):
        """
        Property 1d: Logical command parsing completeness
        For any logical command, parsing should succeed
        **Validates: Requirements 3.1**
        """
        # Create temporary VM file with logical command
        vm_content = f"{logical_cmd}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == (logical_cmd,), f"Expected ('{logical_cmd}',), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Logical command parsing failed for {logical_cmd}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        function_name=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.', min_size=1, max_size=20),
        num_locals=st.integers(min_value=0, max_value=50)
    )
    @settings(max_examples=100)
    def test_function_command_parsing(self, function_name, num_locals):
        """
        Property 1e: Function command parsing completeness
        For any valid function name and local count, function commands should parse correctly
        **Validates: Requirements 3.2**
        """
        # Ensure function name starts with letter or underscore
        if not function_name or not (function_name[0].isalpha() or function_name[0] == '_'):
            assume(False)
            
        # Create temporary VM file with function command
        vm_content = f"function {function_name} {num_locals}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == ("function", function_name, num_locals), f"Expected ('function', '{function_name}', {num_locals}), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Function command parsing failed for name={function_name}, locals={num_locals}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        function_name=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.', min_size=1, max_size=20),
        num_args=st.integers(min_value=0, max_value=20)
    )
    @settings(max_examples=100)
    def test_call_command_parsing(self, function_name, num_args):
        """
        Property 1f: Call command parsing completeness
        For any valid function name and argument count, call commands should parse correctly
        **Validates: Requirements 3.2**
        """
        # Ensure function name starts with letter or underscore
        if not function_name or not (function_name[0].isalpha() or function_name[0] == '_'):
            assume(False)
            
        # Create temporary VM file with call command
        vm_content = f"call {function_name} {num_args}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
            assert commands[0] == ("call", function_name, num_args), f"Expected ('call', '{function_name}', {num_args}), got {commands[0]}"
            
        except Exception as e:
            raise AssertionError(f"Call command parsing failed for name={function_name}, args={num_args}: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        label_name=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.', min_size=1, max_size=20)
    )
    @settings(max_examples=100)
    def test_control_flow_command_parsing(self, label_name):
        """
        Property 1g: Control flow command parsing completeness
        For any valid label name, control flow commands should parse correctly
        **Validates: Requirements 3.3**
        """
        # Ensure label name starts with letter or underscore
        if not label_name or not (label_name[0].isalpha() or label_name[0] == '_'):
            assume(False)
            
        control_commands = ['label', 'goto', 'if-goto']
        
        for cmd in control_commands:
            # Create temporary VM file with control flow command
            vm_content = f"{cmd} {label_name}\n"
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
                f.write(vm_content)
                temp_file = f.name
                
            try:
                commands = vm_parser.parse_vm_file(temp_file)
                
                assert len(commands) == 1, f"Expected 1 command, got {len(commands)}"
                assert commands[0] == (cmd, label_name), f"Expected ('{cmd}', '{label_name}'), got {commands[0]}"
                
            except Exception as e:
                raise AssertionError(f"Control flow command parsing failed for {cmd} {label_name}: {e}")
            finally:
                os.unlink(temp_file)
                
    @given(
        commands=st.lists(
            st.one_of(
                st.tuples(st.just('push'), st.sampled_from(['constant', 'local', 'argument']), st.integers(0, 10)),
                st.tuples(st.sampled_from(['add', 'sub', 'mul'])),
                st.tuples(st.sampled_from(['eq', 'lt', 'gt'])),
                st.tuples(st.just('return'))
            ),
            min_size=1,
            max_size=10
        )
    )
    @settings(max_examples=100)
    def test_multi_command_parsing(self, commands):
        """
        Property 1h: Multi-command parsing completeness
        For any sequence of valid commands, parsing should handle all commands correctly
        **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
        """
        # Build VM content from command tuples
        vm_lines = []
        expected_commands = []
        
        for cmd_tuple in commands:
            if len(cmd_tuple) == 1:
                vm_lines.append(cmd_tuple[0])
                expected_commands.append(cmd_tuple)
            elif len(cmd_tuple) == 3:
                vm_lines.append(f"{cmd_tuple[0]} {cmd_tuple[1]} {cmd_tuple[2]}")
                expected_commands.append(cmd_tuple)
                
        vm_content = '\n'.join(vm_lines) + '\n'
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            parsed_commands = vm_parser.parse_vm_file(temp_file)
            
            assert len(parsed_commands) == len(expected_commands), f"Expected {len(expected_commands)} commands, got {len(parsed_commands)}"
            
            for i, (parsed, expected) in enumerate(zip(parsed_commands, expected_commands)):
                assert parsed == expected, f"Command {i}: expected {expected}, got {parsed}"
                
        except Exception as e:
            raise AssertionError(f"Multi-command parsing failed: {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        invalid_segment=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', min_size=1, max_size=10).filter(
            lambda x: x not in ['constant', 'local', 'argument', 'static', 'temp', 'pointer', 'this', 'that']
        )
    )
    @settings(max_examples=100)
    def test_invalid_segment_rejection(self, invalid_segment):
        """
        Property 1i: Invalid segment rejection
        For any invalid memory segment, parsing should fail with appropriate error
        **Validates: Requirements 3.4, 3.5**
        """
        # Create temporary VM file with invalid segment
        vm_content = f"push {invalid_segment} 0\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            # This should raise a VMParseError
            commands = vm_parser.parse_vm_file(temp_file)
            # If we get here, parsing succeeded when it should have failed
            raise AssertionError(f"Parser should have rejected invalid segment '{invalid_segment}'")
            
        except VMParseError:
            # This is expected - invalid segment should be rejected
            pass
        except Exception as e:
            raise AssertionError(f"Unexpected error for invalid segment '{invalid_segment}': {e}")
        finally:
            os.unlink(temp_file)
            
    @given(
        invalid_command=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=10).filter(
            lambda x: x not in ['push', 'pop', 'add', 'sub', 'mul', 'div', 'neg', 'eq', 'lt', 'gt', 'and', 'or', 'not', 'label', 'goto', 'if-goto', 'function', 'call', 'return']
        )
    )
    @settings(max_examples=100)
    def test_invalid_command_rejection(self, invalid_command):
        """
        Property 1j: Invalid command rejection
        For any invalid command, parsing should fail with appropriate error
        **Validates: Requirements 3.5**
        """
        # Create temporary VM file with invalid command
        vm_content = f"{invalid_command}\n"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.vm', delete=False, encoding='utf-8') as f:
            f.write(vm_content)
            temp_file = f.name
            
        try:
            # This should raise a VMParseError
            commands = vm_parser.parse_vm_file(temp_file)
            # If we get here, parsing succeeded when it should have failed
            raise AssertionError(f"Parser should have rejected invalid command '{invalid_command}'")
            
        except VMParseError:
            # This is expected - invalid command should be rejected
            pass
        except Exception as e:
            raise AssertionError(f"Unexpected error for invalid command '{invalid_command}': {e}")
        finally:
            os.unlink(temp_file)

def run_property_tests():
    """Run all property-based tests for VM parser completeness"""
    print("Running Property-Based Tests for VM Parser Completeness")
    print("=" * 60)
    
    pbt = VMParserCompletenessPBT()
    
    try:
        print("Testing Property 1a: Push command parsing...")
        pbt.test_push_command_parsing()
        print("✅ Push command parsing PASSED")
        
        print("\nTesting Property 1b: Pop command parsing...")
        pbt.test_pop_command_parsing()
        print("✅ Pop command parsing PASSED")
        
        print("\nTesting Property 1c: Arithmetic command parsing...")
        pbt.test_arithmetic_command_parsing()
        print("✅ Arithmetic command parsing PASSED")
        
        print("\nTesting Property 1d: Logical command parsing...")
        pbt.test_logical_command_parsing()
        print("✅ Logical command parsing PASSED")
        
        print("\nTesting Property 1e: Function command parsing...")
        pbt.test_function_command_parsing()
        print("✅ Function command parsing PASSED")
        
        print("\nTesting Property 1f: Call command parsing...")
        pbt.test_call_command_parsing()
        print("✅ Call command parsing PASSED")
        
        print("\nTesting Property 1g: Control flow command parsing...")
        pbt.test_control_flow_command_parsing()
        print("✅ Control flow command parsing PASSED")
        
        print("\nTesting Property 1h: Multi-command parsing...")
        pbt.test_multi_command_parsing()
        print("✅ Multi-command parsing PASSED")
        
        print("\nTesting Property 1i: Invalid segment rejection...")
        pbt.test_invalid_segment_rejection()
        print("✅ Invalid segment rejection PASSED")
        
        print("\nTesting Property 1j: Invalid command rejection...")
        pbt.test_invalid_command_rejection()
        print("✅ Invalid command rejection PASSED")
        
        print("\n🎉 ALL VM PARSER COMPLETENESS PROPERTY TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ VM PARSER COMPLETENESS PROPERTY TEST FAILED: {e}")
        return False

if __name__ == "__main__":
    success = run_property_tests()
    sys.exit(0 if success else 1)