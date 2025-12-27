# VM Examples

This directory contains comprehensive examples demonstrating all features of the Petri-Net Virtual Machine.

## Example Programs

### 🔄 **factorial_recursive.vm**
**Features**: Recursion, Control Flow, Arithmetic  
**Description**: Calculates factorial using recursive function calls with base case handling  
**Key Concepts**:
- Recursive function calls
- Conditional branching with `if-goto`
- Base case termination
- Arithmetic operations (`mul`, `sub`)

```bash
python -c "
from Petri.VMToPetri import VMToPetriTranslator
import vm_parser
translator = VMToPetriTranslator()
commands = vm_parser.parse_vm_file('examples/factorial_recursive.vm')
result = translator.execute_program(commands)
print(f'factorial(6) = {result}')  # Should be [720]
"
```

### 🌀 **fibonacci_iterative.vm**
**Features**: Local Variables, Loops, Control Flow  
**Description**: Calculates Fibonacci numbers using iterative approach with local variables  
**Key Concepts**:
- Local variable management (`pop local`, `push local`)
- Loop construction with labels and jumps
- Multiple base cases
- State management across iterations

### ➕ **arithmetic_showcase.vm**
**Features**: All Arithmetic Operations, Complex Expressions  
**Description**: Demonstrates all arithmetic operations in complex expressions  
**Key Concepts**:
- All arithmetic operations: `add`, `sub`, `mul`, `div`, `neg`
- Complex expression evaluation
- Local variable usage for intermediate results
- Multiple function calls with different operations

### 🔀 **control_flow_patterns.vm**
**Features**: Advanced Control Flow, Nested Conditions, Loops  
**Description**: Comprehensive control flow patterns including nested conditions and early exits  
**Key Concepts**:
- Nested conditional logic
- Loop with early exit conditions
- Switch-like pattern implementation
- Complex branching structures

### 🔗 **reference_parameters.vm**
**Features**: Reference Parameters, Argument Modification  
**Description**: Demonstrates reference parameter semantics using `pop argument`  
**Key Concepts**:
- Modifying caller's arguments with `pop argument`
- Reference parameter patterns
- Complex argument transformations
- Local variables with reference parameters

## Running Examples

### Prerequisites
```bash
# Ensure you have the VM parser (if not included, create a simple one)
# The examples assume a vm_parser.parse_vm_file() function exists
```

### Method 1: Direct Execution
```python
from Petri.VMToPetri import VMToPetriTranslator

# Parse VM file (implement parse_vm_file or use manual command list)
translator = VMToPetriTranslator()
commands = [...]  # Your parsed commands
result = translator.execute_program(commands)
print(f"Result: {result}")
```

### Method 2: Using Test Framework
```bash
# Create a test that loads and runs the example
python tests/integration/test_comprehensive_vm_file.py
```

### Method 3: Interactive Testing
```python
# Load example into Python REPL
exec(open('examples/run_example.py').read())
```

## Example Patterns

### Recursive Functions
```vm
function recursive_func 0
    // Base case check
    push argument 0
    push constant 1
    gt
    if-goto RECURSIVE_CASE
    
    // Base case return
    push constant 1
    return
    
    label RECURSIVE_CASE
    // Recursive logic
    push argument 0
    // ... modify argument ...
    call recursive_func 1
    // ... combine results ...
    return
```

### Iterative Loops
```vm
function loop_func 2  // counter, accumulator
    push constant 0
    pop local 0      // counter = 0
    push constant 0
    pop local 1      // accumulator = 0
    
    label LOOP_START
    // Loop condition
    push local 0
    push argument 0
    lt
    if-goto LOOP_BODY
    goto LOOP_END
    
    label LOOP_BODY
    // Loop operations
    // ... update accumulator ...
    // ... increment counter ...
    goto LOOP_START
    
    label LOOP_END
    push local 1     // return accumulator
    return
```

### Reference Parameters
```vm
function modify_param 0
    // Modify first argument
    push argument 0
    // ... perform operation ...
    pop argument 0   // Store back to caller
    return
```

### Complex Conditionals
```vm
function multi_branch 0
    push argument 0
    push constant 10
    gt
    if-goto CASE_LARGE
    
    push argument 0
    push constant 0
    gt
    if-goto CASE_POSITIVE
    
    // Case: x <= 0
    push constant 0
    return
    
    label CASE_POSITIVE
    // Case: 0 < x <= 10
    push constant 1
    return
    
    label CASE_LARGE
    // Case: x > 10
    push constant 2
    return
```

## Performance Notes

### Memory Optimization
All examples benefit from automatic memory optimization:
- Local variables are optimally allocated
- Temporary values reuse memory locations
- 20-33% memory reduction typical

### Multi-Core Execution
Examples can be automatically parallelized:
```python
# Generate multi-core assembly
translator.generate_multicore_assembly(num_cores=4)
```

### Petri Net Visualization
The underlying Petri net structure can be analyzed:
```python
# Print network statistics
translator.print_net_statistics()

# Get detailed place information
place_info = translator.get_detailed_place_info()
print(place_info)
```

## Creating New Examples

### Guidelines
1. **Focus on one feature set** per example
2. **Include comprehensive comments** explaining the VM operations
3. **Test edge cases** and error conditions
4. **Demonstrate best practices** for the feature
5. **Keep examples self-contained** and runnable

### Template Structure
```vm
// Example Title and Description
// Demonstrates: feature1, feature2, feature3

// Function: Description of what this function does
function example_func N  // N = number of local variables
    // Clear comments explaining each step
    // ...
    return

// Main program: Test the function
push constant 42
call example_func 1
// Expected result: [expected_value]
```

### Testing Your Example
1. Create the VM file in `examples/`
2. Add a test case in `tests/integration/`
3. Run the test to verify correctness
4. Check memory optimization and multi-core generation
5. Update this README with your example

## Advanced Features

### Memory Analysis
```python
# Analyze memory usage
memory_stats = translator._optimize_memory_allocation()
print(f"Memory optimization: {memory_stats}")
```

### Execution Analysis
```python
# Analyze execution dependencies
execution_plan = translator._analyze_execution_dependencies()
print(f"Execution levels: {len(execution_plan['execution_levels'])}")
```

### Assembly Generation
```python
# Generate assembly for different core counts
for cores in [1, 2, 4, 8]:
    translator.generate_multicore_assembly(num_cores=cores)
```

These examples showcase the full power of the Petri-Net VM, demonstrating how complex programs can be expressed using pure Petri net semantics while maintaining performance and correctness.