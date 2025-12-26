# Petri-Net Native Virtual Machine Implementation

## What We Built

A **Petri-net native virtual machine** that translates VM stack operations into Petri net semantics, where:

- **Each stack element is a place** in the Petri net
- **Each operation is a transition** that consumes input places and produces output places
- **Control flow is token flow** through the network
- **No hidden program counter** - execution is purely structural

## Key Design Principles

### Virtual Stack as Places
Instead of modeling the stack as a single place with a list token, we use a **virtual stack** where:
- Each stack element is represented by its own place
- Operations pop places from the virtual stack as inputs
- Operations push new result places onto the virtual stack

### Six Petri-Net Primitives
Following the README's constraint of exactly six primitives:

1. **source** - `push constant` creates new places with values
2. **choice** - (not yet implemented, for branching)
3. **dup** - explicit token duplication
4. **drop** - explicit token discard  
5. **join** - arithmetic/logical operations that consume multiple inputs
6. **loop** - (not yet implemented, for iteration)

## Implemented Operations

### Stack Operations
- `push constant N` - Creates a new place with value N, adds to virtual stack

### Arithmetic Operations  
- `add` - Pops two places, creates add transition, pushes result place
- `sub` - Pops two places, creates subtract transition  
- `neg` - Pops one place, creates negation transition

### Logical Operations
- `eq` - Equality comparison (returns -1 for true, 0 for false)
- `lt` - Less than comparison
- `gt` - Greater than comparison  
- `and` - Bitwise AND
- `or` - Bitwise OR
- `not` - Bitwise NOT

## Test Results

### SimpleAdd.vm
```
push constant 7
push constant 8  
add
```
**Result**: `[15]` ✅

### StackTest.vm (Complex Operations)
```
push constant 17, push constant 17, eq,
push constant 892, push constant 891, lt,
push constant 32767, push constant 32766, gt,
push constant 56, push constant 31, push constant 53, add,
push constant 112, sub, neg, and,
push constant 82, or
```
**Result**: `[-1, 0, -1, 90]` ✅

## Architecture

```
VMToPetriTranslator
├── Virtual Stack (list of places)
├── PetriNet
│   ├── Places (each holds tokens with values)
│   ├── Transitions (operations that transform tokens)
│   └── Arcs (connections between places and transitions)
└── Token (carries values through the network)
```

## Key Benefits

1. **Structural Correctness** - Control flow is explicit in the network structure
2. **Concurrency by Construction** - Multiple tokens can flow simultaneously  
3. **No Hidden State** - All execution state is visible in token positions
4. **Analyzable** - The same network can be executed, simulated, or formally verified
5. **Composable** - Operations are modular Petri net fragments

## Next Steps

To complete the VM implementation:

1. **Memory segments** - `push/pop local`, `push/pop argument`, etc.
2. **Control flow** - `label`, `goto`, `if-goto` using choice primitive
3. **Functions** - `function`, `call`, `return` using loop primitive  
4. **Optimization** - Place classification for memory hierarchy
5. **Backends** - Code generation to assembly, JVM, etc.

The Petri net remains the **semantic truth** - all other targets are optional and erasable.