from Petri.net import PetriNet
from Petri.Token import Token
from Petri.Place import Place
from Petri.Transition import Transition

class PetriEmitter:

    def __init__(self):
        self.net = PetriNet()
        self.control_stack = []

        self.net.add_place(Place("init"))
        self.net.add_place(Place("end"))

        self.net.places["init"].put_token(Token("control"))

    def _insert_operation(self, transition, output_place, consumes_stack=0, produces_stack=1):
        """
        Insert an operation into the Petri net with proper stack-based connections.
        Handles branching with dup transitions when multiple operations need the same input.
        
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
            # Operation consumes 0 from stack - needs to connect from init or create dup
            if len(self.control_stack) == 0:
                # First operation - connect directly from init
                self.net.add_arc(self.net.places["init"], transition)
            else:
                # Need to create dup transition to branch from init
                self._create_dup_branch(transition)
        
        # Connect output place
        self.net.add_arc(transition, output_place)
        
        # Push output place to stack if operation produces a value
        if produces_stack == 1:
            self.control_stack.append(output_place)
        
        return transition

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
        # """Handle function command"""
        # Add your custom logic here
        pass
            
    def call(self, vmc):
        # """Handle call command"""
        # Add your custom logic here
        pass
            
    def ret(self, vmc):
        # """Handle return command"""
        # Add your custom logic here
        pass


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
            operation=lambda tokens: [Token(constant_value)],
            emit_function=emit_push_constant
        )
        
        # Use the general method to add this operation (pushes 1 item to stack)
        return self._insert_operation(push_const_transition, constant_place, consumes_stack=0, produces_stack=1)

    def push_local(self, vmc):
        # """Handle push local command"""
        # Add your custom logic here
        pass

    def push_argument(self, vmc):
        # """Handle push argument command"""
        # Add your custom logic here
        pass

    def push_this(self, vmc):
        # """Handle push this command"""
        # Add your custom logic here
        pass

    def push_that(self, vmc):
        # """Handle push that command"""
        # Add your custom logic here
        pass

    def push_pointer(self, vmc):
        # """Handle push pointer command"""
        # Add your custom logic here
        pass

    def push_temp(self, vmc):
        # """Handle push temp command"""
        # Add your custom logic here
        pass

    def push_static(self, vmc):
        # """Handle push static command"""
        # Add your custom logic here
        pass

    def pop_local(self, vmc):
        # """Handle pop local command"""
        # Add your custom logic here
        pass

    def pop_argument(self, vmc):
        # """Handle pop argument command"""
        # Add your custom logic here
        pass

    def pop_this(self, vmc):
        # """Handle pop this command"""
        # Add your custom logic here
        pass

    def pop_that(self, vmc):
        # """Handle pop that command"""
        # Add your custom logic here
        pass

    def pop_pointer(self, vmc):
        # """Handle pop pointer command"""
        # Add your custom logic here
        pass

    def pop_temp(self, vmc):
        # """Handle pop temp command"""
        # Add your custom logic here
        pass

    def pop_static(self, vmc):
        # """Handle pop static command"""
        # Add your custom logic here
        pass