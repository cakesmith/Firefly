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

    def _create_dup_branch(self, new_transition):
        """
        Create a dup transition to enable branching when multiple operations
        need to consume from the same source.
        """
        # For operations that consume 0 from stack, we need to branch from the current control state
        # This could be 'init' or the result of the last operation that didn't consume from stack
        
        # Find the current control source - either init or the last place on the control stack
        if len(self.control_stack) == 0:
            # No operations have produced anything yet - branch from init
            control_source = self.net.places["init"]
        else:
            # There are operations on the stack, but this operation consumes 0
            # It should branch from init, not from stack results
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
            
            # Create dup transition
            dup_transition = Transition(
                name=f"dup_{len(self.net.transitions)}",
                operation=lambda tokens: [tokens[0], tokens[0]],  # Duplicate the token
                emit_function=self._emit_dup_assembly
            )
            self.net.add_transition(dup_transition)
            
            # Create intermediate places for the dup outputs
            dup_out1 = Place(f"dup_out1_{len(self.net.places)}")
            dup_out2 = Place(f"dup_out2_{len(self.net.places)}")
            self.net.add_place(dup_out1)
            self.net.add_place(dup_out2)
            
            # Connect: source -> dup -> {dup_out1, dup_out2}
            self.net.add_arc(control_source, dup_transition)
            self.net.add_arc(dup_transition, dup_out1)
            self.net.add_arc(dup_transition, dup_out2)
            
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
        # """Handle label command"""
        # Add your custom logic here
        pass
        
    def goto(self, vmc):
        # """Handle goto command"""
        # Add your custom logic here
        pass
            
    def ifgoto(self, vmc):
        # """Handle if-goto command"""
        # Add your custom logic here
        pass
                
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
        # """Handle sub operation"""
        # Add your custom logic here
        pass

    def neg(self, vmc):
        # """Handle neg operation"""
        # Add your custom logic here
        pass

    def lt(self, vmc):
        # """Handle lt (less than) operation"""
        # Add your custom logic here
        pass

    def eq(self, vmc):
        # """Handle eq (equals) operation"""
        # Add your custom logic here
        pass

    def gt(self, vmc):
        # """Handle gt (greater than) operation"""
        # Add your custom logic here
        pass

    def and_op(self, vmc):
        # """Handle and operation"""
        # Add your custom logic here
        pass

    def or_op(self, vmc):
        # """Handle or operation"""
        # Add your custom logic here
        pass

    def not_op(self, vmc):
        # """Handle not operation"""
        # Add your custom logic here
        pass

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
            name=f"push_const_{constant_value}",
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