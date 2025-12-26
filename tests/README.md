# Petri-Net VM Test Suite

This directory contains the organized test suite for the Petri-Net VM system.

## Test Organization

Tests are organized into three categories:

### Unit Tests (`tests/unit/`)
- `test_arithmetic_edge_cases_unit.py` - Edge cases for arithmetic operations
- `test_local_variables_unit.py` - Local variable functionality tests
- `test_simple_local.py` - Basic local variable operations

### Integration Tests (`tests/integration/`)
- `test_complex_functions.py` - Complex function call scenarios
- `test_distributed_multicore.py` - Multi-core distributed execution
- `test_function_calls.py` - Function call mechanisms
- `test_function_with_args.py` - Function calls with arguments
- `test_petri_net_vm.py` - Comprehensive VM functionality
- `test_single_vm.py` - Single VM file testing

### Property-Based Tests (`tests/property/`)
- `test_arithmetic_operations_pbt.py` - Property-based arithmetic testing
- `test_local_variables_pbt.py` - Property-based local variable testing

## Running Tests

### Run All Tests
```bash
python run_tests.py
```

### Run Tests by Category
```bash
python run_tests.py --category unit
python run_tests.py --category integration
python run_tests.py --category property
```

### Additional Options
```bash
python run_tests.py --verbose          # Show detailed output
python run_tests.py --stop-on-fail     # Stop on first failure
python run_tests.py --help             # Show all options
```

## Test Results

Test results and generated assembly files are stored in the `test_results/` directory.

## Adding New Tests

1. Create test files with the `test_*.py` naming convention
2. Place them in the appropriate category directory
3. The test runner will automatically discover and run them
4. Tests should be self-contained and not depend on external state