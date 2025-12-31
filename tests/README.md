# Petri Net VM Compiler Test Suite

This directory contains comprehensive tests for the Petri net-based virtual machine compiler system.

## Test Organization

### 🔧 Core Operations
Tests for fundamental Petri net operations and stack management:
- `test_insert_operation.py` - Stack-based operation insertion logic
- `test_dup_branching.py` - Branching logic for multiple push constants

### 💾 Memory Management  
Tests for memory allocation and optimization algorithms:
- `test_memory_allocator.py` - Basic memory allocation patterns
- `test_interference_analysis.py` - Interference detection correctness
- `test_allocation_debugging.py` - Memory safety validation
- `test_large_network_optimization.py` - Large-scale optimization testing

### 🖥️ VM Operations
Tests for virtual machine instruction parsing and compilation:
- `test_push_constant.py` - Push constant instruction handling

### 🔥 Edge Cases & Stress Testing
Tests for pathological cases and robustness:
- `test_pathological_cases.py` - Worst-case scenarios and stress tests

## Running Tests

### Run All Tests (Organized)
```bash
python tests/test_suite_runner.py
```

### Run All Tests (Legacy)
```bash
python run_tests.py
```

### Run Individual Test Categories
```bash
# Core operations only
python tests/test_insert_operation.py
python tests/test_dup_branching.py

# Memory management only  
python tests/test_memory_allocator.py
python tests/test_interference_analysis.py
python tests/test_allocation_debugging.py

# VM operations only
python tests/test_push_constant.py

# Stress testing only
python tests/test_pathological_cases.py
python tests/test_large_network_optimization.py
```

## Test Coverage

### ✅ Well Covered
- Stack-based operation logic
- Memory allocation algorithms
- Interference detection
- Dup branching for push constants
- Large-scale network optimization
- Pathological edge cases

### 🚧 Areas for Future Enhancement
- Additional VM operations (arithmetic, comparison, memory segments)
- Integration testing with complete VM programs
- Assembly generation validation
- Function call sequences
- Error handling for malformed VM code

## Test Results Interpretation

### Memory Efficiency Metrics
- **>90% efficiency**: Excellent optimization (linear chains, trees)
- **50-90% efficiency**: Good optimization (moderate interference)
- **<50% efficiency**: High interference (expected for complex graphs)

### Success Criteria
- All assertions pass without errors
- Memory slot assignments are safe (no interference violations)
- Generated assembly follows expected patterns
- Network execution produces correct token values

## Adding New Tests

1. Create test file following naming convention: `test_<feature>.py`
2. Include comprehensive docstrings and assertions
3. Add to appropriate category in `test_suite_runner.py`
4. Ensure tests are self-contained and deterministic
5. Include both positive and negative test cases