from Petri.net import PetriNet
from Petri.Token import Token
from Petri.Place import Place
from Petri.Transition import Transition

class PetriEmitter:

    def __init__(self):
        self.net = PetriNet()
        self.control_stack = []
        self.memory_simulation = {}  # Shared memory for simulation: {segment_type: {index: value}}

        self.net.add_place(Place("init"))
        self.net.add_place(Place("end"))

        self.net.places["init"].put_token(Token("control"))

    def _insert_operation(self, transition, output_place, consumes_stack=0, produces_stack=1):
        """
        Insert an operation into the Petri net with proper stack-based connections.
        
        For operations that consume 0 from stack (like push), we use a dup-based
        branching strategy to allow parallel execution while maintaining stack order.
        
        Args:
            transition: The transition to add
            output_place: The output place of the transition
            consumes_stack: Number of stack items this operation consumes
            produces_stack: Number of stack items this operation produces (0 or 1)
        
        Returns:
            The added transition
        """
        # Validate inputs
        if consumes_stack < 0 or produces_stack < 0 or produces_stack > 1:
            raise ValueError("Invalid stack consumption/production values")
        
        if consumes_stack > len(self.control_stack):
            raise RuntimeError(f"Stack underflow: need {consumes_stack} items, have {len(self.control_stack)}")
        
        # Add the transition to the network
        self.net.add_transition(transition)
        
        # Handle input connections
        if consumes_stack > 0:
            # Connect input places from stack (pop in reverse order to maintain stack semantics)
            for i in range(consumes_stack):
                input_place = self.control_stack.pop()
                self.net.add_arc(input_place, transition)
        else:
            # Operation consumes 0 from stack (e.g., push constant)
            # These can run in parallel - connect directly to init via dup branching
            self._connect_parallel_operation(transition)
        
        # Connect output place (data)
        self.net.add_arc(transition, output_place)
        
        # Push output place to stack if operation produces a value
        if produces_stack == 1:
            self.control_stack.append(output_place)
        
        return transition

    def _connect_parallel_operation(self, transition):
        """
        Connect a parallel operation (consumes 0 from stack) using dup branching.
        This allows multiple push operations to execute in parallel.
        """
        init_place = self.net.places["init"]
        
        # Find existing transitions connected to init
        init_consumers = [t for t in self.net.transitions.values() 
                        if init_place in t.in_places]
        
        if len(init_consumers) == 0:
            # First parallel operation - connect directly to init
            self.net.add_arc(init_place, transition)
        else:
            # Need to create/extend dup chain for parallel execution
            # Find the dup transition that feeds from init, or create one
            dup_trans = None
            for t in self.net.transitions.values():
                if t.name.startswith("dup_") and init_place in t.in_places:
                    dup_trans = t
                    break
            
            if dup_trans is None:
                # Create first dup: init -> dup -> {existing_consumer, new_transition}
                existing_consumer = init_consumers[0]
                
                # Remove arc from init to existing consumer
                self.net.arcs = [(src, tgt) for src, tgt in self.net.arcs 
                               if not (src == init_place.name and tgt == existing_consumer.name)]
                existing_consumer.in_places.remove(init_place)
                
                # Create dup outputs
                dup_out1, dup_out2 = self._create_dup_transition(init_place)
                
                # Connect existing consumer to first dup output
                self.net.add_arc(dup_out1, existing_consumer)
                
                # Connect new transition to second dup output
                self.net.add_arc(dup_out2, transition)
            else:
                # Extend existing dup chain - add another output
                # Create a new dup output place and connect the new transition
                new_dup_out = Place(f"dup_out_{len(self.net.places)}")
                self.net.add_place(new_dup_out)
                
                # Modify dup to have additional output
                dup_trans.out_places.append(new_dup_out)
                self.net.arcs.append((dup_trans.name, new_dup_out.name))
                
                # Update dup operation to produce more tokens
                num_outputs = len(dup_trans.out_places)
                dup_trans.operation = lambda tokens, n=num_outputs: [tokens[0]] * n
                
                # Connect new transition to new dup output
                self.net.add_arc(new_dup_out, transition)

    def _generate_label_assembly(self):
        """
        Generate assembly labels for all label places that have incoming transitions.
        This should be called after all operations are added to the net.
        """
        if not hasattr(self.net, 'labels'):
            return []
        
        assembly_lines = []
        for label_name, label_place in self.net.labels.items():
            # Always generate labels that exist in the registry
            # They will be referenced by goto/if-goto operations
            assembly_lines.append(f"({label_name})")
        
        return assembly_lines

    def _create_dup_transition(self, input_place):
        """
        Create a dup transition that takes 1 input and produces 2 outputs.
        Returns the two output places.
        """
        # Create dup transition
        dup_transition = Transition(
            name=f"dup_{len(self.net.transitions)}",
            operation=lambda tokens: [tokens[0], tokens[0]],  # Duplicate the token
            emit_function=self._emit_dup_assembly
        )
        self.net.add_transition(dup_transition)
        
        # Create output places
        dup_out1 = Place(f"dup_out1_{len(self.net.places)}")
        dup_out2 = Place(f"dup_out2_{len(self.net.places)}")
        self.net.add_place(dup_out1)
        self.net.add_place(dup_out2)
        
        # Connect: input_place -> dup -> {dup_out1, dup_out2}
        self.net.add_arc(input_place, dup_transition)
        self.net.add_arc(dup_transition, dup_out1)
        self.net.add_arc(dup_transition, dup_out2)
        
        return dup_out1, dup_out2

    def _create_dup_branch(self, new_transition):
        """
        Create a dup transition to enable branching when multiple operations
        need to consume from the same source.
        """
        # Always branch from init for operations that consume 0 from stack
        control_source = self.net.places["init"]
        
        # Find existing transitions that consume from the control source
        source_consumers = []
        for trans in self.net.transitions.values():
            if control_source in trans.in_places:
                source_consumers.append(trans)
        
        if len(source_consumers) == 1:
            # There's exactly one existing consumer - create dup to branch
            existing_transition = source_consumers[0]
            
            # Remove existing arc from source to existing transition
            self.net.arcs = [(src, tgt) for src, tgt in self.net.arcs 
                           if not (src == control_source.name and tgt == existing_transition.name)]
            existing_transition.in_places.remove(control_source)
            
            # Create dup transition using the helper method
            dup_out1, dup_out2 = self._create_dup_transition(control_source)
            
            # Connect existing transition to one dup output
            self.net.add_arc(dup_out1, existing_transition)
            
            # Connect new transition to other dup output
            self.net.add_arc(dup_out2, new_transition)
            
        elif len(source_consumers) > 1:
            # Multiple consumers already exist - connect to source directly
            self.net.add_arc(control_source, new_transition)
        else:
            # No existing consumers - connect directly
            self.net.add_arc(control_source, new_transition)

    def _emit_dup_assembly(self, transition):
        """
        Generate assembly code for dup transition.
        For control flow duplication, no actual data needs to be read or written.
        """
        assembly = []
        
        if len(transition.in_places) != 1 or len(transition.out_places) != 2:
            return ["// dup - invalid configuration"]
        
        input_place = transition.in_places[0]
        
        # If this is duplicating from init (control flow), no data movement needed
        if input_place.name == "init":
            assembly.append("// dup control token - no data movement needed")
            return assembly
        
        # Check if this is duplicating between dup output places (also control flow)
        if input_place.name.startswith("dup_out"):
            assembly.append("// dup control token - no data movement needed")
            return assembly
        
        # For other cases, read from input and write to outputs
        output_place1 = transition.out_places[0]
        output_place2 = transition.out_places[1]
        
        # Read from input place
        if input_place.memory_address is not None:
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
        else:
            assembly.append("// dup - input has no memory address")
            return assembly
        
        # Write to first output place
        if output_place1.memory_address is not None:
            assembly.append(f"@R{output_place1.memory_address}")
            assembly.append("M=D")
        
        # Write to second output place
        if output_place2.memory_address is not None:
            assembly.append(f"@R{output_place2.memory_address}")
            assembly.append("M=D")
        
        return assembly


    def label(self, vmc):
        """
        Implement label operation by creating a label place that can be referenced by goto/if-goto.
        Labels are places in the Petri net, not transitions, so multiple transitions can reference them.
        With shared ROM, labels can be jumped to from any CPU core.
        """
        label_name = vmc.index  # The label name from the VM command
        
        # Create a place to represent this label - this is the jump target
        label_place_name = f"label_{label_name}"
        label_place = Place(label_place_name)
        label_place.label_name = label_name  # Store the original label name for reference
        label_place.is_label = True  # Mark this as a label place
        self.net.add_place(label_place)
        
        # Store label in a registry for goto/if-goto to find
        if not hasattr(self.net, 'labels'):
            self.net.labels = {}
        self.net.labels[label_name] = label_place
        
        # Labels don't need transitions - they're just places that can be jumped to
        # The assembly label will be generated when a transition connects to this place
        return label_place
        
    def goto(self, vmc):
        """
        Implement goto operation by creating an unconditional jump to a label place.
        With shared ROM, any CPU can jump to any label in the shared instruction space.
        """
        target_label = vmc.index  # The target label name
        
        # Find the label place (it should have been created by a label command)
        if not hasattr(self.net, 'labels'):
            self.net.labels = {}
        
        if target_label not in self.net.labels:
            # Create the label place if it doesn't exist yet (forward reference)
            label_place = Place(f"label_{target_label}")
            label_place.label_name = target_label
            label_place.is_label = True
            self.net.add_place(label_place)
            self.net.labels[target_label] = label_place
        
        target_place = self.net.labels[target_label]
        
        # Create emit function for goto
        def emit_goto(transition):
            assembly = []
            # Generate unconditional jump to target label in shared ROM
            assembly.append(f"@{target_label}")
            assembly.append("0;JMP")
            return assembly
        
        # Create transition that performs the goto
        goto_transition = Transition(
            name=f"goto_{target_label}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(f"goto_{target_label}")],  # Control token
            emit_function=emit_goto
        )
        
        # Add the transition and connect it to the target label place
        self.net.add_transition(goto_transition)
        
        # Goto connects from current control flow to the label place
        if len(self.control_stack) == 0:
            # Connect from init if no stack
            self.net.add_arc(self.net.places["init"], goto_transition)
        else:
            # This is tricky - goto should consume control flow but not stack values
            # For now, connect from init and handle branching
            self._create_dup_branch(goto_transition)
        
        # Connect to the target label place
        self.net.add_arc(goto_transition, target_place)
        
        return goto_transition
            
    def ifgoto(self, vmc):
        """
        Implement if-goto operation by creating a conditional jump to a label place.
        Pops one value from stack and jumps to label if value is non-zero (true).
        With shared ROM, any CPU can jump to any label in the shared instruction space.
        """
        target_label = vmc.index  # The target label name
        
        # Find the label place (it should have been created by a label command)
        if not hasattr(self.net, 'labels'):
            self.net.labels = {}
        
        if target_label not in self.net.labels:
            # Create the label place if it doesn't exist yet (forward reference)
            label_place = Place(f"label_{target_label}")
            label_place.label_name = target_label
            label_place.is_label = True
            self.net.add_place(label_place)
            self.net.labels[target_label] = label_place
        
        target_place = self.net.labels[target_label]
        
        # Create emit function for if-goto
        def emit_ifgoto(transition):
            assembly = []
            
            # Get input place (should be 1) - the condition value
            if len(transition.in_places) != 1:
                return ["// if-goto - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load condition value into D register
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// if-goto - condition has no memory address")
                return assembly
            
            # Jump to target label in shared ROM if D != 0 (non-zero means true)
            assembly.append(f"@{target_label}")
            assembly.append("D;JNE")
            
            return assembly
        
        # Create transition that performs the conditional jump
        ifgoto_transition = Transition(
            name=f"ifgoto_{target_label}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(f"ifgoto_{target_label}")],  # Control token
            emit_function=emit_ifgoto
        )
        
        # Add the transition
        self.net.add_transition(ifgoto_transition)
        
        # If-goto consumes 1 from stack (the condition)
        if len(self.control_stack) > 0:
            condition_place = self.control_stack.pop()
            self.net.add_arc(condition_place, ifgoto_transition)
        else:
            raise RuntimeError("Stack underflow: if-goto needs a condition value")
        
        # Connect to the target label place
        self.net.add_arc(ifgoto_transition, target_place)
        
        return ifgoto_transition
                
    def function(self, vmc):
        """
        Implement function declaration by creating a function entry place.
        The function place serves as a control flow target for calls.
        """
        function_name = vmc.segment  # Function name
        n_locals = vmc.index        # Number of local variables
        
        # Create a place to represent this function entry point
        function_place_name = f"function_{function_name}"
        function_place = Place(function_place_name)
        function_place.function_name = function_name
        function_place.n_locals = n_locals
        function_place.is_function = True
        self.net.add_place(function_place)
        
        # Store function in a registry for call to find
        if not hasattr(self.net, 'functions'):
            self.net.functions = {}
        self.net.functions[function_name] = function_place
        
        # Create emit function for function declaration
        def emit_function(transition):
            assembly = []
            # Generate function label - this is the main assembly output
            assembly.append(f"({function_name})")
            return assembly
        
        # Create transition for function entry
        function_transition = Transition(
            name=f"function_{function_name}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(f"function_{function_name}")],
            emit_function=emit_function
        )
        
        # Use the general method to add this operation
        return self._insert_operation(function_transition, function_place, consumes_stack=0, produces_stack=1)
            
    def call(self, vmc):
        """
        Implement function call by creating a call transition.
        This represents the control flow to the called function.
        """
        function_name = vmc.segment  # Function name to call
        n_args = vmc.index          # Number of arguments
        
        # Create a place to hold the call result
        call_result_place = Place(f"call_result_{function_name}_{len(self.net.places)}")
        self.net.add_place(call_result_place)
        
        # Create emit function for call
        def emit_call(transition):
            assembly = []
            # Generate call assembly - minimal for Petri net approach
            assembly.append(f"@{function_name}")
            assembly.append("0;JMP")
            return assembly
        
        # Create transition for function call
        call_transition = Transition(
            name=f"call_{function_name}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(f"call_{function_name}")],
            emit_function=emit_call
        )
        
        # Call consumes n_args from stack and produces 1 result
        return self._insert_operation(call_transition, call_result_place, consumes_stack=n_args, produces_stack=1)
            
    def ret(self, vmc):
        """
        Implement return from function by creating a return transition.
        This represents the control flow back to the caller.
        """
        # Create a place to represent the return point
        return_place = Place(f"return_{len(self.net.places)}")
        self.net.add_place(return_place)
        
        # Create emit function for return
        def emit_return(transition):
            assembly = []
            # Simple return assembly for Petri net approach
            assembly.append("// return")
            return assembly
        
        # Create transition for return
        return_transition = Transition(
            name=f"return_{len(self.net.transitions)}",
            operation=lambda tokens: [Token("return")],
            emit_function=emit_return
        )
        
        # Return consumes 1 from stack (the return value) and produces 1 (control flow)
        return self._insert_operation(return_transition, return_place, consumes_stack=1, produces_stack=1)


    def add(self, vmc):
        """
        Implement add operation by creating a transition that consumes two values
        from the stack and produces their sum.
        """
        # Create a place to hold the result
        result_place_name = f"add_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for add operation
        def emit_add(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// add - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// add - first operand has no memory address")
                return assembly
            
            # Add second operand to D register
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D+M")
            else:
                assembly.append("// add - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the addition
        add_transition = Transition(
            name=f"add_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(tokens[1].value + tokens[0].value)],  # tokens[1] + tokens[0] (stack order)
            emit_function=emit_add
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(add_transition, result_place, consumes_stack=2, produces_stack=1)

    def sub(self, vmc):
        """
        Implement sub operation by creating a transition that consumes two values
        from the stack and produces their difference (second operand - first operand).
        """
        # Create a place to hold the result
        result_place_name = f"sub_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for sub operation
        def emit_sub(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// sub - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// sub - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// sub - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the subtraction
        sub_transition = Transition(
            name=f"sub_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(tokens[1].value - tokens[0].value)],  # tokens[1] - tokens[0] (stack order)
            emit_function=emit_sub
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(sub_transition, result_place, consumes_stack=2, produces_stack=1)

    def neg(self, vmc):
        """
        Implement neg operation by creating a transition that consumes one value
        from the stack and produces its negation (-value).
        """
        # Create a place to hold the result
        result_place_name = f"neg_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for neg operation
        def emit_neg(transition):
            assembly = []
            
            # Get input place (should be 1) and output place
            if len(transition.in_places) != 1:
                return ["// neg - invalid input configuration"]
            
            input_place = transition.in_places[0]
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load operand into D register
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// neg - operand has no memory address")
                return assembly
            
            # Negate D register (D = -D)
            assembly.append("D=-D")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the negation
        neg_transition = Transition(
            name=f"neg_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(-tokens[0].value)],  # Negate the single token
            emit_function=emit_neg
        )
        
        # Use the general method to add this operation (consumes 1, produces 1)
        return self._insert_operation(neg_transition, result_place, consumes_stack=1, produces_stack=1)

    def lt(self, vmc):
        """
        Implement lt (less than) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if second operand < first operand, 0 (false) otherwise.
        Stack semantics: second_operand < first_operand
        """
        # Create a place to hold the result
        result_place_name = f"lt_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for lt operation
        def emit_lt(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// lt - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// lt - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// lt - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"LT_TRUE_{id(transition)}"
            end_label = f"LT_END_{id(transition)}"
            
            # Jump to true label if D < 0 (second_operand < first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JLT")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the less than comparison
        lt_transition = Transition(
            name=f"lt_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(-1 if tokens[1].value < tokens[0].value else 0)],  # tokens[1] < tokens[0] (stack order)
            emit_function=emit_lt
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(lt_transition, result_place, consumes_stack=2, produces_stack=1)

    def eq(self, vmc):
        """
        Implement eq (equals) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if they are equal, 0 (false) otherwise.
        Stack semantics: second_operand == first_operand
        """
        # Create a place to hold the result
        result_place_name = f"eq_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for eq operation
        def emit_eq(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// eq - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// eq - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// eq - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"EQ_TRUE_{len(transition.out_places)}_{id(transition)}"
            end_label = f"EQ_END_{len(transition.out_places)}_{id(transition)}"
            
            # Jump to true label if D == 0 (second_operand == first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JEQ")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the equality comparison
        eq_transition = Transition(
            name=f"eq_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(-1 if tokens[1].value == tokens[0].value else 0)],  # tokens[1] == tokens[0] (stack order)
            emit_function=emit_eq
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(eq_transition, result_place, consumes_stack=2, produces_stack=1)

    def gt(self, vmc):
        """
        Implement gt (greater than) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if second operand > first operand, 0 (false) otherwise.
        Stack semantics: second_operand > first_operand
        """
        # Create a place to hold the result
        result_place_name = f"gt_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for gt operation
        def emit_gt(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// gt - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// gt - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// gt - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"GT_TRUE_{id(transition)}"
            end_label = f"GT_END_{id(transition)}"
            
            # Jump to true label if D > 0 (second_operand > first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JGT")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the greater than comparison
        gt_transition = Transition(
            name=f"gt_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(-1 if tokens[1].value > tokens[0].value else 0)],  # tokens[1] > tokens[0] (stack order)
            emit_function=emit_gt
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(gt_transition, result_place, consumes_stack=2, produces_stack=1)

    def and_op(self, vmc):
        """
        Implement and (bitwise AND) operation by creating a transition that consumes two values
        from the stack and produces their bitwise AND result.
        Stack semantics: second_operand & first_operand
        """
        # Create a place to hold the result
        result_place_name = f"and_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for and operation
        def emit_and(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// and - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// and - first operand has no memory address")
                return assembly
            
            # Perform bitwise AND with second operand (top of stack)
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D&M")
            else:
                assembly.append("// and - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise AND
        and_transition = Transition(
            name=f"and_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(tokens[1].value & tokens[0].value)],  # tokens[1] & tokens[0] (stack order)
            emit_function=emit_and
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(and_transition, result_place, consumes_stack=2, produces_stack=1)

    def or_op(self, vmc):
        """
        Implement or (bitwise OR) operation by creating a transition that consumes two values
        from the stack and produces their bitwise OR result.
        Stack semantics: second_operand | first_operand
        """
        # Create a place to hold the result
        result_place_name = f"or_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for or operation
        def emit_or(transition):
            assembly = []
            
            # Get input places (should be 2) and output place
            if len(transition.in_places) != 2:
                return ["// or - invalid input configuration"]
            
            input_place1 = transition.in_places[0]  # Second operand (top of stack)
            input_place2 = transition.in_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// or - first operand has no memory address")
                return assembly
            
            # Perform bitwise OR with second operand (top of stack)
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D|M")
            else:
                assembly.append("// or - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise OR
        or_transition = Transition(
            name=f"or_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(tokens[1].value | tokens[0].value)],  # tokens[1] | tokens[0] (stack order)
            emit_function=emit_or
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(or_transition, result_place, consumes_stack=2, produces_stack=1)

    def not_op(self, vmc):
        """
        Implement not (bitwise NOT) operation by creating a transition that consumes one value
        from the stack and produces its bitwise NOT result (~value).
        """
        # Create a place to hold the result
        result_place_name = f"not_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for not operation
        def emit_not(transition):
            assembly = []
            
            # Get input place (should be 1) and output place
            if len(transition.in_places) != 1:
                return ["// not - invalid input configuration"]
            
            input_place = transition.in_places[0]
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load operand into D register
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// not - operand has no memory address")
                return assembly
            
            # Perform bitwise NOT (D = !D)
            assembly.append("D=!D")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise NOT
        not_transition = Transition(
            name=f"not_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(~tokens[0].value)],  # Bitwise NOT of the single token
            emit_function=emit_not
        )
        
        # Use the general method to add this operation (consumes 1, produces 1)
        return self._insert_operation(not_transition, result_place, consumes_stack=1, produces_stack=1)

    def push_constant(self, vmc):
        """
        Implement push constant operation by creating a place for the constant
        and a transition that produces it.
        """
        constant_value = vmc.index
        
        # Create a place to hold the constant value
        constant_place_name = f"const_{constant_value}_{len(self.net.places)}"
        constant_place = Place(constant_place_name)
        self.net.add_place(constant_place)
        
        # Create emit function for push constant
        def emit_push_constant(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load constant value into D register
            assembly.append(f"@{constant_value}")
            assembly.append("D=A")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that produces the constant
        push_const_transition = Transition(
            name=f"push_const_{constant_value}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(constant_value), Token(constant_value)],  # Data token, then flow token
            emit_function=emit_push_constant
        )
        
        # Use the general method to add this operation (pushes 1 item to stack)
        return self._insert_operation(push_const_transition, constant_place, consumes_stack=0, produces_stack=1)

    def push_local(self, vmc):
        """Handle push local command - pushes local[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the local value
        local_place = Place(f"local_{index}_{len(self.net.places)}")
        self.net.add_place(local_place)
        
        # Create emit function for push local
        def emit_push_local(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load local[index] into D register
            assembly.append("@LCL")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the local value
        def push_local_operation(tokens):
            # Read the value from shared memory simulation
            if 'local' in self.memory_simulation and index in self.memory_simulation['local']:
                value = self.memory_simulation['local'][index]
            else:
                value = 0  # Default value if not set
            return [Token(value), Token(value)]  # Data token, then flow token
        
        push_local_transition = Transition(
            name=f"push_local_{index}_{len(self.net.transitions)}",
            operation=push_local_operation,
            emit_function=emit_push_local
        )
        
        return self._insert_operation(push_local_transition, local_place, consumes_stack=0, produces_stack=1)

    def push_argument(self, vmc):
        """Handle push argument command - pushes argument[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the argument value
        arg_place = Place(f"arg_{index}_{len(self.net.places)}")
        self.net.add_place(arg_place)
        
        # Create emit function for push argument
        def emit_push_argument(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load argument[index] into D register
            assembly.append("@ARG")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the argument value
        # Create transition that pushes the argument value
        def push_arg_operation(tokens):
            # Read the value from shared memory simulation
            if 'argument' in self.memory_simulation and index in self.memory_simulation['argument']:
                value = self.memory_simulation['argument'][index]
            else:
                value = 0  # Default value if not set
            return [Token(value), Token(value)]  # Data token, then flow token
        
        push_arg_transition = Transition(
            name=f"push_arg_{index}_{len(self.net.transitions)}",
            operation=push_arg_operation,
            emit_function=emit_push_argument
        )
        
        return self._insert_operation(push_arg_transition, arg_place, consumes_stack=0, produces_stack=1)

    def push_this(self, vmc):
        """Handle push this command - pushes this[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the this value
        this_place = Place(f"this_{index}_{len(self.net.places)}")
        self.net.add_place(this_place)
        
        # Create emit function for push this
        def emit_push_this(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load this[index] into D register
            assembly.append("@THIS")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the this value
        # Create transition that pushes the this value
        def push_this_operation(tokens):
            # Read the value from shared memory simulation
            if 'this' in self.memory_simulation and index in self.memory_simulation['this']:
                value = self.memory_simulation['this'][index]
            else:
                value = 0  # Default value if not set
            return [Token(value), Token(value)]  # Data token, then flow token
        
        push_this_transition = Transition(
            name=f"push_this_{index}_{len(self.net.transitions)}",
            operation=push_this_operation,
            emit_function=emit_push_this
        )
        
        return self._insert_operation(push_this_transition, this_place, consumes_stack=0, produces_stack=1)

    def push_that(self, vmc):
        """Handle push that command - pushes that[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the that value
        that_place = Place(f"that_{index}_{len(self.net.places)}")
        self.net.add_place(that_place)
        
        # Create emit function for push that
        def emit_push_that(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load that[index] into D register
            assembly.append("@THAT")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the that value
        # Create transition that pushes the that value
        def push_that_operation(tokens):
            # Read the value from shared memory simulation
            if 'that' in self.memory_simulation and index in self.memory_simulation['that']:
                value = self.memory_simulation['that'][index]
            else:
                value = 0  # Default value if not set
            return [Token(value), Token(value)]  # Data token, then flow token
        
        push_that_transition = Transition(
            name=f"push_that_{index}_{len(self.net.transitions)}",
            operation=push_that_operation,
            emit_function=emit_push_that
        )
        
        return self._insert_operation(push_that_transition, that_place, consumes_stack=0, produces_stack=1)

    def push_pointer(self, vmc):
        """Handle push pointer command - pushes THIS (0) or THAT (1) pointer"""
        index = vmc.index
        
        # Create a place to hold the pointer value
        pointer_place = Place(f"pointer_{index}_{len(self.net.places)}")
        self.net.add_place(pointer_place)
        
        # Create emit function for push pointer
        def emit_push_pointer(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load pointer (THIS or THAT) into D register
            if index == 0:
                assembly.append("@THIS")
            elif index == 1:
                assembly.append("@THAT")
            else:
                assembly.append(f"// Invalid pointer index: {index}")
                return assembly
            
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the pointer value
        push_pointer_transition = Transition(
            name=f"push_pointer_{index}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(0), Token(0)],  # Data token, then flow token
            emit_function=emit_push_pointer
        )
        
        return self._insert_operation(push_pointer_transition, pointer_place, consumes_stack=0, produces_stack=1)

    def push_temp(self, vmc):
        """Handle push temp command - pushes temp[index] (R5-R12)"""
        index = vmc.index
        
        # Create a place to hold the temp value
        temp_place = Place(f"temp_{index}_{len(self.net.places)}")
        self.net.add_place(temp_place)
        
        # Create emit function for push temp
        def emit_push_temp(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load temp[index] (R5+index) into D register
            temp_address = 5 + index
            assembly.append(f"@R{temp_address}")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the temp value
        # Create transition that pushes the temp value
        def push_temp_operation(tokens):
            # Read the value from shared memory simulation
            if 'temp' in self.memory_simulation and index in self.memory_simulation['temp']:
                value = self.memory_simulation['temp'][index]
            else:
                value = 0  # Default value if not set
            return [Token(value), Token(value)]  # Data token, then flow token
        
        push_temp_transition = Transition(
            name=f"push_temp_{index}_{len(self.net.transitions)}",
            operation=push_temp_operation,
            emit_function=emit_push_temp
        )
        
        return self._insert_operation(push_temp_transition, temp_place, consumes_stack=0, produces_stack=1)

    def push_static(self, vmc):
        """Handle push static command - pushes static variable"""
        index = vmc.index
        
        # Create a place to hold the static value
        static_place = Place(f"static_{index}_{len(self.net.places)}")
        self.net.add_place(static_place)
        
        # Create emit function for push static
        def emit_push_static(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load static variable into D register
            # Static variables are typically named ClassName.index
            assembly.append(f"@Static.{index}")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that pushes the static value
        push_static_transition = Transition(
            name=f"push_static_{index}_{len(self.net.transitions)}",
            operation=lambda tokens: [Token(0), Token(0)],  # Data token, then flow token
            emit_function=emit_push_static
        )
        
        return self._insert_operation(push_static_transition, static_place, consumes_stack=0, produces_stack=1)

    def pop_local(self, vmc):
        """Handle pop local command - pops stack top to local[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_local_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop local
        def emit_pop_local(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop local - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop local - input has no memory address")
                return assembly
            
            # Store to local[index] - need two-step addressing
            assembly.append("@LCL")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = LCL + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of local[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to local[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to local
        def pop_local_operation(tokens):
            # Store the value in shared memory simulation
            if 'local' not in self.memory_simulation:
                self.memory_simulation['local'] = {}
            self.memory_simulation['local'][index] = tokens[0].value
            return [tokens[0]]  # Pass through the input token value
        
        pop_local_transition = Transition(
            name=f"pop_local_{index}_{len(self.net.transitions)}",
            operation=pop_local_operation,
            emit_function=emit_pop_local
        )
        
        return self._insert_operation(pop_local_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_argument(self, vmc):
        """Handle pop argument command - pops stack top to argument[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_arg_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop argument
        def emit_pop_argument(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop argument - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop argument - input has no memory address")
                return assembly
            
            # Store to argument[index] - need two-step addressing
            assembly.append("@ARG")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = ARG + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of argument[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to argument[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to argument
        # Create transition that pops to argument
        def pop_arg_operation(tokens):
            # Store the value in shared memory simulation
            if 'argument' not in self.memory_simulation:
                self.memory_simulation['argument'] = {}
            self.memory_simulation['argument'][index] = tokens[0].value
            return [tokens[0]]  # Pass through the input token value
        
        pop_arg_transition = Transition(
            name=f"pop_arg_{index}_{len(self.net.transitions)}",
            operation=pop_arg_operation,
            emit_function=emit_pop_argument
        )
        
        return self._insert_operation(pop_arg_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_this(self, vmc):
        """Handle pop this command - pops stack top to this[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_this_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop this
        def emit_pop_this(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop this - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop this - input has no memory address")
                return assembly
            
            # Store to this[index] - need two-step addressing
            assembly.append("@THIS")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = THIS + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of this[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to this[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to this
        # Create transition that pops to this
        def pop_this_operation(tokens):
            # Store the value in shared memory simulation
            if 'this' not in self.memory_simulation:
                self.memory_simulation['this'] = {}
            self.memory_simulation['this'][index] = tokens[0].value
            return [tokens[0]]  # Pass through the input token value
        
        pop_this_transition = Transition(
            name=f"pop_this_{index}_{len(self.net.transitions)}",
            operation=pop_this_operation,
            emit_function=emit_pop_this
        )
        
        return self._insert_operation(pop_this_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_that(self, vmc):
        """Handle pop that command - pops stack top to that[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_that_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop that
        def emit_pop_that(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop that - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop that - input has no memory address")
                return assembly
            
            # Store to that[index] - need two-step addressing
            assembly.append("@THAT")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = THAT + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of that[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to that[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to that
        # Create transition that pops to that
        def pop_that_operation(tokens):
            # Store the value in shared memory simulation
            if 'that' not in self.memory_simulation:
                self.memory_simulation['that'] = {}
            self.memory_simulation['that'][index] = tokens[0].value
            return [tokens[0]]  # Pass through the input token value
        
        pop_that_transition = Transition(
            name=f"pop_that_{index}_{len(self.net.transitions)}",
            operation=pop_that_operation,
            emit_function=emit_pop_that
        )
        
        return self._insert_operation(pop_that_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_pointer(self, vmc):
        """Handle pop pointer command - pops stack top to THIS (0) or THAT (1) pointer"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_pointer_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop pointer
        def emit_pop_pointer(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop pointer - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop pointer - input has no memory address")
                return assembly
            
            # Store to pointer (THIS or THAT)
            if index == 0:
                assembly.append("@THIS")
            elif index == 1:
                assembly.append("@THAT")
            else:
                assembly.append(f"// Invalid pointer index: {index}")
                return assembly
            
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to pointer
        pop_pointer_transition = Transition(
            name=f"pop_pointer_{index}_{len(self.net.transitions)}",
            operation=lambda tokens: [tokens[0]],  # Pass through the input token value
            emit_function=emit_pop_pointer
        )
        
        return self._insert_operation(pop_pointer_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_temp(self, vmc):
        """Handle pop temp command - pops stack top to temp[index] (R5-R12)"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_temp_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop temp
        def emit_pop_temp(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop temp - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop temp - input has no memory address")
                return assembly
            
            # Store to temp[index] (R5+index)
            temp_address = 5 + index
            assembly.append(f"@R{temp_address}")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to temp
        # Create transition that pops to temp
        def pop_temp_operation(tokens):
            # Store the value in shared memory simulation
            if 'temp' not in self.memory_simulation:
                self.memory_simulation['temp'] = {}
            self.memory_simulation['temp'][index] = tokens[0].value
            return [tokens[0]]  # Pass through the input token value
        
        pop_temp_transition = Transition(
            name=f"pop_temp_{index}_{len(self.net.transitions)}",
            operation=pop_temp_operation,
            emit_function=emit_pop_temp
        )
        
        return self._insert_operation(pop_temp_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_static(self, vmc):
        """Handle pop static command - pops stack top to static variable"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_static_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop static
        def emit_pop_static(transition):
            assembly = []
            
            # Get input place (should be 1) - the value to pop
            if len(transition.in_places) != 1:
                return ["// pop static - invalid input configuration"]
            
            input_place = transition.in_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop static - input has no memory address")
                return assembly
            
            # Store to static variable
            # Static variables are typically named ClassName.index
            assembly.append(f"@Static.{index}")
            assembly.append("M=D")
            
            return assembly
        
        # Create transition that pops to static
        pop_static_transition = Transition(
            name=f"pop_static_{index}_{len(self.net.transitions)}",
            operation=lambda tokens: [tokens[0]],  # Pass through the input token value
            emit_function=emit_pop_static
        )
        
        return self._insert_operation(pop_static_transition, pop_result_place, consumes_stack=1, produces_stack=0)