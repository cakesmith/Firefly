# VM Translator Comparison Framework

## Overview

This project now includes a comprehensive comparison framework between two VM translators:

1. **Legacy Stack-Based VM Translator** (`VirtualMachine.py`) - Traditional single-core, stack-based assembly generation
2. **Current Petri Net VM Translator** (`vm_parser.py` + `Petri/VMToPetri.py`) - Modern Petri net-based, multi-core capable translator

## Files Created

### Test Scripts

- **`test_vm_comparison.py`** - Comprehensive comparison suite that tests all .vm files in the OS directory
- **`test_single_vm.py`** - Test individual VM files with both translators
- **`test_simple.vm`** - Simple test case for basic arithmetic operations

### Updated Files

- **`VirtualMachine.py`** - Added command-line argument support for standalone usage

## Key Features

### Comparison Metrics

The comparison framework analyzes and compares:

- **Assembly Code Statistics:**
  - Total lines of code
  - Instruction lines vs comments/labels
  - Memory locations used
  - Code complexity metrics

- **Petri Net Specific Metrics:**
  - Number of places and transitions
  - Network connectivity (arcs)
  - Memory optimization results
  - Parallel execution potential

### Current Status

**Petri Net VM Translator:**
- ✅ Supports: `push constant`, arithmetic operations (`add`, `sub`, `neg`, `and`, `or`, `not`, `eq`, `lt`, `gt`)
- ❌ Missing: `pop` operations, function calls, control flow (`if-goto`, `goto`, `label`)
- ✅ Features: Memory optimization, parallel execution analysis, multi-core assembly generation

**Legacy Stack-Based VM Translator:**
- ✅ Supports: Full VM command set including functions, control flow, memory segments
- ✅ Features: Traditional stack-based execution model
- ❌ Limitations: Single-core only, no memory optimization

## Example Results

For the simple test case (`push constant 7`, `push constant 8`, `add`, `push constant 2`, `sub`):

### Petri Net VM Translator
- **Result:** 44 lines of assembly (24 instructions)
- **Memory:** 3 optimized locations (saved 2 locations through reuse)
- **Network:** 5 places, 2 transitions, 6 arcs
- **Execution:** 2 parallel levels identified

### Legacy Stack-Based VM Translator
- **Result:** 200 lines of assembly (169 instructions)
- **Memory:** Traditional stack-based approach
- **Execution:** Sequential only

## Performance Comparison

| Metric | Petri Net VM | Legacy VM | Difference |
|--------|--------------|-----------|------------|
| Assembly Lines | 44 | 200 | -156 (78% reduction) |
| Instructions | 24 | 169 | -145 (86% reduction) |
| Memory Efficiency | Optimized reuse | Stack-based | 40% memory savings |
| Parallelization | 2 levels detected | None | Concurrent execution potential |

## Usage

### Test Individual Files
```bash
python test_single_vm.py <vm_file> [--show-assembly]
```

### Run Full Comparison Suite
```bash
python test_vm_comparison.py
```

### Use Legacy VM Translator Standalone
```bash
python VirtualMachine.py <vm_file_or_directory> [-o output.asm] [--no-bootstrap] [--overwrite]
```

## Next Steps

To complete the comparison framework:

1. **Implement missing VM commands in Petri net translator:**
   - `pop` operations for all memory segments
   - Function definitions and calls
   - Control flow (`label`, `goto`, `if-goto`)

2. **Enhance comparison metrics:**
   - Execution time simulation
   - Memory usage analysis
   - Parallelization efficiency metrics

3. **Add more test cases:**
   - Function call scenarios
   - Complex control flow
   - Memory management operations

## Architecture Benefits

The Petri net approach demonstrates several advantages:

- **Memory Optimization:** Automatic detection of memory reuse opportunities
- **Parallelization:** Natural identification of concurrent execution paths
- **Multi-core Support:** Built-in capability for distributed execution
- **Code Efficiency:** Significant reduction in generated assembly code
- **Formal Verification:** Petri net semantics enable formal analysis

This comparison framework provides a solid foundation for evaluating and improving both VM translation approaches.