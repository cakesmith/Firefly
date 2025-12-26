"""
Arithmetic Operations for Petri Net VM
Handles arithmetic operations: add, sub, mul, div, neg
"""

from .Token import Token

class ArithmeticOperations:
    """
    Handles arithmetic operations in Petri net semantics
    """
    
    def add_operation(self, translator):
        """
        Implement add operation: consume two most recent result places,
        create add transition, produce new result place
        """
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for add operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = translator.result_places.pop()  # Top 
        a_place = translator.result_places.pop()  # Second from top
        
        # Create result place for the sum
        result_place = translator.net.add_place(translator.get_unique_place_name("add_result"))
        
        # Create add transition that consumes from both input places
        def add_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val + b_val)
            
        add_transition = translator.net.add_transition(
            translator.get_unique_transition_name("add"), 
            add_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        translator.net.add_arc(a_place, add_transition)
        translator.net.add_arc(b_place, add_transition)
        translator.net.add_arc(add_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        translator.result_places.append(result_place)
        
        return result_place
        
    def sub_operation(self, translator):
        """
        Implement sub operation: consume two most recent result places
        Result = first - second (where second is most recent)
        """
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for sub operation")
            
        # Pop operands from result places
        b_place = translator.result_places.pop()  # Most recent (subtrahend)
        a_place = translator.result_places.pop()  # Second most recent (minuend)
        
        # Create result place
        result_place = translator.net.add_place(translator.get_unique_place_name("sub_result"))
        
        def sub_op(tokens):
            a_val = tokens[0].value  # First operand
            b_val = tokens[1].value  # Second operand
            return Token(a_val - b_val)
            
        sub_transition = translator.net.add_transition(
            translator.get_unique_transition_name("sub"), 
            sub_op
        )
        
        # Wire: input_places -> transition -> output_place
        translator.net.add_arc(a_place, sub_transition)
        translator.net.add_arc(b_place, sub_transition)
        translator.net.add_arc(sub_transition, result_place)
        
        # Add result to result places
        translator.result_places.append(result_place)
        return result_place
        
    def neg_operation(self, translator):
        """
        Implement neg operation: consume most recent result place
        """
        if len(translator.result_places) < 1:
            raise RuntimeError("Not enough operands for neg operation")
            
        # Pop single operand from result places
        a_place = translator.result_places.pop()
        
        # Create result place
        result_place = translator.net.add_place(translator.get_unique_place_name("neg_result"))
        
        def neg_op(tokens):
            a_val = tokens[0].value
            return Token(-a_val)
            
        neg_transition = translator.net.add_transition(
            translator.get_unique_transition_name("neg"), 
            neg_op
        )
        
        # Wire: input_place -> transition -> output_place
        translator.net.add_arc(a_place, neg_transition)
        translator.net.add_arc(neg_transition, result_place)
        
        # Add result to result places
        translator.result_places.append(result_place)
        return result_place
        
    def mul_operation(self, translator):
        """
        Implement mul operation: consume two most recent result places,
        create mul transition, produce new result place
        Handles integer overflow according to VM specification
        """
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for mul operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = translator.result_places.pop()  # Top 
        a_place = translator.result_places.pop()  # Second from top
        
        # Create result place for the product
        result_place = translator.net.add_place(translator.get_unique_place_name("mul_result"))
        
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
            
        mul_transition = translator.net.add_transition(
            translator.get_unique_transition_name("mul"), 
            mul_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        translator.net.add_arc(a_place, mul_transition)
        translator.net.add_arc(b_place, mul_transition)
        translator.net.add_arc(mul_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        translator.result_places.append(result_place)
        
        return result_place
        
    def div_operation(self, translator):
        """
        Implement div operation: consume two most recent result places,
        create div transition, produce new result place
        Performs integer division (truncated toward zero)
        Handles division by zero appropriately
        """
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for div operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = translator.result_places.pop()  # Top (divisor)
        a_place = translator.result_places.pop()  # Second from top (dividend)
        
        # Create result place for the quotient
        result_place = translator.net.add_place(translator.get_unique_place_name("div_result"))
        
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
            
        div_transition = translator.net.add_transition(
            translator.get_unique_transition_name("div"), 
            div_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        translator.net.add_arc(a_place, div_transition)
        translator.net.add_arc(b_place, div_transition)
        translator.net.add_arc(div_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        translator.result_places.append(result_place)
        
        return result_place