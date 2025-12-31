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

    def _add_operation(self, transition, output_place, consumes_stack=0, produces_stack=1):
        """
        Add an operation to the Petri net with proper stack-based connections.
        
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
        
        # Connect input places from stack (pop in reverse order to maintain stack semantics)
        input_places = []
        for i in range(consumes_stack):
            input_place = self.control_stack.pop()
            input_places.append(input_place)
            self.net.add_arc(input_place, transition)
        
        # If no stack items consumed and stack is empty, connect from init
        if consumes_stack == 0 and len(self.control_stack) == 0:
            self.net.add_arc(self.net.places["init"], transition)
        
        # Connect output place
        self.net.add_arc(transition, output_place)
        
        # Push output place to stack if operation produces a value
        if produces_stack == 1:
            self.control_stack.append(output_place)
        
        return transition


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
        # """Handle add operation"""
        # Add your custom logic here
        pass

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
        return self._add_operation(push_const_transition, constant_place, consumes_stack=0, produces_stack=1)

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