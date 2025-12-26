"""
Function Operations for Petri Net VM
Handles function call and return operations
"""

from .Token import Token

class FunctionOperations:
    """
    Handles function operations in Petri net semantics
    """
    
    def call_operation(self, translator, function_name, num_args):
        """
        Implement function call using Petri net semantics
        Execute the function body with the provided arguments
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
        
        # Store arguments in call stack for function to access
        call_frame = {
            'function_name': function_name,
            'arguments': args,
            'saved_result_places': translator.result_places.copy(),
            'saved_function': translator.current_function
        }
        translator.call_stack.append(call_frame)
        
        # Set current function context
        translator.current_function = function_name
        
        print(f"Calling function {function_name} with {num_args} arguments")
        
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
                # Save current command index and set function context
                saved_index = translator.command_index
                translator.command_index = func_index
                
                result = translator._execute_command(command)
                
                # Check for cross-scope jump
                if result == "CROSS_SCOPE_JUMP" or translator._cross_scope_jump_pending:
                    # Exit function and let main program handle the jump
                    print(f"Cross-scope jump detected, exiting function {function_name}")
                    # Don't call return_operation() - we're jumping out of the function
                    # The main program will handle the jump
                    translator.command_index = saved_index
                    return "CROSS_SCOPE_JUMP"
                
                # Check if command modified the index (goto/if-goto within function)
                if translator.command_index != func_index:
                    # Jump occurred within function, update function index
                    func_index = translator.command_index
                    # Don't increment func_index, continue from the jump target
                else:
                    # Normal progression
                    func_index += 1
                
                # Restore main program index
                translator.command_index = saved_index
        
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
        Implement function return using Petri net semantics
        Returns value and restores caller context
        """
        if not translator.call_stack:
            # No active function call - this is a program return
            print("Program return")
            return None
        
        # Get the current call frame
        call_frame = translator.call_stack.pop()
        
        # Get return value (top of result places, if any)
        if translator.result_places:
            return_value_place = translator.result_places.pop()  # Remove and return the top value
            print(f"Returning value from {call_frame['function_name']}")
        else:
            # No return value - create a default (0)
            return_value_place = translator.net.add_place(translator.get_unique_place_name("return_default"))
            return_value_place.put_token(Token(0))
            print(f"Returning default value 0 from {call_frame['function_name']}")
        
        # Restore caller's result places and add the returned value
        translator.result_places = call_frame['saved_result_places']
        translator.result_places.append(return_value_place)
        
        # Restore function context
        translator.current_function = call_frame['saved_function']
        
        return return_value_place