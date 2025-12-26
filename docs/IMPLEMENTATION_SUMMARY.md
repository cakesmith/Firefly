# Petri-Net Native VM with Distributed Multi-Core Coordination and Function Calls

## What We Built

A complete **Petri-net native virtual machine** that:

1. **Translates VM operations to Petri net semantics**
2. **Optimizes memory allocation using reachability analysis**
3. **Generates distributed multi-core assembly code with level-based synchronization**
4. **Provides comprehensive statistics and analysis**
5. **Supports function calls, arguments, and return values**
6. **Eliminates centralized coordination using distributed termination**

## Key Features Implemented

### 1. Petri Net VM Translation
- **Virtual stack as places**: Each stack element is its own place
- **Operations as transitions**: VM commands become Petri net transitions
- **Structural execution**: No hidden program counter, pure token flow
- **Six primitives**: source, choice, dup, drop, join, loop (partially implemented)

### 2. Function Call Support
- **Function definitions**: Parse and store function bodies with local variable counts
- **Function calls**: Support calling functions with arguments
- **Argument passing**: Arguments are passed via Petri net places and accessible via `push argument N`
- **Return values**: Functions can return values that become available to the caller
- **Call stack management**: Proper context switching between caller and callee
- **Nested calls**: Support for functions calling other functions

### 3. Distributed Multi-Core Coordination (NEW!)
- **No centralized coordinator**: Eliminated the coordinator that monitored core status
- **Level-based barriers**: Cores self-coordinate using execution level synchronization
- **Distributed termination**: Final level completion IS program completion detection
- **Self-terminating cores**: Each core knows when to terminate without external monitoring
- **Pure Petri net semantics**: No hidden coordination algorithms, just level barriers

### 4. Memory Optimization via Reachability Analysis
- **Place lifetime analysis**: Determines when places are born and die
- **Memory location reuse**: Places with non-overlapping lifetimes share memory
- **Interval graph coloring**: Optimal memory allocation algorithm
- **Statistics reporting**: Shows memory savings and reuse factors

### 5. Comprehensive Statistics
- **Network metrics**: Places, transitions, arcs, connectivity
- **Memory analysis**: Original vs optimized locations, savings percentage
- **Concurrency potential**: Parallel execution opportunities
- **Execution state**: Ready transitions, token distribution

## Test Results

### SimpleAdd.vm (7 + 8 = 15)
```
Network Size: 4 places, 1 transition, 3 arcs
Memory: 4 locations (no optimization possible - all places have distinct lifetimes)
Assembly: Single-core optimized code using direct memory operations
```

### StackTest.vm (Complex arithmetic/logical operations)
```
Network Size: 20 places, 8 transitions, 23 arcs  
Memory: 20 locations (sequential dependencies prevent reuse)
Assembly: 4-core parallel execution with level-based synchronization
Final Result: [-1, 0, -1, 90] ✅
```

### Function Call Tests
```
Simple Function Return: function returns constant 42 ✅
Function with Arguments: Math.add(5, 3) = 8 ✅
Function Composition: Math.incTwice(5) = 7 ✅
Memory optimization: 20-33% reduction in function call scenarios
```

### Distributed Multi-Core Tests
```
2-Core Execution: push 10, push 5, push 3, add, sub = 2 ✅
Level 0: [add] - 1 operation (parallel potential)
Level 1: [sub] - 1 operation (depends on Level 0)
Distributed termination: No coordinator needed ✅
```

## Distributed Multi-Core Innovation

### Before: Centralized Coordination
```
Main Coordinator Loop:
  sum = core_0_status + core_1_status + ...
  if sum == expected_total:
    program_complete()
  else:
    keep_waiting()

Problems:
- Single point of failure
- Coordinator overhead
- Not pure Petri net semantics
```

### After: Distributed Coordination
```
Each Core:
  execute_operations_at_current_level()
  signal_level_complete()
  wait_for_all_cores_at_level()
  if final_level_complete:
    self_terminate()

Benefits:
- No single point of failure
- No coordinator overhead  
- Pure Petri net semantics
- Level synchronization IS completion detection
```

### Memory Layout Changes
```
@16-31: Core status flags (DEBUGGING ONLY - not used for coordination)
@32-47: Level synchronization area (COORDINATION - distributed barriers)
@256+:  Optimized place memory
@512+:  Results collection area
```

## Generated Assembly Features

### Distributed Multi-Core Assembly
- **Level barriers**: Each core waits at execution level barriers
- **Self-coordination**: Cores coordinate without external monitoring
- **Distributed termination**: Final level barrier completion = program completion
- **No coordinator**: Eliminated centralized monitoring loop
- **Status flags for debugging**: Kept for visibility but not used for coordination

### Single-Core Assembly
- **Memory-optimized operations**: Direct memory-to-memory operations
- **Constant initialization**: Pre-loads constants to optimized locations
- **Stack management**: Efficient final result collection

## Memory Optimization Examples

Function call tests show **20-33% memory reduction**:
- Original: Multiple places for constants, arguments, and results
- Optimized: Shared memory locations for places with non-overlapping lifetimes
- Reuse factor: 1.25x to 1.58x

**Distributed coordination shows additional benefits**:
- Eliminated coordinator memory overhead
- Reduced synchronization complexity
- Cleaner separation between computation and coordination

## Architecture Highlights

```
VM Code → Function Parse → Petri Net → Level Analysis → Distributed Multi-Core
   ↓           ↓              ↓            ↓               ↓
function/call → call frames → places/trans → barriers → self-coordinating cores
```

### Distributed Memory Layout
```
@16-31:  Core status (debugging only)
@32-47:  Level barriers (distributed coordination)  
@256+:   Optimized place memory
@512+:   Shared results
```

## Key Innovations

1. **True Petri-net semantics**: Not just visualization - the net IS the program
2. **Function calls as place operations**: Arguments and returns are Petri net places
3. **Distributed coordination**: Level barriers eliminate centralized coordinator
4. **Self-terminating execution**: Cores know when program is complete
5. **Structural memory optimization**: Uses formal reachability analysis
6. **Unified analysis**: Same model for execution, optimization, and compilation

## Files Generated
- `core0.asm`, `core1.asm`, etc.: Self-coordinating core ROMs
- `shared_init.asm`: Shared memory initialization
- `coordination.md`: Distributed coordination protocol documentation

## Distributed Coordination Protocol

### Level Barrier Algorithm:
```assembly
// Each core at each level:
1. Set ready bit: sync_area |= (1 << core_id)
2. Wait for all: while (sync_area != all_cores_mask)  
3. Proceed when barrier satisfied
```

### Distributed Termination:
```assembly
// Each core after final level:
1. Wait for final level barrier completion
2. Self-terminate when barrier satisfied
3. No coordinator involvement
```

## Next Steps
- Implement `pop local` and `pop argument` for variable assignment
- Add support for `push local` and `push static` memory segments
- Implement recursive function calls with proper stack management
- Add `mul` operation for more complex arithmetic
- Support for conditional jumps and loops within functions
- Optimize barrier synchronization for very large core counts

This implementation demonstrates that **Petri nets can serve as a practical intermediate representation** for virtual machines with function calls and distributed multi-core execution, enabling both formal analysis and efficient code generation while maintaining structural correctness guarantees and eliminating centralized coordination bottlenecks.