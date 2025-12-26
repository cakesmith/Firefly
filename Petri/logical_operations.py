"""
Logical Operations for Petri Net VM
Handles logical and comparison operations: and, or, not, eq, lt, gt
"""

from .Token import Token

class LogicalOperations:
    """
    Handles logical and comparison operations in Petri net semantics
    """
    
    def eq_operation(self, translator):
        """Implement eq operation: true if x == y, else false"""
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for eq operation")
            
        b_place = translator.result_places.pop()
        a_place = translator.result_places.pop()
        result_place = translator.net.add_place(translator.get_unique_place_name("eq_result"))
        
        def eq_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val == b_val else 0)  # VM uses -1 for true, 0 for false
            
        eq_transition = translator.net.add_transition(translator.get_unique_transition_name("eq"), eq_op)
        translator.net.add_arc(a_place, eq_transition)
        translator.net.add_arc(b_place, eq_transition)
        translator.net.add_arc(eq_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place
        
    def lt_operation(self, translator):
        """Implement lt operation: true if x < y, else false"""
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for lt operation")
            
        b_place = translator.result_places.pop()  # y (top of stack)
        a_place = translator.result_places.pop()  # x (second from top)
        result_place = translator.net.add_place(translator.get_unique_place_name("lt_result"))
        
        def lt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val < b_val else 0)
            
        lt_transition = translator.net.add_transition(translator.get_unique_transition_name("lt"), lt_op)
        translator.net.add_arc(a_place, lt_transition)
        translator.net.add_arc(b_place, lt_transition)
        translator.net.add_arc(lt_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place
        
    def gt_operation(self, translator):
        """Implement gt operation: true if x > y, else false"""
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for gt operation")
            
        b_place = translator.result_places.pop()  # y (top of stack)
        a_place = translator.result_places.pop()  # x (second from top)
        result_place = translator.net.add_place(translator.get_unique_place_name("gt_result"))
        
        def gt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val > b_val else 0)
            
        gt_transition = translator.net.add_transition(translator.get_unique_transition_name("gt"), gt_op)
        translator.net.add_arc(a_place, gt_transition)
        translator.net.add_arc(b_place, gt_transition)
        translator.net.add_arc(gt_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place
        
    def and_operation(self, translator):
        """Implement and operation: bitwise AND"""
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for and operation")
            
        b_place = translator.result_places.pop()
        a_place = translator.result_places.pop()
        result_place = translator.net.add_place(translator.get_unique_place_name("and_result"))
        
        def and_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val & b_val)
            
        and_transition = translator.net.add_transition(translator.get_unique_transition_name("and"), and_op)
        translator.net.add_arc(a_place, and_transition)
        translator.net.add_arc(b_place, and_transition)
        translator.net.add_arc(and_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place
        
    def or_operation(self, translator):
        """Implement or operation: bitwise OR"""
        if len(translator.result_places) < 2:
            raise RuntimeError("Not enough operands for or operation")
            
        b_place = translator.result_places.pop()
        a_place = translator.result_places.pop()
        result_place = translator.net.add_place(translator.get_unique_place_name("or_result"))
        
        def or_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val | b_val)
            
        or_transition = translator.net.add_transition(translator.get_unique_transition_name("or"), or_op)
        translator.net.add_arc(a_place, or_transition)
        translator.net.add_arc(b_place, or_transition)
        translator.net.add_arc(or_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place
        
    def not_operation(self, translator):
        """Implement not operation: bitwise NOT"""
        if len(translator.result_places) < 1:
            raise RuntimeError("Not enough operands for not operation")
            
        a_place = translator.result_places.pop()
        result_place = translator.net.add_place(translator.get_unique_place_name("not_result"))
        
        def not_op(tokens):
            a_val = tokens[0].value
            return Token(~a_val & 0xFFFF)  # 16-bit NOT
            
        not_transition = translator.net.add_transition(translator.get_unique_transition_name("not"), not_op)
        translator.net.add_arc(a_place, not_transition)
        translator.net.add_arc(not_transition, result_place)
        
        translator.result_places.append(result_place)
        return result_place