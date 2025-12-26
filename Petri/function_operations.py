"""
Function Operations for Petri Net VM
Handles function call and return operations with enhanced recursive support
"""

from .Token import Token

class FunctionOperations:
    """
    Handles function operations in Petri net semantics with recursive function support
    """
    
    # Default maximum recursion depth to prevent stack overflow
    DEFAULT_MAX_RECURSION_DEPTH = 100
    
    def __init__(self, max_recursion_depth=None):
        """
        Initialize function operations with configurable recursion depth
        
        Args:
            max_recursion_depth: Maximum allowed recursion depth (default: 100)
                                For comparison:
                                - Python default: ~1000
                                - Java default: varies by JVM, typically 1000-10000
                                - Our conservative default: 100 (good for embedded/constrained environments)
        """
        self.MAX_RECURSION_DEPTH = max_recursion_depth or self.DEFAULT_MAX_RECURSION_DEPTH
    
    def call_operation(self, translator, function_name, num_args, is_tail_call=False):
        """
        Implement function call using Petri net semantics with enhanced recursive support
        Execute the function body with the provided arguments
        
        Args:
            translator: VM translator instance
            function_name: Name of function to call
            num_args: Number of arguments
            is_tail_call: Whether this is a tail call (can reuse current frame)
        """
        if function_name not in translator.function_definitions:
            raise RuntimeError(f"Function {function_name} not defined")
        
        if len(translator.result_places) < num_args:
            raise RuntimeError(f"Not enough arguments for call to {function_name}")
        
        # Pop arguments from result places
        args = []
        for i in range(num_args):
            args.append(translator.result_places.pop())
        args.reverse()  # Restore correct order
        
        # TAIL CALL OPTIMIZATION: Reuse current frame if this is a tail call
        if is_tail_call and translator.call_stack:
            return self._handle_tail_call(translator, function_name, args)
        
        # Regular call: Check recursion depth to prevent infinite recursion
        current_depth = len(translator.call_stack)
        if current_depth >= self.MAX_RECURSION_DEPTH:
            raise RuntimeError(f"Maximum recursion depth ({self.MAX_RECURSION_DEPTH}) exceeded")
        
        # Store arguments in call stack for function to access
        call_frame = {
            'function_name': function_name,
            'arguments': args,
            'saved_result_places': translator.result_places.copy(),
            'saved_function': translator.current_function,
            'recursion_depth': current_depth + 1,  # Track recursion depth
            'local_variables': {}  # Track local variables for this call frame
        }
        translator.call_stack.append(call_frame)
        
        # Set current function context
        translator.current_function = function_name
        
        print(f"Calling function {function_name} with {num_args} arguments (depth: {call_frame['recursion_depth']})")
        
        return self._execute_function_body(translator, function_name)
    
    def _handle_tail_call(self, translator, function_name, args):
        """
        Handle tail call optimization by reusing the current stack frame
        This prevents stack growth for tail-recursive functions
        """
        if not translator.call_stack:
            raise RuntimeError("Cannot perform tail call with empty call stack")
        
        # Get current frame (we'll reuse it)
        current_frame = translator.call_stack[-1]
        original_depth = current_frame['recursion_depth']
        
        print(f"TAIL CALL: {current_frame['function_name']} -> {function_name} (reusing depth {original_depth})")
        
        # Clean up current frame's local variables
        self._cleanup_call_frame_locals(translator, current_frame)
        
        # Update the frame for the new function (REUSE instead of creating new)
        current_frame['function_name'] = function_name
        current_frame['arguments'] = args
        current_frame['local_variables'] = {}  # Reset locals for new function
        # Keep same recursion_depth (no stack growth!)
        # Keep saved_result_places and saved_function from original call
        
        # Set current function context
        translator.current_function = function_name
        
        return self._execute_function_body(translator, function_name)
    
    def _execute_function_body(self, translator, function_name):
        """
        Execute function body with proper control flow and tail call detection
        """
        # Pre-process labels in function body before execution
        function_def = translator.function_definitions[function_name]
        self._preprocess_function_labels(translator, function_def['body'], function_name)
        
        # Execute function body with proper control flow
        function_commands = function_def['body']
        func_index = 0
        
        while func_index < len(function_commands):
            command = function_commands[func_index]
            
            if command[0] == "return":
                # Handle return - don't execute more commands
                self.return_operation(translator)
                break
            elif self._is_tail_call(function_commands, func_index):
                # TAIL CALL OPTIMIZATION: Detect tail calls
                call_command = function_commands[func_index]
                if call_command[0] == "call":
                    target_function = call_command[1]
                    target_args = call_command[2]
                    
                    print(f"Detected tail call to {target_function}")
                    
                    # Execute the tail call (this will reuse the current frame)
                    return self.call_operation(translator, target_function, target_args, is_tail_call=True)
            
            # Regular command execution
            # Maintain function execution context
            # Save main program state
            saved_main_index = translator.command_index
            saved_current_function = translator.current_function
            
            # Set function execution context
            translator.current_function = function_name
            # Don't modify command_index - it's used for main program
            
            print(f"Executing function command {func_index}: {command}")
            result = translator._execute_command(command)
            
            # Restore function context (in case _execute_command changed it)
            translator.current_function = function_name
            
            # Check for cross-scope jump
            if result == "CROSS_SCOPE_JUMP" or translator._cross_scope_jump_pending:
                # Exit function and let main program handle the jump
                print(f"Cross-scope jump detected, exiting function {function_name}")
                # Restore main program state
                translator.command_index = saved_main_index
                translator.current_function = saved_current_function
                return "CROSS_SCOPE_JUMP"
            
            # Handle control flow within function
            if hasattr(translator, '_function_jump_target') and translator._function_jump_target is not None:
                # Jump occurred within function
                func_index = translator._function_jump_target
                translator._function_jump_target = None
                # Don't increment func_index, continue from the jump target
            else:
                # Normal progression
                func_index += 1
            
            # Restore main program state
            translator.command_index = saved_main_index
            translator.current_function = saved_current_function
        
        return translator.call_stack[-1] if translator.call_stack else None
    
    def _is_tail_call(self, function_commands, current_index):
        """
        Detect if the current command is a tail call
        A tail call is a function call that is immediately followed by a return
        """
        if current_index >= len(function_commands):
            return False
        
        current_command = function_commands[current_index]
        
        # Must be a call command
        if current_command[0] != "call":
            return False
        
        # Check if the next command is a return (or end of function)
        next_index = current_index + 1
        
        # If this is the last command, it's a tail call
        if next_index >= len(function_commands):
            return True
        
        # If the next command is return, it's a tail call
        next_command = function_commands[next_index]
        if next_command[0] == "return":
            return True
        
        # More sophisticated analysis: check if there are only stack-neutral operations
        # between the call and return (like drop, or operations that don't affect the result)
        remaining_commands = function_commands[next_index:]
        return self._are_commands_tail_call_compatible(remaining_commands)
    
    def _are_commands_tail_call_compatible(self, commands):
        """
        Check if a sequence of commands is compatible with tail call optimization
        Compatible commands are those that don't modify the return value
        """
        for command in commands:
            cmd_type = command[0]
            
            # Return is always compatible (ends the function)
            if cmd_type == "return":
                return True
            
            # Drop is compatible (removes unused values)
            if cmd_type == "drop":
                continue
            
            # Most other operations modify the stack and break tail call optimization
            # We could be more sophisticated here, but for safety, we're conservative
            return False
        
        # If we reach here, there's no return statement, which is unusual
        return False
        
    def _preprocess_function_labels(self, translator, function_body, function_name):
        """
        Pre-process all label definitions in a function body
        This ensures labels are defined before any goto/if-goto operations reference them
        """
        saved_function = translator.current_function
        translator.current_function = function_name
        
        # First pass: define all labels
        for command in function_body:
            if command[0] == "label":
                label_name = command[1]
                # Only define the label, don't execute it
                translator.control_flow.define_label(label_name, function_name)
                print(f"Pre-processed label '{label_name}' in function '{function_name}'")
        
        translator.current_function = saved_function
        
    def return_operation(self, translator):
        """
        Implement function return using Petri net semantics with enhanced recursive support
        Returns value and restores caller context with proper cleanup
        """
        if not translator.call_stack:
            # No active function call - this is a program return
            print("Program return")
            return None
        
        # Get the current call frame
        call_frame = translator.call_stack.pop()
        
        # Clean up local variables for this call frame to optimize memory
        self._cleanup_call_frame_locals(translator, call_frame)
        
        # Get return value (top of result places, if any)
        if translator.result_places:
            return_value_place = translator.result_places.pop()  # Remove and return the top value
            print(f"Returning value from {call_frame['function_name']} (depth: {call_frame['recursion_depth']})")
        else:
            # No return value - create a default (0)
            return_value_place = translator.net.add_place(translator.get_unique_place_name("return_default"))
            return_value_place.put_token(Token(0))
            print(f"Returning default value 0 from {call_frame['function_name']} (depth: {call_frame['recursion_depth']})")
        
        # Restore caller's result places and add the returned value
        translator.result_places = call_frame['saved_result_places']
        translator.result_places.append(return_value_place)
        
        # Restore function context
        translator.current_function = call_frame['saved_function']
        
        return return_value_place
    
    def _cleanup_call_frame_locals(self, translator, call_frame):
        """
        Clean up local variables associated with this call frame
        This helps optimize memory allocation for recursive call patterns
        """
        function_name = call_frame['function_name']
        
        # Remove local variables for this specific call frame
        # Note: We keep the places but could mark them for reuse in memory optimization
        locals_to_remove = []
        for local_key in translator.local_places:
            if local_key[0] == function_name:
                # This local belongs to the function we're returning from
                # In a more sophisticated implementation, we'd track which locals
                # belong to which call frame depth
                pass  # For now, keep locals as they might be reused
        
        print(f"Cleaned up call frame for {function_name}")
    
    def get_current_recursion_depth(self, translator):
        """
        Get the current recursion depth
        Useful for debugging and optimization
        """
        return len(translator.call_stack)
    
    def get_stack_usage_info(self, translator):
        """
        Get detailed stack usage information for monitoring
        
        Returns:
            dict: Stack usage statistics including current depth, max depth, 
                  and percentage utilization
        """
        current_depth = len(translator.call_stack)
        max_depth = self.MAX_RECURSION_DEPTH
        utilization_percent = (current_depth / max_depth) * 100 if max_depth > 0 else 0
        
        return {
            'current_depth': current_depth,
            'max_depth': max_depth,
            'utilization_percent': utilization_percent,
            'remaining_depth': max_depth - current_depth,
            'is_near_limit': utilization_percent > 80  # Warning threshold
        }
    
    def check_stack_health(self, translator, warning_threshold=0.8):
        """
        Check if stack usage is approaching dangerous levels
        
        Args:
            translator: VM translator instance
            warning_threshold: Fraction of max depth that triggers warning (default: 0.8)
            
        Returns:
            tuple: (is_healthy, warning_message)
        """
        current_depth = len(translator.call_stack)
        max_depth = self.MAX_RECURSION_DEPTH
        
        if current_depth >= max_depth:
            return False, f"Stack overflow imminent! Depth: {current_depth}/{max_depth}"
        elif current_depth >= (max_depth * warning_threshold):
            return False, f"Stack usage high: {current_depth}/{max_depth} ({(current_depth/max_depth)*100:.1f}%)"
        else:
            return True, f"Stack healthy: {current_depth}/{max_depth}"
    
    def analyze_tail_call_opportunities(self, translator):
        """
        Analyze function definitions to identify tail call optimization opportunities
        
        Returns:
            dict: Analysis of functions and their tail call potential
        """
        analysis = {
            'tail_recursive_functions': [],
            'tail_call_functions': [],
            'optimization_opportunities': 0,
            'details': {}
        }
        
        for func_name, func_def in translator.function_definitions.items():
            func_analysis = self._analyze_function_for_tail_calls(func_name, func_def['body'])
            analysis['details'][func_name] = func_analysis
            
            if func_analysis['has_tail_recursion']:
                analysis['tail_recursive_functions'].append(func_name)
                analysis['optimization_opportunities'] += func_analysis['tail_call_count']
            
            if func_analysis['has_tail_calls']:
                analysis['tail_call_functions'].append(func_name)
        
        return analysis
    
    def _analyze_function_for_tail_calls(self, func_name, commands):
        """
        Analyze a single function for tail call patterns
        """
        analysis = {
            'has_tail_calls': False,
            'has_tail_recursion': False,
            'tail_call_count': 0,
            'tail_call_targets': [],
            'tail_recursive_calls': 0
        }
        
        for i, command in enumerate(commands):
            if self._is_tail_call(commands, i):
                analysis['has_tail_calls'] = True
                analysis['tail_call_count'] += 1
                
                if command[0] == "call":
                    target_func = command[1]
                    analysis['tail_call_targets'].append(target_func)
                    
                    # Check if it's tail recursion (calling itself)
                    if target_func == func_name:
                        analysis['has_tail_recursion'] = True
                        analysis['tail_recursive_calls'] += 1
        
        return analysis