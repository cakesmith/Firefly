from Petri.net import PetriNet
from Petri.Token import Token
from Petri.Place import Place
from Petri.Transition import Transition

class PetriEmitter:

    def __init__(self, memory_read_callback=None, memory_write_callback=None):
        """
        Initialize PetriEmitter with optional memory I/O callbacks.
        
        Args:
            memory_read_callback: Function(addr) -> value, called when reading memory
            memory_write_callback: Function(addr, value), called when writing memory
        
        These callbacks enable memory-mapped I/O:
        - Screen writes (16384-24575) can update a display
        - Keyboard reads (24576) can return current key state
        """
        self.net = PetriNet()
        self.control_stack = []
        
        # Memory I/O callbacks
        self.memory_read = memory_read_callback
        self.memory_write = memory_write_callback
        
        # Simulated RAM for when no callbacks provided
        self._ram = [0] * 32768
        
        # Control flow tracking
        self.pending_control_place = None  # Set by label, consumed by next operation
        self.net.labels = {}  # label_name -> place

        self.net.add_place(Place("init"))
        self.net.add_place(Place("end"))

        # Put starting token in init - Sys.init will use this place
        self.net.places["init"].put_token(Token("control"))
        
        # Sequential control flow tracking
        self.control_place = None  # Will be set by first function declaration
        
        # Central dispatch for function returns
        self.return_dispatch = Place("return_dispatch")
        self.net.add_place(self.return_dispatch)
        
        # Track call sites for return routing
        self.call_sites = {}  # Maps call_id -> return_place
        self.call_counter = 0
        
        # Track current function for label scoping
        self.current_function = None
        
        # Track static variable addresses per class
        # Maps "ClassName.index" -> RAM address (starting at 16)
        self.static_vars = {}
        self.next_static_addr = 16
        
        # Create I/O places and transitions if callbacks provided
        self._setup_io_places()
    
    def finalize(self):
        """
        Finalize the Petri net after all VM commands are parsed.
        Creates dispatch transitions that route returns to the correct call sites.
        """
        if not self.call_sites:
            return
        
        # Create a dispatch transition for each call site
        for call_id, places in self.call_sites.items():
            return_ctrl_place, return_data_place = places
            cid = call_id
            
            def make_dispatch_guard(target_cid):
                """Guard that checks if this dispatch should handle the return."""
                def guard(tokens):
                    if not tokens:
                        return False
                    token = tokens[0]
                    if hasattr(token, 'value') and isinstance(token.value, tuple) and len(token.value) == 3:
                        ret_val, return_addr, remaining_stack = token.value
                        return return_addr == target_cid
                    return False
                return guard
            
            def make_dispatch_op(target_cid):
                def dispatch_op(tokens):
                    if not tokens:
                        return [None, None]
                    
                    token = tokens[0]
                    if hasattr(token, 'value') and isinstance(token.value, tuple) and len(token.value) == 3:
                        ret_val, return_addr, remaining_stack = token.value
                        # Return two tokens: control (call stack in tuple format) and data (return value)
                        # Use tuple format ("callstack", [...]) so seq_operation recognizes it
                        if remaining_stack:
                            ctrl_token = Token(("callstack", remaining_stack))
                        else:
                            ctrl_token = Token([])  # Empty control token
                        return [ctrl_token, Token(ret_val)]
                    return [None, None]
                return dispatch_op
            
            dispatch_trans = Transition(
                name=f"dispatch_to_{call_id}",
                operation=make_dispatch_op(cid),
                guard=make_dispatch_guard(cid)
            )
            self.net.add_transition(dispatch_trans)
            self.net.add_arc(self.return_dispatch, dispatch_trans)
            # Output to both control and data places
            self.net.add_arc(dispatch_trans, return_ctrl_place)
            self.net.add_arc(dispatch_trans, return_data_place)
    
    def _setup_io_places(self):
        """Create I/O places for screen output and keyboard input if callbacks exist."""
        
        # Screen output sink - receives (addr, value) tokens
        if self.memory_write:
            self.screen_output_place = Place("screen_output")
            self.net.add_place(self.screen_output_place)
            
            # Create sink transition that calls the write callback
            write_callback = self.memory_write
            def screen_sink_operation(tokens):
                # Token contains (addr, value) tuple
                if tokens and hasattr(tokens[0], 'value'):
                    data = tokens[0].value
                    if isinstance(data, tuple) and len(data) == 2:
                        addr, value = data
                        write_callback(addr, value)
                return []  # Sink consumes token, produces nothing
            
            screen_sink = Transition(
                name="screen_sink",
                operation=screen_sink_operation
            )
            self.net.add_transition(screen_sink)
            self.net.add_arc(self.screen_output_place, screen_sink)
        else:
            self.screen_output_place = None
        
        # Keyboard input source - provides current key value
        if self.memory_read:
            self.keyboard_input_place = Place("keyboard_input")
            self.net.add_place(self.keyboard_input_place)
            # Keyboard place gets tokens put into it by keyboard_source transition
            # which is triggered when something needs to read keyboard
        else:
            self.keyboard_input_place = None
    
    def write_to_screen(self, addr, value):
        """Write to screen - calls callback directly."""
        if self.memory_write:
            self.memory_write(addr, value)
        elif 0 <= addr < len(self._ram):
            self._ram[addr] = value & 0xFFFF
    
    def read_from_keyboard(self):
        """Read keyboard by calling the callback."""
        if self.memory_read:
            return self.memory_read(24576)  # KBD_ADDR
        return 0
    
    def _get_static_address(self, index):
        """Get RAM address for static variable, scoped by current class."""
        # Extract class name from current function (e.g., "Screen.init" -> "Screen")
        if self.current_function and '.' in self.current_function:
            class_name = self.current_function.split('.')[0]
        else:
            class_name = "Global"
        
        key = f"{class_name}.{index}"
        if key not in self.static_vars:
            self.static_vars[key] = self.next_static_addr
            self.next_static_addr += 1
        
        return self.static_vars[key]
    
    def read_memory(self, addr):
        """Read from memory, using callback if provided."""
        if self.memory_read:
            return self.memory_read(addr)
        elif 0 <= addr < len(self._ram):
            return self._ram[addr]
        return 0
    
    def write_memory(self, addr, value):
        """Write to memory, using callback if provided."""
        # Check if this is a screen write (16384-24575)
        if 16384 <= addr <= 24575:
            self.write_to_screen(addr, value)
        elif self.memory_write:
            self.memory_write(addr, value)
        elif 0 <= addr < len(self._ram):
            self._ram[addr] = value & 0xFFFF
    
    def _get_data_value(self, tokens, index=0):
        """Extract a data value from tokens, skipping control tokens."""
        data_tokens = []
        for t in tokens:
            if hasattr(t, 'value'):
                val = t.value
                # Skip control tokens (tuples starting with "call")
                if isinstance(val, tuple) and len(val) >= 1 and val[0] == "call":
                    continue
                # Skip "ctrl" string tokens
                if val == "ctrl":
                    continue
                data_tokens.append(val)
        
        if index < len(data_tokens):
            val = data_tokens[index]
            # Convert non-numeric to 0
            if isinstance(val, (str, tuple)):
                return 0
            return val
        return 0

    @staticmethod
    def _get_data_places(in_places):
        """
        Filter input places to get only data places (not control places).
        Control places are named 'ctrl_*', 'init', or are function entry places.
        """
        data_places = []
        for p in in_places:
            name = p.name
            # Skip control places
            if name.startswith('ctrl_') or name == 'init':
                continue
            # Skip function entry places
            if name.startswith('function_'):
                continue
            # Skip label places
            if name.startswith('label_'):
                continue
            # Skip return places
            if name.startswith('return_to_'):
                continue
            # Skip ifgoto fallthrough places
            if name.startswith('ifgoto_fallthrough_'):
                continue
            data_places.append(p)
        return data_places

    def _insert_operation(self, transition, output_place, consumes_stack=0, produces_stack=1):
        """
        Insert an operation into the Petri net with proper data and control flow.
        
        Data flow: Operations consume from and produce to the data stack.
        Control flow: All operations are sequenced through a control place chain.
        The control token carries the call_id for return routing.
        
        Args:
            transition: The transition to add
            output_place: The output place of the transition
            consumes_stack: Number of data items to consume from stack
            produces_stack: Number of data items to produce (0 or 1)
        
        Returns:
            The added transition
        """
        if consumes_stack > len(self.control_stack):
            raise RuntimeError(f"Stack underflow: need {consumes_stack} items, have {len(self.control_stack)}")
        
        # Add the transition to the network
        self.net.add_transition(transition)
        
        # Connect control flow input (ensures sequential execution)
        if self.pending_control_place is not None:
            self.net.add_arc(self.pending_control_place, transition)
            self.pending_control_place = None
        elif self.control_place is not None:
            self.net.add_arc(self.control_place, transition)
        # If control_place is None (after goto), this code is unreachable
        # but we still build the net structure
        
        # Connect data inputs from stack
        for i in range(consumes_stack):
            input_place = self.control_stack.pop()
            self.net.add_arc(input_place, transition)
        
        # Connect data output
        self.net.add_arc(transition, output_place)
        
        # Create control output place for sequential flow
        control_out = Place(f"ctrl_{len(self.net.places)}")
        self.net.add_place(control_out)
        self.net.add_arc(transition, control_out)
        self.control_place = control_out
        
        # Update transition to produce both data and control tokens
        # Control token carries the call stack as a tuple: ("callstack", [addresses...])
        original_op = transition.operation
        def seq_operation(tokens, orig=original_op):
            # Separate data tokens from control tokens
            # Control tokens are either empty lists [] or callstack tuples
            data_tokens = []
            call_stack = []
            for t in tokens:
                if hasattr(t, 'value'):
                    val = t.value
                    if isinstance(val, list):
                        # Empty list is a control token (no call stack)
                        pass
                    elif isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                        # This is a call stack token
                        call_stack = list(val[1])
                    else:
                        data_tokens.append(t)  # This is a data token
                else:
                    data_tokens.append(t)
            
            # Pass only data tokens to the original operation
            result = orig(data_tokens)
            
            # Create control token with call stack (as tuple to distinguish from empty list)
            if call_stack:
                ctrl_token = Token(("callstack", call_stack))
            else:
                ctrl_token = Token([])  # Empty control token
            
            if isinstance(result, list):
                result.append(ctrl_token)
            else:
                result = [result, ctrl_token]
            return result
        transition.operation = seq_operation
        
        # Push data output to stack if operation produces data
        if produces_stack == 1:
            self.control_stack.append(output_place)
        
        return transition

    def _connect_parallel_operation(self, transition):
        """
        Connect a parallel operation (consumes 0 from stack) using dup branching.
        This allows multiple push operations to execute in parallel.
        """
        init_place = self.net.places["init"]
        
        # Find existing transitions connected to init
        init_consumers = [t for t in self.net.transitions.values() 
                        if init_place in t.in_places]
        
        if len(init_consumers) == 0:
            # First parallel operation - connect directly to init
            self.net.add_arc(init_place, transition)
        else:
            # Need to create/extend dup chain for parallel execution
            # Find the dup transition that feeds from init, or create one
            dup_trans = None
            for t in self.net.transitions.values():
                if t.name.startswith("dup_") and init_place in t.in_places:
                    dup_trans = t
                    break
            
            if dup_trans is None:
                # Create first dup: init -> dup -> {existing_consumer, new_transition}
                existing_consumer = init_consumers[0]
                
                # Remove arc from init to existing consumer
                self.net.arcs = [(src, tgt) for src, tgt in self.net.arcs 
                               if not (src == init_place.name and tgt == existing_consumer.name)]
                existing_consumer.in_places.remove(init_place)
                
                # Create dup outputs
                dup_out1, dup_out2 = self._create_dup_transition(init_place)
                
                # Connect existing consumer to first dup output
                self.net.add_arc(dup_out1, existing_consumer)
                
                # Connect new transition to second dup output
                self.net.add_arc(dup_out2, transition)
            else:
                # Extend existing dup chain - add another output
                # Create a new dup output place and connect the new transition
                new_dup_out = Place(f"dup_out_{len(self.net.places)}")
                self.net.add_place(new_dup_out)
                
                # Modify dup to have additional output
                dup_trans.out_places.append(new_dup_out)
                self.net.arcs.append((dup_trans.name, new_dup_out.name))
                
                # Update dup operation to produce more tokens
                num_outputs = len(dup_trans.out_places)
                dup_trans.operation = lambda tokens, n=num_outputs: [tokens[0]] * n
                
                # Connect new transition to new dup output
                self.net.add_arc(new_dup_out, transition)

    def _generate_label_assembly(self):
        """
        Generate assembly labels for all label places that have incoming transitions.
        This should be called after all operations are added to the net.
        """
        if not hasattr(self.net, 'labels'):
            return []
        
        assembly_lines = []
        for label_name, label_place in self.net.labels.items():
            # Always generate labels that exist in the registry
            # They will be referenced by goto/if-goto operations
            assembly_lines.append(f"({label_name})")
        
        return assembly_lines

    def _create_dup_transition(self, input_place):
        """
        Create a dup transition that takes 1 input and produces 2 outputs.
        Returns the two output places.
        """
        # Create dup transition
        dup_transition = Transition(
            name=f"dup_{len(self.net.transitions)}",
            operation=lambda tokens: [tokens[0], tokens[0]],  # Duplicate the token
            emit_function=self._emit_dup_assembly
        )
        self.net.add_transition(dup_transition)
        
        # Create output places
        dup_out1 = Place(f"dup_out1_{len(self.net.places)}")
        dup_out2 = Place(f"dup_out2_{len(self.net.places)}")
        self.net.add_place(dup_out1)
        self.net.add_place(dup_out2)
        
        # Connect: input_place -> dup -> {dup_out1, dup_out2}
        self.net.add_arc(input_place, dup_transition)
        self.net.add_arc(dup_transition, dup_out1)
        self.net.add_arc(dup_transition, dup_out2)
        
        return dup_out1, dup_out2

    def _create_dup_branch(self, new_transition):
        """
        Create a dup transition to enable branching when multiple operations
        need to consume from the same source.
        """
        # Always branch from init for operations that consume 0 from stack
        control_source = self.net.places["init"]
        
        # Find existing transitions that consume from the control source
        source_consumers = []
        for trans in self.net.transitions.values():
            if control_source in trans.in_places:
                source_consumers.append(trans)
        
        if len(source_consumers) == 1:
            # There's exactly one existing consumer - create dup to branch
            existing_transition = source_consumers[0]
            
            # Remove existing arc from source to existing transition
            self.net.arcs = [(src, tgt) for src, tgt in self.net.arcs 
                           if not (src == control_source.name and tgt == existing_transition.name)]
            existing_transition.in_places.remove(control_source)
            
            # Create dup transition using the helper method
            dup_out1, dup_out2 = self._create_dup_transition(control_source)
            
            # Connect existing transition to one dup output
            self.net.add_arc(dup_out1, existing_transition)
            
            # Connect new transition to other dup output
            self.net.add_arc(dup_out2, new_transition)
            
        elif len(source_consumers) > 1:
            # Multiple consumers already exist - connect to source directly
            self.net.add_arc(control_source, new_transition)
        else:
            # No existing consumers - connect directly
            self.net.add_arc(control_source, new_transition)

    def _emit_dup_assembly(self, transition):
        """
        Generate assembly code for dup transition.
        For control flow duplication, no actual data needs to be read or written.
        """
        assembly = []
        
        if len(transition.in_places) != 1 or len(transition.out_places) != 2:
            return ["// dup - invalid configuration"]
        
        input_place = transition.in_places[0]
        
        # If this is duplicating from init (control flow), no data movement needed
        if input_place.name == "init":
            assembly.append("// dup control token - no data movement needed")
            return assembly
        
        # Check if this is duplicating between dup output places (also control flow)
        if input_place.name.startswith("dup_out"):
            assembly.append("// dup control token - no data movement needed")
            return assembly
        
        # For other cases, read from input and write to outputs
        output_place1 = transition.out_places[0]
        output_place2 = transition.out_places[1]
        
        # Read from input place
        if input_place.memory_address is not None:
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
        else:
            assembly.append("// dup - input has no memory address")
            return assembly
        
        # Write to first output place
        if output_place1.memory_address is not None:
            assembly.append(f"@R{output_place1.memory_address}")
            assembly.append("M=D")
        
        # Write to second output place
        if output_place2.memory_address is not None:
            assembly.append(f"@R{output_place2.memory_address}")
            assembly.append("M=D")
        
        return assembly


    def label(self, vmc):
        """
        Implement label operation by creating a control flow place.
        
        The label place serves as a merge point - control can arrive here from:
        1. Normal sequential flow (previous operation)
        2. goto/if-goto jumps
        
        The next operation after this label will take this place as a control input.
        """
        label_name = vmc.segment  # The label name from the VM command
        
        # Scope label to current function to avoid collisions
        scoped_label = f"{self.current_function}${label_name}" if self.current_function else label_name
        
        # Check if label place already exists (from forward reference in goto/if-goto)
        if scoped_label in self.net.labels:
            # Reuse existing label place
            label_place = self.net.labels[scoped_label]
        else:
            # Create a new place to represent this label
            label_place_name = f"label_{scoped_label}"
            label_place = Place(label_place_name)
            label_place.label_name = scoped_label
            label_place.is_label = True
            self.net.add_place(label_place)
            
            # Store label in registry for goto/if-goto to find
            self.net.labels[scoped_label] = label_place
        
        # Connect current control flow to the label place
        # This allows sequential flow into the label
        if self.control_place is not None:
            # Create a pass-through transition to merge control flow
            # Must preserve call stack from input token
            def merge_operation(tokens):
                call_stack = []
                for t in tokens:
                    if hasattr(t, 'value'):
                        val = t.value
                        if isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                            call_stack = list(val[1])
                if call_stack:
                    return [Token(("callstack", call_stack))]
                else:
                    return [Token([])]
            
            merge_transition = Transition(
                name=f"merge_to_{scoped_label}_{len(self.net.transitions)}",
                operation=merge_operation
            )
            self.net.add_transition(merge_transition)
            self.net.add_arc(self.control_place, merge_transition)
            self.net.add_arc(merge_transition, label_place)
        
        # Set label as the current control place for next operation
        self.control_place = label_place
        
        # Return the place (no transition for labels)
        return label_place
        
    def goto(self, vmc):
        """
        Implement goto operation by creating a transition that outputs to the target label place.
        
        Instead of generating assembly jump instructions, goto puts a token in the target
        label's place, enabling whatever transition follows that label.
        """
        target_label = vmc.segment  # The target label name
        
        # Scope label to current function
        scoped_label = f"{self.current_function}${target_label}" if self.current_function else target_label
        
        # Find or create the label place
        if scoped_label not in self.net.labels:
            # Create the label place if it doesn't exist yet (forward reference)
            label_place = Place(f"label_{scoped_label}")
            label_place.label_name = scoped_label
            label_place.is_label = True
            self.net.add_place(label_place)
            self.net.labels[scoped_label] = label_place
        
        target_place = self.net.labels[scoped_label]
        
        # Create emit function for goto
        def emit_goto(transition):
            return ["// goto - control transfer via token"]
        
        # Create operation that preserves call stack
        def goto_operation(tokens):
            # Find call stack from tokens
            call_stack = []
            for t in tokens:
                if hasattr(t, 'value'):
                    val = t.value
                    if isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                        call_stack = list(val[1])
            
            # Create control token with call stack
            if call_stack:
                return [Token(("callstack", call_stack))]
            else:
                return [Token([])]
        
        # Create transition that transfers control to the label
        goto_transition = Transition(
            name=f"goto_{scoped_label}_{len(self.net.transitions)}",
            operation=goto_operation,
            emit_function=emit_goto
        )
        
        self.net.add_transition(goto_transition)
        
        # Connect from current control flow (if available)
        if self.control_place is not None:
            self.net.add_arc(self.control_place, goto_transition)
        else:
            # If no control place, connect from init (for standalone tests)
            self.net.add_arc(self.net.places["init"], goto_transition)
        
        # Output to the target label place
        self.net.add_arc(goto_transition, target_place)
        
        # After goto, create a dead control place for any unreachable code
        dead_place = Place(f"dead_{len(self.net.places)}")
        self.net.add_place(dead_place)
        self.control_place = dead_place
        
        return goto_transition
            
    def ifgoto(self, vmc):
        """
        Implement if-goto operation by creating a conditional control transfer.
        
        Pops one value from stack. If non-zero (true), puts token in target label place.
        If zero (false), control continues to the next instruction.
        
        This creates a branch in the Petri net with two possible outputs.
        """
        target_label = vmc.segment  # The target label name
        
        # Scope label to current function
        scoped_label = f"{self.current_function}${target_label}" if self.current_function else target_label
        
        # Find or create the label place
        if scoped_label not in self.net.labels:
            label_place = Place(f"label_{scoped_label}")
            label_place.label_name = scoped_label
            label_place.is_label = True
            self.net.add_place(label_place)
            self.net.labels[scoped_label] = label_place
        
        target_place = self.net.labels[scoped_label]
        
        # Create a "fall-through" place for when condition is false
        fallthrough_place = Place(f"ifgoto_fallthrough_{len(self.net.places)}")
        self.net.add_place(fallthrough_place)
        
        # Create emit function for if-goto
        def emit_ifgoto(transition):
            assembly = []
            assembly.append("// if-goto condition check")
            return assembly
        
        # Create operation that conditionally outputs to label OR fallthrough
        def ifgoto_operation(tokens):
            # Find the condition value and call stack from tokens
            condition = 0
            call_stack = []
            for t in tokens:
                if hasattr(t, 'value'):
                    val = t.value
                    if isinstance(val, int):
                        condition = val
                    elif isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                        call_stack = list(val[1])
                    elif isinstance(val, list):
                        # Empty control token
                        pass
            
            # Create control token with call stack
            if call_stack:
                ctrl_token = Token(("callstack", call_stack))
            else:
                ctrl_token = Token([])
            
            # If condition is non-zero, go to label; else fall through
            if condition != 0:
                return [ctrl_token, None]  # [target, fallthrough]
            else:
                return [None, ctrl_token]  # [target, fallthrough]
        
        # Create transition
        ifgoto_transition = Transition(
            name=f"ifgoto_{scoped_label}_{len(self.net.transitions)}",
            operation=ifgoto_operation,
            emit_function=emit_ifgoto
        )
        
        self.net.add_transition(ifgoto_transition)
        
        # Connect control flow input
        self.net.add_arc(self.control_place, ifgoto_transition)
        
        # If-goto consumes 1 from data stack (the condition)
        if len(self.control_stack) > 0:
            condition_place = self.control_stack.pop()
            self.net.add_arc(condition_place, ifgoto_transition)
        else:
            raise RuntimeError("Stack underflow: if-goto needs a condition value")
        
        # Output to both target label and fallthrough
        self.net.add_arc(ifgoto_transition, target_place)
        self.net.add_arc(ifgoto_transition, fallthrough_place)
        
        # Set fallthrough as the current control place for next instruction
        self.control_place = fallthrough_place
        
        return ifgoto_transition
                
    def function(self, vmc):
        """
        Implement function declaration by creating a function entry place.
        
        A function starts a NEW control flow - it's not connected to the previous
        sequential flow. Functions are only reachable via 'call'.
        
        Special case: Sys.init uses the 'init' place which has the starting token.
        """
        function_name = vmc.segment  # Function name
        n_locals = vmc.index        # Number of local variables
        
        # Capture for closure
        emitter = self
        num_locals = n_locals
        
        # Special case: Sys.init uses the init place (bootstrap entry point)
        if function_name == "Sys.init":
            function_place = self.net.places["init"]
            function_place.function_name = function_name
            function_place.n_locals = n_locals
            function_place.is_function = True
        else:
            # Check if place already exists (created by a forward call reference)
            function_place_name = f"function_{function_name}"
            if function_place_name in self.net.places:
                # Reuse existing place (created by call before function definition)
                function_place = self.net.places[function_place_name]
            else:
                # Create a new place to represent this function entry point
                function_place = Place(function_place_name)
                self.net.add_place(function_place)
            
            function_place.function_name = function_name
            function_place.n_locals = n_locals
            function_place.is_function = True
        
        # Store function in a registry for call to find
        if not hasattr(self.net, 'functions'):
            self.net.functions = {}
        self.net.functions[function_name] = function_place
        
        # Track current function for label scoping
        self.current_function = function_name
        
        # If function has locals, create a transition to allocate them
        if n_locals > 0:
            # Create transition that initializes local variables to 0
            def init_locals_operation(tokens):
                # Allocate space for locals by advancing SP
                if emitter.memory_write:
                    sp = emitter.read_memory(0)
                    # Initialize locals to 0
                    for i in range(num_locals):
                        emitter.write_memory(sp + i, 0)
                    # Advance SP
                    emitter.write_memory(0, sp + num_locals)
                
                # Pass through the control token
                for t in tokens:
                    if hasattr(t, 'value'):
                        val = t.value
                        if isinstance(val, tuple) and val[0] == "callstack":
                            return [Token(val)]
                        if isinstance(val, list):
                            return [Token(val)]
                return [Token([])]
            
            init_locals_trans = Transition(
                name=f"init_locals_{function_name}",
                operation=init_locals_operation
            )
            self.net.add_transition(init_locals_trans)
            
            # Create output place for after locals init
            locals_done_place = Place(f"locals_done_{function_name}")
            self.net.add_place(locals_done_place)
            
            self.net.add_arc(function_place, init_locals_trans)
            self.net.add_arc(init_locals_trans, locals_done_place)
            
            # Control continues from locals_done_place
            self.control_place = locals_done_place
        else:
            # No locals, control continues from function_place
            self.control_place = function_place
        
        # Clear the data stack for this function (functions start with empty stack)
        self.control_stack = []
        
        return function_place
            
    def call(self, vmc):
        """
        Implement function call using token-based call stack.
        
        The token flowing through a function carries the call stack as its value.
        - call pushes the return address onto the token's stack
        - return pops from the token's stack to route back
        
        Token value is a list: [return_addr_n, return_addr_n-1, ..., return_addr_0]
        (most recent call at index 0)
        """
        function_name = vmc.segment
        n_args = vmc.index
        
        # Create call site ID
        call_id = self.call_counter
        self.call_counter += 1
        
        # Find or create the function entry place
        if not hasattr(self.net, 'functions'):
            self.net.functions = {}
        
        func_place_name = f"function_{function_name}"
        if func_place_name not in self.net.places:
            func_place = Place(func_place_name)
            func_place.function_name = function_name
            func_place.is_function = True
            self.net.add_place(func_place)
            self.net.functions[function_name] = func_place
        
        target_func_place = self.net.places[func_place_name]
        
        # Capture emitter and call info for frame setup
        emitter = self
        num_args = n_args
        
        # Create call transition that sets up new frame and pushes return address
        cid = call_id
        fname = function_name  # Capture for debugging
        def call_operation(tokens, return_id=cid):
            # Get current call stack from input token (or start fresh)
            current_stack = []
            arg_values = []
            
            for t in tokens:
                if hasattr(t, 'value'):
                    val = t.value
                    # Call stack is a tuple: ("callstack", [addresses...])
                    if isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                        current_stack = list(val[1])
                    elif isinstance(val, list):
                        # This is a control token (empty list), ignore it
                        pass
                    elif isinstance(val, int):
                        arg_values.append(val)
                    elif isinstance(val, str):
                        # Symbolic value - treat as 0
                        arg_values.append(0)
                    else:
                        # Unknown type - treat as 0
                        arg_values.append(0)
            
            # If callbacks present, set up a new frame using SP
            if emitter.memory_write:
                # Standard Hack VM call sequence:
                # Arguments are passed via tokens, we write them to stack
                # Then push saved frame, set ARG and LCL
                sp = emitter.read_memory(0)  # Current stack pointer
                
                # Arguments come in reverse order (last pushed = first in tokens)
                # Reverse to get correct order for ARG segment
                arg_values = arg_values[::-1]
                
                # Write arguments to stack at current SP
                arg_base = sp
                for i, arg_val in enumerate(arg_values):
                    emitter.write_memory(sp + i, arg_val)
                sp += len(arg_values)
                
                # Push saved frame (5 words)
                emitter.write_memory(sp, return_id)                    # return address
                emitter.write_memory(sp + 1, emitter.read_memory(1))   # saved LCL
                emitter.write_memory(sp + 2, emitter.read_memory(2))   # saved ARG
                emitter.write_memory(sp + 3, emitter.read_memory(3))   # saved THIS
                emitter.write_memory(sp + 4, emitter.read_memory(4))   # saved THAT
                sp += 5
                
                # Set new frame pointers
                emitter.write_memory(2, arg_base)    # ARG = base of arguments
                emitter.write_memory(1, sp)          # LCL = current SP (start of locals)
                emitter.write_memory(0, sp)          # SP = LCL (function will add locals)
            
            # Push return address onto call stack token
            current_stack.insert(0, return_id)
            # Use tuple format to distinguish from control tokens
            return [Token(("callstack", current_stack))]
        
        call_transition = Transition(
            name=f"call_{function_name}_{call_id}",
            operation=call_operation
        )
        
        self.net.add_transition(call_transition)
        
        # Connect control flow
        if self.control_place is not None:
            self.net.add_arc(self.control_place, call_transition)
        
        # Consume arguments from stack
        for i in range(n_args):
            if self.control_stack:
                arg_place = self.control_stack.pop()
                self.net.add_arc(arg_place, call_transition)
        
        # Output to function entry place
        self.net.add_arc(call_transition, target_func_place)
        
        # Create separate places for control flow and return value
        return_ctrl_place = Place(f"return_ctrl_{call_id}")
        return_data_place = Place(f"return_data_{call_id}")
        self.net.add_place(return_ctrl_place)
        self.net.add_place(return_data_place)
        
        # Store both places for dispatch to use
        self.call_sites[call_id] = (return_ctrl_place, return_data_place)
        
        # Control continues from return_ctrl_place
        self.control_place = return_ctrl_place
        
        # Return value comes from return_data_place
        self.control_stack.append(return_data_place)
        
        return call_transition
            
    def ret(self, vmc):
        """
        Implement return from function.
        
        Pops the return address from the call stack (token value) and sends
        the return value + remaining call stack to the dispatch.
        The dispatch routes to the correct return place.
        """
        # Capture emitter for frame restoration
        emitter = self
        
        # Create transition that sends to dispatch
        def return_operation(tokens):
            # Find the call stack and return value from tokens
            call_stack = []
            ret_val = 0
            
            for t in tokens:
                if hasattr(t, 'value'):
                    val = t.value
                    # Call stack is a tuple: ("callstack", [addresses...])
                    if isinstance(val, tuple) and len(val) == 2 and val[0] == "callstack":
                        call_stack = list(val[1])
                    elif isinstance(val, list):
                        # Empty control token, ignore
                        pass
                    elif isinstance(val, int):
                        ret_val = val
            
            # If callbacks present, restore the caller's frame
            if emitter.memory_write:
                # Standard Hack VM return sequence:
                # FRAME = LCL, RET = *(FRAME-5), *ARG = pop(), SP = ARG+1
                # Restore THAT, THIS, ARG, LCL from saved frame
                
                lcl = emitter.read_memory(1)   # FRAME
                arg = emitter.read_memory(2)   # ARG (where return value goes)
                
                # Saved frame is at FRAME - 5
                frame = lcl
                saved_lcl = emitter.read_memory(frame - 4)
                saved_arg = emitter.read_memory(frame - 3)
                saved_this = emitter.read_memory(frame - 2)
                saved_that = emitter.read_memory(frame - 1)
                
                # Put return value at ARG[0]
                emitter.write_memory(arg, ret_val)
                
                # Restore SP to ARG + 1
                emitter.write_memory(0, arg + 1)
                
                # Restore frame pointers
                emitter.write_memory(4, saved_that)
                emitter.write_memory(3, saved_this)
                emitter.write_memory(2, saved_arg)
                emitter.write_memory(1, saved_lcl)
            
            # Pop return address from call stack
            if call_stack:
                return_addr = call_stack[0]
                remaining_stack = call_stack[1:]
            else:
                return_addr = -1  # No return address (shouldn't happen)
                remaining_stack = []
            
            # Return tuple: (return_value, return_address, remaining_call_stack)
            return [Token((ret_val, return_addr, remaining_stack))]
        
        return_transition = Transition(
            name=f"return_{len(self.net.transitions)}",
            operation=return_operation
        )
        
        self.net.add_transition(return_transition)
        
        # Connect control flow
        if self.control_place is not None:
            self.net.add_arc(self.control_place, return_transition)
        
        # Consume return value from stack
        if self.control_stack:
            ret_val_place = self.control_stack.pop()
            self.net.add_arc(ret_val_place, return_transition)
        
        # Output to dispatch
        self.net.add_arc(return_transition, self.return_dispatch)
        
        # After return, create a dead control place for unreachable code
        dead_place = Place(f"dead_{len(self.net.places)}")
        self.net.add_place(dead_place)
        self.control_place = dead_place
        
        return return_transition


    def add(self, vmc):
        """
        Implement add operation by creating a transition that consumes two values
        from the stack and produces their sum.
        """
        # Create a place to hold the result
        result_place_name = f"add_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for add operation
        def emit_add(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// add - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// add - first operand has no memory address")
                return assembly
            
            # Add second operand to D register
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D+M")
            else:
                assembly.append("// add - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the addition
        def add_operation(tokens):
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic, return symbolic result
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"add({val1},{val0})")]
            
            return [Token(val1 + val0)]
        
        add_transition = Transition(
            name=f"add_{len(self.net.transitions)}",
            operation=add_operation,
            emit_function=emit_add
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(add_transition, result_place, consumes_stack=2, produces_stack=1)

    def sub(self, vmc):
        """
        Implement sub operation by creating a transition that consumes two values
        from the stack and produces their difference (second operand - first operand).
        """
        # Create a place to hold the result
        result_place_name = f"sub_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for sub operation
        def emit_sub(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// sub - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// sub - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// sub - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the subtraction
        def sub_operation(tokens):
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic, return symbolic result
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"sub({val1},{val0})")]
            
            return [Token(val1 - val0)]
        
        sub_transition = Transition(
            name=f"sub_{len(self.net.transitions)}",
            operation=sub_operation,
            emit_function=emit_sub
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(sub_transition, result_place, consumes_stack=2, produces_stack=1)

    def neg(self, vmc):
        """
        Implement neg operation by creating a transition that consumes one value
        from the stack and produces its negation (-value).
        """
        # Create a place to hold the result
        result_place_name = f"neg_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for neg operation
        def emit_neg(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// neg - invalid input configuration"]
            
            input_place = data_places[0]
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load operand into D register
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// neg - operand has no memory address")
                return assembly
            
            # Negate D register (D = -D)
            assembly.append("D=-D")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the negation
        def neg_operation(tokens):
            val = tokens[0].value
            
            # If value is symbolic, return symbolic result
            if isinstance(val, str):
                return [Token(f"neg({val})")]
            
            return [Token(-val)]
        
        neg_transition = Transition(
            name=f"neg_{len(self.net.transitions)}",
            operation=neg_operation,
            emit_function=emit_neg
        )
        
        # Use the general method to add this operation (consumes 1, produces 1)
        return self._insert_operation(neg_transition, result_place, consumes_stack=1, produces_stack=1)

    def lt(self, vmc):
        """
        Implement lt (less than) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if second operand < first operand, 0 (false) otherwise.
        Stack semantics: second_operand < first_operand
        """
        # Create a place to hold the result
        result_place_name = f"lt_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for lt operation
        def emit_lt(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// lt - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// lt - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// lt - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"LT_TRUE_{id(transition)}"
            end_label = f"LT_END_{id(transition)}"
            
            # Jump to true label if D < 0 (second_operand < first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JLT")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the less than comparison
        def lt_operation(tokens):
            # Handle symbolic tokens (from memory segment operations)
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic (string), return a symbolic result
            # The actual comparison happens in assembly execution
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"lt({val1},{val0})")]
            
            # Both values are numeric - perform the comparison
            return [Token(-1 if val1 < val0 else 0)]
        
        lt_transition = Transition(
            name=f"lt_{len(self.net.transitions)}",
            operation=lt_operation,
            emit_function=emit_lt
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(lt_transition, result_place, consumes_stack=2, produces_stack=1)

    def eq(self, vmc):
        """
        Implement eq (equals) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if they are equal, 0 (false) otherwise.
        Stack semantics: second_operand == first_operand
        """
        # Create a place to hold the result
        result_place_name = f"eq_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for eq operation
        def emit_eq(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// eq - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// eq - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// eq - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"EQ_TRUE_{len(transition.out_places)}_{id(transition)}"
            end_label = f"EQ_END_{len(transition.out_places)}_{id(transition)}"
            
            # Jump to true label if D == 0 (second_operand == first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JEQ")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the equality comparison
        def eq_operation(tokens):
            # Handle symbolic tokens (from memory segment operations)
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic (string), return a symbolic result
            # The actual comparison happens in assembly execution
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"eq({val1},{val0})")]
            
            # Both values are numeric - perform the comparison
            return [Token(-1 if val1 == val0 else 0)]
        
        eq_transition = Transition(
            name=f"eq_{len(self.net.transitions)}",
            operation=eq_operation,
            emit_function=emit_eq
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(eq_transition, result_place, consumes_stack=2, produces_stack=1)

    def gt(self, vmc):
        """
        Implement gt (greater than) operation by creating a transition that consumes two values
        from the stack and produces -1 (true) if second operand > first operand, 0 (false) otherwise.
        Stack semantics: second_operand > first_operand
        """
        # Create a place to hold the result
        result_place_name = f"gt_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for gt operation
        def emit_gt(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// gt - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// gt - first operand has no memory address")
                return assembly
            
            # Subtract second operand (top of stack) from D register
            # D = second_operand - first_operand
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D-M")
            else:
                assembly.append("// gt - second operand has no memory address")
                return assembly
            
            # Generate unique labels for this comparison
            true_label = f"GT_TRUE_{id(transition)}"
            end_label = f"GT_END_{id(transition)}"
            
            # Jump to true label if D > 0 (second_operand > first_operand)
            assembly.append(f"@{true_label}")
            assembly.append("D;JGT")
            
            # False case: set D = 0
            assembly.append("D=0")
            assembly.append(f"@{end_label}")
            assembly.append("0;JMP")
            
            # True case: set D = -1
            assembly.append(f"({true_label})")
            assembly.append("D=-1")
            
            # End label
            assembly.append(f"({end_label})")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the greater than comparison
        def gt_operation(tokens):
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic, return symbolic result
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"gt({val1},{val0})")]
            
            return [Token(-1 if val1 > val0 else 0)]
        
        gt_transition = Transition(
            name=f"gt_{len(self.net.transitions)}",
            operation=gt_operation,
            emit_function=emit_gt
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(gt_transition, result_place, consumes_stack=2, produces_stack=1)

    def and_op(self, vmc):
        """
        Implement and (bitwise AND) operation by creating a transition that consumes two values
        from the stack and produces their bitwise AND result.
        Stack semantics: second_operand & first_operand
        """
        # Create a place to hold the result
        result_place_name = f"and_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for and operation
        def emit_and(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// and - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// and - first operand has no memory address")
                return assembly
            
            # Perform bitwise AND with second operand (top of stack)
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D&M")
            else:
                assembly.append("// and - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise AND
        def and_operation(tokens):
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic, return symbolic result
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"and({val1},{val0})")]
            
            return [Token(val1 & val0)]
        
        and_transition = Transition(
            name=f"and_{len(self.net.transitions)}",
            operation=and_operation,
            emit_function=emit_and
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(and_transition, result_place, consumes_stack=2, produces_stack=1)

    def or_op(self, vmc):
        """
        Implement or (bitwise OR) operation by creating a transition that consumes two values
        from the stack and produces their bitwise OR result.
        Stack semantics: second_operand | first_operand
        """
        # Create a place to hold the result
        result_place_name = f"or_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for or operation
        def emit_or(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 2:
                return ["// or - invalid input configuration"]
            
            input_place1 = data_places[0]  # Second operand (top of stack)
            input_place2 = data_places[1]  # First operand (second from top)
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load first operand (second from top) into D register
            if input_place2.memory_address is not None:
                assembly.append(f"@R{input_place2.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// or - first operand has no memory address")
                return assembly
            
            # Perform bitwise OR with second operand (top of stack)
            if input_place1.memory_address is not None:
                assembly.append(f"@R{input_place1.memory_address}")
                assembly.append("D=D|M")
            else:
                assembly.append("// or - second operand has no memory address")
                return assembly
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise OR
        def or_operation(tokens):
            val0 = tokens[0].value
            val1 = tokens[1].value
            
            # If either value is symbolic, return symbolic result
            if isinstance(val0, str) or isinstance(val1, str):
                return [Token(f"or({val1},{val0})")]
            
            return [Token(val1 | val0)]
        
        or_transition = Transition(
            name=f"or_{len(self.net.transitions)}",
            operation=or_operation,
            emit_function=emit_or
        )
        
        # Use the general method to add this operation (consumes 2, produces 1)
        return self._insert_operation(or_transition, result_place, consumes_stack=2, produces_stack=1)

    def not_op(self, vmc):
        """
        Implement not (bitwise NOT) operation by creating a transition that consumes one value
        from the stack and produces its bitwise NOT result (~value).
        """
        # Create a place to hold the result
        result_place_name = f"not_result_{len(self.net.places)}"
        result_place = Place(result_place_name)
        self.net.add_place(result_place)
        
        # Create emit function for not operation
        def emit_not(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// not - invalid input configuration"]
            
            input_place = data_places[0]
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load operand into D register
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// not - operand has no memory address")
                return assembly
            
            # Perform bitwise NOT (D = !D)
            assembly.append("D=!D")
            
            # Store result in output place
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
            
            return assembly
        
        # Create transition that performs the bitwise NOT
        def not_operation(tokens):
            val = tokens[0].value
            
            # If value is symbolic, return symbolic result
            if isinstance(val, str):
                return [Token(f"not({val})")]
            
            return [Token(~val)]
        
        not_transition = Transition(
            name=f"not_{len(self.net.transitions)}",
            operation=not_operation,
            emit_function=emit_not
        )
        
        # Use the general method to add this operation (consumes 1, produces 1)
        return self._insert_operation(not_transition, result_place, consumes_stack=1, produces_stack=1)

    def push_constant(self, vmc):
        """
        Implement push constant operation by creating a place for the constant
        and a transition that produces it.
        """
        constant_value = vmc.index
        
        # Create a place to hold the constant value
        constant_place_name = f"const_{constant_value}_{len(self.net.places)}"
        constant_place = Place(constant_place_name)
        self.net.add_place(constant_place)
        
        # Create emit function for push constant
        def emit_push_constant(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load constant value into D register
            assembly.append(f"@{constant_value}")
            assembly.append("D=A")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Create transition that produces the constant
        # Only produce the data token - _insert_operation adds the control token
        push_const_transition = Transition(
            name=f"push_const_{constant_value}_{len(self.net.transitions)}",
            operation=lambda tokens, cv=constant_value: [Token(cv)],
            emit_function=emit_push_constant
        )
        
        # Use the general method to add this operation (pushes 1 item to stack)
        return self._insert_operation(push_const_transition, constant_place, consumes_stack=0, produces_stack=1)

    def push_local(self, vmc):
        """Handle push local command - pushes local[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the local value
        local_place = Place(f"local_{index}_{len(self.net.places)}")
        self.net.add_place(local_place)
        
        # Create emit function for push local
        def emit_push_local(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load local[index] into D register
            assembly.append("@LCL")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        local_index = index
        
        # Create transition that pushes the local value - reads from RAM[LCL + index]
        def push_local_operation(tokens):
            if emitter.memory_read:
                lcl_ptr = emitter.read_memory(1)  # LCL is at RAM[1]
                addr = lcl_ptr + local_index
                value = emitter.read_memory(addr)
                return [Token(value)]
            else:
                return [Token(f"local[{local_index}]")]
        
        push_local_transition = Transition(
            name=f"push_local_{index}_{len(self.net.transitions)}",
            operation=push_local_operation,
            emit_function=emit_push_local
        )
        
        return self._insert_operation(push_local_transition, local_place, consumes_stack=0, produces_stack=1)

    def push_argument(self, vmc):
        """Handle push argument command - pushes argument[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the argument value
        arg_place = Place(f"arg_{index}_{len(self.net.places)}")
        self.net.add_place(arg_place)
        
        # Create emit function for push argument
        def emit_push_argument(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load argument[index] into D register
            assembly.append("@ARG")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        arg_index = index
        
        # Create transition that pushes the argument value
        def push_arg_operation(tokens):
            # If callbacks present, read actual memory; otherwise symbolic
            if emitter.memory_read:
                arg_ptr = emitter.read_memory(2)  # ARG is at RAM[2]
                value = emitter.read_memory(arg_ptr + arg_index)
                return [Token(value)]
            else:
                return [Token(f"argument[{arg_index}]")]
        
        push_arg_transition = Transition(
            name=f"push_arg_{index}_{len(self.net.transitions)}",
            operation=push_arg_operation,
            emit_function=emit_push_argument
        )
        
        return self._insert_operation(push_arg_transition, arg_place, consumes_stack=0, produces_stack=1)

    def push_this(self, vmc):
        """Handle push this command - pushes this[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the this value
        this_place = Place(f"this_{index}_{len(self.net.places)}")
        self.net.add_place(this_place)
        
        # Create emit function for push this
        def emit_push_this(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load this[index] into D register
            assembly.append("@THIS")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        this_index = index
        
        # Create transition that pushes the this value
        def push_this_operation(tokens):
            if emitter.memory_read:
                this_ptr = emitter.read_memory(3)  # THIS is at RAM[3]
                value = emitter.read_memory(this_ptr + this_index)
                return [Token(value)]
            else:
                return [Token(f"this[{this_index}]")]
        
        push_this_transition = Transition(
            name=f"push_this_{index}_{len(self.net.transitions)}",
            operation=push_this_operation,
            emit_function=emit_push_this
        )
        
        return self._insert_operation(push_this_transition, this_place, consumes_stack=0, produces_stack=1)

    def push_that(self, vmc):
        """Handle push that command - pushes that[index] onto stack"""
        index = vmc.index
        
        # Create a place to hold the that value
        that_place = Place(f"that_{index}_{len(self.net.places)}")
        self.net.add_place(that_place)
        
        # Create emit function for push that
        def emit_push_that(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load that[index] into D register
            assembly.append("@THAT")
            assembly.append("D=M")
            assembly.append(f"@{index}")
            assembly.append("A=D+A")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        that_index = index
        
        # Create transition that pushes the that value - actually reads from memory
        def push_that_operation(tokens):
            if emitter.memory_read:
                # Calculate source address: THAT + index
                that_ptr = emitter.read_memory(4)  # THAT is at RAM[4]
                addr = that_ptr + that_index
                
                # Read from memory (this triggers callback for keyboard reads)
                value = emitter.read_memory(addr)
                return [Token(value)]
            else:
                return [Token(f"that[{that_index}]")]
        
        push_that_transition = Transition(
            name=f"push_that_{index}_{len(self.net.transitions)}",
            operation=push_that_operation,
            emit_function=emit_push_that
        )
        
        return self._insert_operation(push_that_transition, that_place, consumes_stack=0, produces_stack=1)

    def push_pointer(self, vmc):
        """Handle push pointer command - pushes THIS (0) or THAT (1) pointer"""
        index = vmc.index
        
        # Create a place to hold the pointer value
        pointer_place = Place(f"pointer_{index}_{len(self.net.places)}")
        self.net.add_place(pointer_place)
        
        # Create emit function for push pointer
        def emit_push_pointer(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load pointer (THIS or THAT) into D register
            if index == 0:
                assembly.append("@THIS")
            elif index == 1:
                assembly.append("@THAT")
            else:
                assembly.append(f"// Invalid pointer index: {index}")
                return assembly
            
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        ptr_index = index
        
        # Create transition that pushes the pointer value - reads from RAM[3] or RAM[4]
        def push_pointer_operation(tokens):
            if emitter.memory_read:
                addr = 3 if ptr_index == 0 else 4  # THIS=3, THAT=4
                value = emitter.read_memory(addr)
                return [Token(value)]
            else:
                return [Token(f"pointer[{ptr_index}]")]
        
        push_pointer_transition = Transition(
            name=f"push_pointer_{index}_{len(self.net.transitions)}",
            operation=push_pointer_operation,
            emit_function=emit_push_pointer
        )
        
        return self._insert_operation(push_pointer_transition, pointer_place, consumes_stack=0, produces_stack=1)

    def push_temp(self, vmc):
        """Handle push temp command - pushes temp[index] (R5-R12)"""
        index = vmc.index
        
        # Create a place to hold the temp value
        temp_place = Place(f"temp_{index}_{len(self.net.places)}")
        self.net.add_place(temp_place)
        
        # Create emit function for push temp
        def emit_push_temp(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load temp[index] (R5+index) into D register
            temp_address = 5 + index
            assembly.append(f"@R{temp_address}")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        temp_index = index
        
        # Create transition that pushes the temp value - actually reads from RAM[5+index]
        def push_temp_operation(tokens):
            if emitter.memory_read:
                addr = 5 + temp_index
                value = emitter.read_memory(addr)
                return [Token(value)]
            else:
                return [Token(f"temp[{temp_index}]")]
        
        push_temp_transition = Transition(
            name=f"push_temp_{index}_{len(self.net.transitions)}",
            operation=push_temp_operation,
            emit_function=emit_push_temp
        )
        
        return self._insert_operation(push_temp_transition, temp_place, consumes_stack=0, produces_stack=1)

    def push_static(self, vmc):
        """Handle push static command - pushes static variable"""
        index = vmc.index
        
        # Get the scoped static address for this class
        static_addr = self._get_static_address(index)
        
        # Create a place to hold the static value
        static_place = Place(f"static_{index}_{len(self.net.places)}")
        self.net.add_place(static_place)
        
        # Create emit function for push static
        def emit_push_static(transition):
            assembly = []
            output_place = transition.out_places[0] if transition.out_places else None
            
            # Load static variable into D register
            # Static variables are typically named ClassName.index
            assembly.append(f"@Static.{index}")
            assembly.append("D=M")
            
            # Store in output place memory location
            if output_place and output_place.memory_address is not None:
                assembly.append(f"@R{output_place.memory_address}")
                assembly.append("M=D")
                
            return assembly
        
        # Capture emitter and address for memory access
        emitter = self
        addr = static_addr
        
        # Create transition that pushes the static value - reads from scoped address
        def push_static_operation(tokens):
            if emitter.memory_read:
                value = emitter.read_memory(addr)
                return [Token(value)]
            else:
                return [Token(f"static[{index}]")]
        
        push_static_transition = Transition(
            name=f"push_static_{index}_{len(self.net.transitions)}",
            operation=push_static_operation,
            emit_function=emit_push_static
        )
        
        return self._insert_operation(push_static_transition, static_place, consumes_stack=0, produces_stack=1)

    def pop_local(self, vmc):
        """Handle pop local command - pops stack top to local[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_local_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop local
        def emit_pop_local(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop local - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop local - input has no memory address")
                return assembly
            
            # Store to local[index] - need two-step addressing
            assembly.append("@LCL")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = LCL + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of local[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to local[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        local_index = index
        
        # Create transition that pops to local - writes to RAM[LCL + index]
        def pop_local_operation(tokens):
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str):
                value = 0
            
            lcl_ptr = emitter.read_memory(1)  # LCL is at RAM[1]
            addr = lcl_ptr + local_index
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_local_transition = Transition(
            name=f"pop_local_{index}_{len(self.net.transitions)}",
            operation=pop_local_operation,
            emit_function=emit_pop_local
        )
        
        return self._insert_operation(pop_local_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_argument(self, vmc):
        """Handle pop argument command - pops stack top to argument[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_arg_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop argument
        def emit_pop_argument(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop argument - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop argument - input has no memory address")
                return assembly
            
            # Store to argument[index] - need two-step addressing
            assembly.append("@ARG")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = ARG + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of argument[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to argument[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        arg_index = index
        
        # Create transition that pops to argument - actually writes to memory
        def pop_arg_operation(tokens):
            # Get the value from input token
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str) or isinstance(value, tuple):
                value = 0
            
            # Calculate target address: ARG + index
            arg_ptr = emitter.read_memory(2)  # ARG is at RAM[2]
            addr = arg_ptr + arg_index
            
            # Write to memory
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_arg_transition = Transition(
            name=f"pop_arg_{index}_{len(self.net.transitions)}",
            operation=pop_arg_operation,
            emit_function=emit_pop_argument
        )
        
        return self._insert_operation(pop_arg_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_this(self, vmc):
        """Handle pop this command - pops stack top to this[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_this_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop this
        def emit_pop_this(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop this - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop this - input has no memory address")
                return assembly
            
            # Store to this[index] - need two-step addressing
            assembly.append("@THIS")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = THIS + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of this[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to this[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        this_index = index
        
        # Create transition that pops to this - actually writes to memory
        def pop_this_operation(tokens):
            # Get the value from input token
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str) or isinstance(value, tuple):
                value = 0
            
            # Calculate target address: THIS + index
            this_ptr = emitter.read_memory(3)  # THIS is at RAM[3]
            addr = this_ptr + this_index
            
            # Write to memory
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_this_transition = Transition(
            name=f"pop_this_{index}_{len(self.net.transitions)}",
            operation=pop_this_operation,
            emit_function=emit_pop_this
        )
        
        return self._insert_operation(pop_this_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_that(self, vmc):
        """Handle pop that command - pops stack top to that[index]"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_that_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop that
        def emit_pop_that(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop that - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop that - input has no memory address")
                return assembly
            
            # Store to that[index] - need two-step addressing
            assembly.append("@THAT")
            assembly.append("A=M")
            assembly.append(f"@{index}")
            assembly.append("D=A+D")  # D = THAT + index
            assembly.append("@R13")   # Use R13 as temp
            assembly.append("M=D")    # R13 = address of that[index]
            
            # Get the value to store (already in D from input place)
            assembly.append(f"@R{input_place.memory_address}")
            assembly.append("D=M")
            
            # Store to that[index]
            assembly.append("@R13")
            assembly.append("A=M")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter reference and index for memory access
        emitter = self
        that_index = index
        
        # Create transition that pops to that - actually writes to memory
        def pop_that_operation(tokens):
            # Get the value from input token
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str):
                value = 0  # Symbolic values become 0
            
            # Calculate target address: THAT + index
            that_ptr = emitter.read_memory(4)  # THAT is at RAM[4]
            addr = that_ptr + that_index
            
            # Write to memory (this triggers the callback for screen writes)
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_that_transition = Transition(
            name=f"pop_that_{index}_{len(self.net.transitions)}",
            operation=pop_that_operation,
            emit_function=emit_pop_that
        )
        
        return self._insert_operation(pop_that_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_pointer(self, vmc):
        """Handle pop pointer command - pops stack top to THIS (0) or THAT (1) pointer"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_pointer_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop pointer
        def emit_pop_pointer(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop pointer - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop pointer - input has no memory address")
                return assembly
            
            # Store to pointer (THIS or THAT)
            if index == 0:
                assembly.append("@THIS")
            elif index == 1:
                assembly.append("@THAT")
            else:
                assembly.append(f"// Invalid pointer index: {index}")
                return assembly
            
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        ptr_index = index
        
        # Create transition that pops to pointer - actually writes to RAM[3] or RAM[4]
        def pop_pointer_operation(tokens):
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str):
                value = 0
            
            # THIS is RAM[3], THAT is RAM[4]
            addr = 3 if ptr_index == 0 else 4
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_pointer_transition = Transition(
            name=f"pop_pointer_{index}_{len(self.net.transitions)}",
            operation=pop_pointer_operation,
            emit_function=emit_pop_pointer
        )
        
        return self._insert_operation(pop_pointer_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_temp(self, vmc):
        """Handle pop temp command - pops stack top to temp[index] (R5-R12)"""
        index = vmc.index
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_temp_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop temp
        def emit_pop_temp(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop temp - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop temp - input has no memory address")
                return assembly
            
            # Store to temp[index] (R5+index)
            temp_address = 5 + index
            assembly.append(f"@R{temp_address}")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and index for memory access
        emitter = self
        temp_index = index
        
        # Create transition that pops to temp - actually writes to RAM[5+index]
        def pop_temp_operation(tokens):
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            if isinstance(value, str):
                value = 0
            
            # temp[index] is at RAM[5+index]
            addr = 5 + temp_index
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_temp_transition = Transition(
            name=f"pop_temp_{index}_{len(self.net.transitions)}",
            operation=pop_temp_operation,
            emit_function=emit_pop_temp
        )
        
        return self._insert_operation(pop_temp_transition, pop_result_place, consumes_stack=1, produces_stack=0)

    def pop_static(self, vmc):
        """Handle pop static command - pops stack top to static variable"""
        index = vmc.index
        
        # Get the scoped static address for this class
        static_addr = self._get_static_address(index)
        
        # Create a place to represent the pop operation result
        pop_result_place = Place(f"pop_static_{index}_{len(self.net.places)}")
        self.net.add_place(pop_result_place)
        
        # Create emit function for pop static
        def emit_pop_static(transition):
            assembly = []
            
            # Get data input places (filter out control places)
            data_places = PetriEmitter._get_data_places(transition.in_places)
            if len(data_places) != 1:
                return ["// pop static - invalid input configuration"]
            
            input_place = data_places[0]
            
            # Load value from input place
            if input_place.memory_address is not None:
                assembly.append(f"@R{input_place.memory_address}")
                assembly.append("D=M")
            else:
                assembly.append("// pop static - input has no memory address")
                return assembly
            
            # Store to static variable
            # Static variables are typically named ClassName.index
            assembly.append(f"@Static.{index}")
            assembly.append("M=D")
            
            return assembly
        
        # Capture emitter and address for memory access
        emitter = self
        addr = static_addr
        
        # Create transition that pops to static - writes to scoped address
        def pop_static_operation(tokens):
            value = tokens[0].value if hasattr(tokens[0], 'value') else 0
            # Handle symbolic or tuple values
            if isinstance(value, str) or isinstance(value, tuple):
                value = 0
            
            emitter.write_memory(addr, value)
            
            return [None]  # Pop doesn't produce a data value
        
        pop_static_transition = Transition(
            name=f"pop_static_{index}_{len(self.net.transitions)}",
            operation=pop_static_operation,
            emit_function=emit_pop_static
        )
        
        return self._insert_operation(pop_static_transition, pop_result_place, consumes_stack=1, produces_stack=0)