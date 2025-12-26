#!/usr/bin/env python3
"""
Simple test to debug local variable functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Petri.VMToPetri import VMToPetriTranslator

def test_simple_local():
    """Test simple local variable operations"""
    translator = VMToPetriTranslator()
    
    # Simple test: store and retrieve a local variable
    commands = [
        ("push", "constant", 42),
        ("pop", "local", 0),
        ("push", "local", 0)
    ]
    
    # Set up function context manually
    translator.current_function = "test"
    translator.function_locals["test"] = 2
    
    print("Testing simple local operations...")
    
    try:
        # Execute commands one by one
        for i, command in enumerate(commands):
            print(f"Executing command {i}: {command}")
            translator._execute_command(command)
            print(f"Result places after command {i}: {[p.name for p in translator.result_places]}")
        
        # Execute the Petri net
        steps = 0
        max_steps = 10
        while steps < max_steps:
            fired = translator.execute_step()
            if not fired:
                break
            steps += 1
        
        result = translator.get_result_values()
        print(f"Final result: {result}")
        
        return result == [42]
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = test_simple_local()
    if success:
        print("✅ Simple local test PASSED")
    else:
        print("❌ Simple local test FAILED")
    sys.exit(0 if success else 1)