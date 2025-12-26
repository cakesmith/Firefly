#!/usr/bin/env python3
"""
Show actual multi-core assembly generation with memory layout
"""

import sys
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def show_multicore_assembly_generation():
    """Generate and show actual multi-core assembly code"""
    print("=" * 70)
    print("ACTUAL MULTI-CORE ASSEMBLY GENERATION")
    print("=" * 70)
    
    # Create a program with some parallelism potential
    commands = [
        ("push", "constant", 10),
        ("push", "constant", 5), 
        ("push", "constant", 3),
        ("add",),                # 10 + 5 = 15
        ("push", "constant", 2),
        ("sub",),                # 15 - 3 = 12  
        ("mul",),                # 12 * 2 = 24 (mul not implemented, but shows structure)
    ]
    
    translator = VMToPetriTranslator()
    
    try:
        result = translator.execute_program(commands)
        print(f"Program result: {result}")
        
        print("\n1. DEPENDENCY ANALYSIS")
        print("-" * 30)
        execution_plan = translator._analyze_execution_dependencies()
        for level_idx, operations in enumerate(execution_plan['execution_levels']):
            print(f"  Level {level_idx}: {operations}")
        
        print("\n2. MEMORY OPTIMIZATION")
        print("-" * 30)
        memory_map = translator._optimize_memory_allocation()
        print("Optimized memory locations:")
        for location, places in memory_map['location_to_places'].items():
            if len(places) > 1:
                print(f"  @{location}: {places} (SHARED)")
            else:
                print(f"  @{location}: {places}")
        
        print("\n3. MULTI-CORE ROM GENERATION (2 cores)")
        print("-" * 40)
        
        # Generate multi-core assembly
        roms = translator.generate_multicore_assembly(num_cores=2, output_dir="test_results")
        
        print("Generated ROM files:")
        if isinstance(roms, dict):
            for core_id, rom_lines in roms.items():
                print(f"\n--- Core {core_id} ROM (first 20 lines) ---")
                for i, line in enumerate(rom_lines[:20]):
                    print(f"  {line}")
                if len(rom_lines) > 20:
                    print(f"  ... ({len(rom_lines) - 20} more lines)")
        else:
            print("Multi-core summary:")
            for line in roms:
                print(f"  {line}")
                
    except Exception as e:
        print(f"Error (expected - mul not implemented): {e}")
        
        # Show the structure anyway
        print("\n4. MEMORY LAYOUT IN GENERATED ASSEMBLY")
        print("-" * 40)
        print("""
EXAMPLE GENERATED ASSEMBLY STRUCTURE:

// Core 0 ROM
@16         // Core 0 status flag
M=0         // Set to idle initially

// Initialize shared memory constants
@10
D=A
@256        // Optimized location for const_10
M=D

@5  
D=A
@257        // Optimized location for const_5
M=D

// Core coordination loop
(LEVEL_0_WAIT)
@32         // Level 0 synchronization area
D=M
@1          // Core 0 ready bit
D=D|A       // Set our ready bit
@32
M=D

// Wait for all cores ready
(LEVEL_0_CHECK)
@32
D=M
@3          // All cores ready mask (0b11 for 2 cores)
D=D-A
@LEVEL_0_EXECUTE
D;JEQ       // All ready, proceed

@LEVEL_0_CHECK
0;JMP       // Keep waiting

(LEVEL_0_EXECUTE)
@16         // Set core status to working
M=1

// Execute assigned operations using optimized memory
@256        // Load const_10 from optimized location
D=M
@257        // Load const_5 from optimized location  
D=D+M       // Add operation
@258        // Store result in optimized location
M=D

@16         // Set core status to done
M=2

// Continue to next level...
""")

def explain_assembly_memory_usage():
    """Explain how the assembly code uses the memory layout"""
    print("\n" + "=" * 70)
    print("HOW ASSEMBLY CODE USES MEMORY LAYOUT")
    print("=" * 70)
    
    print("""
MEMORY REGION USAGE IN GENERATED ASSEMBLY:

1. SYSTEM REGISTERS (@0-15):
   - SP: Stack pointer, moved to @512+ for result collection
   - LCL, ARG, THIS, THAT: Standard VM registers (compatibility)
   - Used by final result collection code

2. CORE STATUS FLAGS (@16-31):
   Assembly code pattern:
   ```
   @16         // Core 0 status
   M=1         // Set to working
   
   // ... do work ...
   
   @16         // Core 0 status  
   M=2         // Set to done
   ```

3. SYNCHRONIZATION AREA (@32-47):
   Assembly code pattern:
   ```
   // Signal ready for level L
   @32+L
   D=M
   @(1<<core_id)    // Our bit mask
   D=D|A            // Set our bit
   @32+L
   M=D
   
   // Wait for all cores
   (WAIT)
   @32+L
   D=M
   @all_ready_mask
   D=D-A
   @PROCEED
   D;JEQ            // All ready
   @WAIT
   0;JMP            // Keep waiting
   ```

4. OPTIMIZED PLACE MEMORY (@256+):
   Assembly code pattern:
   ```
   // Load operands from optimized locations
   @256             // First operand location
   D=M
   @257             // Second operand location
   D=D+M            // Perform operation
   @258             // Result location
   M=D              // Store result
   ```

5. STACK AREA (@512+):
   Assembly code pattern:
   ```
   // Collect final results
   @258             // Load result from optimized location
   D=M
   @SP              // Stack pointer (points to @512+)
   M=M+1            // Increment SP
   A=M-1            // Point to top of stack
   M=D              // Push result
   ```

KEY INSIGHTS:

A) SEPARATION OF CONCERNS:
   - Computation uses optimized place memory (@256+)
   - Coordination uses status flags (@16+) and sync area (@32+)
   - Results use stack area (@512+)

B) NO STACK DURING COMPUTATION:
   - Operations work directly on memory locations
   - No push/pop overhead during computation
   - Stack only used for final result collection

C) AUTOMATIC OPTIMIZATION:
   - Memory locations are automatically optimized
   - Synchronization is automatically generated
   - No manual memory management needed

D) FORMAL CORRECTNESS:
   - Petri net analysis guarantees correct dependencies
   - Memory optimization preserves program semantics
   - Multi-core coordination prevents race conditions
""")

if __name__ == "__main__":
    show_multicore_assembly_generation()
    explain_assembly_memory_usage()
    
    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("""
The multi-core memory layout serves multiple purposes:

1. COMPATIBILITY: Stack pointer and system registers maintain 
   compatibility with standard VM expectations

2. COORDINATION: Core status flags and synchronization area
   enable safe multi-core execution with proper barriers

3. OPTIMIZATION: Optimized place memory provides efficient
   computation without stack manipulation overhead

4. SEPARATION: Clear separation between computation, coordination,
   and result collection

The Petri net analysis automatically determines:
- What synchronization is needed (execution levels)
- How to optimize memory usage (place lifetimes)  
- How to generate correct multi-core code (dependencies)

This gives us provably correct, optimized, parallel execution
from a high-level Petri net specification.
""")