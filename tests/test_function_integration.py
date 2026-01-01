#!/usr/bin/env python3

"""
Integration test for function/call/return with VMParser
"""

import sys
import os
import tempfile
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser

def test_simple_function_parsing():
    """Test parsing a simple function with VMParser"""
    print("Testing VMParser integration with function commands...")
    
    # Create a temporary directory with our test VM file
    with tempfile.TemporaryDirectory() as temp_dir:
        vm_file_path = os.path.join(temp_dir, "SimpleFunction.vm")
        
        # Write test VM code
        vm_code = """// Simple function test
function SimpleFunction.test 2
push local 0
push local 1
add
not
push argument 0
add
push argument 1
sub
return
"""
        
        with open(vm_file_path, 'w') as f:
            f.write(vm_code)
        
        # Parse with VMParser
        try:
            parser = VMParser(temp_dir)
            
            print(f"Successfully parsed {len(parser.results)} commands")
            
            # Print the parsed commands
            for i, (vmc, result) in enumerate(parser.results):
                print(f"Command {i}: {vmc.command} {vmc.segment or ''} {vmc.index or ''}")
                if result:
                    print(f"  -> Transition: {result.name}")
            
            # Check that we have the expected commands
            commands = [vmc.command for vmc, result in parser.results]
            expected = ['function', 'push', 'push', 'add', 'not', 'push', 'add', 'push', 'sub', 'return']
            
            if commands == expected:
                print("✓ All commands parsed correctly")
            else:
                print(f"✗ Command mismatch. Expected: {expected}, Got: {commands}")
                return False
            
            # Check that function was registered
            emitter = parser.emitter
            if hasattr(emitter.net, 'functions') and 'SimpleFunction.test' in emitter.net.functions:
                print("✓ Function registered correctly")
            else:
                print("✗ Function not registered")
                return False
            
            print(f"Final control stack size: {len(emitter.control_stack)}")
            print(f"Total places: {len(emitter.net.places)}")
            print(f"Total transitions: {len(emitter.net.transitions)}")
            
            return True
            
        except Exception as e:
            print(f"Error during parsing: {e}")
            import traceback
            traceback.print_exc()
            return False

def test_fibonacci_example():
    """Test with the Fibonacci example from TECS"""
    print("\nTesting with Fibonacci example...")
    
    # Use the existing Fibonacci example
    fibonacci_dir = "tecs/projects/08/FunctionCalls/FibonacciElement"
    
    if not os.path.exists(fibonacci_dir):
        print("Fibonacci example directory not found, skipping...")
        return True
    
    try:
        parser = VMParser(fibonacci_dir)
        
        print(f"Successfully parsed {len(parser.results)} commands from Fibonacci example")
        
        # Count command types
        command_counts = {}
        for vmc, result in parser.results:
            cmd = vmc.command
            command_counts[cmd] = command_counts.get(cmd, 0) + 1
        
        print("Command counts:")
        for cmd, count in sorted(command_counts.items()):
            print(f"  {cmd}: {count}")
        
        # Check that functions were registered
        emitter = parser.emitter
        if hasattr(emitter.net, 'functions'):
            print(f"Functions registered: {list(emitter.net.functions.keys())}")
        
        print(f"Final control stack size: {len(emitter.control_stack)}")
        print(f"Total places: {len(emitter.net.places)}")
        print(f"Total transitions: {len(emitter.net.transitions)}")
        
        return True
        
    except Exception as e:
        print(f"Error during Fibonacci parsing: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run integration tests"""
    print("Testing VMParser integration with function/call/return")
    print("=" * 60)
    
    try:
        success1 = test_simple_function_parsing()
        success2 = test_fibonacci_example()
        
        if success1 and success2:
            print("\n" + "=" * 60)
            print("All integration tests completed successfully!")
            return True
        else:
            print("\n" + "=" * 60)
            print("Some tests failed!")
            return False
        
    except Exception as e:
        print(f"\nIntegration test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)