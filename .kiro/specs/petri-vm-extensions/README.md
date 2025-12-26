# Petri Net VM Extensions - Project Specification

## Overview

This specification defines the next phase of development for the **Petri Net Virtual Machine**, a groundbreaking implementation that translates VM operations into pure Petri net semantics with distributed multi-core execution and memory optimization.

## Current Achievement Summary

The Petri Net VM has successfully implemented:

### ✅ **Core VM Operations**
- Arithmetic: `add`, `sub`, `neg`, `eq`, `lt`, `gt`, `and`, `or`, `not`
- Stack operations: `push constant`, `push argument`, `dup`, `drop`
- Pure Petri net semantics: Places ARE the stack elements

### ✅ **Function Call System**
- Function definition parsing and storage
- Function calls with argument passing via Petri net places
- Return value handling and context restoration
- Call stack management for nested calls
- All tests passing for simple calls, arguments, and composition

### ✅ **Distributed Multi-Core Coordination**
- **Revolutionary approach**: Eliminated centralized coordinator
- **Level-based barriers**: Cores self-coordinate using execution level synchronization
- **Distributed termination**: Final level completion IS program completion detection
- **Pure Petri net semantics**: No hidden coordination algorithms

### ✅ **Memory Optimization**
- Place lifetime analysis using reachability analysis
- Memory location reuse for places with non-overlapping lifetimes
- 20-33% memory reduction in function call scenarios
- Interval graph coloring for optimal allocation

### ✅ **Assembly Generation**
- Single-core optimized assembly with direct memory operations
- Multi-core ROM generation with separate core files
- Shared memory initialization and coordination documentation
- Comprehensive statistics and analysis

## Next Phase: Extensions and Enhancements

### 🎯 **Primary Objectives**

1. **Complete Local Variable Support**
   - Implement `pop local N` for storing to local variables
   - Enhance `push local N` reliability
   - Full function-local state management

2. **Arithmetic Extensions**
   - Add `mul` (multiplication) operation
   - Add `div` (division) operation
   - Maintain pure Petri net semantics

3. **Control Flow Support**
   - Implement `label NAME` definitions
   - Add `goto LABEL` unconditional jumps
   - Add `if-goto LABEL` conditional jumps
   - Use choice and join primitives structurally

4. **Advanced Function Features**
   - Support recursive function calls
   - Implement `pop argument N` for reference parameters
   - Optimize recursive call patterns

## Project Structure

This specification consists of four key documents:

### 📋 **[requirements.md](./requirements.md)**
- **User stories** with acceptance criteria
- **Epic breakdown** by feature area
- **Success criteria** and test strategy
- **Risk mitigation** and constraints

### 🏗️ **[design.md](./design.md)**
- **Technical architecture** for new features
- **Petri net mapping** for each operation
- **Multi-core integration** approach
- **Memory optimization** enhancements

### 🔧 **[implementation-guide.md](./implementation-guide.md)**
- **Step-by-step** implementation instructions
- **Code examples** and test cases
- **Debugging utilities** and troubleshooting
- **Validation checklists** for each phase

### 📖 **[README.md](./README.md)** (this file)
- **Project overview** and current state
- **Quick start** guide for contributors
- **File organization** and navigation

## Quick Start Guide

### For Contributors

1. **Read the current implementation**:
   ```bash
   # Key files to understand
   cat Petri/VMToPetri.py              # Main implementation
   cat docs/IMPLEMENTATION_SUMMARY.md  # Feature overview
   cat test_function_calls.py          # Working examples
   ```

2. **Review the specification**:
   ```bash
   # Start with requirements
   cat .kiro/specs/petri-vm-extensions/requirements.md
   
   # Then review technical design
   cat .kiro/specs/petri-vm-extensions/design.md
   
   # Finally, follow implementation guide
   cat .kiro/specs/petri-vm-extensions/implementation-guide.md
   ```

3. **Run existing tests**:
   ```bash
   python test_function_calls.py
   python test_function_with_args.py
   python test_complex_functions.py
   ```

4. **Start with Phase 1**:
   - Implement `pop local N` operation
   - Add `mul` operation
   - Create comprehensive tests

### For Project Managers

**Priority 1 (Immediate)**:
- Local variable operations (`pop local`, enhanced `push local`)
- Multiplication operation (`mul`)
- Comprehensive testing of new features

**Priority 2 (Next Sprint)**:
- Control flow framework (labels, goto)
- Conditional jumps (`if-goto`)
- Integration with multi-core execution

**Priority 3 (Future)**:
- Division operation and advanced arithmetic
- Recursive function optimization
- Performance scaling and tools

## Key Design Principles

### 🎯 **Pure Petri Net Semantics**
- **No hidden state**: All program state exists as tokens in places
- **Structural execution**: Control flow through place/transition topology
- **Six primitives only**: source, choice, dup, drop, join, loop

### 🚀 **Distributed Execution**
- **No coordinator**: Level-based barriers eliminate centralized coordination
- **Self-termination**: Cores know when program is complete
- **Scalable**: Works efficiently with multiple cores

### 💾 **Memory Optimization**
- **Lifetime analysis**: Places with non-overlapping lifetimes share memory
- **Formal methods**: Uses interval graph coloring for optimal allocation
- **Measurable results**: 20-33% memory reduction demonstrated

## Success Metrics

### Functional Metrics
- ✅ All new operations work correctly in isolation
- ✅ Complex programs combining multiple features execute properly
- ✅ Function calls with local variables and control flow work together
- ✅ Recursive functions execute without errors

### Performance Metrics
- 🎯 **Memory optimization**: Target 30%+ reduction for complex programs
- 🎯 **Multi-core scaling**: Efficient execution on 4+ cores
- 🎯 **Execution speed**: Control flow operations don't significantly impact performance

### Quality Metrics
- ✅ All existing tests continue to pass
- ✅ New comprehensive test suite covers all new features
- ✅ Documentation updated to reflect new capabilities
- ✅ Code maintains current quality standards

## Technical Innovation

### Revolutionary Distributed Coordination

**Before**: Traditional multi-core VMs use centralized coordinators
```
Main Coordinator:
  monitor all cores
  detect completion
  single point of failure
```

**After**: Our distributed approach eliminates the coordinator
```
Each Core:
  execute operations at current level
  signal level complete
  wait for all cores at level
  self-terminate when final level completes
```

**Benefits**:
- No single point of failure
- No coordinator overhead
- Pure Petri net semantics
- Level synchronization IS completion detection

### Memory Optimization Through Formal Analysis

**Traditional Approach**: Static memory allocation
```
Each variable gets its own memory location
Memory usage = number of variables
No reuse, high memory consumption
```

**Our Approach**: Place lifetime analysis with interval graph coloring
```
Analyze when each place is "live" (has tokens)
Places with non-overlapping lifetimes share memory
Optimal allocation using formal graph algorithms
20-33% memory reduction demonstrated
```

### Pure Petri Net Semantics

**Traditional VMs**: Hidden stack and program counter
```
Stack: [hidden data structure]
PC: [hidden program counter]
Operations modify hidden state
```

**Our VM**: Places ARE the data, structure IS the program
```
Stack elements: Individual places with tokens
Program flow: Transition firing based on token availability
No hidden state: Everything visible in net structure
```

## Getting Started

### Immediate Next Steps

1. **Implement `pop local N`** following the implementation guide
2. **Add `mul` operation** using the existing binary operation pattern
3. **Create comprehensive tests** for local variable operations
4. **Verify multi-core execution** still works with new operations

### Development Workflow

1. **Read specification documents** in order (requirements → design → implementation)
2. **Implement features in phases** as outlined in the implementation guide
3. **Test thoroughly** at each step using provided test cases
4. **Validate integration** with existing multi-core and optimization features
5. **Update documentation** as features are completed

### Support and Resources

- **Current implementation**: `Petri/VMToPetri.py` - fully functional base
- **Working tests**: `test_function_*.py` - examples of current capabilities
- **Documentation**: `docs/IMPLEMENTATION_SUMMARY.md` - comprehensive overview
- **Multi-core examples**: `test_results/multicore_*cores/` - generated assembly

## Project Vision

The Petri Net VM represents a fundamental rethinking of virtual machine architecture:

- **Theoretical foundation**: Grounded in formal Petri net theory
- **Practical implementation**: Real working VM with comprehensive features
- **Performance benefits**: Memory optimization and distributed execution
- **Educational value**: Demonstrates pure functional programming concepts
- **Research contribution**: Novel approach to VM design and multi-core coordination

This specification provides the roadmap for the next phase of this innovative project, extending its capabilities while preserving its core architectural strengths.

---

**Ready to contribute?** Start with the [requirements document](./requirements.md) to understand what we're building, then move to the [design document](./design.md) for technical details, and finally follow the [implementation guide](./implementation-guide.md) for step-by-step instructions.