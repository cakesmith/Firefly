"""
Continuation Transformer for Non-Tail Recursive Calls
Transforms non-tail calls into continuation-based operations for infinite recursion capability
"""

from .Token import Token, ContinuationToken

class ContinuationTransformer:
    """
    Transforms non-tail recursive calls into continuation-based operations
    This enables infinite recursion for both tail and non-tail calls
    """
    
    def __init__(self, translator):
        self.translator = translator
        self.continuation_counter = 0
        
    def transform_function_for_continuations(self, function_name, function_body):
        """
        Transform a function body to use continuations for non-tail calls
        
        Args:
            function_name: Name of the function
            function_body: List of VM commands
            
        Returns:
            Transformed function body with continuation operations
        """
        print(f"Transforming function {function_name} for continuations")
        print(f"Original function body: {function_body}")
        
        transformed_body = []
        i = 0
        
        while i < len(function_body):
            command = function_body[i]
            
            if command[0] == "call":
                # Check if this is a tail call or non-tail call
                is_tail = self._is_tail_call(function_body, i)
                print(f"Call at index {i} to {command[1]}: is_tail={is_tail}")
                
                if is_tail:
                    # Tail call - keep as is for trampoline optimization
                    transformed_body.append(command)
                else:
                    # Non-tail call - transform to continuation
                    call_command = command
                    target_function = call_command[1]
                    num_args = call_command[2]
                    
                    print(f"Transforming non-tail call to {target_function}")
                    
                    # Find the rest of the function after this call
                    rest_of_function = function_body[i+1:]
                    
                    # Create continuation for the rest of the function
                    continuation_name = self._create_continuation_transition(
                        function_name, rest_of_function, i
                    )
                    
                    # Replace call with call_with_continuation
                    transformed_body.append((
                        "call_with_continuation", 
                        target_function, 
                        num_args, 
                        continuation_name
                    ))
                    
                    # IMPORTANT: We need to preserve the rest of the function body
                    # including labels and base case logic, but skip the commands
                    # that are now in the continuation
                    
                    # The continuation contains the commands immediately after the call
                    # We need to find where the continuation ends and normal function logic resumes
                    continuation_end = self._find_continuation_end(function_body, i+1)
                    
                    # Skip to after the continuation commands
                    i = continuation_end
                    
                    # Continue processing the rest of the function (labels, base cases, etc.)
                    while i < len(function_body):
                        transformed_body.append(function_body[i])
                        i += 1
                    break
            else:
                transformed_body.append(command)
            
            i += 1
        
        print(f"Transformed function body: {transformed_body}")
        return transformed_body
    
    def _is_tail_call(self, function_body, call_index):
        """
        Check if a call is in tail position
        
        Args:
            function_body: List of function commands
            call_index: Index of the call command
            
        Returns:
            bool: True if this is a tail call
        """
        # Check if the next command is return or end of function
        next_index = call_index + 1
        
        print(f"Checking tail call at index {call_index}")
        print(f"Function body length: {len(function_body)}")
        
        if next_index >= len(function_body):
            print("Tail call: end of function")
            return True  # Last command in function
            
        next_command = function_body[next_index]
        print(f"Next command: {next_command}")
        is_tail = next_command[0] == "return"
        print(f"Is tail call: {is_tail}")
        return is_tail
    
    def _find_continuation_end(self, function_body, start_index):
        """
        Find where the continuation commands end and normal function logic resumes
        
        Args:
            function_body: List of function commands
            start_index: Index to start searching from
            
        Returns:
            int: Index where continuation ends
        """
        # For now, simple heuristic: continuation ends at the first label or end of function
        # This works for the factorial case where the continuation is just [mul, return]
        # and then we have [label BASE_CASE, push constant 1, return]
        
        i = start_index
        while i < len(function_body):
            cmd = function_body[i]
            if cmd[0] == "label":
                # Found a label - continuation ends here
                return i
            elif cmd[0] == "return":
                # Found return - continuation includes this, so end after it
                return i + 1
            i += 1
        
        # If no label found, continuation goes to end of function
        return len(function_body)
    
    def _create_continuation_transition(self, function_name, rest_of_function, call_index):
        """
        Create a continuation transition for the rest of the function
        
        Args:
            function_name: Original function name
            rest_of_function: Commands to execute after the call returns
            call_index: Index where the call occurred
            
        Returns:
            str: Name of the created continuation transition
        """
        self.continuation_counter += 1
        continuation_name = f"{function_name}_continuation_{call_index}_{self.continuation_counter}"
        
        # Store the continuation for later execution
        if not hasattr(self.translator, '_continuations'):
            self.translator._continuations = {}
            
        self.translator._continuations[continuation_name] = {
            'original_function': function_name,
            'commands': rest_of_function,
            'call_index': call_index
        }
        
        print(f"Created continuation '{continuation_name}' for {len(rest_of_function)} commands after call")
        
        return continuation_name
    
    def execute_continuation(self, continuation_name, call_result, captured_context):
        """
        Execute a continuation with the result of a function call
        
        Args:
            continuation_name: Name of the continuation to execute
            call_result: Result from the function call
            captured_context: Context captured when continuation was created
            
        Returns:
            Result of executing the continuation
        """
        if continuation_name not in self.translator._continuations:
            raise RuntimeError(f"Continuation {continuation_name} not found")
        
        continuation = self.translator._continuations[continuation_name]
        
        print(f"Executing continuation {continuation_name} with call result {call_result}")
        print(f"Continuation commands: {continuation['commands']}")
        
        # Set up execution context for continuation
        saved_result_places = self.translator.result_places.copy()
        saved_call_stack = self.translator.call_stack.copy()
        saved_current_function = self.translator.current_function
        
        # Restore the captured result places (operands for the continuation)
        self.translator.result_places = []
        
        # First, restore any captured result places (these were on the stack before the call)
        if 'result_places_values' in captured_context:
            for value in captured_context['result_places_values']:
                place = self.translator.net.add_place(
                    self.translator.get_unique_place_name("continuation_operand")
                )
                place.put_token(Token(value))
                self.translator.result_places.append(place)
                print(f"Restored operand: {value}")
        
        # Then, put the call result on the result stack
        result_place = self.translator.net.add_place(
            self.translator.get_unique_place_name("continuation_call_result")
        )
        result_place.put_token(Token(call_result))
        self.translator.result_places.append(result_place)
        print(f"Added call result: {call_result}")
        print(f"Result stack for continuation: {[p.tokens[0].value if p.has_token() else 0 for p in self.translator.result_places]}")
        
        # Restore any captured context (local variables, etc.)
        self._restore_captured_context(captured_context)
        
        try:
            # Execute the continuation commands
            result = self._execute_continuation_commands(continuation['commands'])
            print(f"Continuation {continuation_name} returned: {result}")
            return result
            
        finally:
            # Restore original context
            self.translator.result_places = saved_result_places
            self.translator.call_stack = saved_call_stack
            self.translator.current_function = saved_current_function
    
    def _restore_captured_context(self, captured_context):
        """
        Restore the execution context that was captured when the continuation was created
        
        Args:
            captured_context: Dictionary containing captured variables and state
        """
        print(f"Restoring captured context: {captured_context}")
        
        # Set current function context
        if 'function_name' in captured_context:
            self.translator.current_function = captured_context['function_name']
        
        # Create a temporary call frame for the continuation execution
        temp_call_frame = {
            'function_name': captured_context.get('function_name', 'continuation'),
            'arguments': [],
            'saved_result_places': [],
            'saved_function': None,
            'recursion_depth': 0,
            'local_variables': {}
        }
        
        # Restore local variables and other context
        if 'local_variables' in captured_context:
            for var_name, var_value in captured_context['local_variables'].items():
                print(f"Restoring local variable {var_name} = {var_value}")
                # Create place for local variable
                local_place = self.translator.net.add_place(
                    self.translator.get_unique_place_name(f"continuation_local_{var_name}")
                )
                local_place.put_token(Token(var_value))
                temp_call_frame['local_variables'][var_name] = local_place
        
        # Add the temporary call frame to the call stack
        self.translator.call_stack.append(temp_call_frame)
    
    def _execute_continuation_commands(self, commands):
        """
        Execute the commands in a continuation
        
        Args:
            commands: List of VM commands to execute
            
        Returns:
            Result of executing the commands
        """
        # Use lightweight execution similar to trampoline executor
        for command in commands:
            if command[0] == "return":
                # Return the current result
                if self.translator.result_places:
                    return_place = self.translator.result_places[-1]
                    if return_place.has_token():
                        return return_place.tokens[0].value
                return 0
            else:
                # Execute the command using existing lightweight execution
                self._execute_command_lightweight(command)
        
        # If no explicit return, return 0
        return 0
    
    def _execute_command_lightweight(self, command):
        """
        Execute a single command with minimal Petri net impact
        Reuses the lightweight execution from trampoline executor
        """
        # Import here to avoid circular imports
        from .trampoline_executor import TrampolineExecutor
        
        # Create temporary trampoline executor for command execution
        temp_executor = TrampolineExecutor(self.translator)
        temp_executor._execute_command_lightweight(command)
    
    def create_continuation_call_operation(self, translator, target_function, num_args, continuation_name):
        """
        Create a continuation-based call operation
        
        Args:
            translator: VM translator instance
            target_function: Function to call
            num_args: Number of arguments
            continuation_name: Name of continuation to execute after call
            
        Returns:
            ContinuationToken for the call with continuation
        """
        # Capture current context (local variables, etc.)
        captured_context = self._capture_current_context()
        
        # Collect arguments for the call
        if len(translator.result_places) < num_args:
            raise RuntimeError(f"Not enough arguments for continuation call to {target_function}")
        
        args = []
        for i in range(num_args):
            arg_place = translator.result_places.pop()
            args.append(arg_place)
        args.reverse()  # Restore correct order
        
        # Create a special continuation token that includes the continuation info
        return ContinuationCallToken(
            target_function, 
            args, 
            continuation_name, 
            captured_context
        )
    
    def _capture_current_context(self):
        """
        Capture the current execution context for continuation
        
        Returns:
            Dictionary containing captured context
        """
        context = {
            'local_variables': {},
            'function_name': self.translator.current_function
        }
        
        # Capture local variables from current call frame
        if self.translator.call_stack:
            call_frame = self.translator.call_stack[-1]
            for var_name, var_place in call_frame.get('local_variables', {}).items():
                if var_place.has_token():
                    context['local_variables'][var_name] = var_place.tokens[0].value
                else:
                    context['local_variables'][var_name] = 0
        
        return context
    
    def create_continuation_return_operation(self, translator, function_name, num_args):
        """
        Create a return operation that triggers a continuation
        Used by trampoline executor for continuation-based calls
        """
        return ContinuationToken(function_name, [])
    
    def create_value_return_operation(self, translator):
        """
        Create a value return operation for continuation execution
        """
        if translator.result_places:
            return_place = translator.result_places[-1]
            if return_place.has_token():
                from .Token import ValueToken
                return ValueToken(return_place.tokens[0].value)
        
        from .Token import ValueToken
        return ValueToken(0)


class ContinuationCallToken(ContinuationToken):
    """
    Special continuation token for calls that need continuation execution
    """
    
    def __init__(self, function_name, args, continuation_name, captured_context, level=0):
        super().__init__(function_name, args, level)
        self.continuation_name = continuation_name
        self.captured_context = captured_context
        self.is_continuation_call = True
        
    def __repr__(self):
        return f"ContinuationCallToken({self.function_name}, {len(self.args)} args, continuation={self.continuation_name})"