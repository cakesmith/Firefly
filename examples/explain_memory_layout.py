#!/usr/bin/env python3
"""
Demonstrate and explain the Petri net VM memory layout
"""

import sys
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def demonstrate_memory_layout():
    """Show how memory optimization works in practice"""
    print("=" * 60)
    print("PETRI NET VM MEMORY LAYOUT DEMONSTRATION")
    print("=" * 60)
    
    # Simple program: add two numbers
    commands = [
        ("push", "constant", 7),    # Creates const_7 place
        ("push", "constant", 8),    # Creates const_8 place  
        ("add",),                   # Creates add_result place
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print("\n1. PLACES CREATED (Before Optimization)")
    print("-" * 40)
    place_info = translator.get_detailed_place_info()
    for name, info in place_info.items():
        tokens = info['tokens']
        print(f"  {name}: {tokens}")
    
    print(f"\n   Total places: {len(place_info)}")
    
    print("\n2. MEMORY OPTIMIZATION ANALYSIS")
    print("-" * 40)
    memory_map = translator._optimize_memory_allocation()
    
    print("   Place Lifetimes:")
    for place_name in place_info.keys():
        location = memory_map['location_map'][place_name]
        print(f"     {place_name} → @{location}")
    
    print(f"\n   Memory Locations Used:")
    for location, places in memory_map['location_to_places'].items():
        if len(places) > 1:
            print(f"     @{location}: {places} (SHARED)")
        else:
            print(f"     @{location}: {places}")
    
    print(f"\n   Optimization Results:")
    print(f"     Original places: {len(place_info)}")
    print(f"     Memory locations: {len(memory_map['location_to_places'])}")
    print(f"     Memory saved: {len(place_info) - len(memory_map['location_to_places'])} locations")
    
    return result

def demonstrate_function_call_memory():
    """Show memory layout for function calls"""
    print("\n" + "=" * 60)
    print("FUNCTION CALL MEMORY LAYOUT")
    print("=" * 60)
    
    commands = [
        # Define function
        ("function", "Math.add", 0),
        ("push", "argument", 0),        # arg0 place → pushed_arg_0 place
        ("push", "argument", 1),        # arg1 place → pushed_arg_1 place
        ("add",),                       # pushed_arg_0 + pushed_arg_1 → add_result
        ("return",),                    # add_result → caller
        
        # Main program
        ("push", "constant", 5),        # const_5 place
        ("push", "constant", 3),        # const_3 place
        ("call", "Math.add", 2),        # const_5, const_3 → function args
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print("\n1. FUNCTION CALL PLACE FLOW")
    print("-" * 40)
    print("   Main Program:")
    print("     push constant 5  → const_5 place")
    print("     push constant 3  → const_3 place")
    print("     call Math.add 2  → pops const_5, const_3 as arguments")
    print()
    print("   Function Math.add:")
    print("     push argument 0  → duplicates arg0 (const_5) → pushed_arg_0")
    print("     push argument 1  → duplicates arg1 (const_3) → pushed_arg_1") 
    print("     add              → pushed_arg_0 + pushed_arg_1 → add_result")
    print("     return           → add_result → caller's result")
    
    print("\n2. MEMORY OPTIMIZATION FOR FUNCTION CALLS")
    print("-" * 40)
    memory_map = translator._optimize_memory_allocation()
    
    for location, places in memory_map['location_to_places'].items():
        if len(places) > 1:
            print(f"   @{location}: {places} (SHARED - non-overlapping lifetimes)")
        else:
            print(f"   @{location}: {places}")
    
    savings = len(translator.net.places) - len(memory_map['location_to_places'])
    percent = (savings / len(translator.net.places)) * 100 if translator.net.places else 0
    print(f"\n   Memory Reduction: {savings} locations ({percent:.1f}%)")
    
    return result

def explain_multi_core_memory():
    """Explain multi-core memory layout"""
    print("\n" + "=" * 60)
    print("MULTI-CORE MEMORY LAYOUT")
    print("=" * 60)
    
    print("""
MEMORY REGIONS:
┌─────────────────────────────────────────────────────────┐
│ @0-15:   System Registers (SP, LCL, ARG, THIS, THAT)   │
│          - Standard VM compatibility                     │
│          - Used by generated assembly code              │
├─────────────────────────────────────────────────────────┤
│ @16-31:  Core Status Flags                             │
│          - @16+core_id: Core status (0=idle, 1=work,   │
│            2=done)                                      │
│          - Used for multi-core coordination             │
├─────────────────────────────────────────────────────────┤
│ @32-47:  Core Synchronization Area                     │
│          - @32+level: Synchronization bits for         │
│            execution level                              │
│          - Barrier synchronization between cores       │
├─────────────────────────────────────────────────────────┤
│ @256+:   Optimized Place Memory                        │
│          - Each Petri net place gets a memory location │
│          - Optimized using lifetime analysis           │
│          - Places with non-overlapping lifetimes share │
│            memory locations                             │
├─────────────────────────────────────────────────────────┤
│ @512+:   Shared Results Area                           │
│          - Final program results                        │
│          - Stack pointer moved here in multi-core      │
└─────────────────────────────────────────────────────────┘

PLACE LIFETIME OPTIMIZATION:
- Each place has a "birth" time (when created) and "death" time (when consumed)
- Places with non-overlapping lifetimes can share the same memory location
- This is solved using interval graph coloring algorithm
- Example: const_5 (birth=0, death=2) can share memory with add_result (birth=3, death=∞)
""")

def show_memory_reuse_example():
    """Show a concrete example of memory reuse"""
    print("\n" + "=" * 60)
    print("MEMORY REUSE EXAMPLE")
    print("=" * 60)
    
    print("""
PROGRAM: push 7, push 8, add

EXECUTION TIMELINE:
Time 0: push constant 7
  - Creates const_7 place @256
  - Token(7) → const_7

Time 1: push constant 8  
  - Creates const_8 place @257
  - Token(8) → const_8

Time 2: add
  - Creates add_result place @258
  - Consumes Token(7) from const_7, Token(8) from const_8
  - Produces Token(15) → add_result
  - const_7 and const_8 places are now empty (dead)

MEMORY OPTIMIZATION:
- const_7: lifetime (0, 2) - dies at time 2
- const_8: lifetime (1, 2) - dies at time 2  
- add_result: lifetime (2, ∞) - lives forever (final result)

OPTIMIZATION RESULT:
- const_7 gets @256
- const_8 and add_result can share @257 because:
  - const_8 dies at time 2
  - add_result is born at time 2
  - No overlap!

MEMORY LAYOUT:
@256: const_7 (time 0-2)
@257: const_8 (time 1-2) → add_result (time 2-∞)

SAVINGS: 3 places → 2 memory locations (33% reduction)
""")

if __name__ == "__main__":
    # Run demonstrations
    result1 = demonstrate_memory_layout()
    print(f"\nResult: {result1}")
    
    result2 = demonstrate_function_call_memory()
    print(f"\nResult: {result2}")
    
    explain_multi_core_memory()
    show_memory_reuse_example()
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print("""
1. NO TRADITIONAL STACK: Values exist as tokens in Petri net places
2. STRUCTURAL MEMORY: Memory layout reflects program structure, not execution order
3. LIFETIME OPTIMIZATION: Memory reuse based on formal place lifetime analysis
4. MULTI-CORE READY: Memory layout supports parallel execution with synchronization
5. ASSEMBLY GENERATION: Optimized memory locations used in generated assembly code

This approach enables:
- Formal verification of memory usage
- Automatic parallelization opportunities
- Optimal memory allocation
- Clear separation between computation and storage
""")