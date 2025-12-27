# VM Operations Reference

Complete reference for all supported VM operations in the Petri-Net Virtual Machine.

## Memory Operations

### Local Variables

#### `push local N`
**Description**: Push the value of local variable N onto the stack  
**Petri Net Mapping**: Creates a dup transition from local variable place to result place  
**Example**:
```vm
function test 2
push constant 42
pop local 0      // Store 42 in local variable 0
push local 0     // Push value of local variable 0 (42)
return
```

#### `pop local N`
**Description**: Pop the top stack value and store it in local variable N  
**Petri Net Mapping**: Creates assignment transition from stack place to local variable place  
**Example**:
```vm
function test 2
push constant 100
pop local 1      // Store 100 in local variable 1
push local 1     // Retrieve the value (100)
return
```

### Arguments

#### `push argument N`
**Description**: Push the value of argument N onto the stack  
**Petri Net Mapping**: Creates dup transition from argument place to result place  
**Example**:
```vm
function add_numbers 0
push argument 0   // First argument
push argument 1   // Second argument
add              // Add them
return
```

#### `pop argument N`
**Description**: Pop the top stack value and store it back to argument N (reference parameter)  
**Petri Net Mapping**: Creates assignment transition to caller's argument place  
**Example**:
```vm
function double_arg 0
push argument 0   // Get argument value
push constant 2   // Push 2
mul              // Multiply by 2
pop argument 0   // Store back to caller's argument
return
```

### Constants

#### `push constant N`
**Description**: Push the constant value N onto the stack  
**Petri Net Mapping**: Creates source transition producing token with value N  
**Example**:
```vm
push constant 42  // Pushes 42 onto stack
push constant -5  // Pushes -5 onto stack
```

## Arithmetic Operations

### Binary Operations

#### `add`
**Description**: Pop two values, push their sum  
**Petri Net Mapping**: Join transition consuming two places, producing sum  
**Example**:
```vm
push constant 7
push constant 8
add              // Result: 15
```

#### `sub`
**Description**: Pop two values (b, a), push a - b  
**Petri Net Mapping**: Join transition with subtraction function  
**Example**:
```vm
push constant 10
push constant 3
sub              // Result: 7 (10 - 3)
```

#### `mul`
**Description**: Pop two values, push their product  
**Petri Net Mapping**: Join transition with multiplication function  
**Example**:
```vm
push constant 6
push constant 7
mul              // Result: 42
```

#### `div`
**Description**: Pop two values (b, a), push integer division a / b  
**Petri Net Mapping**: Join transition with division function  
**Example**:
```vm
push constant 20
push constant 4
div              // Result: 5
```

### Unary Operations

#### `neg`
**Description**: Pop one value, push its negation  
**Petri Net Mapping**: Single-input transition with negation function  
**Example**:
```vm
push constant 42
neg              // Result: -42
```

## Logical Operations

### Comparison Operations

#### `eq`
**Description**: Pop two values, push -1 if equal, 0 if not equal  
**Petri Net Mapping**: Join transition with equality comparison  
**Example**:
```vm
push constant 5
push constant 5
eq               // Result: -1 (true)
```

#### `lt`
**Description**: Pop two values (b, a), push -1 if a < b, 0 otherwise  
**Petri Net Mapping**: Join transition with less-than comparison  
**Example**:
```vm
push constant 3
push constant 7
lt               // Result: -1 (true, 3 < 7)
```

#### `gt`
**Description**: Pop two values (b, a), push -1 if a > b, 0 otherwise  
**Petri Net Mapping**: Join transition with greater-than comparison  
**Example**:
```vm
push constant 10
push constant 5
gt               // Result: -1 (true, 10 > 5)
```

### Boolean Operations

#### `and`
**Description**: Pop two values, push bitwise AND  
**Petri Net Mapping**: Join transition with AND function  
**Example**:
```vm
push constant -1  // true
push constant 0   // false
and              // Result: 0 (false)
```

#### `or`
**Description**: Pop two values, push bitwise OR  
**Petri Net Mapping**: Join transition with OR function  
**Example**:
```vm
push constant -1  // true
push constant 0   // false
or               // Result: -1 (true)
```

#### `not`
**Description**: Pop one value, push bitwise NOT  
**Petri Net Mapping**: Single-input transition with NOT function  
**Example**:
```vm
push constant 0
not              // Result: -1 (true)
```

## Control Flow Operations

### Labels

#### `label NAME`
**Description**: Define a jump target with the given name  
**Petri Net Mapping**: Creates control flow place for the label  
**Scope**: Function-local (labels are scoped to their containing function)  
**Example**:
```vm
function test 0
label LOOP_START
  // ... loop body ...
goto LOOP_START
return
```

### Unconditional Jumps

#### `goto LABEL`
**Description**: Jump unconditionally to the specified label  
**Petri Net Mapping**: Choice transition routing execution token to label place  
**Example**:
```vm
function test 0
goto SKIP_CODE
push constant 999  // This is skipped
label SKIP_CODE
push constant 42   // This executes
return
```

### Conditional Jumps

#### `if-goto LABEL`
**Description**: Pop one value, jump to label if value is non-zero  
**Petri Net Mapping**: Choice transition with condition evaluation  
**Example**:
```vm
function test 0
push argument 0    // Get condition
if-goto TRUE_CASE  // Jump if non-zero
// False case
push constant 0
return
label TRUE_CASE
// True case  
push constant 1
return
```

## Function Operations

### Function Definition

#### `function NAME LOCALS`
**Description**: Define a function with the given name and number of local variables  
**Petri Net Mapping**: Creates function subnet with local variable places  
**Example**:
```vm
function factorial 1  // Function with 1 local variable
// ... function body ...
return
```

### Function Calls

#### `call FUNCTION ARGS`
**Description**: Call the specified function with the given number of arguments  
**Petri Net Mapping**: Creates call transition routing tokens to function subnet  
**Example**:
```vm
push constant 5
push constant 3
call add_numbers 2  // Call with 2 arguments
```

### Function Return

#### `return`
**Description**: Return from the current function  
**Petri Net Mapping**: Routes return value token back to caller  
**Example**:
```vm
function add_one 0
push argument 0
push constant 1
add
return           // Return the sum
```

## Advanced Patterns

### Recursive Functions

Recursive functions work naturally with the Petri net model:

```vm
function factorial 0
push argument 0
push constant 1
gt
if-goto RECURSIVE_CASE

// Base case: return 1
push constant 1
return

label RECURSIVE_CASE
// Recursive case: n * factorial(n-1)
push argument 0
push argument 0
push constant 1
sub
call factorial 1
mul
return
```

### Loops with Control Flow

```vm
function count_to_n 2  // locals: counter, sum
push constant 0
pop local 0        // counter = 0
push constant 0  
pop local 1        // sum = 0

label LOOP_START
push local 0       // counter
push argument 0    // n
lt                 // counter < n?
if-goto LOOP_BODY
goto LOOP_END

label LOOP_BODY
push local 1       // sum
push local 0       // counter
add                // sum + counter
pop local 1        // sum = sum + counter

push local 0       // counter
push constant 1
add                // counter + 1
pop local 0        // counter = counter + 1

goto LOOP_START

label LOOP_END
push local 1       // return sum
return
```

### Reference Parameters

Functions can modify their arguments using `pop argument`:

```vm
function swap_args 0
push argument 1    // Get second argument
push argument 0    // Get first argument
pop argument 1     // Store first in second position
pop argument 0     // Store second in first position
return
```

## Memory Model

### Local Variables
- Scoped to function calls
- Automatically allocated when function is called
- Deallocated when function returns
- Can be optimized for memory reuse

### Arguments
- Passed by value by default
- Can be modified using `pop argument` (reference semantics)
- Changes via `pop argument` are visible to caller

### Stack Semantics
- No explicit stack - values live in places
- Stack operations are token movements between places
- All state is visible in the Petri net structure

## Error Handling

### Common Errors
- **Insufficient operands**: Attempting operations without enough stack values
- **Undefined labels**: Jumping to non-existent labels
- **Function not found**: Calling undefined functions
- **Argument out of bounds**: Accessing non-existent arguments or locals
- **Division by zero**: Handled according to VM specification

### Error Recovery
The Petri net structure makes many classes of errors impossible:
- No stack underflow (structural impossibility)
- No memory leaks (place lifetime analysis)
- No hidden state corruption (all state is visible)

## Performance Characteristics

### Memory Optimization
- Place lifetime analysis reduces memory usage by 20-33%
- Optimal memory allocation using interval graph coloring
- Local variables and temporaries are aggressively optimized

### Multi-Core Execution
- Automatic parallelization based on dependency analysis
- Linear scaling up to 8+ cores
- No coordination overhead - cores self-terminate

### Control Flow Efficiency
- Labels and jumps are compiled to direct place connections
- No runtime label lookup overhead
- Conditional jumps use native Petri net choice semantics