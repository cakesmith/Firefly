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
        Function call implementation using FunctionContextManager
        
        Args:
            translator: VM translator instance
            function_name: Name of function to call
            num_args: Number of arguments
        """
        if function_name not in translator.function_definitions:
            raise RuntimeError(f"Function {function_name} not defined")
        
        if len(translator.result_places) < num_args:
            raise RuntimeError(f"Not enough arguments for call to {function_name}")
        
        # Get function definition
        func_def = translator.function_definitions[function_name]
        num_locals = func_def['num_locals']
        
        # Pre-process labels in function body BEFORE entering context
        self._preprocess_function_labels(translator, func_def['body'], function_name)
        
        # Enter function context using FunctionContextManager
        context = translator.function_context_manager.enter_function_context(
            function_name, num_locals, num_args
        )
        
        try:
            # Execute function body directly without recursion
            print(f"Executing function {function_name} with {len(func_def['body'])} commands")
            
            # Execute each command in the function body
            for command in func_def['body']:
                cmd_type = command[0]
                
                if cmd_type == "return":
                    # Handle return - exit function
                    self.return_operation(translator)
                    break
                else:
                    # Execute the command directly
                    print(f"Executing function command: {command}")
                    translator._execute_command(command)
            
            print(f"Completed function {function_name}")
            return None
            
        except Exception as e:
            # Clean up on error - exit function context
            translator.function_context_manager.exit_function_context()
            raise e
    
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
        Implement function return using FunctionContextManager
        """
        # Exit function context using FunctionContextManager
        context = translator.function_context_manager.exit_function_context()
        
        if context is None:
            # No active function call - this is a program return
            print("Program return")
            return None
        
        # Also clean up the existing call stack for compatibility
        if translator.call_stack:
            call_frame = translator.call_stack.pop()
            translator.current_function = call_frame.get('saved_function', None)
        
        print(f"Returned from function {context['function_name']}")
        return context
    
    def get_stack_usage_info(self, translator):
        """
        Get stack usage information for monitoring using FunctionContextManager
        """
        current_depth = translator.function_context_manager.get_call_depth()
        max_depth = translator.function_context_manager.max_recursion_depth
        
        return {
            'current_depth': current_depth,
            'max_depth': max_depth,
            'utilization_percent': (current_depth / max_depth) * 100,
            'remaining_depth': max_depth - current_depth,
            'is_near_limit': current_depth > (max_depth * 0.8)
        }
    
    def check_stack_health(self, translator):
        """
        Check stack health using FunctionContextManager
        """
        current_depth = translator.function_context_manager.get_call_depth()
        max_depth = translator.function_context_manager.max_recursion_depth
        
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