# Petri Net VM Extensions - Implementation Guide

## Getting Started

This guide provides step-by-step implementation instructions for extending the Petri Net VM. Each task includes code examples, test cases, and validation steps.

## Phase 1: Local Variable Operations

### Task 1.1: Implement `pop local N`

**Objective:** Store the top stack element to a local variable.

**Location:** Add to `VMToPetriTranslator` class in `Petri/VMToPetri.py`

**Implementation:**

```python
def pop_local(self, index):
    """
    Store top stack element to local variable N
    Implements: pop local N
    """
    if not self.current_function:
        raise RuntimeError("No function context for local variable access")
    
    if len(self.result_places) < 1:
        raise RuntimeError("No value to pop for local variable")
    
    # Get the value to store
    value_place = self.result_places.pop()
    
    # Get or create the local variable place
    local_place_name = f"local_{self.current_function}_{index}"
    local_place = self._get_or_create_local_place(local_place_name, index)
    
    # Create assignment transition that moves value to local
    def assign_local_func(tokens):
        return tokens[0]  # Pass the value through
    
    assign_transition = self.net.add_transition(
        self.get_unique_transition_name(f"pop_local_{index}"),
        assign_local_func
    )
    
    # Wire: value_place → assign_transition → local_place
    self.net.add_arc(value_place, assign_transition)
    self.net.add_arc(assign_transition, local_place)
    
    print(f"Stored value to local variable {index}")
    return local_place

def _get_or_create_local_place(self, local_place_name, index):
    """Get existing local place or create new one"""
    # Check if local place already exists
    for place_name, place in self.net.places.items():
        if local_place_name in place_name:
            return place
    
    # Create new local place
    local_place = self.net.add_place(self.get_unique_place_name(local_place_name))
    
    # Initialize with default value (0) if needed
    local_place.put_token(Token(0))
    
    return local_place
```

**Update Command Execution:**

```python
def _execute_command(self, command):
    """Execute a single VM command - ADD pop local support"""
    cmd_type = command[0]
    
    if cmd_type == "push":
        segment = command[1]
        index = command[2]
        self.push_operation(segment, index)
    elif cmd_type == "pop":
        segment = command[1]
        index = command[2]
        self.pop_operation(segment, index)  # NEW: Add pop operation
    # ... existing operations ...

def pop_operation(self, segment, index):
    """General pop operation for different memory segments"""
    if segment == "local":
        return self.pop_local(index)
    elif segment == "argument":
        return self.pop_argument(index)  # For future implementation
    else:
        raise NotImplementedError(f"Pop {segment} not implemented")
```

**Test Case:**

```python
def test_pop_local():
    """Test pop local operation"""
    commands = [
        ("function", "Test.locals", 2),  # Function with 2 locals
        ("push", "constant", 42),        # Push value
        ("pop", "local", 0),             # Store to local 0
        ("push", "constant", 17),        # Push another value
        ("pop", "local", 1),             # Store to local 1
        ("push", "local", 0),            # Load local 0
        ("push", "local", 1),            # Load local 1
        ("add",),                        # Add them: 42 + 17 = 59
        ("return",),
        
        ("call", "Test.locals", 0),      # Call function
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    assert result[-1] == 59, f"Expected 59, got {result[-1]}"
```

### Task 1.2: Implement `mul` Operation

**Objective:** Add multiplication operation following the existing binary operation pattern.

**Implementation:**

```python
def mul_operation(self):
    """
    Implement mul operation: consume two most recent result places
    Result = first * second
    """
    if len(self.result_places) < 2:
        raise RuntimeError("Not enough operands for mul operation")
        
    # Pop operands from result places
    b_place = self.result_places.pop()  # Second operand
    a_place = self.result_places.pop()  # First operand
    
    # Create result place
    result_place = self.net.add_place(self.get_unique_place_name("mul_result"))
    
    def mul_op(tokens):
        a_val = tokens[0].value
        b_val = tokens[1].value
        result = a_val * b_val
        # Handle overflow if needed (VM specification dependent)
        return Token(result & 0xFFFF)  # 16-bit result
        
    mul_transition = self.net.add_transition(
        self.get_unique_transition_name("mul"), 
        mul_op
    )
    
    # Wire: input_places → transition → output_place
    self.net.add_arc(a_place, mul_transition)
    self.net.add_arc(b_place, mul_transition)
    self.net.add_arc(mul_transition, result_place)
    
    # Add result to result places
    self.result_places.append(result_place)
    return result_place
```

**Update Command Execution:**

```python
def _execute_command(self, command):
    """Execute a single VM command - ADD mul support"""
    # ... existing commands ...
    elif cmd_type == "mul":
        self.mul_operation()
    # ... rest of commands ...
```

**Test Case:**

```python
def test_multiplication():
    """Test multiplication operation"""
    commands = [
        ("push", "constant", 6),
        ("push", "constant", 7),
        ("mul",),  # 6 * 7 = 42
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    assert result[-1] == 42, f"Expected 42, got {result[-1]}"
```

### Task 1.3: Enhanced Local Variable Testing

**Create comprehensive test file:** `test_local_variables.py`

```python
#!/usr/bin/env python3
"""
Test local variable operations in Petri net VM
"""

import sys
import os
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def test_basic_local_operations():
    """Test basic pop/push local operations"""
    print("=== Testing Basic Local Operations ===")
    
    commands = [
        ("function", "Test.basic", 2),   # Function with 2 locals
        ("push", "constant", 100),       # Push 100
        ("pop", "local", 0),             # local[0] = 100
        ("push", "constant", 200),       # Push 200
        ("pop", "local", 1),             # local[1] = 200
        ("push", "local", 0),            # Push local[0] (100)
        ("push", "local", 1),            # Push local[1] (200)
        ("add",),                        # 100 + 200 = 300
        ("return",),
        
        ("call", "Test.basic", 0),       # Call function
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [300]")
    
    if result and result[-1] == 300:
        print("✅ Basic local operations test PASSED")
        return True
    else:
        print("❌ Basic local operations test FAILED")
        return False

def test_local_with_arguments():
    """Test local variables combined with arguments"""
    print("\n=== Testing Locals with Arguments ===")
    
    commands = [
        ("function", "Test.combined", 1), # Function with 1 local
        ("push", "argument", 0),          # Get first argument
        ("push", "argument", 1),          # Get second argument
        ("mul",),                         # Multiply them
        ("pop", "local", 0),              # Store result in local
        ("push", "local", 0),             # Load local
        ("push", "constant", 10),         # Add 10
        ("add",),
        ("return",),
        
        ("push", "constant", 5),          # First argument
        ("push", "constant", 6),          # Second argument
        ("call", "Test.combined", 2),     # Call with 2 args
        # Result should be (5 * 6) + 10 = 40
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [40]")
    
    if result and result[-1] == 40:
        print("✅ Locals with arguments test PASSED")
        return True
    else:
        print("❌ Locals with arguments test FAILED")
        return False

if __name__ == "__main__":
    print("Testing Local Variable Operations")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    total_tests += 1
    if test_basic_local_operations():
        tests_passed += 1
    
    total_tests += 1
    if test_local_with_arguments():
        tests_passed += 1
    
    print(f"\nTest Results: {tests_passed}/{total_tests} tests passed")
```

## Phase 2: Control Flow Framework

### Task 2.1: Label Management System

**Objective:** Create infrastructure for managing labels and control flow.

**Add to VMToPetriTranslator:**

```python
def __init__(self):
    # ... existing initialization ...
    
    # Control flow management
    self.labels = {}  # label_name → control_place
    self.current_execution_context = None
    self.control_flow_stack = []  # For nested control structures

def define_label(self, label_name):
    """
    Define a label for jump targets
    Implements: label NAME
    """
    if not self.current_function:
        raise RuntimeError("Labels must be defined within functions")
    
    # Create scoped label name
    scoped_label = f"{self.current_function}.{label_name}"
    
    if scoped_label in self.labels:
        raise RuntimeError(f"Label {label_name} already defined in function {self.current_function}")
    
    # Create control place for this label
    label_place = self.net.add_place(self.get_unique_place_name(f"label_{scoped_label}"))
    self.labels[scoped_label] = label_place
    
    print(f"Defined label {label_name} in function {self.current_function}")
    return label_place

def _get_current_execution_context(self):
    """Get the current execution context place"""
    if self.current_execution_context is None:
        # Create initial execution context
        self.current_execution_context = self.net.add_place(
            self.get_unique_place_name("exec_context")
        )
        # Initialize with execution token
        self.current_execution_context.put_token(Token("executing"))
    
    return self.current_execution_context
```

### Task 2.2: Implement `goto LABEL`

**Objective:** Implement unconditional jumps using control flow tokens.

**Implementation:**

```python
def goto_operation(self, label_name):
    """
    Implement unconditional goto using control flow redirection
    Implements: goto LABEL
    """
    if not self.current_function:
        raise RuntimeError("goto must be used within a function")
    
    # Create scoped label name
    scoped_label = f"{self.current_function}.{label_name}"
    
    if scoped_label not in self.labels:
        raise RuntimeError(f"Undefined label: {label_name}")
    
    target_place = self.labels[scoped_label]
    current_context = self._get_current_execution_context()
    
    # Create goto transition that redirects execution flow
    def goto_func(tokens):
        return tokens  # Pass execution token to target
    
    goto_transition = self.net.add_transition(
        self.get_unique_transition_name(f"goto_{label_name}"),
        goto_func
    )
    
    # Wire: current_context → goto_transition → target_place
    self.net.add_arc(current_context, goto_transition)
    self.net.add_arc(goto_transition, target_place)
    
    # Update current execution context to target
    self.current_execution_context = target_place
    
    print(f"Created goto to label {label_name}")
    return target_place
```

### Task 2.3: Update Command Execution for Control Flow

**Add control flow commands:**

```python
def _execute_command(self, command):
    """Execute a single VM command - ADD control flow support"""
    cmd_type = command[0]
    
    # ... existing commands ...
    elif cmd_type == "label":
        label_name = command[1]
        self.define_label(label_name)
    elif cmd_type == "goto":
        label_name = command[1]
        self.goto_operation(label_name)
    elif cmd_type == "if-goto":
        label_name = command[1]
        self.if_goto_operation(label_name)
    # ... rest of commands ...
```

### Task 2.4: Test Control Flow

**Create test file:** `test_control_flow.py`

```python
#!/usr/bin/env python3
"""
Test control flow operations in Petri net VM
"""

import sys
import os
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def test_simple_goto():
    """Test basic goto operation"""
    print("=== Testing Simple Goto ===")
    
    commands = [
        ("function", "Test.goto", 0),
        ("push", "constant", 1),         # This should be skipped
        ("goto", "SKIP"),                # Jump over next instruction
        ("push", "constant", 999),       # This should be skipped
        ("label", "SKIP"),               # Target label
        ("push", "constant", 42),        # This should execute
        ("return",),
        
        ("call", "Test.goto", 0),
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [42] (999 should be skipped)")
    
    # Note: This test may need adjustment based on actual control flow implementation
    # The key is that 999 should not appear in the result
    
    return True  # Placeholder - implement proper validation

if __name__ == "__main__":
    print("Testing Control Flow Operations")
    print("=" * 50)
    
    test_simple_goto()
```

## Phase 3: Conditional Control Flow

### Task 3.1: Implement `if-goto LABEL`

**Objective:** Implement conditional jumps using the choice primitive.

**Implementation:**

```python
def if_goto_operation(self, label_name):
    """
    Implement conditional goto using choice primitive
    Implements: if-goto LABEL
    """
    if not self.current_function:
        raise RuntimeError("if-goto must be used within a function")
    
    if len(self.result_places) < 1:
        raise RuntimeError("No condition for if-goto")
    
    # Get condition value
    condition_place = self.result_places.pop()
    
    # Get target label
    scoped_label = f"{self.current_function}.{label_name}"
    if scoped_label not in self.labels:
        raise RuntimeError(f"Undefined label: {label_name}")
    
    target_place = self.labels[scoped_label]
    current_context = self._get_current_execution_context()
    
    # Create continue context for false branch
    continue_place = self.net.add_place(
        self.get_unique_place_name("if_continue")
    )
    
    # Create choice transition (choice primitive)
    def choice_func(tokens):
        condition = tokens[0].value
        exec_token = tokens[1]
        
        if condition != 0:  # Non-zero is true
            return [exec_token]  # Route to target (first output)
        else:
            return [exec_token]  # Route to continue (second output)
    
    choice_transition = self.net.add_transition(
        self.get_unique_transition_name(f"if_goto_{label_name}"),
        choice_func
    )
    
    # Wire the choice (condition and execution context as inputs)
    self.net.add_arc(condition_place, choice_transition)
    self.net.add_arc(current_context, choice_transition)
    
    # Two possible outputs: target or continue
    self.net.add_arc(choice_transition, target_place)
    self.net.add_arc(choice_transition, continue_place)
    
    # Update execution context to continue place
    # (The choice will route to target if condition is true)
    self.current_execution_context = continue_place
    
    print(f"Created if-goto to label {label_name}")
    return choice_transition
```

### Task 3.2: Test Conditional Control Flow

**Add to test_control_flow.py:**

```python
def test_if_goto():
    """Test conditional goto operation"""
    print("\n=== Testing If-Goto ===")
    
    commands = [
        ("function", "Test.if_goto", 0),
        ("push", "constant", 1),         # Push true condition
        ("if-goto", "TRUE_BRANCH"),      # Should jump
        ("push", "constant", 999),       # Should be skipped
        ("goto", "END"),
        ("label", "TRUE_BRANCH"),
        ("push", "constant", 42),        # Should execute
        ("label", "END"),
        ("return",),
        
        ("call", "Test.if_goto", 0),
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [42] (true branch taken)")
    
    return True  # Implement proper validation

def test_if_goto_false():
    """Test if-goto with false condition"""
    print("\n=== Testing If-Goto False ===")
    
    commands = [
        ("function", "Test.if_goto_false", 0),
        ("push", "constant", 0),         # Push false condition
        ("if-goto", "TRUE_BRANCH"),      # Should NOT jump
        ("push", "constant", 42),        # Should execute
        ("goto", "END"),
        ("label", "TRUE_BRANCH"),
        ("push", "constant", 999),       # Should be skipped
        ("label", "END"),
        ("return",),
        
        ("call", "Test.if_goto_false", 0),
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [42] (false branch, no jump)")
    
    return True  # Implement proper validation
```

## Phase 4: Integration and Testing

### Task 4.1: Update Multi-Core Execution

**Objective:** Ensure control flow works with distributed multi-core execution.

**Update level analysis:**

```python
def _analyze_execution_dependencies(self):
    """
    Enhanced dependency analysis including control flow
    """
    dependencies = {}
    reverse_deps = {}
    
    # Initialize all transitions
    for trans_name, transition in self.net.transitions.items():
        dependencies[trans_name] = []
        reverse_deps[trans_name] = []
    
    # Analyze data flow dependencies
    for trans_name, transition in self.net.transitions.items():
        for input_place in transition.in_places:
            # Find producer of this place
            for producer_name, producer in self.net.transitions.items():
                if input_place in producer.out_places:
                    dependencies[trans_name].append(producer_name)
                    reverse_deps[producer_name].append(trans_name)
    
    # Analyze control flow dependencies
    for trans_name, transition in self.net.transitions.items():
        if trans_name.startswith('goto_') or trans_name.startswith('if_goto_'):
            # Control flow operations create additional dependencies
            # Conservative approach: they depend on all previous operations
            # in the same function
            pass
    
    # Rest of existing topological sort logic...
    return {
        'dependencies': dependencies,
        'reverse_deps': reverse_deps,
        'execution_levels': self._compute_execution_levels(dependencies)
    }
```

### Task 4.2: Comprehensive Testing

**Create integration test:** `test_integration.py`

```python
#!/usr/bin/env python3
"""
Integration tests for all new Petri net VM features
"""

import sys
import os
sys.path.append('.')

from Petri.VMToPetri import VMToPetriTranslator

def test_factorial_iterative():
    """Test iterative factorial using local variables and control flow"""
    print("=== Testing Iterative Factorial ===")
    
    commands = [
        ("function", "Math.factorial", 2),  # 2 locals: result, counter
        
        # Initialize result = 1, counter = argument
        ("push", "constant", 1),
        ("pop", "local", 0),              # result = 1
        ("push", "argument", 0),
        ("pop", "local", 1),              # counter = n
        
        ("label", "LOOP"),
        # Check if counter <= 1
        ("push", "local", 1),             # Push counter
        ("push", "constant", 1),
        ("gt",),                          # counter > 1?
        ("if-goto", "CONTINUE"),          # If yes, continue loop
        ("goto", "END"),                  # Else, end loop
        
        ("label", "CONTINUE"),
        # result = result * counter
        ("push", "local", 0),             # Push result
        ("push", "local", 1),             # Push counter
        ("mul",),                         # result * counter
        ("pop", "local", 0),              # Store back to result
        
        # counter = counter - 1
        ("push", "local", 1),             # Push counter
        ("push", "constant", 1),
        ("sub",),                         # counter - 1
        ("pop", "local", 1),              # Store back to counter
        
        ("goto", "LOOP"),                 # Repeat loop
        
        ("label", "END"),
        ("push", "local", 0),             # Return result
        ("return",),
        
        # Main program: calculate 5!
        ("push", "constant", 5),
        ("call", "Math.factorial", 1),
        # Result should be 120
    ]
    
    translator = VMToPetriTranslator()
    result = translator.execute_program(commands)
    
    print(f"Result: {result}")
    print(f"Expected: [120] (5! = 120)")
    
    if result and result[-1] == 120:
        print("✅ Iterative factorial test PASSED")
        return True
    else:
        print("❌ Iterative factorial test FAILED")
        return False

if __name__ == "__main__":
    print("Integration Testing - All Features")
    print("=" * 50)
    
    test_factorial_iterative()
```

## Validation and Testing Strategy

### Unit Test Checklist

For each new operation, create tests that verify:

- ✅ **Basic functionality**: Operation works in isolation
- ✅ **Error handling**: Proper error messages for invalid usage
- ✅ **Memory optimization**: New places participate in lifetime analysis
- ✅ **Multi-core execution**: Operations work with distributed coordination
- ✅ **Integration**: Operations work together with existing features

### Integration Test Checklist

- ✅ **Complex programs**: Multiple features working together
- ✅ **Function calls**: New operations work within function contexts
- ✅ **Control flow patterns**: Loops, conditionals, nested structures
- ✅ **Performance**: Memory usage and execution time remain reasonable

### Regression Test Checklist

- ✅ **Existing tests pass**: All current tests continue to work
- ✅ **Assembly generation**: Multi-core ROM generation still works
- ✅ **Statistics**: Network analysis includes new operation types
- ✅ **Documentation**: Examples and docs are updated

## Debugging and Troubleshooting

### Common Issues

**Issue: Control flow breaks multi-core execution**
- *Symptom*: Cores hang or don't terminate properly
- *Solution*: Verify control flow operations participate in level analysis
- *Debug*: Check execution level assignments include control flow

**Issue: Local variables not found**
- *Symptom*: RuntimeError about undefined local variables
- *Solution*: Ensure local places are created during function definition
- *Debug*: Print local place names and function contexts

**Issue: Memory optimization fails**
- *Symptom*: No memory savings or optimization errors
- *Solution*: Verify new operations participate in lifetime analysis
- *Debug*: Print place lifetimes and memory allocation maps

### Debug Utilities

Add debugging methods to help with development:

```python
def debug_print_state(self):
    """Print current VM state for debugging"""
    print(f"Current function: {self.current_function}")
    print(f"Result places: {[p.name for p in self.result_places]}")
    print(f"Call stack depth: {len(self.call_stack)}")
    print(f"Labels defined: {list(self.labels.keys())}")
    print(f"Execution context: {self.current_execution_context.name if self.current_execution_context else None}")

def debug_print_network(self):
    """Print network structure for debugging"""
    print(f"Places: {len(self.net.places)}")
    print(f"Transitions: {len(self.net.transitions)}")
    print(f"Arcs: {len(self.net.arcs)}")
    
    for name, place in self.net.places.items():
        if place.has_token():
            print(f"  {name}: {[t.value for t in place.tokens]}")
```

This implementation guide provides concrete steps and code examples for extending the Petri Net VM while maintaining its architectural integrity and performance characteristics.