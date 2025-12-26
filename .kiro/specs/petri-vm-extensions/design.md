# Petri Net VM Extensions - Technical Design

## Design Overview

This document outlines the technical approach for extending the Petri Net VM with local variables, arithmetic operations, and control flow while maintaining pure Petri net semantics and distributed execution capabilities.

## Core Design Principles

### 1. Pure Petri Net Semantics
- **No hidden state**: All program state exists as tokens in places
- **Structural execution**: Control flow through place/transition topology, not program counters
- **Six primitives only**: source, choice, dup, drop, join, loop

### 2. Distributed Execution Preservation
- **Level-based coordination**: New operations must fit into execution level analysis
- **No coordinator**: Control flow must not require centralized coordination
- **Self-termination**: Cores must still self-terminate via level barriers

### 3. Memory Optimization Integration
- **Place lifetime analysis**: New operations must participate in lifetime tracking
- **Memory reuse**: Local variables and control flow places must be optimizable
- **Dependency tracking**: Control flow dependencies must be analyzable

## Feature Design Details

### Phase 1: Local Variable Operations

#### `pop local N` Implementation

**Petri Net Mapping:**
```
[stack_top] → [pop_local_N] → [local_N]
```

**Technical Approach:**
1. **Place Management**: Local variables are places scoped to function call frames
2. **Memory Allocation**: Local places get memory locations during optimization
3. **Lifetime Tracking**: Local variables live from function start to function end

**Implementation Steps:**
```python
def pop_local(self, index):
    """Store top stack element to local variable"""
    if not self.current_function:
        raise RuntimeError("No function context for local variable")
    
    if len(self.result_places) < 1:
        raise RuntimeError("No value to pop")
    
    # Get the value to store
    value_place = self.result_places.pop()
    
    # Get or create local variable place
    local_place_name = f"local_{self.current_function}_{index}"
    local_place = self._get_or_create_local_place(local_place_name)
    
    # Create assignment transition (consumes value, updates local)
    assign_transition = self.net.add_transition(
        self.get_unique_transition_name(f"pop_local_{index}"),
        lambda tokens: tokens[0]  # Pass through the value
    )
    
    # Wire: value_place → assign_transition → local_place
    self.net.add_arc(value_place, assign_transition)
    self.net.add_arc(assign_transition, local_place)
```

**Memory Optimization Impact:**
- Local variables have function-scoped lifetimes
- Can reuse memory from previous function's locals
- Participate in place lifetime analysis

#### Enhanced `push local N`

**Current Issues:**
- Needs better error handling for uninitialized locals
- Should work reliably with memory optimization

**Improvements:**
```python
def push_local(self, index):
    """Enhanced local variable access with better error handling"""
    # Verify function context and local existence
    # Create proper dup transition for memory optimization
    # Handle uninitialized locals gracefully
```

### Phase 2: Arithmetic Extensions

#### `mul` Operation Implementation

**Petri Net Mapping:**
```
[operand_a] → [mul_transition] → [result]
[operand_b] →
```

**Technical Approach:**
```python
def mul_operation(self):
    """Implement multiplication using binary operation pattern"""
    if len(self.result_places) < 2:
        raise RuntimeError("Not enough operands for mul operation")
    
    b_place = self.result_places.pop()
    a_place = self.result_places.pop()
    result_place = self.net.add_place(self.get_unique_place_name("mul_result"))
    
    def mul_op(tokens):
        a_val = tokens[0].value
        b_val = tokens[1].value
        return Token(a_val * b_val)
    
    mul_transition = self.net.add_transition(
        self.get_unique_transition_name("mul"), 
        mul_op
    )
    
    # Wire the operation
    self.net.add_arc(a_place, mul_transition)
    self.net.add_arc(b_place, mul_transition)
    self.net.add_arc(mul_transition, result_place)
    
    self.result_places.append(result_place)
    return result_place
```

**Multi-Core Integration:**
- Multiplication fits existing binary operation pattern
- No special coordination requirements
- Participates in level-based execution analysis

#### `div` Operation Implementation

**Technical Considerations:**
- Integer division with truncation toward zero
- Division by zero handling (VM specification dependent)
- Same pattern as other binary operations

### Phase 3: Control Flow Design

#### Label Management

**Design Challenge:**
Control flow in Petri nets requires structural representation, not program counter jumps.

**Approach: Control Flow Places**
```python
class ControlFlowManager:
    def __init__(self):
        self.labels = {}  # label_name → control_place
        self.pending_jumps = []  # Jumps waiting for label resolution
        
    def define_label(self, label_name):
        """Create a control flow place for this label"""
        control_place = self.net.add_place(f"label_{label_name}")
        self.labels[label_name] = control_place
        return control_place
        
    def create_goto(self, label_name):
        """Create unconditional jump to label"""
        # Implementation depends on current execution context
        pass
```

#### `goto LABEL` Implementation

**Petri Net Challenge:**
Traditional goto changes program counter, but Petri nets have no program counter.

**Solution: Control Flow Tokens**
```
Current execution context → [goto_transition] → [label_place]
                                              → [skip_subsequent_operations]
```

**Technical Approach:**
1. **Control tokens**: Special tokens that carry execution context
2. **Choice transitions**: Route control tokens to appropriate labels
3. **Execution guards**: Operations only fire when control token is present

**Implementation Strategy:**
```python
def goto_operation(self, label_name):
    """Implement goto using control flow tokens"""
    # Create control flow transition that routes execution
    # to the target label's control place
    
    if label_name not in self.labels:
        raise RuntimeError(f"Undefined label: {label_name}")
    
    target_place = self.labels[label_name]
    
    # Create goto transition (choice primitive)
    goto_transition = self.net.add_transition(
        self.get_unique_transition_name(f"goto_{label_name}"),
        lambda tokens: tokens  # Pass control token through
    )
    
    # Wire current execution context to target label
    current_context = self._get_current_execution_context()
    self.net.add_arc(current_context, goto_transition)
    self.net.add_arc(goto_transition, target_place)
```

#### `if-goto LABEL` Implementation

**Petri Net Mapping (Choice Primitive):**
```
[condition] → [if_goto_transition] → [label_place] (if true)
                                  → [continue_place] (if false)
```

**Technical Approach:**
```python
def if_goto_operation(self, label_name):
    """Implement conditional goto using choice primitive"""
    if len(self.result_places) < 1:
        raise RuntimeError("No condition for if-goto")
    
    condition_place = self.result_places.pop()
    target_place = self.labels[label_name]
    continue_place = self._get_current_execution_context()
    
    # Create choice transition
    def choice_op(tokens):
        condition = tokens[0].value
        if condition != 0:  # Non-zero is true
            return [Token("goto")]  # Route to target
        else:
            return [Token("continue")]  # Route to continue
    
    choice_transition = self.net.add_transition(
        self.get_unique_transition_name(f"if_goto_{label_name}"),
        choice_op
    )
    
    # Wire the choice
    self.net.add_arc(condition_place, choice_transition)
    self.net.add_arc(choice_transition, target_place)
    self.net.add_arc(choice_transition, continue_place)
```

### Phase 4: Advanced Features

#### Recursive Function Support

**Current State:**
- Basic function calls work
- Call stack management exists
- Need to handle deeper recursion

**Enhancements Needed:**
1. **Stack depth limits**: Prevent infinite recursion
2. **Memory optimization**: Handle recursive call patterns
3. **Performance**: Optimize repeated function calls

#### Reference Parameters (`pop argument N`)

**Design Challenge:**
Arguments are currently copied to function context. Reference parameters need to modify caller's data.

**Solution: Argument Place Sharing**
```python
def pop_argument(self, index):
    """Store value back to caller's argument location"""
    if not self.call_stack:
        raise RuntimeError("No function call context")
    
    current_call = self.call_stack[-1]
    if index >= len(current_call['arguments']):
        raise RuntimeError(f"Argument index {index} out of bounds")
    
    # Get value to store
    value_place = self.result_places.pop()
    
    # Get caller's argument place (shared reference)
    caller_arg_place = current_call['argument_references'][index]
    
    # Create assignment transition
    # This modifies the caller's data directly
```

## Multi-Core Execution Integration

### Control Flow and Level Analysis

**Challenge:**
Control flow creates dynamic execution paths that complicate static level analysis.

**Solution: Conservative Level Assignment**
```python
def _analyze_control_flow_dependencies(self):
    """Analyze dependencies including control flow"""
    # For control flow operations:
    # 1. goto/if-goto create dependencies on their target labels
    # 2. Labels depend on all operations that might jump to them
    # 3. Conservative approach: assume all possible paths
    
    dependencies = {}
    
    for operation in self.operations:
        if operation.type == "goto":
            # goto depends on current context, targets label
            dependencies[operation] = [self.current_context]
            dependencies[operation.target_label] = [operation]
        elif operation.type == "if-goto":
            # if-goto creates choice dependency
            dependencies[operation] = [self.current_context]
            # Both paths are possible
            dependencies[operation.target_label] = [operation]
            dependencies[operation.continue_context] = [operation]
```

### Distributed Coordination with Control Flow

**Key Insight:**
Control flow doesn't break distributed coordination because:
1. **Static analysis**: We analyze all possible execution paths
2. **Conservative barriers**: Cores wait for all possible operations at each level
3. **Structural semantics**: Control flow is encoded in net structure, not runtime decisions

**Implementation:**
```python
def _assign_control_flow_to_cores(self, execution_plan, num_cores):
    """Assign control flow operations to cores"""
    # Control flow operations (goto, if-goto, labels) are assigned
    # to cores based on their execution level
    # 
    # Key principle: All cores must participate in control flow
    # barriers even if they don't execute the specific operation
    
    for level_idx, level_operations in enumerate(execution_plan['execution_levels']):
        control_flow_ops = [op for op in level_operations 
                           if op.type in ['goto', 'if-goto', 'label']]
        
        if control_flow_ops:
            # All cores must synchronize at control flow levels
            # Even idle cores participate in the barrier
            pass
```

## Memory Optimization Enhancements

### Local Variable Lifetime Analysis

**Enhanced Algorithm:**
```python
def _analyze_local_variable_lifetimes(self):
    """Analyze lifetimes of local variables across function calls"""
    lifetimes = {}
    
    for function_name, function_def in self.function_definitions.items():
        # Local variables live from function start to function end
        function_start_level = self._get_function_start_level(function_name)
        function_end_level = self._get_function_end_level(function_name)
        
        for local_idx in range(function_def['num_locals']):
            local_name = f"local_{function_name}_{local_idx}"
            lifetimes[local_name] = {
                'birth': function_start_level,
                'death': function_end_level,
                'scope': 'function',
                'function': function_name
            }
    
    return lifetimes
```

### Control Flow Place Optimization

**Challenge:**
Control flow creates temporary places (labels, choice results) that need optimization.

**Solution:**
```python
def _optimize_control_flow_places(self):
    """Optimize memory allocation for control flow constructs"""
    # Label places can often be eliminated through structural optimization
    # Choice result places have short lifetimes
    # goto/if-goto temporary places can be reused
    
    control_flow_places = {}
    
    for place_name, place in self.net.places.items():
        if place_name.startswith(('label_', 'choice_', 'goto_')):
            # Analyze control flow place lifetimes
            lifetime = self._analyze_control_flow_place_lifetime(place)
            control_flow_places[place_name] = lifetime
    
    # Apply aggressive optimization to control flow places
    # They often have very short lifetimes and high reuse potential
```

## Implementation Plan

### Phase 1: Foundation (Week 1-2)
1. Implement `pop local N` with proper place management
2. Add `mul` operation following existing binary operation pattern
3. Enhance `push local N` reliability and error handling
4. Update tests to cover new operations

### Phase 2: Control Flow Framework (Week 3-4)
1. Design and implement label management system
2. Create control flow token mechanism
3. Implement `goto LABEL` with structural approach
4. Update level analysis to handle control flow

### Phase 3: Conditional Control Flow (Week 5-6)
1. Implement `if-goto LABEL` using choice primitive
2. Integrate control flow with multi-core execution
3. Update memory optimization for control flow places
4. Comprehensive testing of control flow patterns

### Phase 4: Advanced Features (Week 7-8)
1. Add `div` operation
2. Implement `pop argument N` for reference parameters
3. Enhance recursive function support
4. Performance optimization and scaling tests

### Phase 5: Polish and Documentation (Week 9-10)
1. Comprehensive test suite for all new features
2. Update documentation and examples
3. Performance benchmarking and optimization
4. Code review and quality improvements

## Risk Mitigation

### Technical Risks

**Risk: Control flow breaks Petri net semantics**
- *Mitigation*: Use structural representation, not runtime program counters
- *Validation*: Verify all control flow maps to choice/join primitives

**Risk: Multi-core coordination becomes complex**
- *Mitigation*: Conservative level analysis, maintain barrier-based coordination
- *Validation*: Test control flow with multiple core counts

**Risk: Memory optimization becomes ineffective**
- *Mitigation*: Enhance lifetime analysis for new operation types
- *Validation*: Benchmark memory usage improvements

### Implementation Risks

**Risk: Feature creep and complexity**
- *Mitigation*: Implement in phases, maintain clear boundaries
- *Validation*: Regular code reviews and complexity metrics

**Risk: Regression in existing functionality**
- *Mitigation*: Comprehensive regression testing
- *Validation*: All existing tests must pass

**Risk: Performance degradation**
- *Mitigation*: Performance testing at each phase
- *Validation*: Benchmark against baseline implementation

This design provides a clear technical roadmap for extending the Petri Net VM while preserving its core architectural strengths.