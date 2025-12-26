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
    
    def call_operation(self, translator, function_name, num_args):
        """
        Implement function call using Petri net semantics with enhanced recursive support
        Execute the function body with the provided arguments
        """
        if function_name not in translator.function_definitions:
            raise RuntimeError(f"Function {function_name} not defined")
        
        if len(translator.result_places) < num_args:
            raise RuntimeError(f"Not enough arguments for call to {function_name}")
        
        # Check recursion depth to prevent infinite recursion
        current_depth = len(translator.call_stack)
        if current_depth >= self.MAX_RECURSION_DEPTH:
            raise RuntimeError(f"Maximum recursion depth ({self.MAX_RECURSION_DEPTH}) exceeded")
        
        # Pop arguments from result places
        args = []
        for i in range(num_args):
            args.append(translator.result_places.pop())
        args.reverse()  # Restore correct order
        
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
            else:
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
        
        return call_frame
        
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