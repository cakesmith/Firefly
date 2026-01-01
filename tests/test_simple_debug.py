#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser
from Petri.Token import Token

def test_simple_add():
    """Test SimpleAdd case with debugging"""
    
    print("Testing SimpleAdd with debugging...")
    
    # Get the correct path relative to the test file
    test_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(test_dir)
    vm_path = os.path.join(project_dir, "tecs", "projects", "07", "StackArithmetic", "SimpleAdd")
    
    # Check if path exists
    if not os.path.exists(vm_path):
        print(f"Skipping test - path not found: {vm_path}")
        return True  # Skip but don't fail
    
    # Parse the SimpleAdd VM code
    parser = VMParser(vm_path)
    emitter = parser.emitter
    
    print(f"Parsed {len(parser.results)} commands")
    print(f"Generated {len(emitter.net.places)} places, {len(emitter.net.transitions)} transitions")
    
    # Allocate memory
    slots_used = emitter.net.allocate_memory()
    print(f"Memory allocated: {slots_used} slots")
    
    # Show places with memory addresses
    print("\nPlaces with memory addresses:")
    for place_name, place in emitter.net.places.items():
        if hasattr(place, 'memory_address') and place.memory_address is not None:
            print(f"  {place_name}: R{place.memory_address}")
    
    # Initialize and execute
    if "init" in emitter.net.places:
        emitter.net.places["init"].put_token(Token("start"))
    
    print("\nExecuting Petri net...")
    execution_steps = 0
    max_steps = 10
    
    while execution_steps < max_steps:
        # Find enabled transitions
        enabled = []
        for transition in emitter.net.transitions.values():
            if transition.can_fire():
                enabled.append(transition)
        
        if not enabled:
            print(f"No enabled transitions after {execution_steps} steps")
            break
            
        # Fire one enabled transition
        transition = enabled[0]
        print(f"  Step {execution_steps + 1}: Firing {transition.name}")
        
        # Show input tokens
        input_tokens = []
        for place in transition.in_places:
            if place.has and place.token:
                input_tokens.append(place.token)
        print(f"    Input tokens: {[str(t) for t in input_tokens]}")
        
        transition.fire()
        
        # Show output tokens
        for place in transition.out_places:
            if place.has and place.token:
                print(f"    Output to {place.name}: {place.token}")
        
        execution_steps += 1
    
    print(f"\nExecution completed after {execution_steps} steps")
    
    # Show final state
    print("\nFinal place states:")
    for place_name, place in emitter.net.places.items():
        if place.has and place.token:
            print(f"  {place_name}: {place.token}")
            if hasattr(place, 'memory_address') and place.memory_address is not None:
                print(f"    -> Memory address R{place.memory_address}")

if __name__ == "__main__":
    test_simple_add()