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
        Push argument[index] onto stack
        Arguments are passed from the caller
        """
        if not translator.call_stack:
            raise RuntimeError("No function call context for argument access")
        
        current_call = translator.call_stack[-1]
        if index >= len(current_call['arguments']):
            raise RuntimeError(f"Argument index {index} out of bounds")
        
        # Get the argument place
        arg_place = current_call['arguments'][index]
        
        # Create a new place for the pushed value (duplicate the argument)
        pushed_place = translator.net.add_place(translator.get_unique_place_name(f"pushed_arg_{index}"))
        
        # Create dup transition to copy the argument value
        def dup_arg_func(tokens):
            if tokens:
                val = tokens[0].value
                return [Token(val), Token(val)]  # Original and copy
            return [Token(0), Token(0)]
        
        dup_transition = translator.net.add_transition(
            translator.get_unique_transition_name(f"dup_arg_{index}"),
            dup_arg_func
        )
        
        # Wire: arg_place -> dup_transition -> [arg_place, pushed_place]
        translator.net.add_arc(arg_place, dup_transition)
        translator.net.add_arc(dup_transition, arg_place)  # Keep original
        translator.net.add_arc(dup_transition, pushed_place)  # Create copy
        
        # Add to result places
        translator.result_places.append(pushed_place)
        return pushed_place
    
    def push_local(self, translator, index):
        """
        Push local[index] onto stack with enhanced reliability
        Improved error handling and memory optimization integration
        """
        if not translator.current_function:
            raise RuntimeError("No function context for local variable access")
        
        if translator.current_function not in translator.function_locals:
            raise RuntimeError(f"Function {translator.current_function} not defined")
        
        if index >= translator.function_locals[translator.current_function]:
            raise RuntimeError(f"Local index {index} out of bounds for function {translator.current_function}")
        
        # Get or create the local variable place (handles uninitialized locals gracefully)
        local_place_name = f"local_{translator.current_function}_{index}"
        local_place = self._get_or_create_local_place(translator, local_place_name, index)
        
        # Create a new place for the pushed value
        pushed_place = translator.net.add_place(translator.get_unique_place_name(f"pushed_local_{index}"))
        
        # Create dup transition to copy the local value (memory optimization friendly)
        def dup_local_func(tokens):
            if tokens:
                val = tokens[0].value
                return [Token(val), Token(val)]  # Original and copy
            return [Token(0), Token(0)]  # Default value if uninitialized
        
        dup_transition = translator.net.add_transition(
            translator.get_unique_transition_name(f"dup_local_{index}"),
            dup_local_func
        )
        
        # Wire: local_place -> dup_transition -> [local_place, pushed_place]
        translator.net.add_arc(local_place, dup_transition)
        translator.net.add_arc(dup_transition, local_place)  # Keep original
        translator.net.add_arc(dup_transition, pushed_place)  # Create copy
        
        # Add to result places
        translator.result_places.append(pushed_place)
        print(f"Pushed local variable {index} (function: {translator.current_function})")
        return pushed_place
    
    def pop_local(self, translator, index):
        """
        Store top stack element to local variable N
        Implements pop local using Petri net semantics with single-token constraint
        """
        if not translator.current_function:
            raise RuntimeError("No function context for local variable")
        
        if translator.current_function not in translator.function_locals:
            raise RuntimeError(f"Function {translator.current_function} not defined")
        
        if index >= translator.function_locals[translator.current_function]:
            raise RuntimeError(f"Local index {index} out of bounds for function {translator.current_function}")
        
        if len(translator.result_places) < 1:
            raise RuntimeError("No value to pop")
        
        # Get the value to store
        value_place = translator.result_places.pop()
        
        # Get or create local variable place
        local_place_name = f"local_{translator.current_function}_{index}"
        local_place = self._get_or_create_local_place(translator, local_place_name, index)
        
        # With single-token constraint, we can directly replace the token
        # Get the value from the value_place and put it in the local_place
        if value_place.has_token():
            new_value = value_place.get_token()
            local_place.put_token(new_value)  # This will replace existing token
        else:
            # Default value if no token
            local_place.put_token(Token(0))
        
        print(f"Stored value to local variable {index}")
        return local_place
    
    def _get_or_create_local_place(self, translator, local_place_name, index):
        """Get existing local place or create new one"""
        local_key = (translator.current_function, index)
        
        # Check if local place already exists
        if local_key in translator.local_places:
            place = translator.local_places[local_key]
            return place
        
        # Create new local place
        local_place = translator.net.add_place(translator.get_unique_place_name(local_place_name))
        
        # Initialize with default value (0) if needed
        local_place.put_token(Token(0))
        
        # Store in local places dictionary
        translator.local_places[local_key] = local_place
        
        return local_place
    
    def pop_argument(self, translator, index):
        """
        Store top stack element back to caller's argument location
        Implements reference parameter semantics - changes are visible to caller
        """
        if not translator.call_stack:
            raise RuntimeError("No function call context for argument modification")
        
        current_call = translator.call_stack[-1]
        if index >= len(current_call['arguments']):
            raise RuntimeError(f"Argument index {index} out of bounds")
        
        if len(translator.result_places) < 1:
            raise RuntimeError("No value to pop")
        
        # Get the value to store
        value_place = translator.result_places.pop()
        
        # Get the caller's argument place (shared reference)
        caller_arg_place = current_call['arguments'][index]
        
        # With single-token constraint, directly replace the token in caller's argument
        if value_place.has_token():
            new_value = value_place.get_token()
            caller_arg_place.put_token(new_value)  # This modifies caller's data directly
        else:
            # Default value if no token
            caller_arg_place.put_token(Token(0))
        
        print(f"Modified caller's argument {index} (reference parameter)")
        return caller_arg_place
    
    def pop_operation(self, translator, segment, index):
        """General pop operation for different memory segments"""
        if segment == "local":
            return self.pop_local(translator, index)
        elif segment == "argument":
            return self.pop_argument(translator, index)
        else:
            raise NotImplementedError(f"Pop {segment} not implemented")