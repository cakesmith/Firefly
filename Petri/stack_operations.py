"""
Stack Operations for Petri Net VM
Handles stack manipulation operations: dup, drop
"""

from .Token import Token

class StackOperations:
    """
    Handles stack manipulation operations in Petri net semantics
    """
    
    def dup_operation(self, translator):
        """
        Implement dup operation using 'dup' primitive
        Duplicates the top stack element
        """
        if len(translator.result_places) < 1:
            raise RuntimeError("Not enough operands for dup operation")
            
        top_place = translator.result_places[-1]  # Peek at top without popping
        
        # Create duplicate place
        dup_place = translator.net.add_place(translator.get_unique_place_name("dup_result"))
        
        # Create dup transition (explicit duplication)
        def dup_op(tokens):
            val = tokens[0].value
            return [Token(val), Token(val)]  # Return two identical tokens
            
        dup_transition = translator.net.add_transition(
            translator.get_unique_transition_name("dup"), 
            dup_op
        )
        
        # Connect: top_place -> dup_transition -> [top_place, dup_place]
        # This requires consuming the original and producing two
        translator.result_places.pop()  # Remove original
        translator.net.add_arc(top_place, dup_transition)
        translator.net.add_arc(dup_transition, top_place)  # Put back original
        translator.net.add_arc(dup_transition, dup_place)  # Add duplicate
        
        # Push both back onto result places
        translator.result_places.append(top_place)
        translator.result_places.append(dup_place)
        
        return dup_place
        
    def drop_operation(self, translator):
        """
        Implement drop operation using 'drop' primitive
        Discards the top stack element
        """
        if len(translator.result_places) < 1:
            raise RuntimeError("Not enough operands for drop operation")
            
        top_place = translator.result_places.pop()
        
        # Create drop transition that consumes but produces nothing
        drop_transition = translator.net.add_transition(
            translator.get_unique_transition_name("drop"), 
            lambda tokens: []  # Consume input, produce nothing
        )
        
        translator.net.add_arc(top_place, drop_transition)
        # No output connections - token is consumed and discarded
        
        return None