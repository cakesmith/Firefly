#!/usr/bin/env python3
"""Test that static variables are properly scoped by class."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PetriEmitter import PetriEmitter

def test_static_scoping():
    emitter = PetriEmitter()
    
    # Simulate Screen.init setting static 1
    emitter.current_function = "Screen.init"
    screen_addr = emitter._get_static_address(1)
    print(f"Screen.static[1] -> RAM[{screen_addr}]")
    
    # Simulate Output.init setting static 1
    emitter.current_function = "Output.init"
    output_addr = emitter._get_static_address(1)
    print(f"Output.static[1] -> RAM[{output_addr}]")
    
    # Simulate Math.init setting static 1
    emitter.current_function = "Math.init"
    math_addr = emitter._get_static_address(1)
    print(f"Math.static[1] -> RAM[{math_addr}]")
    
    # Go back to Screen and verify same address
    emitter.current_function = "Screen.drawPixel"
    screen_addr2 = emitter._get_static_address(1)
    print(f"Screen.static[1] (again) -> RAM[{screen_addr2}]")
    
    # Verify they're all different
    assert screen_addr != output_addr, "Screen and Output should have different addresses!"
    assert screen_addr != math_addr, "Screen and Math should have different addresses!"
    assert output_addr != math_addr, "Output and Math should have different addresses!"
    assert screen_addr == screen_addr2, "Same class should get same address!"
    
    print("\nAll static variables properly scoped by class!")
    print(f"Static var map: {emitter.static_vars}")

if __name__ == "__main__":
    test_static_scoping()
