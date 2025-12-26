# Petri-Net Native VM with Memory Optimization, Multi-Core Assembly Generation, and Function Calls

## What We Built

A complete **Petri-net native virtual machine** that:

1. **Translates VM operations to Petri net semantics**
2. **Optimizes memory allocation using reachability analysis**
3. **Generates multi-core assembly code with synchronization**
4. **Provides comprehensive statistics and analysis**
5. **Supports function calls, arguments, and return values**

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

### 3. Memory Optimization via Reachability Analysis
- **Place lifetime analysis**: Determines when places are born and die
- **Memory location reuse**: Places with non-overlapping lifetimes share memory
- **Interval graph coloring**: Optimal memory allocation algorithm
- **Statistics reporting**: Shows memory savings and reuse factors

### 4. Multi-Core Assembly Generation
- **Dependency analysis**: Identifies parallelizable operations
- **Core assignment**: Load balances operations across cores
- **Memory-optimized code**: Uses optimized memory locations in assembly
- **Synchronization**: Generates core coordination and status tracking

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
Memory optimization: 20% reduction (5 places → 4 locations)
```

## Function Call Implementation

### VM Commands Supported
- `function FunctionName nLocals` - Define a function with local variables
- `call FunctionName nArgs` - Call a function with N arguments from stack
- `return` - Return from function (with optional return value on stack)
- `push argument N` - Access function argument N
- `push local N` - Access local variable N (planned)

### Petri Net Semantics for Functions
1. **Function Definition**: Parse function body and store for later execution
2. **Function Call**: 
   - Pop arguments from result places
   - Create call frame with argument places
   - Execute function body in new context
   - Handle return to restore caller context
3. **Argument Access**: Duplicate argument places to push values onto stack
4. **Return**: Transfer return value back to caller's result places

### Example Function Call Flow
```
Main Program:
  push constant 5      → Creates const_5 place
  push constant 3      → Creates const_3 place  
  call Math.add 2      → Pops args, calls function

Function Math.add:
  push argument 0      → Duplicates first argument (5)
  push argument 1      → Duplicates second argument (3)
  add                  → Creates add_result place (8)
  return               → Returns add_result to caller

Result: [8] ✅
```

## Generated Assembly Features

### Single-Core Assembly
- **Memory-optimized operations**: Direct memory-to-memory operations
- **Constant initialization**: Pre-loads constants to optimized locations
- **Stack management**: Efficient final result collection

### Multi-Core Assembly
- **Core synchronization**: Status flags and coordination loops
- **Level-based execution**: Respects operation dependencies
- **Memory layout**: Organized memory regions for cores, data, and stack
- **Load balancing**: Round-robin operation assignment

## Memory Optimization Examples

Function call test shows **20% memory reduction**:
- Original: 5 places for constants, arguments, and results
- Optimized: 4 memory locations (1 location shared between add_result and pushed_arg_1)
- Reuse factor: 1.25x

**Future optimization opportunities**:
- Loop constructs (reuse iteration variables)
- Complex function calls (reuse parameter/local memory)
- Recursive functions (stack frame optimization)

## Architecture Highlights

```
VM Code → Function Parse → Petri Net → Memory Analysis → Multi-Core Assembly
   ↓           ↓              ↓            ↓               ↓
function/call → call frames → places/trans → @256-275 → core coordination
```

### Memory Layout in Generated Assembly
```
@16-31:  Core status flags
@32-47:  Core communication  
@256+:   Optimized place memory
@512+:   Shared stack
```

## Key Innovations

1. **True Petri-net semantics**: Not just visualization - the net IS the program
2. **Function calls as place operations**: Arguments and returns are Petri net places
3. **Structural memory optimization**: Uses formal reachability analysis
4. **Multi-core code generation**: Automatic parallelization from dependencies
5. **Unified analysis**: Same model for execution, optimization, and compilation

## Files Generated
- `simple_add_single.asm`: Single-core optimized assembly
- `complex_multi.asm`: 2-core parallel assembly  
- `stacktest_4core.asm`: 4-core complex program assembly

## Next Steps
- Implement `pop local` and `pop argument` for variable assignment
- Add support for `push local` and `push static` memory segments
- Implement recursive function calls with proper stack management
- Add `mul` operation for more complex arithmetic
- Support for conditional jumps and loops within functions

This implementation demonstrates that **Petri nets can serve as a practical intermediate representation** for virtual machines with function calls, enabling both formal analysis and efficient code generation while maintaining structural correctness guarantees.