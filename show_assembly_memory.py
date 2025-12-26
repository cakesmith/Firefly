#!/usr/bin/env python3
"""
Show how the memory layout translates to assembly code
"""

import sys
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def show_assembly_generation():
    """Demonstrate assembly generation with memory optimization"""
    print("=" * 60)
    print("ASSEMBLY GENERATION WITH MEMORY OPTIMIZATION")
    print("=" * 60)
    
    # Simple program
    commands = [
        ("push", "constant", 7),
        ("push", "constant", 8), 
        ("add",),
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print("\n1. PETRI NET ANALYSIS")
    print("-" * 30)
    print("Places created:")
    place_info = translator.get_detailed_place_info()
    for name, info in place_info.items():
        print(f"  {name}: tokens={info['tokens']}")
    
    print("\n2. MEMORY OPTIMIZATION")
    print("-" * 30)
    memory_map = translator._optimize_memory_allocation()
    print("Memory allocation:")
    for place_name, location in memory_map['location_map'].items():
        print(f"  {place_name} → @{location}")
    
    print("\n3. GENERATED ASSEMBLY CODE")
    print("-" * 30)
    
    # Generate assembly for single core
    execution_plan = translator._analyze_execution_dependencies()
    core_assignments = translator._assign_operations_to_cores(execution_plan, 1)
    assembly = translator._generate_single_core_assembly(core_assignments[0], memory_map)
    
    print("Generated assembly:")
    for line in assembly:
        print(f"  {line}")
    
    return result

def show_function_call_assembly():
    """Show assembly generation for function calls"""
    print("\n" + "=" * 60)
    print("FUNCTION CALL ASSEMBLY GENERATION")
    print("=" * 60)
    
    commands = [
        ("function", "Math.add", 0),
        ("push", "argument", 0),
        ("push", "argument", 1),
        ("add",),
        ("return",),
        
        ("push", "constant", 5),
        ("push", "constant", 3),
        ("call", "Math.add", 2),
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print("\n1. MEMORY OPTIMIZATION FOR FUNCTION CALLS")
    print("-" * 45)
    memory_map = translator._optimize_memory_allocation()
    
    print("Optimized memory layout:")
    for location, places in memory_map['location_to_places'].items():
        if len(places) > 1:
            print(f"  @{location}: {places} (SHARED)")
        else:
            print(f"  @{location}: {places}")
    
    print(f"\nMemory efficiency:")
    original = len(translator.net.places)
    optimized = len(memory_map['location_to_places'])
    savings = original - optimized
    percent = (savings / original) * 100 if original > 0 else 0
    print(f"  Original places: {original}")
    print(f"  Memory locations: {optimized}")
    print(f"  Savings: {savings} locations ({percent:.1f}%)")
    
    print("\n2. HOW ASSEMBLY USES OPTIMIZED MEMORY")
    print("-" * 40)
    print("""
The generated assembly code uses the optimized memory locations:

For function calls:
1. Constants are pre-loaded into optimized locations
2. Function arguments are accessed from their memory locations  
3. Operations work directly on memory locations (no stack manipulation)
4. Results are stored in optimized locations
5. Return values are moved to caller's result area

Example assembly pattern:
  // Initialize constants
  @5
  D=A
  @256        // Optimized location for const_5
  M=D
  
  // Function call (simplified)
  @256        // Load first argument from optimized location
  D=M
  @257        // Load second argument from optimized location
  D=D+M       // Add directly
  @258        // Store result in optimized location
  M=D
""")
    
    return result

if __name__ == "__main__":
    result1 = show_assembly_generation()
    print(f"\nResult: {result1}")
    
    result2 = show_function_call_assembly()
    print(f"\nResult: {result2}")
    
    print("\n" + "=" * 60)
    print("MEMORY LAYOUT SUMMARY")
    print("=" * 60)
    print("""
TRADITIONAL VM MEMORY MODEL:
- Stack-based execution
- Values pushed/popped from stack
- Memory addresses for stack, heap, static
- Function calls use stack frames

PETRI NET VM MEMORY MODEL:
- Place-based execution  
- Values exist as tokens in places
- Memory addresses for optimized places
- Function calls use place passing

ADVANTAGES OF PETRI NET MODEL:
1. FORMAL ANALYSIS: Can prove memory usage properties
2. OPTIMIZATION: Lifetime analysis enables optimal memory reuse
3. PARALLELIZATION: Clear data dependencies for multi-core
4. VERIFICATION: Can verify correctness of memory optimization
5. EFFICIENCY: No stack manipulation overhead

MEMORY REGIONS:
@0-15:   System compatibility registers
@16-31:  Multi-core coordination  
@32-47:  Synchronization barriers
@256+:   Optimized Petri net places
@512+:   Final results collection

The key insight: Memory layout reflects the STRUCTURE of computation,
not just the SEQUENCE of execution.
""")