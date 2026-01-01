#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from VMParser import VMParser
from Petri.Token import Token

def execute_petri_net_conceptual(net):
    """Execute Petri net conceptual simulation"""
    
    print("  Executing conceptual VM simulation...")
    
    # First allocate memory addresses to places
    net.allocate_memory()
    
    # Initialize tokens in init place
    if "init" in net.places:
        net.places["init"].put_token(Token("start"))
    
    execution_steps = 0
    max_steps = 1000
    
    while execution_steps < max_steps:
        # Find enabled transitions
        enabled = []
        for transition in net.transitions.values():
            if transition.can_fire():
                enabled.append(transition)
        
        if not enabled:
            break
            
        # Fire one enabled transition (deterministic order)
        transition = enabled[0]
        transition.fire()
        execution_steps += 1
    
    print(f"    Executed {execution_steps} steps")
    
    # Extract computed values from places with tokens
    computed_values = {}
    
    # Map places with computed values to memory addresses
    for place_name, place in net.places.items():
        if place.has and place.token and hasattr(place.token, 'value'):
            if isinstance(place.token.value, (int, float)):
                print(f"    Place {place_name}: {place.token.value}")
                # Map to standard VM memory locations
                if "add_result" in place_name or "result" in place_name:
                    computed_values[256] = place.token.value  # Main result location
    
    print(f"    Computed values: {computed_values}")
    
    return computed_values

def test_simple_add():
    """Test SimpleAdd conceptual execution"""
    
    print("Testing SimpleAdd conceptual execution...")
    
    # Parse the SimpleAdd VM code
    parser = VMParser("../tecs/projects/07/StackArithmetic/SimpleAdd")
    emitter = parser.emitter
    
    print(f"Parsed {len(parser.results)} commands")
    
    # Execute conceptual simulation
    result = execute_petri_net_conceptual(emitter.net)
    
    # Expected: {256: 15} (7 + 8 = 15)
    expected = {256: 15}
    
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    
    if result == expected:
        print("✅ PASS - Conceptual execution correct!")
        return True
    else:
        print("❌ FAIL - Conceptual execution incorrect")
        return False

if __name__ == "__main__":
    test_simple_add()