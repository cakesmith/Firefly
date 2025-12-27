"""
Function Context Management System for Petri Net VM
Provides proper function scope isolation, call stack management, and context restoration
"""

from .Token import Token

class FunctionContextManager:
    """
    Manages function execution contexts with proper scope isolation
    Handles function call stack, local variables, and argument mapping
    """
    
    def __init__(self, translator):
        """
        Initialize function context manager
        
        Args:
            translator: VMToPetriTranslator instance
        """
        self.translator = translator
        self.function_contexts = {}  # function_name -> context_info
        self.call_stack = []  # Stack of active function calls
        self.max_recursion_depth = 1000  # Maximum recursion depth limit
        
    def create_function_context(self, function_name, num_locals, num_args):
        """
        Create isolated context for function execution
        
        Args:
            function_name: Name of the function
            num_locals: Number of local variables
            num_args: Number of arguments
            
        Returns:
            dict: Function context information
        """
        context = {
            'function_name': function_name,
            'num_locals': num_locals,
            'num_args': num_args,
            'local_places': {},  # index -> place_name
            'argument_places': {},  # index -> place_name
            'scope_prefix': f"func_{function_name}_{len(self.call_stack)}",
            'call_depth': len(self.call_stack),
            'recursion_depth': self._calculate_recursion_depth(function_name)
        }
        return context
        
    def enter_function_context(self, function_name, num_locals, num_args):
        """
        Enter function context and initialize local variables
        
        Args:
            function_name: Name of the function
            num_locals: Number of local variables
            num_args: Number of arguments
            
        Returns:
            dict: Created function context
            
        Raises:
            RuntimeError: If recursion depth limit exceeded
        """
        # Check recursion depth limit
        recursion_depth = self._calculate_recursion_depth(function_name)
        if recursion_depth >= self.max_recursion_depth:
            raise RuntimeError(f"Maximum recursion depth exceeded: {recursion_depth} >= {self.max_recursion_depth}")
        
        # Create function context
        context = self.create_function_context(function_name, num_locals, num_args)
        
        # Save current state BEFORE consuming arguments
        context['saved_result_places'] = self.translator.result_places.copy()
        context['saved_function'] = self.translator.current_function
        
        # Initialize local variable places with function scope prefixes
        for i in range(num_locals):
            place_name = f"{context['scope_prefix']}_local_{i}"
            place = self.translator.net.add_place(place_name)
            # Initialize with zero token
            place.put_token(Token(0))
            context['local_places'][i] = place_name
            
        # Map argument places from result_places (stack) with proper arc connections
        arguments = []
        for i in range(num_args):
            # Create argument place for this function context
            arg_place_name = f"{context['scope_prefix']}_arg_{i}"
            arg_place = self.translator.net.add_place(arg_place_name)
            
            if i < len(self.translator.result_places):
                # Arguments come from result_places in reverse order (stack semantics)
                stack_place = self.translator.result_places[-(i+1)]
                
                # Create transition to move token from stack to argument place
                trans_name = f"{context['scope_prefix']}_setup_arg_{i}"
                transition = self.translator.net.add_transition(trans_name)
                
                # Connect: stack_place -> transition -> arg_place
                self.translator.net.add_arc(stack_place, transition)
                self.translator.net.add_arc(transition, arg_place)
                
                # Set operation to move token
                def move_arg_op(tokens):
                    return tokens  # Move the token
                    
                transition.operation = move_arg_op
                
                # Execute the transition to move the token
                if stack_place.has_token():
                    token = stack_place.get_token()
                    arg_place.put_token(token)
                
            else:
                # Create default argument place if not enough arguments
                arg_place.put_token(Token(0))
                
            arguments.append(arg_place)
            context['argument_places'][i] = arg_place_name
                
        # Remove consumed arguments from result_places and update saved state
        consumed_places = []
        for _ in range(min(num_args, len(self.translator.result_places))):
            if self.translator.result_places:
                consumed_place = self.translator.result_places.pop()
                consumed_places.append(consumed_place)
                
        # Update saved result places to reflect the consumption
        context['saved_result_places'] = self.translator.result_places.copy()
            
        # Store arguments in context
        context['arguments'] = arguments
        
        # Push context onto call stack
        self.call_stack.append(context)
        
        # Update translator state - start with empty result places for function execution
        self.translator.current_function = function_name
        self.translator.result_places = []
        
        return context
        
    def exit_function_context(self):
        """
        Exit function context and restore caller state
        
        Returns:
            dict: Exited function context or None if no context
        """
        if not self.call_stack:
            return None
            
        context = self.call_stack.pop()
        
        # Get return value (if any) and properly connect it
        return_value = None
        if self.translator.result_places:
            return_place = self.translator.result_places[-1]
            
            # Create a new place for the return value in caller's context
            return_value_name = f"return_value_{context['function_name']}_{context['call_depth']}"
            return_value = self.translator.net.add_place(return_value_name)
            
            # Create transition to move return value
            trans_name = f"return_transition_{context['function_name']}_{context['call_depth']}"
            transition = self.translator.net.add_transition(trans_name)
            
            # Connect: return_place -> transition -> return_value
            self.translator.net.add_arc(return_place, transition)
            self.translator.net.add_arc(transition, return_value)
            
            # Set operation to move token
            def move_return_op(tokens):
                return tokens
                
            transition.operation = move_return_op
            
            # Execute the transition immediately to move the token
            if return_place.has_token():
                token = return_place.get_token()
                return_value.put_token(token)
            
        # Restore caller's state
        self.translator.result_places = context['saved_result_places'].copy()
        self.translator.current_function = context['saved_function']
        
        # Add return value to caller's result places (append to maintain stack semantics)
        if return_value:
            self.translator.result_places.append(return_value)
            
        return context
        
    def get_local_place(self, index):
        """
        Get local variable place for current function context
        
        Args:
            index: Local variable index
            
        Returns:
            Place: Local variable place
            
        Raises:
            RuntimeError: If no function context or index out of bounds
        """
        if not self.call_stack:
            raise RuntimeError("No function context for local variable access")
            
        current_context = self.call_stack[-1]
        
        if index >= current_context['num_locals']:
            raise RuntimeError(f"Local index {index} out of bounds for function {current_context['function_name']}")
            
        place_name = current_context['local_places'][index]
        return self.translator.net.places[place_name]
        
    def get_argument_place(self, index):
        """
        Get argument place for current function context
        
        Args:
            index: Argument index
            
        Returns:
            Place: Argument place
            
        Raises:
            RuntimeError: If no function context or index out of bounds
        """
        if not self.call_stack:
            raise RuntimeError("No function context for argument access")
            
        current_context = self.call_stack[-1]
        
        if index >= current_context['num_args']:
            raise RuntimeError(f"Argument index {index} out of bounds for function {current_context['function_name']}")
            
        place_name = current_context['argument_places'][index]
        return self.translator.net.places[place_name]
        
    def preserve_caller_context(self):
        """
        Preserve caller's local variable context during nested function calls
        
        Returns:
            bool: True if context preserved, False if no caller context
        """
        if len(self.call_stack) < 2:
            return False  # No caller context to preserve
            
        # Context is automatically preserved by the call stack structure
        # Each context maintains its own local_places and argument_places
        return True
        
    def restore_caller_context(self):
        """
        Restore caller's local variable context after function return
        
        Returns:
            bool: True if context restored, False if no caller context
        """
        if len(self.call_stack) < 1:
            return False  # No context to restore
            
        # Context restoration is handled by exit_function_context
        # This method provides explicit interface for restoration
        return True
        
    def get_current_context(self):
        """
        Get current function context
        
        Returns:
            dict: Current function context or None if no context
        """
        if not self.call_stack:
            return None
        return self.call_stack[-1]
        
    def get_call_depth(self):
        """
        Get current call stack depth
        
        Returns:
            int: Current call stack depth
        """
        return len(self.call_stack)
        
    def _calculate_recursion_depth(self, function_name):
        """
        Calculate recursion depth for a specific function
        
        Args:
            function_name: Name of the function
            
        Returns:
            int: Recursion depth for the function
        """
        depth = 0
        for context in self.call_stack:
            if context['function_name'] == function_name:
                depth += 1
        return depth
        
    def validate_context_isolation(self):
        """
        Validate that function contexts are properly isolated
        
        Returns:
            dict: Validation results
        """
        validation = {
            'is_isolated': True,
            'issues': [],
            'contexts_checked': len(self.call_stack)
        }
        
        # Check for local variable name conflicts
        local_place_names = set()
        for context in self.call_stack:
            for place_name in context['local_places'].values():
                if place_name in local_place_names:
                    validation['is_isolated'] = False
                    validation['issues'].append(f"Local place name conflict: {place_name}")
                local_place_names.add(place_name)
                
        # Check for argument place conflicts (these should be shared for reference parameters)
        # This is expected behavior, so we don't flag it as an issue
        
        return validation
        
    def get_context_statistics(self):
        """
        Get statistics about function contexts
        
        Returns:
            dict: Context statistics
        """
        stats = {
            'total_contexts': len(self.call_stack),
            'max_recursion_depth': self.max_recursion_depth,
            'current_recursion_usage': len(self.call_stack),
            'recursion_utilization_percent': (len(self.call_stack) / self.max_recursion_depth) * 100,
            'functions_in_stack': [ctx['function_name'] for ctx in self.call_stack],
            'total_local_places': sum(len(ctx['local_places']) for ctx in self.call_stack),
            'total_argument_places': sum(len(ctx['argument_places']) for ctx in self.call_stack)
        }
        
        return stats