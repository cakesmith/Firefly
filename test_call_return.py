#!/usr/bin/env python3
"""
Minimal test for call/return mechanism in Petri net.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PetriEmitter import PetriEmitter
from VMParser import vmcommand

def test_simple_call_return():
    """Test a simple function call and return."""
    print("=" * 60)
    print("Testing simple call/return")
    print("=" * 60)
    
    emitter = PetriEmitter()
    
    # Simulate:
    # function Sys.init 0
    # push constant 5
    # call Test.double 1
    # // result should be 10
    
    # function Test.double 0
    # push argument 0
    # push argument 0
    # add
    # return
    
    # First, define Sys.init (uses init place)
    emitter.function(vmcommand('function', 'Sys.init', 0))
    print(f"After Sys.init: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Push constant 5 (argument for call)
    emitter.push_constant(vmcommand('push', 'constant', 5))
    print(f"After push 5: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Call Test.double with 1 argument
    emitter.call(vmcommand('call', 'Test.double', 1))
    print(f"After call: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    print(f"  Call sites: {emitter.call_sites}")
    
    # Now define Test.double
    emitter.function(vmcommand('function', 'Test.double', 0))
    print(f"After Test.double: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Push argument 0 (the parameter)
    emitter.push_argument(vmcommand('push', 'argument', 0))
    print(f"After push arg 0: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Push argument 0 again
    emitter.push_argument(vmcommand('push', 'argument', 0))
    print(f"After push arg 0 again: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Add
    emitter.add(vmcommand('add'))
    print(f"After add: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Return
    emitter.ret(vmcommand('return'))
    print(f"After return: control_place={emitter.control_place.name if emitter.control_place else None}")
    print(f"  Stack: {[p.name for p in emitter.control_stack]}")
    
    # Finalize
    emitter.finalize()
    print(f"\nFinalized. Dispatch transitions created for: {list(emitter.call_sites.keys())}")
    
    # Print net structure
    print("\n--- Petri Net Structure ---")
    print(f"Places ({len(emitter.net.places)}):")
    for name, place in emitter.net.places.items():
        token_val = place.token.value if place.has and place.token else None
        print(f"  {name}: has={place.has}, token={token_val}")
    
    print(f"\nTransitions ({len(emitter.net.transitions)}):")
    for name, trans in emitter.net.transitions.items():
        in_names = [p.name for p in trans.in_places]
        out_names = [p.name for p in trans.out_places]
        print(f"  {name}: {in_names} -> {out_names}")
    
    # Try to execute
    print("\n--- Execution ---")
    net = emitter.net
    
    for step in range(20):
        enabled = [t for t in net.transitions.values() if t.can_fire()]
        if not enabled:
            print(f"Step {step}: No enabled transitions")
            # Debug: show why transitions can't fire
            for name, t in net.transitions.items():
                in_has = [(p.name, p.has) for p in t.in_places]
                out_has = [(p.name, p.has) for p in t.out_places]
                if not all(p.has for p in t.in_places):
                    missing = [p.name for p in t.in_places if not p.has]
                    print(f"  {name}: missing input tokens in {missing}")
                    # Check if there's a different place with same name that has token
                    for p in t.in_places:
                        if not p.has:
                            net_place = net.places.get(p.name)
                            if net_place and net_place is not p:
                                print(f"    WARNING: {p.name} in transition is different object from net.places!")
                                print(f"      transition.in_place: id={id(p)}, has={p.has}")
                                print(f"      net.places[name]: id={id(net_place)}, has={net_place.has}")
                elif any(p.has for p in t.out_places):
                    blocked = [p.name for p in t.out_places if p.has]
                    print(f"  {name}: output places blocked {blocked}")
            break
        
        for t in enabled:
            print(f"Step {step}: Firing {t.name}")
            # Debug: show input tokens
            in_tokens = [(p.name, p.token.value if p.token else None) for p in t.in_places]
            print(f"  Input tokens: {in_tokens}")
            t.fire()
            # Debug: show output tokens IMMEDIATELY after fire
            for p in t.out_places:
                net_place = net.places.get(p.name)
                same_obj = "SAME" if net_place is p else "DIFFERENT"
                print(f"  Output {p.name}: has={p.has}, token={p.token.value if p.token else None}, obj={same_obj}")
        
        # Show token state
        tokens_state = {name: p.token.value 
                       for name, p in net.places.items() if p.has and p.token}
        print(f"  All tokens after step {step}: {tokens_state}")

if __name__ == "__main__":
    test_simple_call_return()
