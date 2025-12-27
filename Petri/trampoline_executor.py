"""
Trampoline Executor for Infinite Recursion Support
Handles trampolined execution when level-based recursion limits are exceeded
"""

from .Token import Token, ValueToken, ContinuationToken

class TrampolineExecutor:
    """
    Executes functions using trampolining for infinite recursion capability
    """
    
    def __init__(self, translator):
        self.translator = translator
        
    def execute_trampolined_call(self, function_name, args):
        """
        Execute a function call using trampolining for infinite recursion
        
        Args:
            function_name: Name of function to call
            args: List of argument places/tokens
            
        Returns:
            ValueToken with final result
        """
        print(f"Starting trampolined execution of {function_name}")
        
        # Create initial continuation
        initial_continuation = ContinuationToken(function_name, args)
        
        # Execute trampoline loop
        return self.trampoline_loop(initial_continuation)
    
    def trampoline_loop(self, initial_continuation):
        """
        Main trampoline loop - executes continuations iteratively
        Enhanced to handle continuation-based non-tail calls without recursion
        
        Args:
            initial_continuation: First continuation to execute
            
        Returns:
            ValueToken with final result
        """
        current = initial_continuation
        iteration = 0
        max_iterations = 1000  # Safety limit for testing
        continuation_stack = []  # Stack to handle nested continuations
        
        while (current.is_continuation or continuation_stack) and iteration < max_iterations:
            print(f"Trampoline iteration {iteration}: executing {current.function_name if hasattr(current, 'function_name') else 'continuation'}")
            
            if hasattr(current, 'is_continuation') and current.is_continuation:
                # Execute function once, get result (ValueToken, ContinuationToken, or ContinuationCallToken)
                result = self.execute_function_to_continuation(
                    current.function_name, 
                    current.args
                )
                
                # Handle different types of results
                if hasattr(result, 'is_continuation_call') and result.is_continuation_call:
                    # This is a continuation call - push current continuation to stack
                    print(f"Handling continuation call to {result.function_name}")
                    
                    # Push the continuation info to stack for later execution
                    continuation_stack.append({
                        'continuation_name': result.continuation_name,
                        'captured_context': result.captured_context
                    })
                    
                    # Set current to the target function continuation
                    current = ContinuationToken(result.function_name, result.args)
                    
                else:
                    # Regular continuation or value result
                    current = result
            
            # If we have a value result and there are pending continuations, execute them
            if (not hasattr(current, 'is_continuation') or not current.is_continuation) and continuation_stack:
                # We have a value and pending continuations
                from .Token import ValueToken
                if not isinstance(current, ValueToken):
                    if hasattr(current, 'value'):
                        current_value = current.value
                    else:
                        current_value = 0
                else:
                    current_value = current.value
                
                # Pop and execute the most recent continuation
                continuation_info = continuation_stack.pop()
                
                print(f"Executing pending continuation {continuation_info['continuation_name']} with value {current_value}")
                
                # Execute the continuation
                from .continuation_transformer import ContinuationTransformer
                transformer = ContinuationTransformer(self.translator)
                continuation_result = transformer.execute_continuation(
                    continuation_info['continuation_name'], 
                    current_value, 
                    continuation_info['captured_context']
                )
                
                # Continue with the continuation result
                current = ValueToken(continuation_result)
                
            iteration += 1
        
        if iteration >= max_iterations:
            raise RuntimeError(f"Trampoline exceeded maximum iterations ({max_iterations}) - possible infinite loop")
        
        from .Token import ValueToken
        if not isinstance(current, ValueToken):
            # Convert final result to ValueToken if needed
            if hasattr(current, 'value'):
                current = ValueToken(current.value)
            else:
                current = ValueToken(0)  # Default value
        
        print(f"Trampoline completed after {iteration} iterations, result: {current.value}")
        return current
    
    def execute_function_to_continuation(self, function_name, args):
        """
        Execute a function body and return either a ValueToken or ContinuationToken
        
        Args:
            function_name: Name of function to execute
            args: List of argument places/tokens
            
        Returns:
            ValueToken (if function returns normally) or ContinuationToken (if recursive call)
        """
        if function_name not in self.translator.function_definitions:
            raise RuntimeError(f"Function {function_name} not defined")
        
        # Check if we have a cached function subnet for this function
        subnet_key = f"trampoline_subnet_{function_name}"
        if not hasattr(self.translator, '_trampoline_subnets'):
            self.translator._trampoline_subnets = {}
        
        if subnet_key not in self.translator._trampoline_subnets:
            # Create the function subnet once and cache it
            self._create_function_subnet(function_name, subnet_key)
        
        # Execute the cached subnet with the provided arguments
        return self._execute_cached_subnet(function_name, subnet_key, args)
    
    def _create_function_subnet(self, function_name, subnet_key):
        """
        Create a reusable function subnet for trampolined execution
        """
        print(f"Creating reusable subnet for function {function_name}")
        
        # Set up temporary execution context for subnet creation
        saved_result_places = self.translator.result_places.copy()
        saved_current_function = self.translator.current_function
        saved_net_state = self._save_net_state()
        
        # Create temporary call frame for argument access during subnet creation
        temp_call_frame = {
            'function_name': function_name,
            'arguments': [],  # Will be populated during execution
            'saved_result_places': saved_result_places,
            'saved_function': saved_current_function,
            'recursion_depth': 0,
            'local_variables': {}
        }
        
        self.translator.call_stack.append(temp_call_frame)
        self.translator.current_function = function_name
        self.translator.result_places = []
        
        try:
            # Pre-process labels
            function_def = self.translator.function_definitions[function_name]
            self._preprocess_function_labels(function_def['body'], function_name)
            
            # Create subnet structure by analyzing function body
            subnet_info = self._analyze_function_for_subnet(function_def['body'])
            
            # Cache the subnet information
            self.translator._trampoline_subnets[subnet_key] = subnet_info
            
        finally:
            # Restore execution context
            self.translator.call_stack.pop()
            self.translator.result_places = saved_result_places
            self.translator.current_function = saved_current_function
            self._restore_net_state(saved_net_state)
    
    def _save_net_state(self):
        """Save current net state for restoration"""
        return {
            'place_counter': self.translator.place_counter,
            'transition_counter': self.translator.transition_counter,
            'places_count': len(self.translator.net.places),
            'transitions_count': len(self.translator.net.transitions)
        }
    
    def _restore_net_state(self, saved_state):
        """Restore net state to prevent subnet creation from affecting main net"""
        # Remove any places/transitions created during subnet analysis
        current_places = list(self.translator.net.places.keys())
        current_transitions = list(self.translator.net.transitions.keys())
        
        # Remove places created after the saved state
        places_to_remove = current_places[saved_state['places_count']:]
        for place_name in places_to_remove:
            if place_name in self.translator.net.places:
                del self.translator.net.places[place_name]
        
        # Remove transitions created after the saved state
        transitions_to_remove = current_transitions[saved_state['transitions_count']:]
        for trans_name in transitions_to_remove:
            if trans_name in self.translator.net.transitions:
                del self.translator.net.transitions[trans_name]
        
        # Restore counters
        self.translator.place_counter = saved_state['place_counter']
        self.translator.transition_counter = saved_state['transition_counter']
    
    def _analyze_function_for_subnet(self, function_commands):
        """
        Analyze function body to create a reusable execution pattern
        """
        # For now, use a simplified approach - just store the commands
        # In a full implementation, this would create a reusable Petri net fragment
        return {
            'commands': function_commands,
            'labels': self.translator.control_flow.get_function_labels(self.translator.current_function).copy()
        }
    
    def _execute_cached_subnet(self, function_name, subnet_key, args):
        """
        Execute a cached function subnet with the provided arguments
        """
        subnet_info = self.translator._trampoline_subnets[subnet_key]
        
        # Set up execution context with the provided arguments
        saved_result_places = self.translator.result_places.copy()
        saved_current_function = self.translator.current_function
        
        # Create call frame with actual arguments
        temp_call_frame = {
            'function_name': function_name,
            'arguments': args,
            'saved_result_places': saved_result_places,
            'saved_function': saved_current_function,
            'recursion_depth': 0,
            'local_variables': {}
        }
        
        self.translator.call_stack.append(temp_call_frame)
        self.translator.current_function = function_name
        self.translator.result_places = []
        
        # Reuse existing places for arguments instead of creating new ones
        if not hasattr(self.translator, '_trampoline_arg_places'):
            self.translator._trampoline_arg_places = {}
        
        # Set up arguments in result_places for function access
        for i, arg in enumerate(args):
            arg_key = f"{function_name}_arg_{i}"
            
            # Reuse existing argument place if available
            if arg_key not in self.translator._trampoline_arg_places:
                self.translator._trampoline_arg_places[arg_key] = self.translator.net.add_place(
                    self.translator.get_unique_place_name(f"trampoline_arg_{function_name}_{i}")
                )
            
            arg_place = self.translator._trampoline_arg_places[arg_key]
            
            # Clear existing tokens and add new argument value
            arg_place.tokens.clear()
            if hasattr(arg, 'tokens') and arg.tokens:
                arg_place.put_token(arg.tokens[0])
            elif hasattr(arg, 'value'):
                # If arg is a Token directly, use its value
                arg_place.put_token(Token(arg.value))
            else:
                # Default value
                arg_place.put_token(Token(0))
            
            self.translator.result_places.append(arg_place)
        
        try:
            # Execute function body with continuation detection (reuse existing logic)
            result = self._execute_function_body_for_continuation(subnet_info['commands'])
            return result
            
        finally:
            # Restore execution context
            self.translator.call_stack.pop()
            self.translator.result_places = saved_result_places
            self.translator.current_function = saved_current_function
    
    def _preprocess_function_labels(self, function_body, function_name):
        """
        Pre-process all label definitions in a function body
        """
        saved_function = self.translator.current_function
        self.translator.current_function = function_name
        
        print(f"Preprocessing labels for function {function_name}")
        
        # First pass: define all labels
        for command in function_body:
            if command[0] == "label":
                label_name = command[1]
                # Only define the label, don't execute it
                self.translator.control_flow.define_label(label_name, function_name)
                print(f"Pre-processed label '{label_name}' in function '{function_name}'")
        
        # Debug: check what labels are now defined
        print(f"Labels defined in function {function_name}: {self.translator.control_flow.get_function_labels(function_name)}")
        
        self.translator.current_function = saved_function
    
    def _execute_function_body_for_continuation(self, function_commands):
        """
        Execute function body and detect continuation returns without creating new net elements
        
        Args:
            function_commands: List of VM commands in function body
            
        Returns:
            ValueToken or ContinuationToken
        """
        func_index = 0
        
        # Use a lightweight execution approach that doesn't create new net elements
        while func_index < len(function_commands):
            command = function_commands[func_index]
            
            if command[0] == "return":
                # Check if this is a continuation return or value return
                if self.translator.result_places:
                    # Get the return value
                    return_place = self.translator.result_places[-1]
                    if return_place.has_token():
                        token = return_place.tokens[0]
                        if isinstance(token, ContinuationToken):
                            return token  # Return continuation for trampolined execution
                        else:
                            return ValueToken(token.value)  # Return value
                    else:
                        return ValueToken(0)  # Default value
                else:
                    return ValueToken(0)  # No return value
            
            elif command[0] == "call":
                # Check if this is a tail call that should become a continuation
                if self._is_tail_call_in_continuation_context(function_commands, func_index):
                    target_function = command[1]
                    num_args = command[2]
                    
                    # Collect arguments for continuation
                    if len(self.translator.result_places) >= num_args:
                        args = []
                        for i in range(num_args):
                            arg_place = self.translator.result_places.pop()
                            # Extract the actual value from the place for the continuation
                            if arg_place.has_token():
                                value = arg_place.tokens[0].value
                            else:
                                value = 0
                            # Create a new place with the value for the continuation
                            value_place = self.translator.net.add_place(
                                self.translator.get_unique_place_name(f"continuation_arg_{i}")
                            )
                            value_place.put_token(Token(value))
                            args.append(value_place)
                        args.reverse()  # Restore correct order
                        
                        # Return continuation instead of executing call
                        return ContinuationToken(target_function, args)
                    else:
                        raise RuntimeError(f"Not enough arguments for continuation call to {target_function}")
                        
            elif command[0] == "call_with_continuation":
                # Handle continuation-based non-tail calls
                target_function = command[1]
                num_args = command[2]
                continuation_name = command[3]
                
                # Import here to avoid circular imports
                from .continuation_transformer import ContinuationCallToken
                
                if len(self.translator.result_places) >= num_args:
                    args = []
                    for i in range(num_args):
                        arg_place = self.translator.result_places.pop()
                        # Extract the actual value from the place for the call
                        if arg_place.has_token():
                            value = arg_place.tokens[0].value
                        else:
                            value = 0
                        # Create a new place with the value for the call
                        value_place = self.translator.net.add_place(
                            self.translator.get_unique_place_name(f"continuation_call_arg_{i}")
                        )
                        value_place.put_token(Token(value))
                        args.append(value_place)
                    args.reverse()  # Restore correct order
                    
                    # Capture current context for continuation
                    captured_context = self._capture_continuation_context()
                    
                    # Return continuation call token
                    return ContinuationCallToken(target_function, args, continuation_name, captured_context)
                else:
                    raise RuntimeError(f"Not enough arguments for continuation call to {target_function}")
            
            elif command[0] == "label":
                # Handle label definition - just skip it since it was preprocessed
                pass
            
            elif command[0] == "goto" or command[0] == "if-goto":
                # Handle control flow with lightweight execution
                jump_occurred = self._execute_control_flow_lightweight(command)
                
                if jump_occurred:
                    # Jump occurred within function
                    func_index = self.translator._function_jump_target
                    self.translator._function_jump_target = None
                    continue  # Don't increment func_index
            
            else:
                # Regular command execution with minimal net impact
                self._execute_command_lightweight(command)
            
            func_index += 1
        
        # Function ended without explicit return
        return ValueToken(0)
    
    def _execute_command_lightweight(self, command):
        """
        Execute a command with minimal Petri net impact for trampoline execution
        """
        cmd_type = command[0]
        
        # Initialize reusable places cache if not exists
        if not hasattr(self.translator, '_trampoline_temp_places'):
            self.translator._trampoline_temp_places = {}
        
        # Handle commands that affect result_places without creating new net elements
        if cmd_type == "push":
            segment = command[1]
            index = command[2]
            
            if segment == "constant":
                # Reuse a constant place
                place_key = f"const_{index}"
                if place_key not in self.translator._trampoline_temp_places:
                    self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                        self.translator.get_unique_place_name(f"trampoline_const_{index}")
                    )
                
                temp_place = self.translator._trampoline_temp_places[place_key]
                temp_place.tokens.clear()  # Clear existing tokens
                temp_place.put_token(Token(index))
                self.translator.result_places.append(temp_place)
            
            elif segment == "argument":
                # Get argument from call frame
                if self.translator.call_stack:
                    call_frame = self.translator.call_stack[-1]
                    if index < len(call_frame['arguments']):
                        arg_place = call_frame['arguments'][index]
                        # Reuse argument copy place
                        place_key = f"arg_copy_{self.translator.current_function}_{index}"
                        if place_key not in self.translator._trampoline_temp_places:
                            self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                                self.translator.get_unique_place_name(f"trampoline_arg_copy_{index}")
                            )
                        
                        temp_place = self.translator._trampoline_temp_places[place_key]
                        temp_place.tokens.clear()
                        if arg_place.has_token():
                            temp_place.put_token(arg_place.tokens[0])
                        elif hasattr(arg_place, 'tokens') and arg_place.tokens:
                            temp_place.put_token(arg_place.tokens[0])
                        else:
                            # Extract value from the argument place if it's a Token
                            if hasattr(arg_place, 'value'):
                                temp_place.put_token(Token(arg_place.value))
                            else:
                                temp_place.put_token(Token(0))
                        self.translator.result_places.append(temp_place)
                    else:
                        # Default value for missing argument
                        place_key = f"default_arg_{index}"
                        if place_key not in self.translator._trampoline_temp_places:
                            self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                                self.translator.get_unique_place_name(f"trampoline_default_arg_{index}")
                            )
                        
                        temp_place = self.translator._trampoline_temp_places[place_key]
                        temp_place.tokens.clear()
                        temp_place.put_token(Token(0))
                        self.translator.result_places.append(temp_place)
            
            elif segment == "local":
                # Push local variable value with bounds checking
                if not self.translator.current_function:
                    raise RuntimeError("No function context for local variable access")
                
                if self.translator.current_function not in self.translator.function_locals:
                    raise RuntimeError(f"Function {self.translator.current_function} not defined")
                
                if index >= self.translator.function_locals[self.translator.current_function]:
                    raise RuntimeError(f"Local index {index} out of bounds for function {self.translator.current_function}")
                
                if self.translator.call_stack:
                    call_frame = self.translator.call_stack[-1]
                    local_key = f"local_{self.translator.current_function}_{index}"
                    
                    if local_key in call_frame['local_variables']:
                        local_place = call_frame['local_variables'][local_key]
                        
                        # Create copy place for local value
                        place_key = f"local_copy_{self.translator.current_function}_{index}"
                        if place_key not in self.translator._trampoline_temp_places:
                            self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                                self.translator.get_unique_place_name(f"trampoline_local_copy_{index}")
                            )
                        
                        copy_place = self.translator._trampoline_temp_places[place_key]
                        copy_place.tokens.clear()
                        if local_place.has_token():
                            copy_place.put_token(local_place.tokens[0])
                        else:
                            copy_place.put_token(Token(0))  # Default value
                        
                        self.translator.result_places.append(copy_place)
                    else:
                        # Local variable not initialized, use default
                        place_key = f"default_local"
                        if place_key not in self.translator._trampoline_temp_places:
                            self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                                self.translator.get_unique_place_name(f"trampoline_default_local")
                            )
                        
                        default_place = self.translator._trampoline_temp_places[place_key]
                        default_place.tokens.clear()
                        default_place.put_token(Token(0))
                        self.translator.result_places.append(default_place)
            
            else:
                # For other segments, use a default place
                place_key = f"default_{segment}_{index}"
                if place_key not in self.translator._trampoline_temp_places:
                    self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                        self.translator.get_unique_place_name(f"trampoline_default_{segment}")
                    )
                
                temp_place = self.translator._trampoline_temp_places[place_key]
                temp_place.tokens.clear()
                temp_place.put_token(Token(0))
                self.translator.result_places.append(temp_place)
        
        elif cmd_type in ["add", "sub", "mul", "div", "eq", "lt", "gt"]:
            # Arithmetic/comparison operations
            if len(self.translator.result_places) >= 2:
                right_place = self.translator.result_places.pop()
                left_place = self.translator.result_places.pop()
                
                # Get values
                left_val = left_place.tokens[0].value if left_place.has_token() else 0
                right_val = right_place.tokens[0].value if right_place.has_token() else 0
                
                # Compute result
                if cmd_type == "add":
                    result_val = left_val + right_val
                elif cmd_type == "sub":
                    result_val = left_val - right_val
                elif cmd_type == "mul":
                    result_val = left_val * right_val
                elif cmd_type == "div":
                    result_val = left_val // right_val if right_val != 0 else 0
                elif cmd_type == "eq":
                    result_val = -1 if left_val == right_val else 0
                elif cmd_type == "lt":
                    result_val = -1 if left_val < right_val else 0
                elif cmd_type == "gt":
                    result_val = -1 if left_val > right_val else 0
                
                # Reuse result place
                place_key = f"result_{cmd_type}"
                if place_key not in self.translator._trampoline_temp_places:
                    self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                        self.translator.get_unique_place_name(f"trampoline_result_{cmd_type}")
                    )
                
                result_place = self.translator._trampoline_temp_places[place_key]
                result_place.tokens.clear()
                result_place.put_token(Token(result_val))
                self.translator.result_places.append(result_place)
        
        elif cmd_type == "pop":
            segment = command[1]
            index = command[2]
            
            if segment == "local":
                # Pop value to local variable with bounds checking
                if not self.translator.current_function:
                    raise RuntimeError("No function context for local variable")
                
                if self.translator.current_function not in self.translator.function_locals:
                    raise RuntimeError(f"Function {self.translator.current_function} not defined")
                
                if index >= self.translator.function_locals[self.translator.current_function]:
                    raise RuntimeError(f"Local index {index} out of bounds for function {self.translator.current_function}")
                
                if self.translator.result_places:
                    value_place = self.translator.result_places.pop()
                    
                    # Store in local variable (reuse local place)
                    if self.translator.call_stack:
                        call_frame = self.translator.call_stack[-1]
                        local_key = f"local_{self.translator.current_function}_{index}"
                        
                        if local_key not in call_frame['local_variables']:
                            # Create local variable place
                            if local_key not in self.translator._trampoline_temp_places:
                                self.translator._trampoline_temp_places[local_key] = self.translator.net.add_place(
                                    self.translator.get_unique_place_name(f"trampoline_local_{index}")
                                )
                            call_frame['local_variables'][local_key] = self.translator._trampoline_temp_places[local_key]
                        
                        local_place = call_frame['local_variables'][local_key]
                        local_place.tokens.clear()
                        if value_place.has_token():
                            local_place.put_token(value_place.tokens[0])
        
        elif cmd_type == "push" and len(command) > 2 and command[1] == "local":
            # Push local variable value
            index = command[2]
            
            if self.translator.call_stack:
                call_frame = self.translator.call_stack[-1]
                local_key = f"local_{self.translator.current_function}_{index}"
                
                if local_key in call_frame['local_variables']:
                    local_place = call_frame['local_variables'][local_key]
                    
                    # Create copy place for local value
                    place_key = f"local_copy_{self.translator.current_function}_{index}"
                    if place_key not in self.translator._trampoline_temp_places:
                        self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                            self.translator.get_unique_place_name(f"trampoline_local_copy_{index}")
                        )
                    
                    copy_place = self.translator._trampoline_temp_places[place_key]
                    copy_place.tokens.clear()
                    if local_place.has_token():
                        copy_place.put_token(local_place.tokens[0])
                    else:
                        copy_place.put_token(Token(0))  # Default value
                    
                    self.translator.result_places.append(copy_place)
                else:
                    # Local variable not initialized, use default
                    place_key = f"default_local"
                    if place_key not in self.translator._trampoline_temp_places:
                        self.translator._trampoline_temp_places[place_key] = self.translator.net.add_place(
                            self.translator.get_unique_place_name(f"trampoline_default_local")
                        )
                    
                    default_place = self.translator._trampoline_temp_places[place_key]
                    default_place.tokens.clear()
                    default_place.put_token(Token(0))
                    self.translator.result_places.append(default_place)
        
        # For other commands, use minimal implementation or skip
    
    def _execute_control_flow_lightweight(self, command):
        """
        Execute control flow commands with minimal net impact
        """
        cmd_type = command[0]
        
        if cmd_type == "if-goto":
            label_name = command[1]
            
            # Check condition
            if self.translator.result_places:
                condition_place = self.translator.result_places.pop()
                condition_value = condition_place.tokens[0].value if condition_place.has_token() else 0
                
                print(f"If-goto condition: {condition_value} (0=false, non-zero=true)")
                
                if condition_value != 0:  # Non-zero means true
                    # Find the label in the current function
                    function_labels = self.translator.control_flow.get_function_labels(self.translator.current_function)
                    if label_name in function_labels:
                        # Find the command index for this label
                        function_def = self.translator.function_definitions[self.translator.current_function]
                        for i, cmd in enumerate(function_def['body']):
                            if cmd[0] == "label" and cmd[1] == label_name:
                                print(f"If-goto jumping to label '{label_name}' at function command index {i}")
                                self.translator._function_jump_target = i
                                return True
                    print(f"If-goto condition true, but label '{label_name}' not found")
                else:
                    print("If-goto condition false, continuing to next command")
            
            return False
        
        elif cmd_type == "goto":
            label_name = command[1]
            # Similar logic for unconditional goto
            function_labels = self.translator.control_flow.get_function_labels(self.translator.current_function)
            if label_name in function_labels:
                function_def = self.translator.function_definitions[self.translator.current_function]
                for i, cmd in enumerate(function_def['body']):
                    if cmd[0] == "label" and cmd[1] == label_name:
                        self.translator._function_jump_target = i
                        return True
            
            return False
        
        return False
    
    def _is_tail_call_in_continuation_context(self, function_commands, current_index):
        """
        Check if a call is in tail position for continuation transformation
        
        Args:
            function_commands: List of function commands
            current_index: Index of current call command
            
        Returns:
            bool: True if this call should become a continuation
        """
        if current_index >= len(function_commands):
            return False
        
        # Check if the next command is return (or end of function)
        next_index = current_index + 1
        
        # If this is the last command, it's a tail call
        if next_index >= len(function_commands):
            return True
        
        # If the next command is return, it's a tail call
        if next_index < len(function_commands):
            next_command = function_commands[next_index]
            if next_command[0] == "return":
                return True
        
        return False
    
    def _capture_continuation_context(self):
        """
        Capture the current execution context for continuation
        """
        context = {
            'local_variables': {},
            'function_name': self.translator.current_function,
            'result_places_values': []  # Capture current result stack values
        }
        
        # Capture current result places (these are the operands for the continuation)
        for place in self.translator.result_places:
            if place.has_token():
                context['result_places_values'].append(place.tokens[0].value)
            else:
                context['result_places_values'].append(0)
        
        print(f"Captured continuation context: {context}")
        
        # Capture local variables from current call frame
        if self.translator.call_stack:
            call_frame = self.translator.call_stack[-1]
            for var_name, var_place in call_frame.get('local_variables', {}).items():
                if var_place.has_token():
                    context['local_variables'][var_name] = var_place.tokens[0].value
                else:
                    context['local_variables'][var_name] = 0
        
        return context