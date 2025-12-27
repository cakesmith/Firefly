#!/usr/bin/env python3
"""
Test Bounded Net Growth for Level-Based Recursion
Verifies that the Petri net doesn't grow unbounded with recursive calls
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from Petri.VMToPetri import VMToPetriTranslator

def test_bounded_net_growth_deep_recursion():
    """
    Test that deep recursion doesn't cause unbounded net growth
    This would fail if we created new subnets for each recursive call
    """
    print("=== Testing Bounded Net Growth with Deep Recursion ===")
    
    # Define a deeply recursive function
    commands = [
        # function deep_recurse 0
        ("function", "deep_recurse", 0),
        ("push", "argument", 0),        # push n
        ("push", "constant", 0),        # push 0
        ("eq",),                        # n == 0?
        ("if-goto", "BASE_CASE"),       # if n == 0, goto BASE_CASE
        
        # Recursive case: deep_recurse(n-1)
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("sub",),                       # n - 1
        ("call", "deep_recurse", 1),    # deep_recurse(n-1)
        ("return",),
        
        # Base case: return 999
        ("label", "BASE_CASE"),
        ("push", "constant", 999),      # return 999
        ("return",),
        
        # Main program: compute deep_recurse(20) - deep recursion
        ("push", "constant", 20),       # push 20
        ("call", "deep_recurse", 1),    # deep_recurse(20)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        # Measure net size before execution
        initial_places = len(translator.net.places)
        initial_transitions = len(translator.net.transitions)
        
        print(f"Initial net size: {initial_places} places, {initial_transitions} transitions")
        
        result = translator.execute_program(commands)
        
        # Measure net size after execution
        final_places = len(translator.net.places)
        final_transitions = len(translator.net.transitions)
        
        print(f"Final net size: {final_places} places, {final_transitions} transitions")
        print(f"Net growth: +{final_places - initial_places} places, +{final_transitions - initial_transitions} transitions")
        
        # Check result correctness
        if result and len(result) >= 1 and result[-1] == 999:
            print("[PASS] Recursive computation result correct")
        else:
            print(f"[FAIL] Incorrect result: {result}, expected [999]")
            return False
        
        # Key test: Net growth should be bounded, not proportional to recursion depth
        # With 20 levels of recursion, if we created new subnets each time,
        # we'd have roughly 20x the function subnet size
        # With level-based approach, growth should be much smaller
        
        places_growth = final_places - initial_places
        transitions_growth = final_transitions - initial_transitions
        
        # Reasonable bounds: growth should be much less than recursion_depth * function_size
        # A single function with ~10 commands might create ~20-30 places/transitions
        # So 20 levels * 30 = 600 would be unbounded growth
        # Level-based should be much smaller, maybe 50-100 total growth
        
        max_reasonable_places_growth = 100
        max_reasonable_transitions_growth = 100
        
        if places_growth <= max_reasonable_places_growth and transitions_growth <= max_reasonable_transitions_growth:
            print(f"[PASS] Net growth is bounded: {places_growth} places, {transitions_growth} transitions")
            print("[PASS] Level-based recursion prevents unbounded subnet creation")
            return True
        else:
            print(f"[FAIL] Net growth appears unbounded: {places_growth} places, {transitions_growth} transitions")
            print("[FAIL] This suggests new subnets are being created for each recursive call")
            return False
            
    except Exception as e:
        print(f"[FAIL] Error in bounded net growth test: {e}")
        return False

def test_bounded_net_growth_multiple_functions():
    """
    Test that multiple recursive functions share subnets properly
    """
    print("\n=== Testing Bounded Net Growth with Multiple Functions ===")
    
    # Define two recursive functions that call each other
    commands = [
        # function even 0
        ("function", "even", 0),
        ("push", "argument", 0),        # push n
        ("push", "constant", 0),        # push 0
        ("eq",),                        # n == 0?
        ("if-goto", "EVEN_BASE"),       # if n == 0, return true (1)
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("sub",),                       # n - 1
        ("call", "odd", 1),             # odd(n-1)
        ("return",),
        ("label", "EVEN_BASE"),
        ("push", "constant", 1),        # return true
        ("return",),
        
        # function odd 0
        ("function", "odd", 0),
        ("push", "argument", 0),        # push n
        ("push", "constant", 0),        # push 0
        ("eq",),                        # n == 0?
        ("if-goto", "ODD_BASE"),        # if n == 0, return false (0)
        ("push", "argument", 0),        # push n
        ("push", "constant", 1),        # push 1
        ("sub",),                       # n - 1
        ("call", "even", 1),            # even(n-1)
        ("return",),
        ("label", "ODD_BASE"),
        ("push", "constant", 0),        # return false
        ("return",),
        
        # Main program: test even(10)
        ("push", "constant", 10),       # push 10
        ("call", "even", 1),            # even(10) should return 1 (true)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        # Measure net size before execution
        initial_places = len(translator.net.places)
        initial_transitions = len(translator.net.transitions)
        
        print(f"Initial net size: {initial_places} places, {initial_transitions} transitions")
        
        result = translator.execute_program(commands)
        
        # Measure net size after execution
        final_places = len(translator.net.places)
        final_transitions = len(translator.net.transitions)
        
        print(f"Final net size: {final_places} places, {final_transitions} transitions")
        print(f"Net growth: +{final_places - initial_places} places, +{final_transitions - initial_transitions} transitions")
        
        # Check result correctness (10 is even, so should return 1)
        if result and len(result) >= 1 and result[-1] == 1:
            print("[PASS] Mutual recursion result correct")
        else:
            print(f"[FAIL] Incorrect result: {result}, expected [1]")
            return False
        
        # With mutual recursion of depth 10, unbounded growth would create
        # 10 copies of each function subnet = ~20 function subnets
        # Level-based should reuse the same 2 function subnets
        
        places_growth = final_places - initial_places
        transitions_growth = final_transitions - initial_transitions
        
        # Even more conservative bounds for multiple functions
        max_reasonable_places_growth = 150
        max_reasonable_transitions_growth = 150
        
        if places_growth <= max_reasonable_places_growth and transitions_growth <= max_reasonable_transitions_growth:
            print(f"[PASS] Net growth is bounded with multiple functions: {places_growth} places, {transitions_growth} transitions")
            print("[PASS] Level-based recursion shares subnets between functions")
            return True
        else:
            print(f"[FAIL] Net growth appears unbounded with multiple functions: {places_growth} places, {transitions_growth} transitions")
            print("[FAIL] This suggests separate subnets are being created for each call")
            return False
            
    except Exception as e:
        print(f"[FAIL] Error in multiple functions bounded growth test: {e}")
        return False

def test_net_size_analysis():
    """
    Analyze net size growth patterns to understand the implementation
    """
    print("\n=== Net Size Growth Analysis ===")
    
    # Test with increasing recursion depths
    depths = [1, 3, 5, 10]
    growth_data = []
    
    for depth in depths:
        commands = [
            # Simple recursive countdown
            ("function", "countdown", 0),
            ("push", "argument", 0),
            ("push", "constant", 0),
            ("eq",),
            ("if-goto", "BASE"),
            ("push", "argument", 0),
            ("push", "constant", 1),
            ("sub",),
            ("call", "countdown", 1),
            ("return",),
            ("label", "BASE"),
            ("push", "constant", 42),
            ("return",),
            
            # Main program
            ("push", "constant", depth),
            ("call", "countdown", 1),
        ]
        
        translator = VMToPetriTranslator()
        
        try:
            initial_places = len(translator.net.places)
            initial_transitions = len(translator.net.transitions)
            
            result = translator.execute_program(commands)
            
            final_places = len(translator.net.places)
            final_transitions = len(translator.net.transitions)
            
            places_growth = final_places - initial_places
            transitions_growth = final_transitions - initial_transitions
            
            growth_data.append({
                'depth': depth,
                'places_growth': places_growth,
                'transitions_growth': transitions_growth,
                'result_correct': result and len(result) >= 1 and result[-1] == 42
            })
            
            print(f"Depth {depth:2d}: +{places_growth:3d} places, +{transitions_growth:3d} transitions, result: {result}")
            
        except Exception as e:
            print(f"Depth {depth:2d}: ERROR - {e}")
            growth_data.append({
                'depth': depth,
                'places_growth': float('inf'),
                'transitions_growth': float('inf'),
                'result_correct': False
            })
    
    # Analyze growth pattern
    print("\nGrowth Pattern Analysis:")
    
    # Check if growth is linear with depth (bad - indicates unbounded growth)
    # or constant/sublinear (good - indicates bounded growth)
    
    valid_data = [d for d in growth_data if d['result_correct'] and d['places_growth'] != float('inf')]
    
    if len(valid_data) >= 2:
        # Compare growth between smallest and largest depth
        min_data = min(valid_data, key=lambda x: x['depth'])
        max_data = max(valid_data, key=lambda x: x['depth'])
        
        depth_ratio = max_data['depth'] / min_data['depth']
        places_ratio = max_data['places_growth'] / max(min_data['places_growth'], 1)
        transitions_ratio = max_data['transitions_growth'] / max(min_data['transitions_growth'], 1)
        
        print(f"Depth increased by {depth_ratio:.1f}x")
        print(f"Places growth increased by {places_ratio:.1f}x")
        print(f"Transitions growth increased by {transitions_ratio:.1f}x")
        
        # If growth is truly bounded/level-based, the ratios should be much smaller than depth ratio
        if places_ratio <= depth_ratio * 0.5 and transitions_ratio <= depth_ratio * 0.5:
            print("[PASS] Growth appears sublinear - indicates good level-based implementation")
            return True
        else:
            print("[FAIL] Growth appears linear with depth - indicates potential unbounded subnet creation")
            return False
    else:
        print("[FAIL] Insufficient valid data for analysis")
        return False

if __name__ == "__main__":
    print("Testing Bounded Net Growth for Level-Based Recursion")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 0
    
    # Run tests
    total_tests += 1
    if test_bounded_net_growth_deep_recursion():
        tests_passed += 1
    
    total_tests += 1
    if test_bounded_net_growth_multiple_functions():
        tests_passed += 1
        
    total_tests += 1
    if test_net_size_analysis():
        tests_passed += 1
    
    print(f"\n" + "=" * 60)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("SUCCESS: All bounded net growth tests passed!")
        print("PASS: Level-based recursion successfully prevents unbounded subnet creation")
        sys.exit(0)
    else:
        print("WARNING: Some tests failed - potential unbounded growth detected")
        sys.exit(1)