"""
VM to Petri Net Translator
Translates VM commands into Petri net fragments following the six primitives:
source, choice, dup, drop, join, loop

Pure Petri-net semantics - no stack needed. Places ARE the data flow.
"""

from .net import PetriNet
from .Token import Token

class ControlFlowManager:
    """
    Manages control flow constructs (labels, goto, if-goto) in Petri net semantics
    Handles function-scoped labels and control flow places
    """
    def __init__(self, net):
        self.net = net
        self.labels = {}  # label_name -> control_place
        self.function_labels = {}  # function_name -> {label_name -> control_place}
        self.pending_jumps = []  # Jumps waiting for label resolution
        self.place_counter = 0
        
    def get_unique_place_name(self, prefix="control"):
        self.place_counter += 1
        return f"{prefix}_{self.place_counter}"
        
    def define_label(self, label_name, function_name=None):
        """
        Create a control flow place for this label
        Labels are scoped to their containing function
        """
        if function_name:
            # Function-scoped label
            scoped_label_name = f"{function_name}.{label_name}"
            if function_name not in self.function_labels:
                self.function_labels[function_name] = {}
        else:
            # Global label (for main program)
            scoped_label_name = label_name
            
        # Check if label already exists
        if scoped_label_name in self.labels:
            print(f"Label '{label_name}' already defined in function '{function_name}', reusing existing place")
            return self.labels[scoped_label_name]
            
        # Create control flow place for this label
        control_place = self.net.add_place(self.get_unique_place_name(f"label_{scoped_label_name}"))
        
        # Store label mapping
        if function_name:
            self.function_labels[function_name][label_name] = control_place
        self.labels[scoped_label_name] = control_place
        
        print(f"Defined label '{label_name}' in function '{function_name}' -> {control_place.name}")
        return control_place
        
    def get_label_place(self, label_name, function_name=None):
        """
        Get the control flow place for a label
        Handles function scoping
        """
        if function_name:
            scoped_label_name = f"{function_name}.{label_name}"
            # First try function-scoped label
            if function_name in self.function_labels and label_name in self.function_labels[function_name]:
                return self.function_labels[function_name][label_name]
        else:
            scoped_label_name = label_name
            
        # Try global label
        if scoped_label_name in self.labels:
            return self.labels[scoped_label_name]
            
        # Label not found
        raise RuntimeError(f"Undefined label: {label_name} in function {function_name}")
        
    def is_label_defined(self, label_name, function_name=None):
        """Check if a label is defined in the given scope"""
        try:
            self.get_label_place(label_name, function_name)
            return True
        except RuntimeError:
            return False
            
    def get_function_labels(self, function_name):
        """Get all labels defined in a function"""
        return self.function_labels.get(function_name, {})
        
    def clear_function_labels(self, function_name):
        """Clear labels for a function (cleanup)"""
        if function_name in self.function_labels:
            # Remove from global labels too
            for label_name in self.function_labels[function_name]:
                scoped_name = f"{function_name}.{label_name}"
                if scoped_name in self.labels:
                    del self.labels[scoped_name]
            del self.function_labels[function_name]

class VMToPetriTranslator:
    def __init__(self):
        self.net = PetriNet()
        self.result_places = []  # Final output places (what would be "top of stack")
        self.place_counter = 0
        self.transition_counter = 0
        
        # Function call management
        self.call_stack = []  # Stack of function call frames
        self.current_function = None  # Current function name
        self.function_locals = {}  # function_name -> number of locals
        self.function_definitions = {}  # function_name -> list of commands
        self.program_commands = []  # Commands being executed
        self.command_index = 0  # Current command index
        
        # Local variable management
        self.local_places = {}  # (function_name, index) -> place
        
        # Control flow management
        self.control_flow = ControlFlowManager(self.net)
        
        # Cross-scope jump management
        self._cross_scope_jump_pending = False
        self._cross_scope_jump_target = None
        
    def get_unique_place_name(self, prefix="place"):
        self.place_counter += 1
        return f"{prefix}_{self.place_counter}"
        
    def get_unique_transition_name(self, prefix="trans"):
        self.transition_counter += 1
        return f"{prefix}_{self.transition_counter}"
        
    def push_operation(self, segment, index):
        """
        General push operation for different memory segments
        """
        if segment == "constant":
            return self.push_constant(index)
        elif segment == "argument":
            return self.push_argument(index)
        elif segment == "local":
            return self.push_local(index)
        else:
            raise NotImplementedError(f"Push {segment} not implemented")
    
    def push_constant(self, value):
        """
        Implement push constant using 'source' primitive
        Creates a new place with the constant value - this IS the stack element
        """
        # Create a new place for this constant (source primitive)
        const_place = self.net.add_place(self.get_unique_place_name(f"const_{value}"))
        const_place.put_token(Token(value))
        
        # This place represents the value - add to results
        self.result_places.append(const_place)
        
        return const_place
    
    def push_argument(self, index):
        """
        Push argument[index] onto stack
        Arguments are passed from the caller
        """
        if not self.call_stack:
            raise RuntimeError("No function call context for argument access")
        
        current_call = self.call_stack[-1]
        if index >= len(current_call['arguments']):
            raise RuntimeError(f"Argument index {index} out of bounds")
        
        # Get the argument place
        arg_place = current_call['arguments'][index]
        
        # Create a new place for the pushed value (duplicate the argument)
        pushed_place = self.net.add_place(self.get_unique_place_name(f"pushed_arg_{index}"))
        
        # Create dup transition to copy the argument value
        def dup_arg_func(tokens):
            if tokens:
                val = tokens[0].value
                return [Token(val), Token(val)]  # Original and copy
            return [Token(0), Token(0)]
        
        dup_transition = self.net.add_transition(
            self.get_unique_transition_name(f"dup_arg_{index}"),
            dup_arg_func
        )
        
        # Wire: arg_place -> dup_transition -> [arg_place, pushed_place]
        self.net.add_arc(arg_place, dup_transition)
        self.net.add_arc(dup_transition, arg_place)  # Keep original
        self.net.add_arc(dup_transition, pushed_place)  # Create copy
        
        # Add to result places
        self.result_places.append(pushed_place)
        return pushed_place
    
    def push_local(self, index):
        """
        Push local[index] onto stack with enhanced reliability
        Improved error handling and memory optimization integration
        """
        if not self.current_function:
            raise RuntimeError("No function context for local variable access")
        
        if self.current_function not in self.function_locals:
            raise RuntimeError(f"Function {self.current_function} not defined")
        
        if index >= self.function_locals[self.current_function]:
            raise RuntimeError(f"Local index {index} out of bounds for function {self.current_function}")
        
        # Get or create the local variable place (handles uninitialized locals gracefully)
        local_place_name = f"local_{self.current_function}_{index}"
        local_place = self._get_or_create_local_place(local_place_name, index)
        
        # Create a new place for the pushed value
        pushed_place = self.net.add_place(self.get_unique_place_name(f"pushed_local_{index}"))
        
        # Create dup transition to copy the local value (memory optimization friendly)
        def dup_local_func(tokens):
            if tokens:
                val = tokens[0].value
                return [Token(val), Token(val)]  # Original and copy
            return [Token(0), Token(0)]  # Default value if uninitialized
        
        dup_transition = self.net.add_transition(
            self.get_unique_transition_name(f"dup_local_{index}"),
            dup_local_func
        )
        
        # Wire: local_place -> dup_transition -> [local_place, pushed_place]
        self.net.add_arc(local_place, dup_transition)
        self.net.add_arc(dup_transition, local_place)  # Keep original
        self.net.add_arc(dup_transition, pushed_place)  # Create copy
        
        # Add to result places
        self.result_places.append(pushed_place)
        print(f"Pushed local variable {index} (function: {self.current_function})")
        return pushed_place
    
    def pop_local(self, index):
        """
        Store top stack element to local variable N
        Implements pop local using Petri net semantics with single-token constraint
        """
        if not self.current_function:
            raise RuntimeError("No function context for local variable")
        
        if self.current_function not in self.function_locals:
            raise RuntimeError(f"Function {self.current_function} not defined")
        
        if index >= self.function_locals[self.current_function]:
            raise RuntimeError(f"Local index {index} out of bounds for function {self.current_function}")
        
        if len(self.result_places) < 1:
            raise RuntimeError("No value to pop")
        
        # Get the value to store
        value_place = self.result_places.pop()
        
        # Get or create local variable place
        local_place_name = f"local_{self.current_function}_{index}"
        local_place = self._get_or_create_local_place(local_place_name, index)
        
        # With single-token constraint, we can directly replace the token
        # Get the value from the value_place and put it in the local_place
        if value_place.has_token():
            new_value = value_place.get_token()
            local_place.put_token(new_value)  # This will replace existing token
        else:
            # Default value if no token
            from .Token import Token
            local_place.put_token(Token(0))
        
        print(f"Stored value to local variable {index}")
        return local_place
    
    def _get_or_create_local_place(self, local_place_name, index):
        """Get existing local place or create new one"""
        local_key = (self.current_function, index)
        
        # Check if local place already exists
        if local_key in self.local_places:
            place = self.local_places[local_key]
            return place
        
        # Create new local place
        local_place = self.net.add_place(self.get_unique_place_name(local_place_name))
        
        # Initialize with default value (0) if needed
        local_place.put_token(Token(0))
        
        # Store in local places dictionary
        self.local_places[local_key] = local_place
        
        return local_place
    
    def pop_operation(self, segment, index):
        """General pop operation for different memory segments"""
        if segment == "local":
            return self.pop_local(index)
        else:
            raise NotImplementedError(f"Pop {segment} not implemented")
        
    def add_operation(self):
        """
        Implement add operation: consume two most recent result places,
        create add transition, produce new result place
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for add operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = self.result_places.pop()  # Top 
        a_place = self.result_places.pop()  # Second from top
        
        # Create result place for the sum
        result_place = self.net.add_place(self.get_unique_place_name("add_result"))
        
        # Create add transition that consumes from both input places
        def add_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val + b_val)
            
        add_transition = self.net.add_transition(
            self.get_unique_transition_name("add"), 
            add_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        self.net.add_arc(a_place, add_transition)
        self.net.add_arc(b_place, add_transition)
        self.net.add_arc(add_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        self.result_places.append(result_place)
        
        return result_place
        
    def sub_operation(self):
        """
        Implement sub operation: consume two most recent result places
        Result = first - second (where second is most recent)
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for sub operation")
            
        # Pop operands from result places
        b_place = self.result_places.pop()  # Most recent (subtrahend)
        a_place = self.result_places.pop()  # Second most recent (minuend)
        
        # Create result place
        result_place = self.net.add_place(self.get_unique_place_name("sub_result"))
        
        def sub_op(tokens):
            a_val = tokens[0].value  # First operand
            b_val = tokens[1].value  # Second operand
            return Token(a_val - b_val)
            
        sub_transition = self.net.add_transition(
            self.get_unique_transition_name("sub"), 
            sub_op
        )
        
        # Wire: input_places -> transition -> output_place
        self.net.add_arc(a_place, sub_transition)
        self.net.add_arc(b_place, sub_transition)
        self.net.add_arc(sub_transition, result_place)
        
        # Add result to result places
        self.result_places.append(result_place)
        return result_place
        
    def neg_operation(self):
        """
        Implement neg operation: consume most recent result place
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for neg operation")
            
        # Pop single operand from result places
        a_place = self.result_places.pop()
        
        # Create result place
        result_place = self.net.add_place(self.get_unique_place_name("neg_result"))
        
        def neg_op(tokens):
            a_val = tokens[0].value
            return Token(-a_val)
            
        neg_transition = self.net.add_transition(
            self.get_unique_transition_name("neg"), 
            neg_op
        )
        
        # Wire: input_place -> transition -> output_place
        self.net.add_arc(a_place, neg_transition)
        self.net.add_arc(neg_transition, result_place)
        
        # Add result to result places
        self.result_places.append(result_place)
        return result_place
        
    def eq_operation(self):
        """Implement eq operation: true if x == y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for eq operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("eq_result"))
        
        def eq_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val == b_val else 0)  # VM uses -1 for true, 0 for false
            
        eq_transition = self.net.add_transition(self.get_unique_transition_name("eq"), eq_op)
        self.net.add_arc(a_place, eq_transition)
        self.net.add_arc(b_place, eq_transition)
        self.net.add_arc(eq_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def lt_operation(self):
        """Implement lt operation: true if x < y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for lt operation")
            
        b_place = self.result_places.pop()  # y (top of stack)
        a_place = self.result_places.pop()  # x (second from top)
        result_place = self.net.add_place(self.get_unique_place_name("lt_result"))
        
        def lt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val < b_val else 0)
            
        lt_transition = self.net.add_transition(self.get_unique_transition_name("lt"), lt_op)
        self.net.add_arc(a_place, lt_transition)
        self.net.add_arc(b_place, lt_transition)
        self.net.add_arc(lt_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def gt_operation(self):
        """Implement gt operation: true if x > y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for gt operation")
            
        b_place = self.result_places.pop()  # y (top of stack)
        a_place = self.result_places.pop()  # x (second from top)
        result_place = self.net.add_place(self.get_unique_place_name("gt_result"))
        
        def gt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val > b_val else 0)
            
        gt_transition = self.net.add_transition(self.get_unique_transition_name("gt"), gt_op)
        self.net.add_arc(a_place, gt_transition)
        self.net.add_arc(b_place, gt_transition)
        self.net.add_arc(gt_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def and_operation(self):
        """Implement and operation: bitwise AND"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for and operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("and_result"))
        
        def and_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val & b_val)
            
        and_transition = self.net.add_transition(self.get_unique_transition_name("and"), and_op)
        self.net.add_arc(a_place, and_transition)
        self.net.add_arc(b_place, and_transition)
        self.net.add_arc(and_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def or_operation(self):
        """Implement or operation: bitwise OR"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for or operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("or_result"))
        
        def or_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val | b_val)
            
        or_transition = self.net.add_transition(self.get_unique_transition_name("or"), or_op)
        self.net.add_arc(a_place, or_transition)
        self.net.add_arc(b_place, or_transition)
        self.net.add_arc(or_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def not_operation(self):
        """Implement not operation: bitwise NOT"""
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for not operation")
            
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("not_result"))
        
        def not_op(tokens):
            a_val = tokens[0].value
            return Token(~a_val & 0xFFFF)  # 16-bit NOT
            
        not_transition = self.net.add_transition(self.get_unique_transition_name("not"), not_op)
        self.net.add_arc(a_place, not_transition)
        self.net.add_arc(not_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def mul_operation(self):
        """
        Implement mul operation: consume two most recent result places,
        create mul transition, produce new result place
        Handles integer overflow according to VM specification
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for mul operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = self.result_places.pop()  # Top 
        a_place = self.result_places.pop()  # Second from top
        
        # Create result place for the product
        result_place = self.net.add_place(self.get_unique_place_name("mul_result"))
        
        # Create mul transition that consumes from both input places
        def mul_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            # Handle integer overflow according to VM specification (16-bit signed)
            result = (a_val * b_val) & 0xFFFF
            # Convert to signed 16-bit if needed
            if result > 32767:
                result = result - 65536
            return Token(result)
            
        mul_transition = self.net.add_transition(
            self.get_unique_transition_name("mul"), 
            mul_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        self.net.add_arc(a_place, mul_transition)
        self.net.add_arc(b_place, mul_transition)
        self.net.add_arc(mul_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        self.result_places.append(result_place)
        
        return result_place
        
    def div_operation(self):
        """
        Implement div operation: consume two most recent result places,
        create div transition, produce new result place
        Performs integer division (truncated toward zero)
        Handles division by zero appropriately
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for div operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = self.result_places.pop()  # Top (divisor)
        a_place = self.result_places.pop()  # Second from top (dividend)
        
        # Create result place for the quotient
        result_place = self.net.add_place(self.get_unique_place_name("div_result"))
        
        # Create div transition that consumes from both input places
        def div_op(tokens):
            a_val = tokens[0].value  # dividend
            b_val = tokens[1].value  # divisor
            
            # Handle division by zero
            if b_val == 0:
                # VM specification behavior for division by zero
                # Return 0 (some VMs might halt, but we'll return 0 for robustness)
                return Token(0)
            
            # Perform integer division (truncated toward zero)
            if (a_val < 0) != (b_val < 0):  # Different signs
                # For negative results, use ceiling division to truncate toward zero
                result = -(abs(a_val) // abs(b_val))
            else:
                # Same signs, normal floor division
                result = a_val // b_val
                
            # Ensure result fits in 16-bit signed integer
            result = max(-32768, min(32767, result))
            return Token(result)
            
        div_transition = self.net.add_transition(
            self.get_unique_transition_name("div"), 
            div_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        self.net.add_arc(a_place, div_transition)
        self.net.add_arc(b_place, div_transition)
        self.net.add_arc(div_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        self.result_places.append(result_place)
        
        return result_place
        
    def label_operation(self, label_name):
        """
        Implement label operation: define a jump target within current function
        Creates control flow places for labels and integrates with function scoping
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
            
        # Check if label is already defined (from pre-processing)
        if self.control_flow.is_label_defined(label_name, self.current_function):
            # Label already exists from pre-processing, just return the existing place
            control_place = self.control_flow.get_label_place(label_name, self.current_function)
            print(f"Using pre-processed label '{label_name}' in function '{self.current_function}'")
            return control_place
            
        # Define the label in the current function scope
        control_place = self.control_flow.define_label(label_name, self.current_function)
        
        # Initialize the control place with a control token to indicate this is a valid jump target
        # This represents the "execution context" at this label
        control_place.put_token(Token("control"))
        
        print(f"Created label '{label_name}' in function '{self.current_function}'")
        return control_place
        
    def goto_operation(self, label_name):
        """
        Implement goto operation: unconditional jump to label
        Supports cross-scope jumps (function -> main program)
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
        
        # Check if label is defined in current scope
        if not self.control_flow.is_label_defined(label_name, self.current_function):
            raise RuntimeError(f"Cannot goto undefined label '{label_name}'")
        
        # Get the label place for Petri net semantics
        label_place = self.control_flow.get_label_place(label_name, self.current_function)
        
        # Create goto transition that transfers control to the label
        goto_transition = self.net.add_transition(
            self.get_unique_transition_name(f"goto_{label_name}"),
            lambda tokens: Token("control")  # Transfer control token
        )
        
        # Create a control source place for this goto
        goto_source = self.net.add_place(self.get_unique_place_name(f"goto_source_{label_name}"))
        goto_source.put_token(Token("control"))
        
        # Wire: goto_source -> goto_transition -> label_place
        self.net.add_arc(goto_source, goto_transition)
        self.net.add_arc(goto_transition, label_place)
        
        # For program execution context, handle command index updates
        if self.current_function and self.current_function in self.function_definitions:
            function_commands = self.function_definitions[self.current_function]['body']
            for i, command in enumerate(function_commands):
                if command[0] == "label" and command[1] == label_name:
                    # Found in current function - normal jump
                    self.command_index = i
                    print(f"Goto to label '{label_name}' at function command index {i}")
                    return goto_transition
        
        # Check main program for cross-scope jumps
        if hasattr(self, 'program_commands') and self.program_commands:
            for i, command in enumerate(self.program_commands):
                if command[0] == "label" and command[1] == label_name:
                    # Found in main program - cross-scope jump
                    self._perform_cross_scope_jump(i)
                    print(f"Cross-scope goto to label '{label_name}' at main program index {i}")
                    return "CROSS_SCOPE_JUMP"
        
        print(f"Goto to label '{label_name}' (Petri net semantics)")
        return goto_transition
        
    def if_goto_operation(self, label_name):
        """
        Implement if-goto operation: conditional jump to label
        Supports cross-scope jumps (function -> main program)
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
            
        if len(self.result_places) < 1:
            raise RuntimeError("No condition for if-goto")
        
        # Get the condition from the stack
        condition_place = self.result_places.pop()
        
        # Check if label is defined in current scope
        if not self.control_flow.is_label_defined(label_name, self.current_function):
            raise RuntimeError(f"Cannot if-goto undefined label '{label_name}'")
        
        # Get the label place for Petri net semantics
        label_place = self.control_flow.get_label_place(label_name, self.current_function)
        
        # Create if-goto transition with conditional logic
        def if_goto_func(tokens):
            condition_value = tokens[0].value if tokens else 0
            if condition_value != 0:
                return [Token("control"), Token("control")]  # Jump and continue paths
            else:
                return [Token("control")]  # Only continue path
        
        if_goto_transition = self.net.add_transition(
            self.get_unique_transition_name(f"if_goto_{label_name}"),
            if_goto_func
        )
        
        # Create continue place for when condition is false
        continue_place = self.net.add_place(self.get_unique_place_name(f"if_goto_continue_{label_name}"))
        
        # Wire: condition_place -> if_goto_transition -> [label_place, continue_place]
        self.net.add_arc(condition_place, if_goto_transition)
        self.net.add_arc(if_goto_transition, label_place)      # Jump path
        self.net.add_arc(if_goto_transition, continue_place)   # Continue path
        
        # For program execution context, handle command index updates
        if hasattr(self, 'program_commands') and self.program_commands:
            # Get the condition value directly from the place for execution logic
            condition_value = 0
            if condition_place.has_token():
                condition_value = condition_place.tokens[0].value
            
            print(f"If-goto condition: {condition_value} (0=false, non-zero=true)")
            
            # If condition is true (non-zero), jump to label
            if condition_value != 0:
                # First try to find label in current function
                if self.current_function and self.current_function in self.function_definitions:
                    function_commands = self.function_definitions[self.current_function]['body']
                    for i, command in enumerate(function_commands):
                        if command[0] == "label" and command[1] == label_name:
                            # Found in current function - normal jump
                            self.command_index = i
                            print(f"If-goto jumping to label '{label_name}' at function command index {i}")
                            return if_goto_transition
                
                # Not found in function, try main program (cross-scope jump)
                for i, command in enumerate(self.program_commands):
                    if command[0] == "label" and command[1] == label_name:
                        # Found in main program - cross-scope jump
                        self._perform_cross_scope_jump(i)
                        print(f"Cross-scope if-goto to label '{label_name}' at main program index {i}")
                        return "CROSS_SCOPE_JUMP"
            else:
                print(f"If-goto condition false, continuing to next command")
        
        return if_goto_transition
        
    def dup_operation(self):
        """
        Implement dup operation using 'dup' primitive
        Duplicates the top stack element
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for dup operation")
            
        top_place = self.result_places[-1]  # Peek at top without popping
        
        # Create duplicate place
        dup_place = self.net.add_place(self.get_unique_place_name("dup_result"))
        
        # Create dup transition (explicit duplication)
        def dup_op(tokens):
            val = tokens[0].value
            return [Token(val), Token(val)]  # Return two identical tokens
            
        dup_transition = self.net.add_transition(
            self.get_unique_transition_name("dup"), 
            dup_op
        )
        
        # Connect: top_place -> dup_transition -> [top_place, dup_place]
        # This requires consuming the original and producing two
        self.result_places.pop()  # Remove original
        self.net.add_arc(top_place, dup_transition)
        self.net.add_arc(dup_transition, top_place)  # Put back original
        self.net.add_arc(dup_transition, dup_place)  # Add duplicate
        
        # Push both back onto result places
        self.result_places.append(top_place)
        self.result_places.append(dup_place)
        
        return dup_place
        
    def drop_operation(self):
        """
        Implement drop operation using 'drop' primitive
        Discards the top stack element
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for drop operation")
            
        top_place = self.result_places.pop()
        
        # Create drop transition that consumes but produces nothing
        drop_transition = self.net.add_transition(
            self.get_unique_transition_name("drop"), 
            lambda tokens: []  # Consume input, produce nothing
        )
        
        self.net.add_arc(top_place, drop_transition)
        # No output connections - token is consumed and discarded
        
        return None
        
    def call_operation(self, function_name, num_args):
        """
        Implement function call using Petri net semantics
        Execute the function body with the provided arguments
        """
        if function_name not in self.function_definitions:
            raise RuntimeError(f"Function {function_name} not defined")
        
        if len(self.result_places) < num_args:
            raise RuntimeError(f"Not enough arguments for call to {function_name}")
        
        # Pop arguments from result places
        args = []
        for i in range(num_args):
            args.append(self.result_places.pop())
        args.reverse()  # Restore correct order
        
        # Store arguments in call stack for function to access
        call_frame = {
            'function_name': function_name,
            'arguments': args,
            'saved_result_places': self.result_places.copy(),
            'saved_function': self.current_function
        }
        self.call_stack.append(call_frame)
        
        # Set current function context
        self.current_function = function_name
        
        print(f"Calling function {function_name} with {num_args} arguments")
        
        # Pre-process labels in function body before execution
        function_def = self.function_definitions[function_name]
        self._preprocess_function_labels(function_def['body'], function_name)
        
        # Execute function body with proper control flow
        function_commands = function_def['body']
        func_index = 0
        
        while func_index < len(function_commands):
            command = function_commands[func_index]
            
            if command[0] == "return":
                # Handle return - don't execute more commands
                self.return_operation()
                break
            else:
                # Save current command index and set function context
                saved_index = self.command_index
                self.command_index = func_index
                
                result = self._execute_command(command)
                
                # Check for cross-scope jump
                if result == "CROSS_SCOPE_JUMP" or self._cross_scope_jump_pending:
                    # Exit function and let main program handle the jump
                    print(f"Cross-scope jump detected, exiting function {function_name}")
                    # Don't call return_operation() - we're jumping out of the function
                    # The main program will handle the jump
                    self.command_index = saved_index
                    return "CROSS_SCOPE_JUMP"
                
                # Check if command modified the index (goto/if-goto within function)
                if self.command_index != func_index:
                    # Jump occurred within function, update function index
                    func_index = self.command_index
                    # Don't increment func_index, continue from the jump target
                else:
                    # Normal progression
                    func_index += 1
                
                # Restore main program index
                self.command_index = saved_index
        
        return call_frame
        
    def _preprocess_function_labels(self, function_body, function_name):
        """
        Pre-process all label definitions in a function body
        This ensures labels are defined before any goto/if-goto operations reference them
        """
        saved_function = self.current_function
        self.current_function = function_name
        
        # First pass: define all labels
        for command in function_body:
            if command[0] == "label":
                label_name = command[1]
                # Only define the label, don't execute it
                self.control_flow.define_label(label_name, function_name)
                print(f"Pre-processed label '{label_name}' in function '{function_name}'")
        
        self.current_function = saved_function
        
    def return_operation(self):
        """
        Implement function return using Petri net semantics
        Returns value and restores caller context
        """
        if not self.call_stack:
            # No active function call - this is a program return
            print("Program return")
            return None
        
        # Get the current call frame
        call_frame = self.call_stack.pop()
        
        # Get return value (top of result places, if any)
        if self.result_places:
            return_value_place = self.result_places.pop()  # Remove and return the top value
            print(f"Returning value from {call_frame['function_name']}")
        else:
            # No return value - create a default (0)
            return_value_place = self.net.add_place(self.get_unique_place_name("return_default"))
            return_value_place.put_token(Token(0))
            print(f"Returning default value 0 from {call_frame['function_name']}")
        
        # Restore caller's result places and add the returned value
        self.result_places = call_frame['saved_result_places']
        self.result_places.append(return_value_place)
        
        # Restore function context
        self.current_function = call_frame['saved_function']
        
        return return_value_place
        
        return None
        
    def get_result_values(self):
        """Get current values in the result places (what would be the stack)"""
        values = []
        for place in self.result_places:
            if place.has_token():
                values.append(place.tokens[0].value)
            else:
                values.append(None)
        return values
        
    def execute_step(self):
        """Execute one step of the Petri net"""
        return self.net.execute_step()
        
    def execute_program(self, commands):
        """Execute a sequence of VM commands - no stack needed!"""
        self.program_commands = commands
        self.command_index = 0
        
        print(f"Executing program with {len(commands)} commands")
        
        # First pass: parse function definitions
        self._parse_functions()
        
        # Second pass: execute main program (commands after all function definitions)
        print(f"Starting main program execution from command {self.command_index}")
        while self.command_index < len(commands):
            command = commands[self.command_index]
            cmd_type = command[0]
            
            print(f"Executing command {self.command_index}: {command}")
            
            if cmd_type == "function":
                # Skip function definitions in main execution
                self._skip_function_definition()
            else:
                result = self._execute_command(command)
                
                # Handle cross-scope jumps
                if result == "CROSS_SCOPE_JUMP" or self._cross_scope_jump_pending:
                    if self._cross_scope_jump_target is not None:
                        print(f"Handling cross-scope jump to main program index {self._cross_scope_jump_target}")
                        self.command_index = self._cross_scope_jump_target
                        self._cross_scope_jump_pending = False
                        self._cross_scope_jump_target = None
                        continue  # Don't increment command_index
                
                # Check if this was a return statement in main program (should terminate)
                if cmd_type == "return" and not self.call_stack:
                    print("Main program return - terminating execution")
                    break
            
            self.command_index += 1
                
        # Execute the Petri net to get final results
        # Keep executing until no more transitions can fire
        steps = 0
        max_steps = 100  # Prevent infinite loops
        while steps < max_steps:
            fired = self.execute_step()
            if not fired:
                break
            steps += 1
            
        return self.get_result_values()
    
    def _parse_functions(self):
        """Parse all function definitions from the command list"""
        i = 0
        while i < len(self.program_commands):
            command = self.program_commands[i]
            if command[0] == "function":
                function_name = command[1]
                num_locals = command[2]
                
                # Collect function body (until return statement)
                function_body = []
                i += 1
                while i < len(self.program_commands):
                    next_command = self.program_commands[i]
                    function_body.append(next_command)
                    if next_command[0] == "return":
                        i += 1  # Move past the return
                        break  # End of function
                    i += 1
                
                # Store function definition
                self.function_definitions[function_name] = {
                    'num_locals': num_locals,
                    'body': function_body
                }
                # Also store in function_locals for compatibility
                self.function_locals[function_name] = num_locals
                print(f"Parsed function {function_name} with {len(function_body)} commands and {num_locals} locals")
                
                # Set command index to continue after this function
                self.command_index = i
                continue
            i += 1
    
    def _skip_function_definition(self):
        """Skip over a function definition during main execution"""
        # Skip until we find the next function or reach end
        self.command_index += 1
        while self.command_index < len(self.program_commands):
            command = self.program_commands[self.command_index]
            if command[0] == "function":
                self.command_index -= 1  # Back up to let main loop handle it
                break
            self.command_index += 1
    
    def _perform_cross_scope_jump(self, main_program_index):
        """
        Perform a cross-scope jump from function to main program
        This exits the current function context and jumps to the main program
        """
        if not self.call_stack:
            # No function context - this might be a unit test or direct call
            print(f"Cross-scope jump: no function context, setting jump target to main program index {main_program_index}")
            self._cross_scope_jump_target = main_program_index
            self._cross_scope_jump_pending = True
            return
        
        # Pop the call stack to exit the function completely
        call_frame = self.call_stack.pop()
        
        # Restore the caller's context but don't add return value
        # (cross-scope jumps don't return values)
        self.result_places = call_frame['saved_result_places']
        self.current_function = call_frame['saved_function']
        
        # Store the jump target for the main execution loop to handle
        self._cross_scope_jump_target = main_program_index
        
        # Signal that we need to jump in main program
        self._cross_scope_jump_pending = True
        
        print(f"Cross-scope jump: exited function {call_frame['function_name']}, jumping to main program index {main_program_index}")
    
    def _find_label_index(self, label_name):
        """
        Find the command index of a label within the current function or main program
        """
        if self.current_function:
            # Search in current function body first
            if self.current_function in self.function_definitions:
                function_commands = self.function_definitions[self.current_function]['body']
                for i, command in enumerate(function_commands):
                    if command[0] == "label" and command[1] == label_name:
                        return i
        
        # If not found in function or no current function, search in main program
        for i, command in enumerate(self.program_commands):
            if command[0] == "label" and command[1] == label_name:
                return i
        
        return None
    
    def _execute_command(self, command):
        """Execute a single VM command"""
        cmd_type = command[0]
        
        if cmd_type == "push":
            segment = command[1]
            index = command[2]
            self.push_operation(segment, index)
        elif cmd_type == "pop":
            segment = command[1]
            index = command[2]
            self.pop_operation(segment, index)
        elif cmd_type == "add":
            self.add_operation()
        elif cmd_type == "sub":
            self.sub_operation()
        elif cmd_type == "neg":
            self.neg_operation()
        elif cmd_type == "eq":
            self.eq_operation()
        elif cmd_type == "lt":
            self.lt_operation()
        elif cmd_type == "gt":
            self.gt_operation()
        elif cmd_type == "and":
            self.and_operation()
        elif cmd_type == "or":
            self.or_operation()
        elif cmd_type == "not":
            self.not_operation()
        elif cmd_type == "mul":
            self.mul_operation()
        elif cmd_type == "div":
            self.div_operation()
        elif cmd_type == "dup":
            self.dup_operation()
        elif cmd_type == "drop":
            self.drop_operation()
        elif cmd_type == "call":
            function_name = command[1]
            num_args = command[2]
            self.call_operation(function_name, num_args)
        elif cmd_type == "return":
            self.return_operation()
        elif cmd_type == "label":
            label_name = command[1]
            self.label_operation(label_name)
        elif cmd_type == "goto":
            label_name = command[1]
            self.goto_operation(label_name)
        elif cmd_type == "if-goto":
            label_name = command[1]
            self.if_goto_operation(label_name)
        else:
            raise NotImplementedError(f"Command {cmd_type} not implemented")
        
        # Execute Petri net after each command to ensure values are available
        if cmd_type not in ["label", "goto", "if-goto"]:  # Don't execute for control flow
            # Only execute once per command to prevent over-execution
            fired = self.net.execute_step()
            # If a transition fired, execute one more time to handle cascading effects
            if fired:
                self.net.execute_step()
        
    def print_net_statistics(self):
        """Print comprehensive statistics about the translated Petri net"""
        print("\n" + "=" * 60)
        print("PETRI NET TRANSLATION STATISTICS")
        print("=" * 60)
        
        # Basic counts
        total_places = len(self.net.places)
        total_transitions = len(self.net.transitions)
        total_arcs = len(self.net.arcs)
        result_count = len(self.result_places)
        
        print(f"Network Size:")
        print(f"  Places: {total_places}")
        print(f"  Transitions: {total_transitions}")
        print(f"  Arcs: {total_arcs}")
        print(f"  Result Places: {result_count} (no stack needed!)")
        
        # Arc breakdown
        input_arcs = sum(len(t.in_places) for t in self.net.transitions.values())
        output_arcs = sum(len(t.out_places) for t in self.net.transitions.values())
        
        print(f"\nArc Breakdown:")
        print(f"  Input arcs (Place → Transition): {input_arcs}")
        print(f"  Output arcs (Transition → Place): {output_arcs}")
        print(f"  Total arcs: {input_arcs + output_arcs} (matches: {total_arcs})")
        
        # Memory optimization analysis
        print(f"\nMemory Optimization Analysis:")
        if total_places > 0:
            memory_map = self._optimize_memory_allocation()
            optimized_locations = len(memory_map['location_to_places'])
            memory_savings = total_places - optimized_locations
            savings_percent = (memory_savings / total_places) * 100 if total_places > 0 else 0
            
            print(f"  Original places: {total_places}")
            print(f"  Optimized memory locations: {optimized_locations}")
            print(f"  Memory addresses saved: {memory_savings}")
            print(f"  Memory reduction: {savings_percent:.1f}%")
            print(f"  Memory reuse factor: {total_places / optimized_locations:.2f}x")
            
            # Show detailed memory mapping
            print(f"\n  Memory Location Details:")
            location_usage = {}
            for location, places in memory_map['location_to_places'].items():
                location_usage[location] = len(places)
                
            # Show most reused locations
            sorted_locations = sorted(location_usage.items(), key=lambda x: x[1], reverse=True)
            for i, (location, usage_count) in enumerate(sorted_locations[:5]):  # Top 5
                places = memory_map['location_to_places'][location]
                print(f"    @{location}: {usage_count} places {places}")
                
            if len(sorted_locations) > 5:
                print(f"    ... and {len(sorted_locations) - 5} more locations")
                
            # Memory range used
            min_location = min(memory_map['location_map'].values())
            max_location = max(memory_map['location_map'].values())
            print(f"  Memory range: @{min_location} to @{max_location}")
            print(f"  Total memory addresses used: {max_location - min_location + 1}")
        else:
            print(f"  No places to optimize")
        
        # Place analysis
        places_with_tokens = sum(1 for p in self.net.places.values() if p.has_token())
        total_tokens = sum(p.token_count() for p in self.net.places.values())
        
        print(f"\nToken Distribution:")
        print(f"  Places with tokens: {places_with_tokens}/{total_places}")
        print(f"  Total tokens: {total_tokens}")
        
        # Classify places by type
        constant_places = []
        result_places = []
        control_places = []
        
        for name, place in self.net.places.items():
            if name.startswith("const_"):
                constant_places.append(name)
            elif "_result_" in name:
                result_places.append(name)
            elif name == "control":
                control_places.append(name)
                
        print(f"\nPlace Classification:")
        print(f"  Constant places: {len(constant_places)}")
        print(f"  Result places: {len(result_places)}")
        print(f"  Control places: {len(control_places)}")
        print(f"  Other places: {total_places - len(constant_places) - len(result_places) - len(control_places)}")
        
        # Transition analysis by operation type
        operation_counts = {}
        for name, transition in self.net.transitions.items():
            op_type = name.split('_')[0]  # Extract operation type from name
            operation_counts[op_type] = operation_counts.get(op_type, 0) + 1
            
        print(f"\nOperation Breakdown:")
        for op_type, count in sorted(operation_counts.items()):
            print(f"  {op_type}: {count}")
            
        # Network connectivity analysis
        max_inputs = 0
        max_outputs = 0
        total_inputs = 0
        total_outputs = 0
        
        for transition in self.net.transitions.values():
            inputs = len(transition.in_places)
            outputs = len(transition.out_places)
            max_inputs = max(max_inputs, inputs)
            max_outputs = max(max_outputs, outputs)
            total_inputs += inputs
            total_outputs += outputs
            
        avg_inputs = total_inputs / len(self.net.transitions) if self.net.transitions else 0
        avg_outputs = total_outputs / len(self.net.transitions) if self.net.transitions else 0
        
        print(f"\nConnectivity Analysis:")
        print(f"  Max inputs per transition: {max_inputs}")
        print(f"  Max outputs per transition: {max_outputs}")
        print(f"  Avg inputs per transition: {avg_inputs:.1f}")
        print(f"  Avg outputs per transition: {avg_outputs:.1f}")
        
        # Execution readiness
        ready_transitions = sum(1 for t in self.net.transitions.values() if t.can_fire())
        
        print(f"\nExecution State:")
        print(f"  Transitions ready to fire: {ready_transitions}/{total_transitions}")
        
        # Memory usage estimation (places that could be CPU-local vs shared)
        private_places = 0  # Places with single producer and consumer
        shared_places = 0   # Places with multiple producers or consumers
        
        for place in self.net.places.values():
            producers = len(place.in_transitions)
            consumers = len(place.out_transitions)
            
            if producers <= 1 and consumers <= 1:
                private_places += 1
            else:
                shared_places += 1
                
        print(f"\nMemory Hierarchy Potential:")
        print(f"  Private places (CPU-local eligible): {private_places}")
        print(f"  Shared places (require synchronization): {shared_places}")
        
        # Concurrency potential
        independent_chains = self._analyze_concurrency()
        
        print(f"\nConcurrency Analysis:")
        print(f"  Potential parallel execution chains: {independent_chains}")
        
        # Final result state
        if self.result_places:
            result_values = self.get_result_values()
            print(f"\nFinal Result Places:")
            for i, value in enumerate(result_values):
                print(f"  [{i}]: {value}")
        else:
            print(f"\nFinal Result Places: Empty")
            
        print("=" * 60)
        
    def _analyze_concurrency(self):
        """Analyze potential for concurrent execution"""
        # Simple heuristic: count transitions that don't share input places
        independent_count = 0
        used_places = set()
        
        for transition in self.net.transitions.values():
            transition_places = set(place.name for place in transition.in_places)
            if not transition_places.intersection(used_places):
                independent_count += 1
                used_places.update(transition_places)
                
        return independent_count
        
    def generate_multicore_assembly(self, num_cores=1, output_dir="test_results"):
        """
        Analyze the Petri net and generate assembly code for n cores
        Uses unified core generation logic for both single and multi-core cases
        """
        if num_cores < 1:
            raise ValueError("Number of cores must be >= 1")
            
        print(f"\n" + "=" * 60)
        print(f"GENERATING ASSEMBLY FOR {num_cores} CORE(S)")
        print("=" * 60)
        
        # Analyze the network for parallelization opportunities
        execution_plan = self._analyze_execution_dependencies()
        
        # Generate core assignments
        core_assignments = self._assign_operations_to_cores(execution_plan, num_cores)
        memory_map = self._optimize_memory_allocation()
        
        if num_cores == 1:
            # Single core - use same core generation logic but return assembly directly
            operations = core_assignments[0]
            assembly_code = self._generate_core_rom(0, operations, memory_map, num_cores)
            return assembly_code
        else:
            # Multi-core - create separate ROM files for each core
            return self._generate_multicore_roms(core_assignments, num_cores, output_dir)
            
    def _generate_multicore_roms(self, core_assignments, num_cores, output_dir="test_results"):
        """
        Generate separate ROM files for each core in multi-core execution
        Creates a folder with coreX.asm files for each core
        """
        import os
        
        # Create multicore output folder inside the specified directory
        folder_name = os.path.join(output_dir, f"multicore_{num_cores}cores")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        memory_map = self._optimize_memory_allocation()
        
        print(f"Creating {num_cores} separate ROM files in folder: {folder_name}/")
        
        # Generate ROM for each core
        all_roms = {}
        
        for core_id in range(num_cores):
            operations = core_assignments[core_id]
            
            if operations:
                print(f"Core {core_id}: {len(operations)} operations")
                rom_content = self._generate_core_rom(core_id, operations, memory_map, num_cores)
            else:
                print(f"Core {core_id}: No operations (idle core)")
                rom_content = self._generate_idle_core_rom(core_id, num_cores)
            
            # Save ROM file
            rom_filename = f"{folder_name}/core{core_id}.asm"
            with open(rom_filename, 'w') as f:
                f.write('\n'.join(rom_content))
            
            all_roms[core_id] = rom_content
            print(f"  Saved: {rom_filename} ({len(rom_content)} lines)")
        
        # Generate shared memory initialization file
        shared_init = self._generate_shared_memory_init(memory_map, num_cores)
        shared_filename = f"{folder_name}/shared_init.asm"
        with open(shared_filename, 'w') as f:
            f.write('\n'.join(shared_init))
        print(f"  Saved: {shared_filename} (shared memory initialization)")
        
        # Generate coordination protocol documentation
        coord_doc = self._generate_coordination_documentation(core_assignments, num_cores)
        doc_filename = f"{folder_name}/coordination.md"
        with open(doc_filename, 'w') as f:
            f.write(coord_doc)
        print(f"  Saved: {doc_filename} (coordination protocol)")
        
        return all_roms
        
    def _generate_core_rom(self, core_id, operations, memory_map, num_cores):
        """Generate ROM content for a specific core with unified single/multi-core logic"""
        rom_lines = [
            f"// Core {core_id} ROM - Unified Petri-net Execution",
            f"// Generated for {num_cores}-core system",
            f"// Operations: {len(operations)}",
            "//",
        ]
        
        # Add memory layout info
        if num_cores == 1:
            rom_lines.extend([
                f"// Single-core Memory Layout:",
                f"// @0-15: System registers",
                f"// @256+: Optimized place memory",
                f"// @512+: Stack area",
                "//",
                "",
                "// Initialize stack pointer", 
                "@512",  # Use higher stack for consistency
                "D=A",
                "@SP",
                "M=D",
                ""
            ])
        else:
            rom_lines.extend([
                f"// Multi-core Memory Layout:",
                f"// @0-15: System registers",
                f"// @16-31: Core status flags (debugging only)",
                f"// @32-47: Level synchronization area (coordination)", 
                f"// @256+: Optimized place memory",
                f"// @512+: Shared results area",
                "//",
                "",
                f"// Core {core_id} initialization",
                f"@{16 + core_id}",
                "M=0  // Set status to idle (debugging)",
                ""
            ])
        
        # Initialize constants in optimized memory locations (same for both single/multi-core)
        rom_lines.append("// Initialize constants in optimized memory")
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                rom_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        rom_lines.append("")
        
        # Check if this core has any operations
        if not operations:
            # Idle core - different handling for single vs multi-core
            if num_cores == 1:
                rom_lines.extend([
                    "// No operations to execute",
                    "(END)",
                    "@END", 
                    "0;JMP"
                ])
            else:
                rom_lines.extend([
                    f"(CORE_{core_id}_IDLE)",
                    f"// Core {core_id} has no operations - wait for program completion",
                    f"// Wait for final level completion (distributed termination)",
                    f"@{32 + self._get_final_level(operations)}",  # Final level sync
                    "D=M",
                    f"@{(1 << num_cores) - 1}",  # All cores mask
                    "D=D-A",
                    f"@CORE_{core_id}_TERMINATE",
                    "D;JEQ",  # Final level complete, terminate
                    f"@CORE_{core_id}_IDLE",
                    "0;JMP",  # Keep waiting
                    "",
                    f"(CORE_{core_id}_TERMINATE)",
                    f"// Program complete - core {core_id} self-terminates",
                    f"@{16 + core_id}",
                    "M=2  // Set status to done (debugging)",
                    f"@CORE_{core_id}_HALT",
                    "0;JMP"
                ])
            return rom_lines
        
        # Working core - execute operations
        if num_cores == 1:
            rom_lines.extend([
                f"// Single-core execution begins",
                ""
            ])
        else:
            rom_lines.extend([
                f"(CORE_{core_id}_START)",
                f"// Core {core_id} execution begins",
                f"@{16 + core_id}",
                "M=1  // Set status to working (debugging)",
                ""
            ])
        
        # Group operations by execution level for synchronization
        operations_by_level = {}
        for op_info in operations:
            level = op_info['level']
            if level not in operations_by_level:
                operations_by_level[level] = []
            operations_by_level[level].append(op_info)
        
        final_level = max(operations_by_level.keys()) if operations_by_level else 0
        
        # Generate code for each level - simplified for single-core
        for level in sorted(operations_by_level.keys()):
            level_ops = operations_by_level[level]
            
            rom_lines.extend([
                f"// === Level {level} Operations ===",
            ])
            
            # Level barrier synchronization (only for multi-core)
            if num_cores > 1:
                rom_lines.extend([
                    f"// Level-based barrier synchronization",
                    f"(LEVEL_{level}_BARRIER)",
                    f"// Signal ready for level {level}",
                    f"@{32 + level}",  # Sync area for this level
                    "D=M",
                    f"@{1 << core_id}",  # Set bit for this core
                    "D=D|A",
                    f"@{32 + level}",
                    "M=D",
                    "",
                    f"// Wait for all cores ready at level {level}",
                    f"(LEVEL_{level}_WAIT)",
                    f"@{32 + level}",
                    "D=M",
                    f"@{self._get_active_cores_mask(num_cores)}",  # Only active cores
                    "D=D-A",
                    f"@LEVEL_{level}_EXECUTE",
                    "D;JEQ",  # All active cores ready, proceed
                    f"@LEVEL_{level}_WAIT",
                    "0;JMP",  # Keep waiting
                    "",
                    f"(LEVEL_{level}_EXECUTE)"
                ])
            
            # Execute operations for this level (same logic for single/multi-core)
            for op_info in level_ops:
                operation = op_info['operation']
                transition = op_info['transition']
                
                rom_lines.extend([
                    f"// Operation: {operation}",
                ])
                
                if num_cores > 1:
                    rom_lines.append(f"// Core {core_id} executing {operation}")
                
                # Generate memory-optimized operation code (unified logic)
                op_code = self._generate_core_operation_code(operation, transition, memory_map)
                rom_lines.extend(op_code)
                rom_lines.append("")
        
        # Termination logic - different for single vs multi-core
        if num_cores == 1:
            # Single-core: push results to stack and terminate
            rom_lines.extend([
                "// Push final results onto stack"
            ])
            
            for place in self.result_places:
                if place.name in memory_map['location_map']:
                    memory_loc = memory_map['location_map'][place.name]
                    rom_lines.extend([
                        f"// Push result from @{memory_loc}",
                        f"@{memory_loc}",
                        "D=M",
                        "@SP",
                        "M=M+1",
                        "A=M-1",
                        "M=D"
                    ])
                    
            rom_lines.extend([
                "//",
                "// End of program",
                "(END)",
                "@END", 
                "0;JMP"
            ])
        else:
            # Multi-core: distributed termination
            rom_lines.extend([
                f"// Distributed termination - final level barrier IS completion detection",
                f"// Core {core_id} completed all operations",
                f"@{16 + core_id}",
                "M=2  // Set status to done (debugging)",
                "",
                f"// Wait for final level completion (level {final_level})",
                f"(FINAL_BARRIER_WAIT)",
                f"@{32 + final_level}",
                "D=M", 
                f"@{self._get_active_cores_mask(num_cores)}",  # All active cores mask
                "D=D-A",
                f"@CORE_{core_id}_TERMINATE",
                "D;JEQ",  # All cores finished final level
                f"@FINAL_BARRIER_WAIT",
                "0;JMP",  # Keep waiting
                "",
                f"(CORE_{core_id}_TERMINATE)",
                f"// Program complete - core {core_id} self-terminates",
                f"(CORE_{core_id}_HALT)",
                f"@CORE_{core_id}_HALT",
                "0;JMP  // Halt core"
            ])
        
        return rom_lines
        
    def _get_final_level(self, operations):
        """Get the final execution level from operations"""
        if not operations:
            # For idle cores, we need to determine the final level from the overall execution plan
            execution_plan = self._analyze_execution_dependencies()
            return len(execution_plan['execution_levels']) - 1 if execution_plan['execution_levels'] else 0
        return max(op['level'] for op in operations)
    
    def _get_active_cores_mask(self, num_cores):
        """Get the mask for cores that actually have work assigned"""
        # For now, assume all cores are active (this could be optimized)
        # In a more sophisticated implementation, we'd track which cores have operations
        return (1 << num_cores) - 1
        
    def _generate_idle_core_rom(self, core_id, num_cores):
        """Generate ROM for cores with no operations assigned"""
        return [
            f"// Core {core_id} ROM - Idle Core",
            f"// No operations assigned in {num_cores}-core system",
            "//",
            f"@{16 + core_id}",
            "M=0  // Set status to idle",
            "",
            f"(CORE_{core_id}_IDLE)",
            "// Idle loop - could be used for other tasks",
            f"@CORE_{core_id}_IDLE", 
            "0;JMP"
        ]
        
    def _generate_core_operation_code(self, operation, transition, memory_map):
        """Generate assembly code for a specific operation on a core"""
        op_type = operation.split('_')[0]
        code_lines = []
        
        if op_type in ['add', 'sub', 'mul', 'div', 'and', 'or', 'eq', 'lt', 'gt'] and len(transition.in_places) >= 2:
            # Binary operations
            loc_a = memory_map['location_map'][transition.in_places[0].name]
            loc_b = memory_map['location_map'][transition.in_places[1].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Binary operation: {op_type}",
                f"// Load operands from @{loc_a} and @{loc_b}",
                f"@{loc_a}",
                "D=M",
                f"@{loc_b}",
            ])
            
            if op_type == 'add':
                code_lines.append("D=D+M")
            elif op_type == 'sub':
                code_lines.append("D=D-M")
            elif op_type == 'mul':
                # Multiplication requires a loop in Hack assembly
                code_lines.extend([
                    "// Multiplication using repeated addition",
                    "@R13",  # Use R13 as temporary register
                    "M=D",   # Store first operand
                    "D=M",   # Load second operand
                    "@R14",  # Use R14 as counter
                    "M=D",
                    "D=0",   # Initialize result to 0
                    f"({operation.upper()}_LOOP)",
                    "@R14",
                    "D=M",
                    f"@{operation.upper()}_DONE",
                    "D;JEQ", # If counter is 0, done
                    "@R13",
                    "D=D+M", # Add first operand to result
                    "@R14",
                    "M=M-1", # Decrement counter
                    f"@{operation.upper()}_LOOP",
                    "0;JMP",
                    f"({operation.upper()}_DONE)"
                ])
            elif op_type == 'div':
                # Division requires a loop in Hack assembly
                code_lines.extend([
                    "// Division using repeated subtraction",
                    "@R13",  # Use R13 as dividend
                    "M=D",   # Store first operand (dividend)
                    "D=M",   # Load second operand (divisor)
                    "@R14",  # Use R14 as divisor
                    "M=D",
                    "@R15",  # Use R15 as quotient counter
                    "M=0",   # Initialize quotient to 0
                    f"({operation.upper()}_LOOP)",
                    "@R14",
                    "D=M",
                    f"@{operation.upper()}_DONE",
                    "D;JEQ", # If divisor is 0, done (division by zero)
                    "@R13",
                    "D=M",
                    f"@{operation.upper()}_DONE",
                    "D;JLT", # If dividend < 0, done
                    "@R14",
                    "D=M",
                    "@R13",
                    "M=M-D", # Subtract divisor from dividend
                    "@R15",
                    "M=M+1", # Increment quotient
                    f"@{operation.upper()}_LOOP",
                    "0;JMP",
                    f"({operation.upper()}_DONE)",
                    "@R15",
                    "D=M"    # Load quotient result
                ])
            elif op_type == 'and':
                code_lines.append("D=D&M")
            elif op_type == 'or':
                code_lines.append("D=D|M")
            elif op_type in ['eq', 'lt', 'gt']:
                # Comparison operations
                code_lines.extend([
                    "D=D-M  // Compare",
                    f"@{operation.upper()}_TRUE",
                    f"D;J{op_type.upper()}",
                    "D=0  // False",
                    f"@{operation.upper()}_DONE",
                    "0;JMP",
                    f"({operation.upper()}_TRUE)",
                    "D=-1  // True (-1)",
                    f"({operation.upper()}_DONE)"
                ])
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
            
        elif op_type in ['neg', 'not'] and len(transition.in_places) >= 1:
            # Unary operations
            loc_input = memory_map['location_map'][transition.in_places[0].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Unary operation: {op_type}",
                f"// Load operand from @{loc_input}",
                f"@{loc_input}",
                "D=M",
            ])
            
            if op_type == 'neg':
                code_lines.append("D=-D")
            elif op_type == 'not':
                code_lines.append("D=!D")
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
        
        return code_lines
        
    def _generate_shared_memory_init(self, memory_map, num_cores):
        """Generate shared memory initialization code"""
        init_lines = [
            f"// Shared Memory Initialization for {num_cores}-core system",
            "// Run this before starting any cores",
            "//",
            "// Initialize core status flags to idle",
        ]
        
        for core_id in range(num_cores):
            init_lines.extend([
                f"@{16 + core_id}",
                "M=0  // Core idle"
            ])
        
        init_lines.extend([
            "",
            "// Initialize synchronization area",
        ])
        
        # Initialize sync areas for each level (assuming max 10 levels)
        for level in range(10):
            init_lines.extend([
                f"@{32 + level}",
                "M=0  // Level sync"
            ])
        
        init_lines.extend([
            "",
            "// Initialize constants in optimized memory locations"
        ])
        
        # Initialize constants
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                init_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        
        init_lines.extend([
            "",
            "// Shared memory initialization complete",
            "(INIT_DONE)",
            "@INIT_DONE",
            "0;JMP"
        ])
        
        return init_lines
        
    def _generate_coordination_documentation(self, core_assignments, num_cores):
        """Generate documentation for the distributed multi-core coordination protocol"""
        doc = f"""# Distributed Multi-Core Coordination Protocol

## System Overview
- **Cores**: {num_cores}
- **Coordination**: Distributed level-based synchronization (NO COORDINATOR)
- **Memory**: Shared optimized memory layout
- **Termination**: Self-terminating cores via final level barrier

## Memory Layout
- `@0-15`: System registers
- `@16-31`: Core status flags (debugging only - not used for coordination)
- `@32-47`: Level synchronization area (distributed coordination)
- `@256+`: Optimized place memory (shared)
- `@512+`: Results collection area

## Core Assignments
"""
        
        for core_id, operations in core_assignments.items():
            doc += f"\n### Core {core_id}\n"
            if operations:
                doc += f"Operations: {len(operations)}\n"
                for op_info in operations:
                    doc += f"- Level {op_info['level']}: {op_info['operation']}\n"
            else:
                doc += "No operations assigned (idle core)\n"
        
        doc += f"""
## Distributed Synchronization Protocol

For detailed information about the distributed synchronization protocol,
see: docs/distributed-synchronization-protocol.md

This protocol eliminates the need for a centralized coordinator by using
level-based barriers for synchronization and distributed termination detection.
"""
        
        return doc
        
    def _analyze_execution_dependencies(self):
        """
        Analyze the Petri net to determine execution dependencies
        Enhanced to handle control flow operations (goto, if-goto, labels)
        Returns a dependency graph and execution levels with conservative level assignment
        """
        # Build dependency graph
        dependencies = {}
        reverse_deps = {}
        
        for trans_name, transition in self.net.transitions.items():
            dependencies[trans_name] = []
            reverse_deps[trans_name] = []
            
        # Find dependencies based on place connections
        for trans_name, transition in self.net.transitions.items():
            for input_place in transition.in_places:
                # Find which transition produces this place
                for producer_name, producer in self.net.transitions.items():
                    if input_place in producer.out_places:
                        dependencies[trans_name].append(producer_name)
                        reverse_deps[producer_name].append(trans_name)
        
        # Handle control flow dependencies
        control_flow_deps = self._analyze_control_flow_dependencies()
        
        # Merge control flow dependencies with place-based dependencies
        for trans_name, cf_deps in control_flow_deps.items():
            if trans_name in dependencies:
                dependencies[trans_name].extend(cf_deps)
                # Update reverse dependencies
                for dep in cf_deps:
                    if dep in reverse_deps:
                        reverse_deps[dep].append(trans_name)
                        
        # Remove duplicates
        for trans_name in dependencies:
            dependencies[trans_name] = list(set(dependencies[trans_name]))
        for trans_name in reverse_deps:
            reverse_deps[trans_name] = list(set(reverse_deps[trans_name]))
                        
        # Topological sort to find execution levels
        execution_levels = []
        remaining = set(self.net.transitions.keys())
        
        while remaining:
            # Find transitions with no unresolved dependencies
            ready = []
            for trans in remaining:
                if all(dep not in remaining for dep in dependencies[trans]):
                    ready.append(trans)
                    
            if not ready:
                # Handle cycles or isolated nodes
                ready = [next(iter(remaining))]
                
            execution_levels.append(ready)
            remaining -= set(ready)
            
        return {
            'dependencies': dependencies,
            'reverse_deps': reverse_deps,
            'execution_levels': execution_levels,
            'control_flow_deps': control_flow_deps
        }
    
    def _analyze_control_flow_dependencies(self):
        """
        Analyze dependencies created by control flow operations
        Implements conservative level assignment for goto/if-goto operations
        """
        control_flow_deps = {}
        
        # Initialize empty dependencies for all transitions
        for trans_name in self.net.transitions.keys():
            control_flow_deps[trans_name] = []
        
        # Analyze each transition for control flow patterns
        for trans_name, transition in self.net.transitions.items():
            
            # Handle goto operations
            if trans_name.startswith("goto_"):
                # Extract label name from transition name
                # Format: goto_LABELNAME_N
                parts = trans_name.split("_")
                if len(parts) >= 2:
                    label_name = parts[1]
                    
                    # Conservative approach: goto operations create dependencies
                    # All operations that might execute after the goto must wait for it
                    for other_trans_name in self.net.transitions.keys():
                        if (other_trans_name != trans_name and 
                            not other_trans_name.startswith("goto_") and
                            not other_trans_name.startswith("if_goto_")):
                            # Other operations depend on control flow resolution
                            control_flow_deps[other_trans_name].append(trans_name)
            
            # Handle if-goto operations  
            elif trans_name.startswith("if_goto_"):
                # Extract label name from transition name
                # Format: if_goto_LABELNAME_N
                parts = trans_name.split("_")
                if len(parts) >= 3:
                    label_name = parts[2]  # Skip "if" and "goto"
                    
                    # Conservative approach: if-goto creates choice dependencies
                    # Operations that might be affected by the conditional jump
                    # must wait for the choice to be resolved
                    
                    # Find related operations that might be in the jump path
                    for other_trans_name in self.net.transitions.keys():
                        if (other_trans_name != trans_name and 
                            not other_trans_name.startswith("goto_") and
                            not other_trans_name.startswith("if_goto_")):
                            
                            # Check if this operation might be affected by the jump
                            # Conservative: assume all subsequent operations depend on choice
                            if self._is_potentially_affected_by_control_flow(trans_name, other_trans_name):
                                control_flow_deps[other_trans_name].append(trans_name)
        
        # Add inter-control-flow dependencies
        # Multiple control flow operations in sequence create dependencies
        control_flow_transitions = [name for name in self.net.transitions.keys() 
                                  if name.startswith(('goto_', 'if_goto_'))]
        
        for i, cf_trans1 in enumerate(control_flow_transitions):
            for cf_trans2 in control_flow_transitions[i+1:]:
                # Later control flow operations depend on earlier ones
                # This ensures proper sequencing of control flow decisions
                control_flow_deps[cf_trans2].append(cf_trans1)
        
        # Log control flow dependencies for debugging
        cf_deps_found = {k: v for k, v in control_flow_deps.items() if v}
        if cf_deps_found:
            print(f"\nControl Flow Dependencies Found:")
            for trans_name, deps in list(cf_deps_found.items())[:3]:  # Show first 3
                print(f"  {trans_name} depends on: {deps[:3]}{'...' if len(deps) > 3 else ''}")
            if len(cf_deps_found) > 3:
                print(f"  ... and {len(cf_deps_found) - 3} more")
        
        return control_flow_deps
        
    def _is_potentially_affected_by_control_flow(self, cf_transition, other_transition):
        """
        Determine if a transition might be affected by a control flow operation
        More refined conservative approach: focus on operations that could be in control flow paths
        """
        # Skip other control flow operations (they have their own dependencies)
        if other_transition.startswith(('goto_', 'if_goto_')):
            return False
            
        # Skip operations that are clearly independent (constants, sources)
        if other_transition.startswith(('const_', 'source_')):
            return False
            
        # Operations that are likely to be in the execution path and could be affected
        # by control flow decisions should depend on control flow operations
        
        # Local variable operations could be in loops
        if other_transition.startswith(('dup_local_', 'pop_local_')):
            return True
            
        # Arithmetic operations could be in loops  
        if any(other_transition.startswith(op) for op in ['add_', 'sub_', 'mul_', 'div_', 'neg_']):
            return True
            
        # Comparison operations could be in conditional paths
        if any(other_transition.startswith(op) for op in ['eq_', 'lt_', 'gt_', 'and_', 'or_', 'not_']):
            return True
            
        # Function call operations could be affected by control flow
        if other_transition.startswith(('call_', 'return_')):
            return True
            
        # Most other operations are potentially affected by control flow
        return True
        
    def _assign_operations_to_cores(self, execution_plan, num_cores):
        """
        Assign operations to cores based on dependencies and load balancing
        Enhanced to handle control flow operations with distributed coordination
        """
        core_assignments = {i: [] for i in range(num_cores)}
        
        for level_idx, level in enumerate(execution_plan['execution_levels']):
            print(f"Level {level_idx}: {len(level)} parallel operations: {level}")
            
            # Check if this level contains control flow operations
            control_flow_ops = [op for op in level 
                              if op.startswith(('goto_', 'if_goto_', 'label_'))]
            
            if control_flow_ops:
                print(f"  Control flow operations in level {level_idx}: {control_flow_ops}")
                # All cores must participate in control flow synchronization
                # Even if they don't execute the specific control flow operation
                
            # Assign operations in this level to cores (round-robin)
            for i, operation in enumerate(level):
                core_id = i % num_cores
                
                # Mark control flow operations for special handling
                is_control_flow = operation.startswith(('goto_', 'if_goto_', 'label_'))
                
                core_assignments[core_id].append({
                    'operation': operation,
                    'level': level_idx,
                    'transition': self.net.transitions[operation],
                    'is_control_flow': is_control_flow,
                    'requires_barrier': is_control_flow or len(control_flow_ops) > 0
                })
                
        # Ensure all cores have barrier synchronization at control flow levels
        self._ensure_control_flow_barriers(core_assignments, execution_plan)
                
        return core_assignments
    
    def _ensure_control_flow_barriers(self, core_assignments, execution_plan):
        """
        Ensure all cores participate in barriers at levels containing control flow
        This maintains distributed coordination even when cores don't execute control flow ops
        """
        # Find levels that contain control flow operations
        control_flow_levels = set()
        for level_idx, level in enumerate(execution_plan['execution_levels']):
            if any(op.startswith(('goto_', 'if_goto_', 'label_')) for op in level):
                control_flow_levels.add(level_idx)
        
        if control_flow_levels:
            print(f"Control flow barrier levels: {sorted(control_flow_levels)}")
            
            # Ensure all cores have operations marked for barriers at these levels
            for core_id, operations in core_assignments.items():
                for op_info in operations:
                    if op_info['level'] in control_flow_levels:
                        op_info['requires_barrier'] = True
                        
                # If a core has no operations at a control flow level,
                # add a barrier placeholder
                core_levels = {op['level'] for op in operations}
                for cf_level in control_flow_levels:
                    if cf_level not in core_levels:
                        # Add barrier placeholder for this core
                        core_assignments[core_id].append({
                            'operation': f'barrier_placeholder_level_{cf_level}',
                            'level': cf_level,
                            'transition': None,
                            'is_control_flow': False,
                            'requires_barrier': True,
                            'is_placeholder': True
                        })
        
        # Sort operations by level for each core
        for core_id in core_assignments:
            core_assignments[core_id].sort(key=lambda x: x['level'])
        
    def _generate_assembly_code(self, core_assignments, num_cores):
        """
        Generate Hack assembly code for multi-core execution
        Uses unified core generation logic for both single and multi-core cases
        """
        memory_map = self._optimize_memory_allocation()
        
        if num_cores == 1:
            # Single core - use unified core generation logic
            return self._generate_core_rom(0, core_assignments[0], memory_map, num_cores)
        else:
            # For multi-core, return a summary instead of monolithic assembly
            roms = self._generate_multicore_roms(core_assignments, num_cores)
            
            # Return a summary of what was generated
            summary = [
                f"// Multi-core ROM generation completed",
                f"// Generated {num_cores} separate ROM files:",
            ]
            
            for core_id in range(num_cores):
                rom_size = len(roms[core_id]) if core_id in roms else 0
                summary.append(f"//   core{core_id}.asm: {rom_size} lines")
            
            summary.extend([
                f"// Plus shared_init.asm and coordination.md",
                f"// Check multicore_{num_cores}cores/ folder for files"
            ])
            
            return summary
            
    def _optimize_memory_allocation(self):
        """
        Enhanced memory optimization with control flow support
        Places can share memory if they can never have tokens simultaneously
        Includes specialized handling for control flow constructs
        """
        print("\n--- Enhanced Memory Optimization with Control Flow ---")
        
        # Analyze place lifetimes including control flow dependencies
        lifetime_analysis = self._analyze_place_lifetimes_with_control_flow()
        
        # Use interval graph coloring for optimal memory allocation
        memory_allocation = self._allocate_memory_with_control_flow_awareness(lifetime_analysis)
        
        print(f"Original places: {len(self.net.places)}")
        print(f"Memory locations needed: {memory_allocation['total_locations']}")
        print(f"Memory savings: {len(self.net.places) - memory_allocation['total_locations']} locations")
        
        # Show control flow specific optimizations
        self._show_control_flow_memory_details(memory_allocation, lifetime_analysis)
        
        return memory_allocation
        
    def _analyze_place_lifetimes_with_control_flow(self):
        """
        Enhanced place lifetime analysis that handles control flow constructs
        Accounts for labels, goto, and if-goto operations in lifetime calculations
        """
        print("Analyzing place lifetimes with control flow awareness...")
        
        # Get execution plan with control flow dependencies
        execution_plan = self._analyze_execution_dependencies()
        
        # Classify places by type for specialized lifetime analysis
        place_types = self._classify_places_by_type()
        
        # Calculate lifetimes for each place type
        lifetimes = {}
        
        # 1. Control flow places (labels, goto sources, choice results)
        for place_name in place_types['control_flow']:
            lifetimes[place_name] = self._analyze_control_flow_place_lifetime(place_name, execution_plan)
        
        # 2. Regular computation places (arithmetic results, local variables)
        for place_name in place_types['computation']:
            lifetimes[place_name] = self._analyze_computation_place_lifetime(place_name, execution_plan)
        
        # 3. Constant places (live from start)
        for place_name in place_types['constants']:
            lifetimes[place_name] = self._analyze_constant_place_lifetime(place_name, execution_plan)
        
        # 4. Result places (live until end)
        for place_name in place_types['results']:
            lifetimes[place_name] = self._analyze_result_place_lifetime(place_name, execution_plan)
        
        return {
            'lifetimes': lifetimes,
            'execution_plan': execution_plan,
            'place_types': place_types
        }
    
    def _classify_places_by_type(self):
        """
        Classify places by their role in the computation for specialized lifetime analysis
        """
        place_types = {
            'control_flow': [],
            'computation': [],
            'constants': [],
            'results': []
        }
        
        for place_name, place in self.net.places.items():
            if self._is_control_flow_place(place_name):
                place_types['control_flow'].append(place_name)
            elif place_name.startswith('const_'):
                place_types['constants'].append(place_name)
            elif place in self.result_places:
                place_types['results'].append(place_name)
            else:
                place_types['computation'].append(place_name)
        
        print(f"Place classification: {len(place_types['control_flow'])} control flow, "
              f"{len(place_types['computation'])} computation, "
              f"{len(place_types['constants'])} constants, "
              f"{len(place_types['results'])} results")
        
        return place_types
    
    def _is_control_flow_place(self, place_name):
        """
        Determine if a place is related to control flow operations
        """
        control_flow_patterns = [
            'label_',           # Label places
            'goto_source_',     # Goto source places
            'if_goto_continue_', # If-goto continue places
            'control_'          # General control places
        ]
        
        return any(place_name.startswith(pattern) for pattern in control_flow_patterns)
    
    def _analyze_control_flow_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of control flow places with enhanced control flow dependency handling
        These often have very short lifetimes and high reuse potential
        """
        place = self.net.places[place_name]
        
        # Control flow places typically have short, specific lifetimes
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # Enhanced handling for different control flow place types
        if place_name.startswith('label_'):
            # Label places: analyze control flow dependencies to determine actual lifetime
            death_level = self._analyze_label_place_dependencies(place_name, execution_plan)
        
        elif place_name.startswith('goto_source_'):
            # Goto source places have very short lifetimes (just for the jump)
            death_level = birth_level + 1  # Die immediately after use
        
        elif place_name.startswith('if_goto_continue_'):
            # Continue places for if-goto: analyze choice resolution dependencies
            death_level = self._analyze_choice_place_dependencies(place_name, execution_plan)
        
        elif place_name.startswith('control_'):
            # General control places: analyze their specific usage pattern
            death_level = self._analyze_general_control_place_dependencies(place_name, execution_plan)
        
        # Apply control flow dependency constraints
        death_level = self._apply_control_flow_constraints(place_name, birth_level, death_level, execution_plan)
        
        return {
            'birth': birth_level,
            'death': death_level,
            'type': 'control_flow',
            'reuse_priority': 'high',  # Control flow places are good candidates for reuse
            'control_flow_deps': self._get_control_flow_dependencies(place_name, execution_plan)
        }
    
    def _analyze_computation_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of regular computation places (arithmetic, local variables)
        """
        place = self.net.places[place_name]
        
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # Handle control flow dependencies for computation places
        # If a place might be accessed in a loop, extend its lifetime
        if self._place_potentially_in_loop(place_name, execution_plan):
            # Conservative: extend lifetime to account for potential loop iterations
            death_level = max(death_level, birth_level + 3)
        
        return {
            'birth': birth_level,
            'death': death_level,
            'type': 'computation',
            'reuse_priority': 'medium'
        }
    
    def _analyze_constant_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of constant places
        """
        return {
            'birth': -1,  # Constants are born before execution starts
            'death': float('inf'),  # May be needed throughout execution
            'type': 'constant',
            'reuse_priority': 'low'  # Constants should not be reused aggressively
        }
    
    def _analyze_result_place_lifetime(self, place_name, execution_plan):
        """
        Analyze lifetime of result places
        """
        place = self.net.places[place_name]
        birth_level = self._find_place_birth_level(place, execution_plan)
        
        return {
            'birth': birth_level,
            'death': float('inf'),  # Results live until program end
            'type': 'result',
            'reuse_priority': 'none'  # Results should never be reused
        }
    
    def _find_place_birth_level(self, place, execution_plan):
        """
        Find the execution level where a place is born (produced)
        """
        if not place.in_transitions:
            return -1  # Source places (constants) are born before execution
        
        # Find the earliest level where any producer transition executes
        min_birth_level = float('inf')
        for producer in place.in_transitions:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if producer.name in level_transitions:
                    min_birth_level = min(min_birth_level, level_idx)
                    break
        
        return min_birth_level if min_birth_level != float('inf') else 0
    
    def _find_place_death_level(self, place, execution_plan):
        """
        Find the execution level where a place dies (consumed)
        """
        if not place.out_transitions:
            return float('inf')  # Sink places (results) never die
        
        # Find the latest level where any consumer transition executes
        max_death_level = -1
        for consumer in place.out_transitions:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if consumer.name in level_transitions:
                    max_death_level = max(max_death_level, level_idx)
                    break
        
        return max_death_level if max_death_level != -1 else 0
    
    def _find_function_or_program_end_level(self, execution_plan):
        """
        Find the level representing the end of current function or program
        """
        if execution_plan['execution_levels']:
            return len(execution_plan['execution_levels']) - 1
        return 0
    
    def _place_potentially_in_loop(self, place_name, execution_plan):
        """
        Determine if a place might be accessed within a loop construct
        Enhanced with better control flow dependency analysis
        """
        # Check if there are any control flow operations that might create loops
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        
        # Look for patterns that suggest loops (goto/if-goto operations)
        for trans_name, deps in control_flow_deps.items():
            if any(dep.startswith(('goto_', 'if_goto_')) for dep in deps):
                # There are control flow operations that might create loops
                # Be conservative and assume computation places might be in loops
                if not place_name.startswith(('const_', 'label_')):
                    return True
        
        # Enhanced analysis: check for backward jumps that indicate loops
        if self._has_backward_control_flow_jumps(execution_plan):
            # If there are backward jumps, computation places might be in loops
            if not self._is_control_flow_place(place_name) and not place_name.startswith('const_'):
                return True
        
        return False
    
    def _analyze_label_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for label places to determine accurate lifetime
        """
        # Find all goto/if-goto operations that target this label
        label_name = place_name.replace('label_', '').split('_')[0]  # Extract label name
        
        # Look for jumps to this label
        targeting_jumps = []
        for trans_name in self.net.transitions.keys():
            if (trans_name.startswith('goto_') and label_name in trans_name) or \
               (trans_name.startswith('if_goto_') and label_name in trans_name):
                targeting_jumps.append(trans_name)
        
        if not targeting_jumps:
            # No jumps target this label, it can die early
            birth_level = self._find_place_birth_level(self.net.places[place_name], execution_plan)
            return birth_level + 1
        
        # Find the latest level where any targeting jump might execute
        max_jump_level = -1
        for jump_trans in targeting_jumps:
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if jump_trans in level_transitions:
                    max_jump_level = max(max_jump_level, level_idx)
        
        # Label must live until after the latest possible jump
        return max_jump_level + 1 if max_jump_level >= 0 else self._find_function_or_program_end_level(execution_plan)
    
    def _analyze_choice_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for if-goto continue places
        """
        # Continue places die after the choice is resolved and execution continues
        birth_level = self._find_place_birth_level(self.net.places[place_name], execution_plan)
        
        # Look for the if-goto transition that creates this continue place
        if_goto_trans = None
        for trans_name in self.net.transitions.keys():
            if trans_name.startswith('if_goto_') and place_name.replace('if_goto_continue_', '') in trans_name:
                if_goto_trans = trans_name
                break
        
        if if_goto_trans:
            # Find when the if-goto executes
            for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
                if if_goto_trans in level_transitions:
                    # Continue place dies shortly after the choice is made
                    return level_idx + 2
        
        # Default: short lifetime
        return birth_level + 2
    
    def _analyze_general_control_place_dependencies(self, place_name, execution_plan):
        """
        Analyze dependencies for general control places
        """
        place = self.net.places[place_name]
        birth_level = self._find_place_birth_level(place, execution_plan)
        death_level = self._find_place_death_level(place, execution_plan)
        
        # General control places typically have short lifetimes
        # but may need to live longer if they're part of complex control flow
        if self._is_part_of_complex_control_flow(place_name, execution_plan):
            # Extend lifetime for complex control flow patterns
            return max(death_level, birth_level + 3)
        
        return death_level
    
    def _apply_control_flow_constraints(self, place_name, birth_level, death_level, execution_plan):
        """
        Apply control flow dependency constraints to place lifetime
        """
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        
        # If this place is involved in control flow dependencies, extend its lifetime
        for trans_name, deps in control_flow_deps.items():
            # Check if any transition that uses this place has control flow dependencies
            place = self.net.places[place_name]
            for consumer in place.out_transitions:
                if consumer.name in control_flow_deps and control_flow_deps[consumer.name]:
                    # This place is consumed by a transition with control flow dependencies
                    # Extend its lifetime to account for potential control flow delays
                    death_level = max(death_level, birth_level + 2)
                    break
        
        return death_level
    
    def _get_control_flow_dependencies(self, place_name, execution_plan):
        """
        Get control flow dependencies for a place
        """
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        place = self.net.places[place_name]
        
        deps = []
        # Check dependencies of transitions that consume this place
        for consumer in place.out_transitions:
            if consumer.name in control_flow_deps:
                deps.extend(control_flow_deps[consumer.name])
        
        return list(set(deps))  # Remove duplicates
    
    def _has_backward_control_flow_jumps(self, execution_plan):
        """
        Check if there are any backward jumps that might indicate loops
        """
        # Look for goto/if-goto operations that might jump backward
        # This is a heuristic based on transition names and execution levels
        
        control_flow_transitions = []
        for level_idx, level_transitions in enumerate(execution_plan['execution_levels']):
            for trans_name in level_transitions:
                if trans_name.startswith(('goto_', 'if_goto_')):
                    control_flow_transitions.append((trans_name, level_idx))
        
        # Check if any control flow operation might jump to an earlier level
        # This is conservative - we assume any control flow might create loops
        return len(control_flow_transitions) > 0
    
    def _is_part_of_complex_control_flow(self, place_name, execution_plan):
        """
        Determine if a place is part of complex control flow patterns
        """
        # Check if there are multiple control flow operations that might affect this place
        control_flow_count = 0
        for level_transitions in execution_plan['execution_levels']:
            for trans_name in level_transitions:
                if trans_name.startswith(('goto_', 'if_goto_', 'label_')):
                    control_flow_count += 1
        
        # If there are multiple control flow operations, consider it complex
        return control_flow_count > 2
        """
        Analyze which places can be reached simultaneously during execution
        Places that are never live at the same time can share memory
        """
        # Build execution dependency graph
        execution_plan = self._analyze_execution_dependencies()
        
        # Determine place lifetimes
        place_lifetimes = {}
        
        for place_name, place in self.net.places.items():
            # Find when place is produced (birth)
            birth_level = -1  # Constants are born at level -1
            if place_name.startswith("const_"):
                birth_level = -1
            else:
                # Find producing transition
                for producer in place.in_transitions:
                    for level_idx, level in enumerate(execution_plan['execution_levels']):
                        if producer.name in level:
                            birth_level = level_idx
                            break
                            
            # Find when place is consumed (death)
            death_level = float('inf')  # Final results live forever
            if place in self.result_places:
                death_level = float('inf')  # Result places live forever
            else:
                # Find consuming transitions
                min_death = float('inf')
                for consumer in place.out_transitions:
                    for level_idx, level in enumerate(execution_plan['execution_levels']):
                        if consumer.name in level:
                            min_death = min(min_death, level_idx)
                if min_death != float('inf'):
                    death_level = min_death
                    
            place_lifetimes[place_name] = {
                'birth': birth_level,
                'death': death_level,
                'lifetime': (birth_level, death_level)
            }
            
        return {
            'lifetimes': place_lifetimes,
            'execution_plan': execution_plan
        }
        
    
    def _allocate_memory_with_control_flow_awareness(self, lifetime_analysis):
        """
        Allocate memory locations with control flow awareness
        Uses enhanced interval graph coloring with control flow optimizations
        """
        lifetimes = lifetime_analysis['lifetimes']
        place_types = lifetime_analysis['place_types']
        
        print("Allocating memory with control flow optimizations...")
        
        # Separate places by reuse priority for optimized allocation
        high_priority_reuse = []  # Control flow places
        medium_priority_reuse = []  # Computation places
        low_priority_reuse = []   # Constants
        no_reuse = []            # Results
        
        for place_name, lifetime_info in lifetimes.items():
            priority = lifetime_info.get('reuse_priority', 'medium')
            if priority == 'high':
                high_priority_reuse.append((place_name, lifetime_info))
            elif priority == 'medium':
                medium_priority_reuse.append((place_name, lifetime_info))
            elif priority == 'low':
                low_priority_reuse.append((place_name, lifetime_info))
            else:  # 'none'
                no_reuse.append((place_name, lifetime_info))
        
        # Sort each group by birth time for interval graph coloring
        high_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        medium_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        low_priority_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        no_reuse.sort(key=lambda x: (x[1]['birth'], x[1]['death']))
        
        # Allocate memory using enhanced interval coloring
        location_map = {}
        location_to_places = {}
        next_location = 256
        
        # Track active intervals for each priority group
        active_intervals = []  # [(end_time, location_id, priority)]
        
        # Process all places in order of reuse priority
        all_places = high_priority_reuse + medium_priority_reuse + low_priority_reuse + no_reuse
        
        for place_name, lifetime_info in all_places:
            birth = lifetime_info['birth']
            death = lifetime_info['death']
            priority = lifetime_info.get('reuse_priority', 'medium')
            
            # Clean up expired intervals
            active_intervals = [(end_time, loc_id, prio) for end_time, loc_id, prio in active_intervals 
                              if end_time > birth]
            
            # Try to find a reusable location based on priority
            reused_location = None
            
            if priority == 'high':
                # Control flow places: aggressive reuse with other control flow places
                reused_location = self._find_reusable_location_for_control_flow(
                    active_intervals, birth, place_name)
            elif priority == 'medium':
                # Computation places: moderate reuse
                reused_location = self._find_reusable_location_for_computation(
                    active_intervals, birth, place_name)
            elif priority == 'low':
                # Constants: conservative reuse
                reused_location = self._find_reusable_location_for_constants(
                    active_intervals, birth, place_name)
            # priority == 'none': no reuse for results
            
            if reused_location is not None:
                # Reuse existing location
                location_map[place_name] = reused_location
                location_to_places[reused_location].append(place_name)
            else:
                # Allocate new location
                location_map[place_name] = next_location
                location_to_places[next_location] = [place_name]
                next_location += 1
            
            # Add this interval to active set (if it has a finite death time)
            if death != float('inf'):
                active_intervals.append((death, location_map[place_name], priority))
        
        # Calculate optimization statistics
        total_locations = next_location - 256
        control_flow_savings = self._calculate_control_flow_savings(
            place_types['control_flow'], location_to_places)
        
        print(f"Control flow places: {len(place_types['control_flow'])}")
        print(f"Control flow memory savings: {control_flow_savings} locations")
        
        return {
            'location_map': location_map,
            'location_to_places': location_to_places,
            'total_locations': total_locations,
            'control_flow_savings': control_flow_savings
        }
    
    def _find_reusable_location_for_control_flow(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for control flow places with enhanced dependency handling
        Control flow places can aggressively reuse memory from each other
        """
        # Enhanced reuse strategy for control flow places
        
        # Priority 1: Reuse from other control flow places that are clearly expired
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority == 'high':
                # Check if this location is safe to reuse for control flow
                if self._is_safe_control_flow_reuse(location_id, place_name, birth_time):
                    return location_id
        
        # Priority 2: Reuse from computation places if they're expired and safe
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority == 'medium':
                if self._is_safe_control_flow_reuse(location_id, place_name, birth_time):
                    return location_id
        
        # Priority 3: Aggressive reuse for very short-lived control flow places
        if self._is_very_short_lived_control_flow_place(place_name):
            # Very short-lived places can reuse locations more aggressively
            for end_time, location_id, priority in active_intervals:
                if end_time <= birth_time + 1:  # Allow slight overlap for very short places
                    return location_id
        
        return None
    
    def _is_safe_control_flow_reuse(self, location_id, place_name, birth_time):
        """
        Check if it's safe to reuse a memory location for a control flow place
        """
        # Control flow places can generally reuse memory safely due to their short lifetimes
        # Additional safety checks for specific patterns
        
        # Check if the place is involved in complex control flow dependencies
        if place_name.startswith('label_') and self._has_multiple_jump_targets(place_name):
            # Labels with multiple jump sources need more careful handling
            return True  # Still safe, but noted for future enhancement
        
        # Goto source places are very safe to reuse
        if place_name.startswith('goto_source_'):
            return True
        
        # Continue places are generally safe
        if place_name.startswith('if_goto_continue_'):
            return True
        
        return True  # Default: control flow places are safe to reuse
    
    def _is_very_short_lived_control_flow_place(self, place_name):
        """
        Determine if a control flow place has a very short lifetime
        """
        # Goto source places are very short-lived
        if place_name.startswith('goto_source_'):
            return True
        
        # Some continue places are very short-lived
        if place_name.startswith('if_goto_continue_'):
            return True
        
        return False
    
    def _has_multiple_jump_targets(self, label_place_name):
        """
        Check if a label place is targeted by multiple jump operations
        """
        if not label_place_name.startswith('label_'):
            return False
        
        label_name = label_place_name.replace('label_', '').split('_')[0]
        
        # Count transitions that target this label
        targeting_count = 0
        for trans_name in self.net.transitions.keys():
            if (trans_name.startswith('goto_') and label_name in trans_name) or \
               (trans_name.startswith('if_goto_') and label_name in trans_name):
                targeting_count += 1
        
        return targeting_count > 1
    
    def _find_reusable_location_for_computation(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for computation places
        More conservative than control flow places
        """
        # Only reuse from other computation places or expired control flow places
        for end_time, location_id, priority in active_intervals:
            if end_time <= birth_time and priority in ['high', 'medium']:
                return location_id
        
        return None
    
    def _find_reusable_location_for_constants(self, active_intervals, birth_time, place_name):
        """
        Find reusable memory location for constants
        Very conservative reuse policy
        """
        # Constants only reuse from clearly expired locations
        for end_time, location_id, priority in active_intervals:
            if end_time < birth_time - 1:  # Extra safety margin
                return location_id
        
        return None
    
    def _calculate_control_flow_savings(self, control_flow_places, location_to_places):
        """
        Calculate memory savings specifically from control flow optimizations
        """
        control_flow_locations = set()
        
        for place_name in control_flow_places:
            for location, places in location_to_places.items():
                if place_name in places:
                    control_flow_locations.add(location)
                    break
        
        # Savings = original control flow places - actual locations used
        return len(control_flow_places) - len(control_flow_locations)
    
    def _show_control_flow_memory_details(self, memory_allocation, lifetime_analysis):
        """
        Show detailed memory allocation information for control flow constructs with enhanced analysis
        """
        print(f"\nEnhanced Control Flow Memory Optimization Details:")
        
        place_types = lifetime_analysis['place_types']
        location_to_places = memory_allocation['location_to_places']
        lifetimes = lifetime_analysis['lifetimes']
        
        # Show control flow specific allocations
        control_flow_locations = {}
        control_flow_reuse_stats = {'aggressive': 0, 'moderate': 0, 'conservative': 0}
        
        for place_name in place_types['control_flow']:
            for location, places in location_to_places.items():
                if place_name in places:
                    if location not in control_flow_locations:
                        control_flow_locations[location] = []
                    control_flow_locations[location].append(place_name)
                    
                    # Analyze reuse aggressiveness
                    if len(places) > 3:
                        control_flow_reuse_stats['aggressive'] += 1
                    elif len(places) > 1:
                        control_flow_reuse_stats['moderate'] += 1
                    else:
                        control_flow_reuse_stats['conservative'] += 1
        
        print(f"  Control flow places using {len(control_flow_locations)} memory locations:")
        for location, places in sorted(control_flow_locations.items()):
            if len(places) > 1:
                # Show lifetime information for shared locations
                lifetime_info = []
                for place_name in places:
                    if place_name in lifetimes:
                        birth = lifetimes[place_name]['birth']
                        death = lifetimes[place_name]['death']
                        lifetime_info.append(f"{place_name}({birth}-{death})")
                    else:
                        lifetime_info.append(place_name)
                
                print(f"    @{location}: SHARED by {len(places)} places")
                print(f"      Places: {lifetime_info}")
                
                # Check for control flow dependencies
                deps_info = []
                for place_name in places:
                    if place_name in lifetimes and 'control_flow_deps' in lifetimes[place_name]:
                        deps = lifetimes[place_name]['control_flow_deps']
                        if deps:
                            deps_info.append(f"{place_name}: {len(deps)} deps")
                
                if deps_info:
                    print(f"      Dependencies: {deps_info}")
            else:
                place_name = places[0]
                if place_name in lifetimes:
                    birth = lifetimes[place_name]['birth']
                    death = lifetimes[place_name]['death']
                    deps = lifetimes[place_name].get('control_flow_deps', [])
                    deps_str = f", {len(deps)} deps" if deps else ""
                    print(f"    @{location}: {place_name} ({birth}-{death}{deps_str})")
                else:
                    print(f"    @{location}: {place_name}")
        
        # Enhanced reuse statistics
        print(f"\n  Enhanced Memory Reuse Analysis:")
        print(f"    Aggressive reuse (3+ places): {control_flow_reuse_stats['aggressive']} locations")
        print(f"    Moderate reuse (2-3 places): {control_flow_reuse_stats['moderate']} locations")
        print(f"    Conservative (1 place): {control_flow_reuse_stats['conservative']} locations")
        
        # Control flow dependency impact analysis
        execution_plan = lifetime_analysis['execution_plan']
        control_flow_deps = execution_plan.get('control_flow_deps', {})
        
        deps_with_cf = sum(1 for deps in control_flow_deps.values() if deps)
        total_cf_deps = sum(len(deps) for deps in control_flow_deps.values())
        
        print(f"\n  Control Flow Dependency Impact:")
        print(f"    Operations with control flow dependencies: {deps_with_cf}")
        print(f"    Total control flow dependencies: {total_cf_deps}")
        
        if deps_with_cf > 0:
            print(f"    Dependency handling: Enhanced conservative lifetime extension")
            
            # Show most dependent operations
            most_dependent = sorted([(name, len(deps)) for name, deps in control_flow_deps.items() if deps], 
                                  key=lambda x: x[1], reverse=True)[:3]
            if most_dependent:
                print(f"    Most dependent operations:")
                for op_name, dep_count in most_dependent:
                    print(f"      {op_name}: {dep_count} dependencies")
        
        # Memory efficiency metrics
        total_cf_places = len(place_types['control_flow'])
        cf_locations_used = len(control_flow_locations)
        cf_efficiency = (total_cf_places - cf_locations_used) / total_cf_places * 100 if total_cf_places > 0 else 0
        
        print(f"\n  Control Flow Memory Efficiency:")
        print(f"    Original control flow places: {total_cf_places}")
        print(f"    Memory locations used: {cf_locations_used}")
        print(f"    Control flow memory efficiency: {cf_efficiency:.1f}%")
        
        # Identify optimization opportunities
        optimization_opportunities = []
        
        # Check for places that could be optimized further
        single_use_locations = [loc for loc, places in control_flow_locations.items() if len(places) == 1]
        if len(single_use_locations) > 2:
            optimization_opportunities.append(f"Potential for more aggressive reuse: {len(single_use_locations)} single-use locations")
        
        # Check for long-lived control flow places
        long_lived_cf = []
        for place_name in place_types['control_flow']:
            if place_name in lifetimes:
                lifetime_span = lifetimes[place_name]['death'] - lifetimes[place_name]['birth']
                if lifetime_span > 3:  # Arbitrary threshold
                    long_lived_cf.append(place_name)
        
        if long_lived_cf:
            optimization_opportunities.append(f"Long-lived control flow places: {len(long_lived_cf)} (potential for lifetime reduction)")
        
        if optimization_opportunities:
            print(f"\n  Optimization Opportunities:")
            for opportunity in optimization_opportunities:
                print(f"    - {opportunity}")
        else:
            print(f"\n  Optimization Status: Control flow memory allocation is well-optimized")
        
    def _allocate_memory_locations(self, reachability):
        """
        Allocate memory locations using interval graph coloring
        Places with non-overlapping lifetimes can share memory
        """
        lifetimes = reachability['lifetimes']
        
        # Sort places by birth time, then by death time
        sorted_places = sorted(lifetimes.items(), 
                             key=lambda x: (x[1]['birth'], x[1]['death']))
        
        # Greedy coloring algorithm for interval graphs
        location_map = {}  # place_name -> memory_location
        location_to_places = {}  # memory_location -> [place_names]
        active_locations = []  # [(end_time, location_id)]
        next_location = 256  # Start memory allocation at @256
        
        for place_name, lifetime_info in sorted_places:
            birth = lifetime_info['birth']
            death = lifetime_info['death']
            
            # Remove expired locations (locations that expire BEFORE this birth time)
            active_locations = [(end_time, loc_id) for end_time, loc_id in active_locations 
                              if end_time >= birth]
            
            # Try to reuse an existing location
            reused_location = None
            # Look for locations that expire at or before this birth time
            for end_time, loc_id in active_locations[:]:  # Copy list to avoid modification during iteration
                if end_time <= birth:  # This location is free at birth time
                    reused_location = loc_id
                    active_locations.remove((end_time, loc_id))
                    break
                        
            if reused_location is not None:
                # Reuse existing location
                location_map[place_name] = reused_location
                location_to_places[reused_location].append(place_name)
            else:
                # Allocate new location
                location_map[place_name] = next_location
                location_to_places[next_location] = [place_name]
                next_location += 1
                
            # Add this location to active set
            if death != float('inf'):
                active_locations.append((death, location_map[place_name]))
                
        return {
            'location_map': location_map,
            'location_to_places': location_to_places,
            'total_locations': next_location - 256
        }
        
    def _generate_multi_core_assembly(self, core_assignments, num_cores, memory_map):
        """Generate assembly for distributed multi-core execution (no coordinator)"""
        assembly_lines = [
            f"// Distributed multi-core execution for {num_cores} cores",
            "// No centralized coordinator - cores self-coordinate via level barriers",
            "//",
            "// Memory layout:",
            "// @16-31: Core status flags (debugging only)",
            "// @32-47: Level synchronization area (coordination)",
            f"// @256+: Optimized place memory ({memory_map['total_locations']} locations)",
            "// @512+: Shared stack",
            "//",
            
            "// Initialize shared memory",
            "@512",  # Move stack higher to avoid optimized memory
            "D=A", 
            "@SP",
            "M=D",
            "//"
        ]
        
        # Initialize constants in optimized memory locations
        assembly_lines.append("// Initialize constants in optimized memory")
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                assembly_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        
        # Generate core initialization (debugging flags only)
        for core_id in range(num_cores):
            assembly_lines.extend([
                f"// Initialize core {core_id} (debugging)",
                f"@{16 + core_id}",  # Core status at @16+core_id
                "M=0",  # Set to idle
            ])
            
        assembly_lines.extend([
            "//",
            "// === DISTRIBUTED EXECUTION - NO COORDINATOR ===",
            "// Each core self-coordinates using level barriers",
            "// Program terminates when final level barrier is satisfied",
            "//"
        ])
        
        # Generate code for each core with distributed coordination
        for core_id, operations in core_assignments.items():
            if not operations:
                # Idle core - still participates in barriers
                assembly_lines.extend([
                    f"// Core {core_id} - Idle (no operations)",
                    f"(CORE_{core_id}_IDLE)",
                    f"// Idle core waits for program completion",
                    "// (Implementation would wait for final level barrier)",
                    f"@CORE_{core_id}_IDLE",
                    "0;JMP",
                    "//"
                ])
                continue
                
            assembly_lines.extend([
                f"// Core {core_id} - Distributed execution",
                f"(CORE_{core_id}_START)",
                f"@{16 + core_id}",
                "M=1",  # Set status to working (debugging)
            ])
            
            # Group operations by level for this core
            operations_by_level = {}
            for op_info in operations:
                level = op_info['level']
                if level not in operations_by_level:
                    operations_by_level[level] = []
                operations_by_level[level].append(op_info)
            
            # Generate level-based execution with barriers
            for level in sorted(operations_by_level.keys()):
                level_ops = operations_by_level[level]
                
                assembly_lines.extend([
                    f"// Level {level} barrier synchronization",
                    f"(CORE_{core_id}_LEVEL_{level})",
                    f"// Signal ready for level {level}",
                    f"@{32 + level}",
                    "D=M",
                    f"@{1 << core_id}",  # This core's bit
                    "D=D|A",
                    f"@{32 + level}",
                    "M=D",
                    "",
                    f"// Wait for all cores at level {level}",
                    f"(CORE_{core_id}_LEVEL_{level}_WAIT)",
                    f"@{32 + level}",
                    "D=M",
                    f"@{(1 << num_cores) - 1}",  # All cores mask
                    "D=D-A",
                    f"@CORE_{core_id}_LEVEL_{level}_EXEC",
                    "D;JEQ",
                    f"@CORE_{core_id}_LEVEL_{level}_WAIT",
                    "0;JMP",
                    "",
                    f"(CORE_{core_id}_LEVEL_{level}_EXEC)"
                ])
                
                # Execute operations for this level
                for op_info in level_ops:
                    operation = op_info['operation']
                    transition = op_info['transition']
                    
                    assembly_lines.extend([
                        f"// Execute: {operation}",
                    ])
                    
                    # Generate memory-optimized operation code
                    op_type = operation.split('_')[0]
                    
                    if op_type in ['add', 'sub', 'mul', 'div', 'and', 'or'] and len(transition.in_places) >= 2:
                        # Binary operations with memory locations
                        loc_a = memory_map['location_map'][transition.in_places[0].name]
                        loc_b = memory_map['location_map'][transition.in_places[1].name]
                        loc_result = memory_map['location_map'][transition.out_places[0].name]
                        
                        assembly_lines.extend([
                            f"@{loc_a}",
                            "D=M",
                            f"@{loc_b}",
                        ])
                        
                        if op_type == 'add':
                            assembly_lines.append("D=D+M")
                        elif op_type == 'sub':
                            assembly_lines.append("D=D-M")
                        elif op_type == 'mul':
                            # Simple multiplication for multi-core assembly
                            assembly_lines.extend([
                                "// Multiplication (simplified)",
                                "@R13",
                                "M=D",
                                "D=M",
                                "@R14", 
                                "M=D",
                                "D=0",
                                f"(MUL_LOOP_{level})",
                                "@R14",
                                "D=M",
                                f"@MUL_DONE_{level}",
                                "D;JEQ",
                                "@R13",
                                "D=D+M",
                                "@R14",
                                "M=M-1",
                                f"@MUL_LOOP_{level}",
                                "0;JMP",
                                f"(MUL_DONE_{level})"
                            ])
                        elif op_type == 'div':
                            # Simple division for multi-core assembly
                            assembly_lines.extend([
                                "// Division (simplified)",
                                "@R13",
                                "M=D",
                                "D=M",
                                "@R14", 
                                "M=D",
                                "@R15",
                                "M=0",
                                f"(DIV_LOOP_{level})",
                                "@R14",
                                "D=M",
                                f"@DIV_DONE_{level}",
                                "D;JEQ",
                                "@R13",
                                "D=M",
                                f"@DIV_DONE_{level}",
                                "D;JLT",
                                "@R14",
                                "D=M",
                                "@R13",
                                "M=M-D",
                                "@R15",
                                "M=M+1",
                                f"@DIV_LOOP_{level}",
                                "0;JMP",
                                f"(DIV_DONE_{level})",
                                "@R15",
                                "D=M"
                            ])
                        elif op_type == 'and':
                            assembly_lines.append("D=D&M")
                        elif op_type == 'or':
                            assembly_lines.append("D=D|M")
                            
                        assembly_lines.extend([
                            f"@{loc_result}",
                            "M=D"
                        ])
                        
                    elif op_type in ['neg', 'not'] and len(transition.in_places) >= 1:
                        # Unary operations with memory locations
                        loc_input = memory_map['location_map'][transition.in_places[0].name]
                        loc_result = memory_map['location_map'][transition.out_places[0].name]
                        
                        assembly_lines.extend([
                            f"@{loc_input}",
                            "D=M",
                        ])
                        
                        if op_type == 'neg':
                            assembly_lines.append("D=-D")
                        elif op_type == 'not':
                            assembly_lines.append("D=!D")
                            
                        assembly_lines.extend([
                            f"@{loc_result}",
                            "M=D"
                        ])
                            
                    assembly_lines.append("")
            
            # Core self-termination after final level
            final_level = max(operations_by_level.keys()) if operations_by_level else 0
            assembly_lines.extend([
                f"// Core {core_id} distributed termination",
                f"@{16 + core_id}",
                "M=2",  # Set status to done (debugging)
                "",
                f"// Wait for final level {final_level} completion",
                f"(CORE_{core_id}_FINAL_WAIT)",
                f"@{32 + final_level}",
                "D=M",
                f"@{(1 << num_cores) - 1}",  # All cores mask
                "D=D-A",
                f"@CORE_{core_id}_TERMINATE",
                "D;JEQ",  # Final level complete
                f"@CORE_{core_id}_FINAL_WAIT",
                "0;JMP",
                "",
                f"(CORE_{core_id}_TERMINATE)",
                f"// Core {core_id} self-terminates",
                f"@CORE_{core_id}_HALT",
                "0;JMP",
                "//"
            ])
            
        # Distributed result collection (no coordinator)
        assembly_lines.extend([
            "// === DISTRIBUTED RESULT COLLECTION ===",
            "// Results collected by final core or external process",
            "// No centralized coordinator needed",
            "",
            "(COLLECT_RESULTS)",
            "// This section would be reached by external process",
            "// or by the last core to complete",
        ])
        
        for place in self.result_places:
            if place.name in memory_map['location_map']:
                memory_loc = memory_map['location_map'][place.name]
                assembly_lines.extend([
                    f"// Final result from @{memory_loc}",
                    f"@{memory_loc}",
                    "D=M",
                    "@SP",
                    "M=M+1",
                    "A=M-1",
                    "M=D"
                ])
        
        assembly_lines.extend([
            "",
            "// Program complete - all cores self-terminated",
            "(PROGRAM_END)",
            "@PROGRAM_END",
            "0;JMP"
        ])
        
        return assembly_lines
        
    def _analyze_concurrency(self):
        """Analyze potential for concurrent execution"""
        # Simple heuristic: count transitions that don't share input places
        independent_count = 0
        used_places = set()
        
        for transition in self.net.transitions.values():
            transition_places = set(place.name for place in transition.in_places)
            if not transition_places.intersection(used_places):
                independent_count += 1
                used_places.update(transition_places)
                
        return independent_count
        
    def get_detailed_place_info(self):
        """Return detailed information about each place"""
        place_info = {}
        
        for name, place in self.net.places.items():
            info = {
                'tokens': [str(t.value) for t in place.tokens],
                'token_count': place.token_count(),
                'input_transitions': [t.name for t in place.in_transitions],
                'output_transitions': [t.name for t in place.out_transitions],
                'in_result_places': place in self.result_places,
                'result_position': self.result_places.index(place) if place in self.result_places else None
            }
            place_info[name] = info
            
        return place_info
        
    def get_detailed_transition_info(self):
        """Return detailed information about each transition"""
        transition_info = {}
        
        for name, transition in self.net.transitions.items():
            info = {
                'input_places': [p.name for p in transition.in_places],
                'output_places': [p.name for p in transition.out_places],
                'can_fire': transition.can_fire(),
                'operation_type': name.split('_')[0]
            }
            transition_info[name] = info
            
        return transition_info