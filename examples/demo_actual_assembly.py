#!/usr/bin/env python3
"""
Generate and show actual assembly files to demonstrate memory layout
"""

import sys
import os
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def generate_actual_assembly_files():
    """Generate real assembly files and show their content"""
    print("=" * 70)
    print("GENERATING ACTUAL ASSEMBLY FILES")
    print("=" * 70)
    
    # Simple program that will generate multi-core assembly
    commands = [
        ("push", "constant", 10),
        ("push", "constant", 5),
        ("add",),
        ("push", "constant", 3),
        ("sub",),  # (10 + 5) - 3 = 12
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Program result: {result}")
    
    print("\n1. SINGLE-CORE ASSEMBLY GENERATION")
    print("-" * 40)
    
    # Generate single-core assembly
    execution_plan = translator._analyze_execution_dependencies()
    core_assignments = translator._assign_operations_to_cores(execution_plan, 1)
    memory_map = translator._optimize_memory_allocation()
    
    single_core_assembly = translator._generate_core_rom(0, core_assignments[0], memory_map, 1)
    
    print("Single-core assembly (showing memory usage):")
    for i, line in enumerate(single_core_assembly):
        print(f"{i+1:2d}: {line}")
        if i > 25:  # Limit output
            print(f"    ... ({len(single_core_assembly) - i - 1} more lines)")
            break
    
    print("\n2. MULTI-CORE ASSEMBLY GENERATION")
    print("-" * 40)
    
    # Generate multi-core assembly files
    roms = translator.generate_multicore_assembly(num_cores=2, output_dir="test_results")
    
    if isinstance(roms, dict):
        print("Multi-core ROM files generated:")
        for core_id, rom_content in roms.items():
            print(f"\n--- Core {core_id} ROM ---")
            for i, line in enumerate(rom_content[:15]):
                print(f"{i+1:2d}: {line}")
            if len(rom_content) > 15:
                print(f"    ... ({len(rom_content) - 15} more lines)")
    
    # Show the actual files created
    print("\n3. GENERATED FILES")
    print("-" * 20)
    
    multicore_dir = "test_results/multicore_2cores"
    if os.path.exists(multicore_dir):
        files = os.listdir(multicore_dir)
        print(f"Files in {multicore_dir}:")
        for file in files:
            file_path = os.path.join(multicore_dir, file)
            file_size = os.path.getsize(file_path)
            print(f"  {file} ({file_size} bytes)")
            
            # Show content of small files
            if file.endswith('.asm') and file_size < 1000:
                print(f"    Content preview:")
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines[:10]):
                        print(f"    {i+1:2d}: {line.rstrip()}")
                    if len(lines) > 10:
                        print(f"        ... ({len(lines) - 10} more lines)")
                print()
    
    return result

def show_memory_layout_in_files():
    """Show how memory layout appears in the generated files"""
    print("\n" + "=" * 70)
    print("MEMORY LAYOUT IN GENERATED FILES")
    print("=" * 70)
    
    print("""
WHAT YOU'LL SEE IN THE GENERATED ASSEMBLY FILES:

1. SHARED_INIT.ASM:
   - Initializes core status flags (@16-31) to 0 (idle)
   - Initializes synchronization area (@32-47) to 0
   - Pre-loads constants into optimized memory locations (@256+)
   - Sets up stack pointer to @512+

2. CORE0.ASM, CORE1.ASM, etc:
   - Core status management (@16+core_id)
   - Synchronization barriers using (@32+level)
   - Operations using optimized memory (@256+)
   - Result collection to stack area (@512+)

3. COORDINATION.MD:
   - Documents the memory layout
   - Explains synchronization protocol
   - Shows core assignments and execution levels

MEMORY ADDRESSES YOU'LL SEE:

@16, @17, @18...    Core status flags
@32, @33, @34...    Level synchronization
@256, @257, @258... Optimized place memory
@512, @513, @514... Stack area for results

ASSEMBLY PATTERNS:

Core Status:
  @16
  M=1              // Set core 0 to working

Synchronization:
  @32
  D=M
  @1               // Core 0 bit
  D=D|A            // Set ready bit
  @32
  M=D

Optimized Memory:
  @256             // Load from optimized location
  D=M
  @257             // Load from another location
  D=D+M            // Compute
  @258             // Store to optimized location
  M=D

Result Collection:
  @258             // Load final result
  D=M
  @SP              // Stack pointer (@512+)
  M=M+1
  A=M-1
  M=D              // Push to stack
""")

if __name__ == "__main__":
    result = generate_actual_assembly_files()
    show_memory_layout_in_files()
    
    print("\n" + "=" * 70)
    print("SUMMARY: MEMORY LAYOUT PURPOSE")
    print("=" * 70)
    print(f"""
FINAL RESULT: {result}

The memory layout serves these purposes:

1. STACK POINTER (@512+):
   - NOT used during Petri net computation
   - ONLY used for final result collection
   - Maintains compatibility with VM standards
   - Provides clean separation from computation memory

2. CORE STATUS FLAGS (@16-31):
   - Enable multi-core coordination
   - Track which cores are idle/working/done
   - Allow completion detection
   - Support debugging and monitoring

3. SYNCHRONIZATION AREA (@32-47):
   - Implement barrier synchronization
   - Ensure correct execution order
   - Respect data dependencies
   - Enable maximum parallelism within constraints

4. OPTIMIZED PLACE MEMORY (@256+):
   - Where actual computation happens
   - Memory locations optimized using lifetime analysis
   - No stack manipulation overhead
   - Direct memory-to-memory operations

This design gives us:
✓ Formal correctness (Petri net analysis)
✓ Memory efficiency (lifetime optimization)  
✓ Parallel execution (automatic multi-core generation)
✓ Standard compatibility (stack-based result format)
""")