from Petri.net import PetriNet
from Petri.Token import Token
from Petri.Place import Place
from Petri.Transition import Transition

class PetriEmitter:

    def __init__(self):
        self.net = PetriNet()

        self.net.add_place(Place("init"))
        self.net.add_place(Place("end"))

        def emit_pass(transition):
            input_place = transition.in_places[0] if transition.in_places else None
            output_place = transition.out_places[0] if transition.out_places else None
            
            # If input and output have same memory address, no assembly needed
            if (input_place and output_place and 
                input_place.memory_address == output_place.memory_address):
                print(f"Optimizing away {transition.name}: same memory location R{input_place.memory_address}")
                return []  # No assembly code needed
            
            assembly = []
            if input_place and input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly

        self.net.add_transition(Transition(
            name = "pass", 
            operation = lambda tokens: tokens,
            emit_function = emit_pass
        ))

        self.net.add_arc(self.net.places["init"], self.net.transitions["pass"])
        self.net.add_arc(self.net.transitions["pass"], self.net.places["end"])

        self.net.places["init"].put_token(Token("control"))


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
        
        
        pass

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