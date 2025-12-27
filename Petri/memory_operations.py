"""
Memory Operations for Petri Net VM
Handles push/pop operations for different memory segments
"""

from .Token import Token

class MemoryOperations:
    """
    Handles memory operations (push/pop) for different segments
    """
    
    def push_operation(self, translator, segment, index):
        """
        General push operation for different memory segments
        """
        if segment == "constant":
            return self.push_constant(translator, index)
        elif segment == "argument":
            return self.push_argument(translator, index)
        elif segment == "local":
            return self.push_local(translator, index)
        else:
            raise NotImplementedError(f"Push {segment} not implemented")
    
    def push_constant(self, translator, value):
        """
        Implement push constant using 'source' primitive
        Creates a new place with the constant value - this IS the stack element
        """
        # Create a new place for this constant (source primitive)
        const_place = translator.net.add_place(translator.get_unique_place_name(f"const_{value}"))
        const_place.put_token(Token(value))
        
        # This place represents the value - add to results
        translator.result_places.append(const_place)
        
        return const_place
    
    def push_argument(self, translator, index):
        """
        Push argument[index] onto stack using FunctionContextManager
        """
        # Use function context manager for proper argument access
        arg_place = translator.function_context_manager.get_argument_place(index)
        
        # Create a new place for the pushed value
        pushed_place = translator.net.add_place(translator.get_unique_place_name(f"pushed_arg_{index}"))
        
        # Create transition to copy value from argument place to pushed place
        trans_name = translator.get_unique_transition_name("push_arg")
        transition = translator.net.add_transition(trans_name)
        
        # Connect: arg_place -> transition -> arg_place, pushed_place
        translator.net.add_arc(arg_place, transition)
        translator.net.add_arc(transition, arg_place)  # Keep original
        translator.net.add_arc(transition, pushed_place)  # Create copy
        
        # Set operation to copy token
        def copy_arg_op(tokens):
            if tokens:
                token = tokens[0]
                return [token, Token(token.value)]  # Original and copy
            return [Token(0), Token(0)]  # Default values
            
        transition.operation = copy_arg_op
        
        # Add to result places
        translator.result_places.append(pushed_place)
        
        current_context = translator.function_context_manager.get_current_context()
        function_name = current_context['function_name'] if current_context else 'unknown'
        print(f"Pushed argument {index} (function: {function_name})")
        return pushed_place
    
    def push_local(self, translator, index):
        """
        Push local[index] onto stack using FunctionContextManager
        """
        # Use function context manager for proper scope isolation
        local_place = translator.function_context_manager.get_local_place(index)
        
        # Create a new place for the pushed value
        pushed_place = translator.net.add_place(translator.get_unique_place_name(f"pushed_local_{index}"))
        
        # Create transition to copy value from local place to pushed place
        trans_name = translator.get_unique_transition_name("push_local")
        transition = translator.net.add_transition(trans_name)
        
        # Connect: local_place -> transition -> local_place, pushed_place
        translator.net.add_arc(local_place, transition)
        translator.net.add_arc(transition, local_place)  # Keep original
        translator.net.add_arc(transition, pushed_place)  # Create copy
        
        # Set operation to copy token
        def copy_local_op(tokens):
            if tokens:
                token = tokens[0]
                return [token, Token(token.value)]  # Original and copy
            return [Token(0), Token(0)]  # Default values
            
        transition.operation = copy_local_op
        
        # Add to result places
        translator.result_places.append(pushed_place)
        
        current_context = translator.function_context_manager.get_current_context()
        function_name = current_context['function_name'] if current_context else 'unknown'
        print(f"Pushed local variable {index} (function: {function_name})")
        return pushed_place
    
    def pop_local(self, translator, index):
        """
        Store top stack element to local variable using FunctionContextManager
        """
        if len(translator.result_places) < 1:
            raise RuntimeError("No value to pop")
        
        # Get the value to store
        value_place = translator.result_places.pop()
        
        # Use function context manager for proper scope isolation
        local_place = translator.function_context_manager.get_local_place(index)
        
        # Create transition to move value from value_place to local_place
        trans_name = translator.get_unique_transition_name("pop_local")
        transition = translator.net.add_transition(trans_name)
        
        # Connect: value_place -> transition -> local_place
        translator.net.add_arc(value_place, transition)
        translator.net.add_arc(transition, local_place)
        
        # Set operation to move token (replacing existing token in local_place)
        def move_to_local_op(tokens):
            if tokens:
                return [tokens[0]]  # Move the token
            return [Token(0)]  # Default value
            
        transition.operation = move_to_local_op
        
        current_context = translator.function_context_manager.get_current_context()
        function_name = current_context['function_name'] if current_context else 'unknown'
        print(f"Stored value to local variable {index} (function: {function_name})")
        return local_place
    
    def _get_or_create_local_place(self, translator, local_place_name, index):
        """Get existing local place or create new one with call-specific scoping"""
        call_depth = len(translator.call_stack)
        local_key = (translator.current_function, call_depth, index)
        
        # Check if local place already exists for this specific call
        if local_key in translator.local_places:
            place = translator.local_places[local_key]
            return place
        
        # Create new local place
        local_place = translator.net.add_place(translator.get_unique_place_name(local_place_name))
        
        # Initialize with default value (0) if needed
        local_place.put_token(Token(0))
        
        # Store in local places dictionary with call-specific key
        translator.local_places[local_key] = local_place
        
        return local_place
    
    def pop_argument(self, translator, index):
        """
        Store top stack element back to caller's argument location using FunctionContextManager
        """
        if len(translator.result_places) < 1:
            raise RuntimeError("No value to pop")
        
        # Get the value to store
        value_place = translator.result_places.pop()
        
        # Use function context manager for proper argument access
        arg_place = translator.function_context_manager.get_argument_place(index)
        
        # Create transition to move value from value_place to argument place
        trans_name = translator.get_unique_transition_name("pop_arg")
        transition = translator.net.add_transition(trans_name)
        
        # Connect: value_place -> transition -> arg_place
        translator.net.add_arc(value_place, transition)
        translator.net.add_arc(transition, arg_place)
        
        # Set operation to move token (replacing existing token in arg_place)
        def move_to_arg_op(tokens):
            if tokens:
                return [tokens[0]]  # Move the token
            return [Token(0)]  # Default value
            
        transition.operation = move_to_arg_op
        
        current_context = translator.function_context_manager.get_current_context()
        function_name = current_context['function_name'] if current_context else 'unknown'
        print(f"Modified caller's argument {index} (function: {function_name})")
        return arg_place
    
    def pop_operation(self, translator, segment, index):
        """General pop operation for different memory segments"""
        if segment == "local":
            return self.pop_local(translator, index)
        elif segment == "argument":
            return self.pop_argument(translator, index)
        else:
            raise NotImplementedError(f"Pop {segment} not implemented")