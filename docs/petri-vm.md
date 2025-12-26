# Petri-Net Native Virtual Machine

## Overview

A breakthrough VM implementation that executes as a pure Petri net - no stack abstraction, no hidden program counter. The network structure IS the program.

## Core Innovation: Stack-Free Architecture

**Traditional VM**: `Stack: [7, 8] → add → Stack: [15]` (hidden state)  
**Petri-Net VM**: `Places: {const_7: 7, const_8: 8} → add_transition → {add_result: 15}` (visible state)

### Key Insight
- **Places ARE the data flow** - each value is its own place
- **Network structure IS the program** - control flow is token flow  
- **All state is visible** - no hidden execution context

## Six Primitives

1. **source** - `push constant` creates places with values
2. **join** - arithmetic/logical operations consuming multiple inputs
3. **dup** - explicit token duplication
4. **drop** - explicit token discard
5. **choice** - branching (future)
6. **loop** - iteration (future)

## Implementation

### VM Operations → Petri Net Translation
```python
# push constant 7
place_7 = self.net.add_place("const_7", 7)
self.result_places.append(place_7)

# add operation  
place_a = self.result_places.pop()  # consume operands
place_b = self.result_places.pop()
add_trans = self.net.add_transition("add")
result_place = self.net.add_place("add_result")
self.net.add_arc(place_a, add_trans)
self.net.add_arc(place_b, add_trans) 
self.net.add_arc(add_trans, result_place)
self.result_places.append(result_place)
```

### Supported Operations
- **Stack**: `push constant`
- **Arithmetic**: `add`, `sub`, `neg`
- **Logic**: `eq`, `lt`, `gt`, `and`, `or`, `not`

## Memory Optimization

### Reachability Analysis
- Analyzes place lifetimes (birth/death points)
- Identifies non-overlapping lifetimes for memory reuse
- Uses interval graph coloring for optimal allocation

### Results
```
SimpleAdd.vm: 4 places → 4 memory locations (1.00x reuse)
StackTest.vm: 20 places → 20 memory locations (1.00x reuse)
```
*Sequential operations prevent reuse in current tests*

## Multi-Core Assembly Generation

### Dependency Analysis
- Builds operation dependency graph
- Identifies parallelizable operations
- Assigns operations to cores via round-robin

### Generated Assembly Features
- Core synchronization with status flags
- Level-based execution respecting dependencies  
- Memory-optimized addressing using place analysis
- Load balancing across available cores

## Test Results

### SimpleAdd.vm (7 + 8 = 15)
```
Network: 3 places, 1 transition, 3 arcs
Result: [15] ✅
Assembly: Single-core optimized
```

### StackTest.vm (Complex operations)
```
Network: 20 places, 8 transitions, 23 arcs  
Result: [-1, 0, -1, 90] ✅
Assembly: 4-core parallel execution
```

## Architecture Benefits

1. **Structural Correctness** - Impossible to have hidden state bugs
2. **Natural Concurrency** - Multiple tokens flow simultaneously
3. **Formal Analysis** - Standard Petri-net tools apply directly
4. **Memory Optimization** - Place lifetime analysis enables reuse
5. **Multi-Core Generation** - Automatic parallelization from structure
6. **Visual Programming** - Network can be edited graphically

## Files

- `PetriMachine.py` - Main VM implementation
- `test_petri_net_vm.py` - Comprehensive test suite for all VM capabilities
- `run_tests.py` - Test runner with filtering options
- `petri_vm_summary.md` - Original implementation notes
- `STACKFREE_BREAKTHROUGH.md` - Architecture breakthrough documentation
- `IMPLEMENTATION_SUMMARY.md` - Detailed technical summary

## Testing

Run all tests:
```bash
python3 test_petri_net_vm.py
# or
python3 run_tests.py
```

Run specific test categories:
```bash
python3 run_tests.py basic      # VM operations only
python3 run_tests.py assembly   # Assembly generation only  
python3 run_tests.py complex    # Complex operations only
```

All test results are organized in the `test_results/` folder:
- `simple_add_single.asm` - Single-core assembly output
- `multicore_2cores/` - 2-core ROM files and coordination
- `multicore_4cores/` - 4-core ROM files and coordination

Each multicore folder contains:
- `core0.asm` to `coreN.asm` - Individual ROM files for each core
- `shared_init.asm` - Shared memory initialization
- `coordination.md` - Multi-core coordination protocol documentation

## Future Work

- Memory segments (`local`, `argument`, `static`, `temp`)
- Control flow (`label`, `goto`, `if-goto`) 
- Function calls (`function`, `call`, `return`)
- Hardware compilation to dataflow architectures
- Distributed execution across nodes