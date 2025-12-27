"""
Function Operations for Petri Net VM
Handles function call and return operations with recursion depth limits
"""

from .Token import Token, ValueToken

class FunctionOperations:
    """
    Handles function operations with recursion depth limits
    """
    
    def __init__(self):
        """
        Initialize function operations with recursion depth limit
        """
        self.MAX_RECURSION_DEPTH = 1000  # Maximum recursion depth to prevent stack overflow
    
    def get_current_recursion_level(self, translator):
        """
        Get the current recursion level (for monitoring only)
        
        Args:
            translator: VM translator instance
            
        Returns:
            int: Current recursion level
        """
        return len(translator.call_stack)
    
    def call_operation(self, translator, function_name, num_args):
        """
        Function call implementation using continuation transitions
        
        Args:
            translator: VM translator instance
            function_name: Name of function to call
            num_args: Number of arguments
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
        
        # Use direct execution for function calls
        return self._execute_function_call(translator, function_name, args)
    
    def _execute_function_call(self, translator, function_name, args):
        """
        Execute function call using direct execution with call stack and recursion limit
        
        Args:
            translator: VM translator instance
            function_name: Name of function to call
            args: Function arguments
        """
        # Check recursion depth
        current_depth = len(translator.call_stack)
        if current_depth >= self.MAX_RECURSION_DEPTH:
            raise RuntimeError(f"Maximum recursion depth exceeded: {current_depth} >= {self.MAX_RECURSION_DEPTH}")
        
        print(f"Direct call to {function_name} (depth: {current_depth})")
        
        # Create call frame
        call_frame = {
            'function_name': function_name,
            'arguments': args,
            'saved_result_places': translator.result_places.copy(),
            'saved_function': translator.current_function,
            'recursion_depth': current_depth,
            'local_variables': {}
        }
        
        # Push call frame
        translator.call_stack.append(call_frame)
        translator.current_function = function_name
        translator.result_places = []
        
        try:
            # Execute function body directly
            result = self._execute_function_body(translator, function_name)
            return result
            
        except Exception as e:
            # Clean up on error
            if translator.call_stack and translator.call_stack[-1]['function_name'] == function_name:
                translator.call_stack.pop()
            raise e
    
    def _execute_function_body(self, translator, function_name):
        """
        Execute function body with proper control flow
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
            
            # Regular command execution
            # Maintain function execution context
            saved_main_index = translator.command_index
            saved_current_function = translator.current_function
            
            # Set function execution context
            translator.current_function = function_name
            
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
    
    def _preprocess_function_labels(self, translator, function_body, function_name):
        """
        Pre-process all label definitions in a function body
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
        Implement function return
        """
        if not translator.call_stack:
            # No active function call - this is a program return
            print("Program return")
            return None
        
        # Get the current call frame
        call_frame = translator.call_stack.pop()
        
        # Get return value (top of result places, if any)
        if translator.result_places:
            return_value_place = translator.result_places.pop()
            print(f"Returning value from {call_frame['function_name']}")
        else:
            # No return value - create a default
            return_value_place = translator.net.add_place(translator.get_unique_place_name("return_default"))
            return_value_place.put_token(Token(0))
            print(f"Returning default value 0 from {call_frame['function_name']}")
        
        # Restore caller's result places and add the returned value
        translator.result_places = call_frame['saved_result_places']
        translator.result_places.append(return_value_place)
        
        # Restore function context
        translator.current_function = call_frame['saved_function']
        
        return return_value_place
    
    def get_stack_usage_info(self, translator):
        """
        Get stack usage information for monitoring
        """
        current_depth = len(translator.call_stack)
        max_depth = self.MAX_RECURSION_DEPTH
        
        return {
            'current_depth': current_depth,
            'max_depth': max_depth,
            'utilization_percent': (current_depth / max_depth) * 100,
            'remaining_depth': max_depth - current_depth,
            'is_near_limit': current_depth > (max_depth * 0.8)
        }
    
    def check_stack_health(self, translator):
        """
        Check stack health
        """
        current_depth = len(translator.call_stack)
        max_depth = self.MAX_RECURSION_DEPTH
        
        if current_depth > max_depth:
            return False, f"Stack overflow: {current_depth} > {max_depth}"
        elif current_depth > (max_depth * 0.8):
            return True, f"Stack near limit: {current_depth}/{max_depth}"
        else:
            return True, f"Stack healthy: {current_depth}/{max_depth}"
    
    def analyze_tail_call_opportunities(self, translator):
        """
        Analyze tail call opportunities in the current program
        
        Args:
            translator: VM translator instance
            
        Returns:
            dict: Analysis of tail call opportunities
        """
        analysis = {
            'total_functions': len(translator.function_definitions),
            'tail_call_opportunities': 0,
            'optimizable_functions': [],
            'non_optimizable_functions': []
        }
        
        for func_name, func_def in translator.function_definitions.items():
            body = func_def['body']
            has_tail_call = False
            
            # Look for tail calls (call followed immediately by return)
            for i in range(len(body) - 1):
                if (body[i][0] == 'call' and 
                    i + 1 < len(body) and 
                    body[i + 1][0] == 'return'):
                    has_tail_call = True
                    analysis['tail_call_opportunities'] += 1
                    break
            
            if has_tail_call:
                analysis['optimizable_functions'].append(func_name)
            else:
                analysis['non_optimizable_functions'].append(func_name)
        
        return analysis