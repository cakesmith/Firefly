"""
VM to Petri Net Translator
Translates VM commands into Petri net fragments following the six primitives:
source, choice, dup, drop, join, loop

Pure Petri-net semantics - no stack needed. Places ARE the data flow.
"""

from .net import PetriNet
from .Token import Token
from .control_flow_manager import ControlFlowManager
from .memory_operations import MemoryOperations
from .arithmetic_operations import ArithmeticOperations
from .logical_operations import LogicalOperations
from .stack_operations import StackOperations
from .control_flow_operations import ControlFlowOperations
from .function_operations import FunctionOperations
from .memory_optimizer import MemoryOptimizer
from .execution_analyzer import ExecutionAnalyzer
from .assembly_generator import AssemblyGenerator

class VMToPetriTranslator:
    def __init__(self):
        self.net = PetriNet()
        self.result_places = []  # Final output places (what would be "top of stack")
        self.place_counter = 0
        self.transition_counter = 0
        
        # Function call management
        self.call_stack = []  # Stack of function call frames
        self.current_function = None  # Current function name
        self.function_locals = {}  # function_name -> number of locals
        self.function_definitions = {}  # function_name -> list of commands
        self.program_commands = []  # Commands being executed
        self.main_program_commands = []  # Main program commands (separated from functions)
        self.command_index = 0  # Current command index
        
        # Local variable management
        self.local_places = {}  # (function_name, index) -> place
        
        # Control flow management
        self.control_flow = ControlFlowManager(self.net)
        
        # Cross-scope jump management
        self._cross_scope_jump_pending = False
        self._cross_scope_jump_target = None
        
        # Function-scope jump management
        self._function_jump_target = None
        
        # Operation handlers
        self.memory_ops = MemoryOperations()
        self.arithmetic_ops = ArithmeticOperations()
        self.logical_ops = LogicalOperations()
        self.stack_ops = StackOperations()
        self.control_flow_ops = ControlFlowOperations()
        self.function_ops = FunctionOperations()
        
        # Advanced feature handlers
        self.memory_optimizer = MemoryOptimizer(self)
        self.execution_analyzer = ExecutionAnalyzer(self)
        self.assembly_generator = AssemblyGenerator(self)
        
    def get_unique_place_name(self, prefix="place"):
        self.place_counter += 1
        return f"{prefix}_{self.place_counter}"
        
    def get_unique_transition_name(self, prefix="trans"):
        self.transition_counter += 1
        return f"{prefix}_{self.transition_counter}"
        
    # Memory operations
    def push_operation(self, segment, index):
        return self.memory_ops.push_operation(self, segment, index)
    
    def push_constant(self, value):
        return self.memory_ops.push_constant(self, value)
    
    def push_argument(self, index):
        return self.memory_ops.push_argument(self, index)
    
    def push_local(self, index):
        return self.memory_ops.push_local(self, index)
    
    def pop_local(self, index):
        return self.memory_ops.pop_local(self, index)
    
    def pop_argument(self, index):
        return self.memory_ops.pop_argument(self, index)
    
    def pop_operation(self, segment, index):
        return self.memory_ops.pop_operation(self, segment, index)
        
    # Arithmetic operations
    def add_operation(self):
        return self.arithmetic_ops.add_operation(self)
        
    def sub_operation(self):
        return self.arithmetic_ops.sub_operation(self)
        
    def neg_operation(self):
        return self.arithmetic_ops.neg_operation(self)
        
    def mul_operation(self):
        return self.arithmetic_ops.mul_operation(self)
        
    def div_operation(self):
        return self.arithmetic_ops.div_operation(self)
        
    # Logical operations
    def eq_operation(self):
        return self.logical_ops.eq_operation(self)
        
    def lt_operation(self):
        return self.logical_ops.lt_operation(self)
        
    def gt_operation(self):
        return self.logical_ops.gt_operation(self)
        
    def and_operation(self):
        return self.logical_ops.and_operation(self)
        
    def or_operation(self):
        return self.logical_ops.or_operation(self)
        
    def not_operation(self):
        return self.logical_ops.not_operation(self)
        
    # Stack operations
    def dup_operation(self):
        return self.stack_ops.dup_operation(self)
        
    def drop_operation(self):
        return self.stack_ops.drop_operation(self)
        
    # Control flow operations
    def label_operation(self, label_name):
        return self.control_flow_ops.label_operation(self, label_name)
        
    def goto_operation(self, label_name):
        return self.control_flow_ops.goto_operation(self, label_name)
        
    def if_goto_operation(self, label_name):
        return self.control_flow_ops.if_goto_operation(self, label_name)
        
    # Function operations
    def call_operation(self, function_name, num_args):
        return self.function_ops.call_operation(self, function_name, num_args)
        
    def return_operation(self):
        return self.function_ops.return_operation(self)
        
    def get_result_values(self):
        """Get current values in the result places (what would be the stack)"""
        values = []
        for place in self.result_places:
            if place.has_token():
                values.append(place.tokens[0].value)
            else:
                values.append(None)
        return values
        
    def execute_step(self):
        """Execute one step of the Petri net"""
        return self.net.execute_step()
        
    def execute_program(self, commands):
        """Execute a sequence of VM commands - no stack needed!"""
        self.program_commands = commands
        self.command_index = 0
        
        print(f"Executing program with {len(commands)} commands")
        
        # First pass: parse function definitions
        self._parse_functions()
        
        # Second pass: execute main program (commands after all function definitions)
        print(f"Starting main program execution")
        main_cmd_index = 0
        while main_cmd_index < len(self.main_program_commands):
            original_index, command = self.main_program_commands[main_cmd_index]
            cmd_type = command[0]
            
            print(f"Executing main command {main_cmd_index}: {command}")
            
            # With fixed parsing, we should not encounter function definitions in main program
            if cmd_type == "function":
                print(f"Warning: Unexpected function definition in main program")
            else:
                # Set command_index for compatibility with existing code
                self.command_index = original_index
                result = self._execute_command(command)
                
                # Handle cross-scope jumps
                if result == "CROSS_SCOPE_JUMP" or self._cross_scope_jump_pending:
                    if self._cross_scope_jump_target is not None:
                        print(f"Handling cross-scope jump to main program index {self._cross_scope_jump_target}")
                        # Find the main command index for the target
                        for i, (orig_idx, _) in enumerate(self.main_program_commands):
                            if orig_idx >= self._cross_scope_jump_target:
                                main_cmd_index = i
                                break
                        self._cross_scope_jump_pending = False
                        self._cross_scope_jump_target = None
                        continue  # Don't increment main_cmd_index
                
                # Check if this was a return statement in main program (should terminate)
                if cmd_type == "return" and not self.call_stack:
                    print("Main program return - terminating execution")
                    break
            
            main_cmd_index += 1
                
        # Execute the Petri net to get final results
        # Keep executing until no more transitions can fire
        steps = 0
        max_steps = 100  # Prevent infinite loops
        while steps < max_steps:
            fired = self.execute_step()
            if not fired:
                break
            steps += 1
            
        return self.get_result_values()
    
    def _parse_functions(self):
        """Parse all function definitions from the command list"""
        i = 0
        functions_found = []
        
        # First pass: find all function starts
        while i < len(self.program_commands):
            command = self.program_commands[i]
            if command[0] == "function":
                functions_found.append(i)
            i += 1
        
        print(f"Found {len(functions_found)} functions")
        
        # Second pass: parse each function
        main_program_start = 0
        for func_idx, func_start in enumerate(functions_found):
            command = self.program_commands[func_start]
            function_name = command[1]
            num_locals = command[2]
            
            # Determine function end
            if func_idx + 1 < len(functions_found):
                # Next function starts here
                func_end = functions_found[func_idx + 1]
            else:
                # This is the last function, find where it ends
                func_end = self._find_function_end(func_start)
            
            # Collect function body
            function_body = []
            for j in range(func_start + 1, func_end):
                if j < len(self.program_commands):
                    function_body.append(self.program_commands[j])
            
            # Store function definition
            self.function_definitions[function_name] = {
                'num_locals': num_locals,
                'body': function_body,
                'start_index': func_start + 1,
                'end_index': func_end
            }
            self.function_locals[function_name] = num_locals
            print(f"Parsed function {function_name} with {len(function_body)} commands and {num_locals} locals")
            
            # Update main program start
            main_program_start = max(main_program_start, func_end)
        
        # Collect main program commands
        main_program_commands = []
        for i in range(main_program_start, len(self.program_commands)):
            main_program_commands.append((i, self.program_commands[i]))
        
        self.main_program_commands = main_program_commands
        self.command_index = 0
        print(f"Main program has {len(main_program_commands)} commands")
    
    def _find_function_end(self, func_start):
        """Find where a function ends by looking for main program patterns"""
        # Start after the function declaration
        i = func_start + 1
        return_count = 0
        
        while i < len(self.program_commands):
            command = self.program_commands[i]
            
            # Count return statements
            if command[0] == "return":
                return_count += 1
                
                # Look ahead to see if the next commands look like main program
                # Main program typically starts with push constant or call
                if i + 1 < len(self.program_commands):
                    next_cmd = self.program_commands[i + 1]
                    # If next command is push constant (not push argument/local), 
                    # it's likely main program
                    if (next_cmd[0] == "push" and next_cmd[1] == "constant") or \
                       (next_cmd[0] == "call"):
                        return i + 1
            
            i += 1
        
        # If we didn't find a clear boundary, assume the whole thing is the function
        return len(self.program_commands)
    
    def _skip_function_definition(self):
        """Skip over a function definition during main execution"""
        # This should not be called anymore with the fixed parsing
        # But keep it for safety
        function_name = self.program_commands[self.command_index][1]
        if function_name in self.function_definitions:
            # Jump to end of this function
            self.command_index = self.function_definitions[function_name]['end_index'] - 1
        else:
            # Fallback: skip until we find return
            while self.command_index < len(self.program_commands):
                command = self.program_commands[self.command_index]
                if command[0] == "return":
                    break
                self.command_index += 1
    
    def _perform_cross_scope_jump(self, main_program_index):
        """
        Perform a cross-scope jump from function to main program
        This exits the current function context and jumps to the main program
        """
        if not self.call_stack:
            # No function context - this might be a unit test or direct call
            print(f"Cross-scope jump: no function context, setting jump target to main program index {main_program_index}")
            self._cross_scope_jump_target = main_program_index
            self._cross_scope_jump_pending = True
            return
        
        # Pop the call stack to exit the function completely
        call_frame = self.call_stack.pop()
        
        # Restore the caller's context but don't add return value
        # (cross-scope jumps don't return values)
        self.result_places = call_frame['saved_result_places']
        self.current_function = call_frame['saved_function']
        
        # Store the jump target for the main execution loop to handle
        self._cross_scope_jump_target = main_program_index
        
        # Signal that we need to jump in main program
        self._cross_scope_jump_pending = True
        
        print(f"Cross-scope jump: exited function {call_frame['function_name']}, jumping to main program index {main_program_index}")
    
    def _execute_command(self, command):
        """Execute a single VM command"""
        cmd_type = command[0]
        
        if cmd_type == "push":
            segment = command[1]
            index = command[2]
            self.push_operation(segment, index)
        elif cmd_type == "pop":
            segment = command[1]
            index = command[2]
            self.pop_operation(segment, index)
        elif cmd_type == "add":
            self.add_operation()
        elif cmd_type == "sub":
            self.sub_operation()
        elif cmd_type == "neg":
            self.neg_operation()
        elif cmd_type == "eq":
            self.eq_operation()
        elif cmd_type == "lt":
            self.lt_operation()
        elif cmd_type == "gt":
            self.gt_operation()
        elif cmd_type == "and":
            self.and_operation()
        elif cmd_type == "or":
            self.or_operation()
        elif cmd_type == "not":
            self.not_operation()
        elif cmd_type == "mul":
            self.mul_operation()
        elif cmd_type == "div":
            self.div_operation()
        elif cmd_type == "dup":
            self.dup_operation()
        elif cmd_type == "drop":
            self.drop_operation()
        elif cmd_type == "call":
            function_name = command[1]
            num_args = command[2]
            return self.call_operation(function_name, num_args)
        elif cmd_type == "return":
            self.return_operation()
        elif cmd_type == "label":
            label_name = command[1]
            self.label_operation(label_name)
        elif cmd_type == "goto":
            label_name = command[1]
            return self.goto_operation(label_name)
        elif cmd_type == "if-goto":
            label_name = command[1]
            return self.if_goto_operation(label_name)
        else:
            raise NotImplementedError(f"Command {cmd_type} not implemented")
        
        # Execute Petri net after each command to ensure values are available
        if cmd_type not in ["label", "goto", "if-goto"]:  # Don't execute for control flow
            # Only execute once per command to prevent over-execution
            fired = self.net.execute_step()
            # If a transition fired, execute one more time to handle cascading effects
            if fired:
                self.net.execute_step()
        
    def get_detailed_place_info(self):
        """Return detailed information about each place"""
        place_info = {}
        
        for name, place in self.net.places.items():
            info = {
                'tokens': [str(t.value) for t in place.tokens],
                'token_count': place.token_count(),
                'input_transitions': [t.name for t in place.in_transitions],
                'output_transitions': [t.name for t in place.out_transitions],
                'in_result_places': place in self.result_places,
                'result_position': self.result_places.index(place) if place in self.result_places else None
            }
            place_info[name] = info
            
        return place_info
        
    def get_detailed_transition_info(self):
        """Return detailed information about each transition"""
        transition_info = {}
        
        for name, transition in self.net.transitions.items():
            info = {
                'input_places': [p.name for p in transition.in_places],
                'output_places': [p.name for p in transition.out_places],
                'can_fire': transition.can_fire(),
                'operation_type': name.split('_')[0]
            }
            transition_info[name] = info
            
        return transition_info
        
    # Placeholder methods for complex functionality that will be added later
    def print_net_statistics(self):
        """Print basic statistics about the translated Petri net"""
        print("\n" + "=" * 60)
        print("PETRI NET TRANSLATION STATISTICS")
        print("=" * 60)
        
        # Basic counts
        total_places = len(self.net.places)
        total_transitions = len(self.net.transitions)
        total_arcs = len(self.net.arcs)
        result_count = len(self.result_places)
        
        print(f"Network Size:")
        print(f"  Places: {total_places}")
        print(f"  Transitions: {total_transitions}")
        print(f"  Arcs: {total_arcs}")
        print(f"  Result Places: {result_count} (no stack needed!)")
        
        # Token Distribution
        places_with_tokens = sum(1 for p in self.net.places.values() if p.has_token())
        total_tokens = sum(p.token_count() for p in self.net.places.values())
        
        print(f"\nToken Distribution:")
        print(f"  Places with tokens: {places_with_tokens}/{total_places}")
        print(f"  Total tokens: {total_tokens}")
        
        # Final result state
        if self.result_places:
            result_values = self.get_result_values()
            print(f"\nFinal Result Places:")
            for i, value in enumerate(result_values):
                print(f"  [{i}]: {value}")
        else:
            print(f"\nFinal Result Places: Empty")
            
        print("=" * 60)
        
    def _optimize_memory_allocation(self):
        """
        Enhanced memory optimization with control flow support
        Delegates to the memory optimizer module
        """
        return self.memory_optimizer.optimize_memory_allocation()
        
    def _analyze_execution_dependencies(self):
        """
        Analyze execution dependencies and create execution plan
        Delegates to the execution analyzer module
        """
        return self.execution_analyzer.analyze_execution_dependencies()
        
    def _assign_operations_to_cores(self, execution_plan, num_cores):
        """
        Assign operations to cores based on dependencies
        Delegates to the execution analyzer module
        """
        return self.execution_analyzer.assign_operations_to_cores(execution_plan, num_cores)
        
    def _generate_core_rom(self, core_id, operations, memory_map, num_cores):
        """
        Generate ROM content for a specific core
        Delegates to the assembly generator module
        """
        return self.assembly_generator._generate_core_rom(core_id, operations, memory_map, num_cores)
        
    def _is_control_flow_place(self, place_name):
        """
        Determine if a place is related to control flow operations
        """
        control_flow_patterns = [
            'label_',           # Label places
            'goto_source_',     # Goto source places
            'if_goto_continue_', # If-goto continue places
            'control_'          # General control places
        ]
        
        return any(place_name.startswith(pattern) for pattern in control_flow_patterns)
        
    def generate_multicore_assembly(self, num_cores=1, output_dir="test_results"):
        """
        Generate assembly code for n cores
        Delegates to the assembly generator module
        """
        return self.assembly_generator.generate_multicore_assembly(num_cores, output_dir)