"""
Control Flow Operations for Petri Net VM
Handles control flow operations: label, goto, if-goto
"""

from .Token import Token

class ControlFlowOperations:
    """
    Handles control flow operations in Petri net semantics
    """
    
    def label_operation(self, translator, label_name):
        """
        Implement label operation: define a jump target within current function
        Creates control flow places for labels and integrates with function scoping
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
            
        # Check if label is already defined (from pre-processing)
        if translator.control_flow.is_label_defined(label_name, translator.current_function):
            # Label already exists from pre-processing, just return the existing place
            control_place = translator.control_flow.get_label_place(label_name, translator.current_function)
            print(f"Using pre-processed label '{label_name}' in function '{translator.current_function}'")
            return control_place
            
        # Define the label in the current function scope
        control_place = translator.control_flow.define_label(label_name, translator.current_function)
        
        # Initialize the control place with a control token to indicate this is a valid jump target
        # This represents the "execution context" at this label
        control_place.put_token(Token("control"))
        
        print(f"Created label '{label_name}' in function '{translator.current_function}'")
        return control_place
        
    def goto_operation(self, translator, label_name):
        """
        Implement goto operation: unconditional jump to label
        Supports cross-scope jumps (function -> main program)
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
        
        # Check if label is defined in current scope
        if not translator.control_flow.is_label_defined(label_name, translator.current_function):
            raise RuntimeError(f"Cannot goto undefined label '{label_name}'")
        
        # Get the label place for Petri net semantics
        label_place = translator.control_flow.get_label_place(label_name, translator.current_function)
        
        # Create goto transition that transfers control to the label
        goto_transition = translator.net.add_transition(
            translator.get_unique_transition_name(f"goto_{label_name}"),
            lambda tokens: Token("control")  # Transfer control token
        )
        
        # Create a control source place for this goto
        goto_source = translator.net.add_place(translator.get_unique_place_name(f"goto_source_{label_name}"))
        goto_source.put_token(Token("control"))
        
        # Wire: goto_source -> goto_transition -> label_place
        translator.net.add_arc(goto_source, goto_transition)
        translator.net.add_arc(goto_transition, label_place)
        
        # For program execution context, handle command index updates
        if translator.current_function and translator.current_function in translator.function_definitions:
            function_commands = translator.function_definitions[translator.current_function]['body']
            for i, command in enumerate(function_commands):
                if command[0] == "label" and command[1] == label_name:
                    # Found in current function - set function jump target
                    translator._function_jump_target = i
                    print(f"Goto to label '{label_name}' at function command index {i}")
                    return goto_transition
        
        # Check main program for cross-scope jumps
        if hasattr(translator, 'program_commands') and translator.program_commands:
            for i, command in enumerate(translator.program_commands):
                if command[0] == "label" and command[1] == label_name:
                    # Found in main program - cross-scope jump
                    translator._perform_cross_scope_jump(i)
                    print(f"Cross-scope goto to label '{label_name}' at main program index {i}")
                    return "CROSS_SCOPE_JUMP"
        
        print(f"Goto to label '{label_name}' (Petri net semantics)")
        return goto_transition
        
    def if_goto_operation(self, translator, label_name):
        """
        Implement if-goto operation: conditional jump to label
        Supports cross-scope jumps (function -> main program)
        """
        if not label_name:
            raise RuntimeError("Label name cannot be empty")
            
        if len(translator.result_places) < 1:
            raise RuntimeError("No condition for if-goto")
        
        # Get the condition from the stack
        condition_place = translator.result_places.pop()
        
        # Check if label is defined in current scope
        if not translator.control_flow.is_label_defined(label_name, translator.current_function):
            raise RuntimeError(f"Cannot if-goto undefined label '{label_name}'")
        
        # Get the label place for Petri net semantics
        label_place = translator.control_flow.get_label_place(label_name, translator.current_function)
        
        # Create if-goto transition with conditional logic (CHOICE semantics)
        def if_goto_func(tokens):
            condition_value = tokens[0].value if tokens else 0
            if condition_value != 0:
                # True: return token for jump path (first output place)
                return [Token("control"), None]  # Jump, no continue
            else:
                # False: return token for continue path (second output place)  
                return [None, Token("control")]  # No jump, continue
        
        if_goto_transition = translator.net.add_transition(
            translator.get_unique_transition_name(f"if_goto_{label_name}"),
            if_goto_func
        )
        
        # Create continue place for when condition is false
        continue_place = translator.net.add_place(translator.get_unique_place_name(f"if_goto_continue_{label_name}"))
        
        # Always wire both paths - the transition function will choose which one to activate
        translator.net.add_arc(condition_place, if_goto_transition)
        translator.net.add_arc(if_goto_transition, label_place)      # Jump path (index 0)
        translator.net.add_arc(if_goto_transition, continue_place)   # Continue path (index 1)
        
        # For program execution context, handle command index updates
        if hasattr(translator, 'program_commands') and translator.program_commands:
            # Get the condition value directly from the place for execution logic
            condition_value = 0
            if condition_place.has_token():
                condition_value = condition_place.tokens[0].value
            
            print(f"If-goto condition: {condition_value} (0=false, non-zero=true)")
            
            # If condition is true (non-zero), jump to label
            if condition_value != 0:
                # First try to find label in current function
                if translator.current_function and translator.current_function in translator.function_definitions:
                    function_commands = translator.function_definitions[translator.current_function]['body']
                    for i, command in enumerate(function_commands):
                        if command[0] == "label" and command[1] == label_name:
                            # Found in current function - set function jump target
                            translator._function_jump_target = i
                            print(f"If-goto jumping to label '{label_name}' at function command index {i}")
                            return if_goto_transition
                
                # Not found in function, try main program (cross-scope jump)
                for i, command in enumerate(translator.program_commands):
                    if command[0] == "label" and command[1] == label_name:
                        # Found in main program - cross-scope jump
                        translator._perform_cross_scope_jump(i)
                        print(f"Cross-scope if-goto to label '{label_name}' at main program index {i}")
                        return "CROSS_SCOPE_JUMP"
            else:
                print(f"If-goto condition false, continuing to next command")
        
        return if_goto_transition