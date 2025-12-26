# Petri-Net VM Documentation

This directory contains focused documentation for the Petri-net native virtual machine implementation.

## Core Documentation

- **[petri-vm.md](petri-vm.md)** - Complete Petri-net VM overview, architecture, and implementation
- **[TODO.txt](TODO.txt)** - Development roadmap and future enhancements

## Implementation Files

The following files in the root directory contain detailed implementation notes:

- `petri_vm_summary.md` - Original implementation summary
- `STACKFREE_BREAKTHROUGH.md` - Stack-free architecture breakthrough
- `IMPLEMENTATION_SUMMARY.md` - Technical implementation details

## Test Files

- `test_petri_net_vm.py` - Comprehensive test suite for all VM capabilities
- `run_tests.py` - Test runner with filtering options (basic/assembly/complex)

## Key Innovation

The Petri-net VM eliminates traditional stack abstractions - the network structure IS the program, with all execution state visible in token positions. This enables formal analysis, memory optimization, and automatic multi-core code generation while maintaining structural correctness guarantees.