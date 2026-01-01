#!/usr/bin/env python3

"""
Test script for function/call/return implementation in PetriEmitter
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser, vmcommand
from PetriEmitter import PetriEmitter

def test_simple_function():
    """Test a simple function definition"""
    print("Testing simple function definition...")
    
    emitter = PetriEmitter()
    
    # Test function command
    func_cmd = vmcommand('function', 'SimpleFunction.test', 2)
    result = emitter.function(func_cmd)
    
    print(f"Function transition created: {result.name}")
    print(f"Control stack size: {len(emitter.control_stack)}")
    
    # Test that function was registered
    if hasattr(emitter.net, 'functions'):
        print(f"Functions registered: {list(emitter.net.functions.keys())}")
    
    return True

def test_function_call():
    """Test a function call"""
    print("\nTesting function call...")
    
    emitter = PetriEmitter()
    
    # First push some arguments
    push_cmd1 = vmcommand('push', 'constant', 7)
    push_cmd2 = vmcommand('push', 'constant', 13)
    emitter.push_constant(push_cmd1)
    emitter.push_constant(push_cmd2)
    
    print(f"Stack size after pushing args: {len(emitter.control_stack)}")
    
    # Test call command
    call_cmd = vmcommand('call', 'SimpleFunction.test', 2)
    result = emitter.call(call_cmd)
    
    print(f"Call transition created: {result.name}")
    print(f"Control stack size after call: {len(emitter.control_stack)}")
    
    return True

def test_return():
    """Test return command"""
    print("\nTesting return...")
    
    emitter = PetriEmitter()
    
    # Push a return value
    push_cmd = vmcommand('push', 'constant', 42)
    emitter.push_constant(push_cmd)
    
    print(f"Stack size before return: {len(emitter.control_stack)}")
    
    # Test return command
    ret_cmd = vmcommand('return')
    result = emitter.ret(ret_cmd)
    
    print(f"Return transition created: {result.name}")
    print(f"Control stack size after return: {len(emitter.control_stack)}")
    
    return True

def test_memory_segments():
    """Test memory segment operations"""
    print("\nTesting memory segments...")
    
    emitter = PetriEmitter()
    
    # Test push local
    push_local_cmd = vmcommand('push', 'local', 0)
    result = emitter.push_local(push_local_cmd)
    print(f"Push local transition: {result.name}")
    
    # Test push argument
    push_arg_cmd = vmcommand('push', 'argument', 1)
    result = emitter.push_argument(push_arg_cmd)
    print(f"Push argument transition: {result.name}")
    
    # Test push this
    push_this_cmd = vmcommand('push', 'this', 2)
    result = emitter.push_this(push_this_cmd)
    print(f"Push this transition: {result.name}")
    
    # Test push that
    push_that_cmd = vmcommand('push', 'that', 3)
    result = emitter.push_that(push_that_cmd)
    print(f"Push that transition: {result.name}")
    
    # Test push pointer
    push_ptr_cmd = vmcommand('push', 'pointer', 0)
    result = emitter.push_pointer(push_ptr_cmd)
    print(f"Push pointer transition: {result.name}")
    
    # Test push temp
    push_temp_cmd = vmcommand('push', 'temp', 5)
    result = emitter.push_temp(push_temp_cmd)
    print(f"Push temp transition: {result.name}")
    
    # Test push static
    push_static_cmd = vmcommand('push', 'static', 0)
    result = emitter.push_static(push_static_cmd)
    print(f"Push static transition: {result.name}")
    
    print(f"Stack size after all pushes: {len(emitter.control_stack)}")
    
    # Test pop operations
    pop_local_cmd = vmcommand('pop', 'local', 0)
    result = emitter.pop_local(pop_local_cmd)
    print(f"Pop local transition: {result.name}")
    
    pop_temp_cmd = vmcommand('pop', 'temp', 1)
    result = emitter.pop_temp(pop_temp_cmd)
    print(f"Pop temp transition: {result.name}")
    
    print(f"Stack size after pops: {len(emitter.control_stack)}")
    
    return True

def main():
    """Run all tests"""
    print("Testing PetriEmitter function/call/return implementation")
    print("=" * 60)
    
    try:
        test_simple_function()
        test_function_call()
        test_return()
        test_memory_segments()
        
        print("\n" + "=" * 60)
        print("All tests completed successfully!")
        
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)