"""
VM to Petri Net Translator
Translates VM commands into Petri net fragments following the six primitives:
source, choice, dup, drop, join, loop

Pure Petri-net semantics - no stack needed. Places ARE the data flow.
"""

from .net import PetriNet
from .Token import Token

class VMToPetriTranslator:
    def __init__(self):
        self.net = PetriNet()
        self.result_places = []  # Final output places (what would be "top of stack")
        self.place_counter = 0
        self.transition_counter = 0
        
    def get_unique_place_name(self, prefix="place"):
        self.place_counter += 1
        return f"{prefix}_{self.place_counter}"
        
    def get_unique_transition_name(self, prefix="trans"):
        self.transition_counter += 1
        return f"{prefix}_{self.transition_counter}"
        
    def push_constant(self, value):
        """
        Implement push constant using 'source' primitive
        Creates a new place with the constant value - this IS the stack element
        """
        # Create a new place for this constant (source primitive)
        const_place = self.net.add_place(self.get_unique_place_name(f"const_{value}"))
        const_place.put_token(Token(value))
        
        # This place represents the value - add to results
        self.result_places.append(const_place)
        
        return const_place
        
    def add_operation(self):
        """
        Implement add operation: consume two most recent result places,
        create add transition, produce new result place
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for add operation")
            
        # Pop two operands from result places (most recent = top of conceptual stack)
        b_place = self.result_places.pop()  # Top 
        a_place = self.result_places.pop()  # Second from top
        
        # Create result place for the sum
        result_place = self.net.add_place(self.get_unique_place_name("add_result"))
        
        # Create add transition that consumes from both input places
        def add_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val + b_val)
            
        add_transition = self.net.add_transition(
            self.get_unique_transition_name("add"), 
            add_op
        )
        
        # Wire the Petri net: input_places -> transition -> output_place
        self.net.add_arc(a_place, add_transition)
        self.net.add_arc(b_place, add_transition)
        self.net.add_arc(add_transition, result_place)
        
        # Result place becomes the new top of conceptual stack
        self.result_places.append(result_place)
        
        return result_place
        
    def sub_operation(self):
        """
        Implement sub operation: consume two most recent result places
        Result = first - second (where second is most recent)
        """
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for sub operation")
            
        # Pop operands from result places
        b_place = self.result_places.pop()  # Most recent (subtrahend)
        a_place = self.result_places.pop()  # Second most recent (minuend)
        
        # Create result place
        result_place = self.net.add_place(self.get_unique_place_name("sub_result"))
        
        def sub_op(tokens):
            a_val = tokens[0].value  # First operand
            b_val = tokens[1].value  # Second operand
            return Token(a_val - b_val)
            
        sub_transition = self.net.add_transition(
            self.get_unique_transition_name("sub"), 
            sub_op
        )
        
        # Wire: input_places -> transition -> output_place
        self.net.add_arc(a_place, sub_transition)
        self.net.add_arc(b_place, sub_transition)
        self.net.add_arc(sub_transition, result_place)
        
        # Add result to result places
        self.result_places.append(result_place)
        return result_place
        
    def neg_operation(self):
        """
        Implement neg operation: consume most recent result place
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for neg operation")
            
        # Pop single operand from result places
        a_place = self.result_places.pop()
        
        # Create result place
        result_place = self.net.add_place(self.get_unique_place_name("neg_result"))
        
        def neg_op(tokens):
            a_val = tokens[0].value
            return Token(-a_val)
            
        neg_transition = self.net.add_transition(
            self.get_unique_transition_name("neg"), 
            neg_op
        )
        
        # Wire: input_place -> transition -> output_place
        self.net.add_arc(a_place, neg_transition)
        self.net.add_arc(neg_transition, result_place)
        
        # Add result to result places
        self.result_places.append(result_place)
        return result_place
        
    def eq_operation(self):
        """Implement eq operation: true if x == y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for eq operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("eq_result"))
        
        def eq_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val == b_val else 0)  # VM uses -1 for true, 0 for false
            
        eq_transition = self.net.add_transition(self.get_unique_transition_name("eq"), eq_op)
        self.net.add_arc(a_place, eq_transition)
        self.net.add_arc(b_place, eq_transition)
        self.net.add_arc(eq_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def lt_operation(self):
        """Implement lt operation: true if x < y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for lt operation")
            
        b_place = self.result_places.pop()  # y (top of stack)
        a_place = self.result_places.pop()  # x (second from top)
        result_place = self.net.add_place(self.get_unique_place_name("lt_result"))
        
        def lt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val < b_val else 0)
            
        lt_transition = self.net.add_transition(self.get_unique_transition_name("lt"), lt_op)
        self.net.add_arc(a_place, lt_transition)
        self.net.add_arc(b_place, lt_transition)
        self.net.add_arc(lt_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def gt_operation(self):
        """Implement gt operation: true if x > y, else false"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for gt operation")
            
        b_place = self.result_places.pop()  # y (top of stack)
        a_place = self.result_places.pop()  # x (second from top)
        result_place = self.net.add_place(self.get_unique_place_name("gt_result"))
        
        def gt_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(-1 if a_val > b_val else 0)
            
        gt_transition = self.net.add_transition(self.get_unique_transition_name("gt"), gt_op)
        self.net.add_arc(a_place, gt_transition)
        self.net.add_arc(b_place, gt_transition)
        self.net.add_arc(gt_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def and_operation(self):
        """Implement and operation: bitwise AND"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for and operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("and_result"))
        
        def and_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val & b_val)
            
        and_transition = self.net.add_transition(self.get_unique_transition_name("and"), and_op)
        self.net.add_arc(a_place, and_transition)
        self.net.add_arc(b_place, and_transition)
        self.net.add_arc(and_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def or_operation(self):
        """Implement or operation: bitwise OR"""
        if len(self.result_places) < 2:
            raise RuntimeError("Not enough operands for or operation")
            
        b_place = self.result_places.pop()
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("or_result"))
        
        def or_op(tokens):
            a_val = tokens[0].value
            b_val = tokens[1].value
            return Token(a_val | b_val)
            
        or_transition = self.net.add_transition(self.get_unique_transition_name("or"), or_op)
        self.net.add_arc(a_place, or_transition)
        self.net.add_arc(b_place, or_transition)
        self.net.add_arc(or_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
        
    def not_operation(self):
        """Implement not operation: bitwise NOT"""
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for not operation")
            
        a_place = self.result_places.pop()
        result_place = self.net.add_place(self.get_unique_place_name("not_result"))
        
        def not_op(tokens):
            a_val = tokens[0].value
            return Token(~a_val & 0xFFFF)  # 16-bit NOT
            
        not_transition = self.net.add_transition(self.get_unique_transition_name("not"), not_op)
        self.net.add_arc(a_place, not_transition)
        self.net.add_arc(not_transition, result_place)
        
        self.result_places.append(result_place)
        return result_place
    def dup_operation(self):
        """
        Implement dup operation using 'dup' primitive
        Duplicates the top stack element
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for dup operation")
            
        top_place = self.result_places[-1]  # Peek at top without popping
        
        # Create duplicate place
        dup_place = self.net.add_place(self.get_unique_place_name("dup_result"))
        
        # Create dup transition (explicit duplication)
        def dup_op(tokens):
            val = tokens[0].value
            return [Token(val), Token(val)]  # Return two identical tokens
            
        dup_transition = self.net.add_transition(
            self.get_unique_transition_name("dup"), 
            dup_op
        )
        
        # Connect: top_place -> dup_transition -> [top_place, dup_place]
        # This requires consuming the original and producing two
        self.result_places.pop()  # Remove original
        self.net.add_arc(top_place, dup_transition)
        self.net.add_arc(dup_transition, top_place)  # Put back original
        self.net.add_arc(dup_transition, dup_place)  # Add duplicate
        
        # Push both back onto result places
        self.result_places.append(top_place)
        self.result_places.append(dup_place)
        
        return dup_place
        
    def drop_operation(self):
        """
        Implement drop operation using 'drop' primitive
        Discards the top stack element
        """
        if len(self.result_places) < 1:
            raise RuntimeError("Not enough operands for drop operation")
            
        top_place = self.result_places.pop()
        
        # Create drop transition that consumes but produces nothing
        drop_transition = self.net.add_transition(
            self.get_unique_transition_name("drop"), 
            lambda tokens: []  # Consume input, produce nothing
        )
        
        self.net.add_arc(top_place, drop_transition)
        # No output connections - token is consumed and discarded
        
        return None
        # No output connections - token is consumed and discarded
        
        return None
        
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
        for command in commands:
            cmd_type = command[0]
            
            if cmd_type == "push" and command[1] == "constant":
                value = command[2]
                self.push_constant(value)
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
            elif cmd_type == "dup":
                self.dup_operation()
            elif cmd_type == "drop":
                self.drop_operation()
            else:
                raise NotImplementedError(f"Command {cmd_type} not implemented")
                
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
        
    def print_net_statistics(self):
        """Print comprehensive statistics about the translated Petri net"""
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
        
        # Arc breakdown
        input_arcs = sum(len(t.in_places) for t in self.net.transitions.values())
        output_arcs = sum(len(t.out_places) for t in self.net.transitions.values())
        
        print(f"\nArc Breakdown:")
        print(f"  Input arcs (Place → Transition): {input_arcs}")
        print(f"  Output arcs (Transition → Place): {output_arcs}")
        print(f"  Total arcs: {input_arcs + output_arcs} (matches: {total_arcs})")
        
        # Memory optimization analysis
        print(f"\nMemory Optimization Analysis:")
        if total_places > 0:
            memory_map = self._optimize_memory_allocation()
            optimized_locations = len(memory_map['location_to_places'])
            memory_savings = total_places - optimized_locations
            savings_percent = (memory_savings / total_places) * 100 if total_places > 0 else 0
            
            print(f"  Original places: {total_places}")
            print(f"  Optimized memory locations: {optimized_locations}")
            print(f"  Memory addresses saved: {memory_savings}")
            print(f"  Memory reduction: {savings_percent:.1f}%")
            print(f"  Memory reuse factor: {total_places / optimized_locations:.2f}x")
            
            # Show detailed memory mapping
            print(f"\n  Memory Location Details:")
            location_usage = {}
            for location, places in memory_map['location_to_places'].items():
                location_usage[location] = len(places)
                
            # Show most reused locations
            sorted_locations = sorted(location_usage.items(), key=lambda x: x[1], reverse=True)
            for i, (location, usage_count) in enumerate(sorted_locations[:5]):  # Top 5
                places = memory_map['location_to_places'][location]
                print(f"    @{location}: {usage_count} places {places}")
                
            if len(sorted_locations) > 5:
                print(f"    ... and {len(sorted_locations) - 5} more locations")
                
            # Memory range used
            min_location = min(memory_map['location_map'].values())
            max_location = max(memory_map['location_map'].values())
            print(f"  Memory range: @{min_location} to @{max_location}")
            print(f"  Total memory addresses used: {max_location - min_location + 1}")
        else:
            print(f"  No places to optimize")
        
        # Place analysis
        places_with_tokens = sum(1 for p in self.net.places.values() if p.has_token())
        total_tokens = sum(p.token_count() for p in self.net.places.values())
        
        print(f"\nToken Distribution:")
        print(f"  Places with tokens: {places_with_tokens}/{total_places}")
        print(f"  Total tokens: {total_tokens}")
        
        # Classify places by type
        constant_places = []
        result_places = []
        control_places = []
        
        for name, place in self.net.places.items():
            if name.startswith("const_"):
                constant_places.append(name)
            elif "_result_" in name:
                result_places.append(name)
            elif name == "control":
                control_places.append(name)
                
        print(f"\nPlace Classification:")
        print(f"  Constant places: {len(constant_places)}")
        print(f"  Result places: {len(result_places)}")
        print(f"  Control places: {len(control_places)}")
        print(f"  Other places: {total_places - len(constant_places) - len(result_places) - len(control_places)}")
        
        # Transition analysis by operation type
        operation_counts = {}
        for name, transition in self.net.transitions.items():
            op_type = name.split('_')[0]  # Extract operation type from name
            operation_counts[op_type] = operation_counts.get(op_type, 0) + 1
            
        print(f"\nOperation Breakdown:")
        for op_type, count in sorted(operation_counts.items()):
            print(f"  {op_type}: {count}")
            
        # Network connectivity analysis
        max_inputs = 0
        max_outputs = 0
        total_inputs = 0
        total_outputs = 0
        
        for transition in self.net.transitions.values():
            inputs = len(transition.in_places)
            outputs = len(transition.out_places)
            max_inputs = max(max_inputs, inputs)
            max_outputs = max(max_outputs, outputs)
            total_inputs += inputs
            total_outputs += outputs
            
        avg_inputs = total_inputs / len(self.net.transitions) if self.net.transitions else 0
        avg_outputs = total_outputs / len(self.net.transitions) if self.net.transitions else 0
        
        print(f"\nConnectivity Analysis:")
        print(f"  Max inputs per transition: {max_inputs}")
        print(f"  Max outputs per transition: {max_outputs}")
        print(f"  Avg inputs per transition: {avg_inputs:.1f}")
        print(f"  Avg outputs per transition: {avg_outputs:.1f}")
        
        # Execution readiness
        ready_transitions = sum(1 for t in self.net.transitions.values() if t.can_fire())
        
        print(f"\nExecution State:")
        print(f"  Transitions ready to fire: {ready_transitions}/{total_transitions}")
        
        # Memory usage estimation (places that could be CPU-local vs shared)
        private_places = 0  # Places with single producer and consumer
        shared_places = 0   # Places with multiple producers or consumers
        
        for place in self.net.places.values():
            producers = len(place.in_transitions)
            consumers = len(place.out_transitions)
            
            if producers <= 1 and consumers <= 1:
                private_places += 1
            else:
                shared_places += 1
                
        print(f"\nMemory Hierarchy Potential:")
        print(f"  Private places (CPU-local eligible): {private_places}")
        print(f"  Shared places (require synchronization): {shared_places}")
        
        # Concurrency potential
        independent_chains = self._analyze_concurrency()
        
        print(f"\nConcurrency Analysis:")
        print(f"  Potential parallel execution chains: {independent_chains}")
        
        # Final result state
        if self.result_places:
            result_values = self.get_result_values()
            print(f"\nFinal Result Places:")
            for i, value in enumerate(result_values):
                print(f"  [{i}]: {value}")
        else:
            print(f"\nFinal Result Places: Empty")
            
        print("=" * 60)
        
    def _analyze_concurrency(self):
        """Analyze potential for concurrent execution"""
        # Simple heuristic: count transitions that don't share input places
        independent_count = 0
        used_places = set()
        
        for transition in self.net.transitions.values():
            transition_places = set(place.name for place in transition.in_places)
            if not transition_places.intersection(used_places):
                independent_count += 1
                used_places.update(transition_places)
                
        return independent_count
        
    def generate_multicore_assembly(self, num_cores=1, output_dir="test_results"):
        """
        Analyze the Petri net and generate assembly code for n cores
        For multi-core, creates separate ROM files for each core
        """
        if num_cores < 1:
            raise ValueError("Number of cores must be >= 1")
            
        print(f"\n" + "=" * 60)
        print(f"GENERATING ASSEMBLY FOR {num_cores} CORE(S)")
        print("=" * 60)
        
        # Analyze the network for parallelization opportunities
        execution_plan = self._analyze_execution_dependencies()
        
        # Generate core assignments
        core_assignments = self._assign_operations_to_cores(execution_plan, num_cores)
        
        if num_cores == 1:
            # Single core - return assembly as before
            assembly_code = self._generate_single_core_assembly(core_assignments[0], self._optimize_memory_allocation())
            return assembly_code
        else:
            # Multi-core - create separate ROM files for each core
            return self._generate_multicore_roms(core_assignments, num_cores, output_dir)
            
    def _generate_multicore_roms(self, core_assignments, num_cores, output_dir="test_results"):
        """
        Generate separate ROM files for each core in multi-core execution
        Creates a folder with coreX.asm files for each core
        """
        import os
        
        # Create multicore output folder inside the specified directory
        folder_name = os.path.join(output_dir, f"multicore_{num_cores}cores")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        memory_map = self._optimize_memory_allocation()
        
        print(f"Creating {num_cores} separate ROM files in folder: {folder_name}/")
        
        # Generate ROM for each core
        all_roms = {}
        
        for core_id in range(num_cores):
            operations = core_assignments[core_id]
            
            if operations:
                print(f"Core {core_id}: {len(operations)} operations")
                rom_content = self._generate_core_rom(core_id, operations, memory_map, num_cores)
            else:
                print(f"Core {core_id}: No operations (idle core)")
                rom_content = self._generate_idle_core_rom(core_id, num_cores)
            
            # Save ROM file
            rom_filename = f"{folder_name}/core{core_id}.asm"
            with open(rom_filename, 'w') as f:
                f.write('\n'.join(rom_content))
            
            all_roms[core_id] = rom_content
            print(f"  Saved: {rom_filename} ({len(rom_content)} lines)")
        
        # Generate shared memory initialization file
        shared_init = self._generate_shared_memory_init(memory_map, num_cores)
        shared_filename = f"{folder_name}/shared_init.asm"
        with open(shared_filename, 'w') as f:
            f.write('\n'.join(shared_init))
        print(f"  Saved: {shared_filename} (shared memory initialization)")
        
        # Generate coordination protocol documentation
        coord_doc = self._generate_coordination_documentation(core_assignments, num_cores)
        doc_filename = f"{folder_name}/coordination.md"
        with open(doc_filename, 'w') as f:
            f.write(coord_doc)
        print(f"  Saved: {doc_filename} (coordination protocol)")
        
        return all_roms
        
    def _generate_core_rom(self, core_id, operations, memory_map, num_cores):
        """Generate ROM content for a specific core"""
        rom_lines = [
            f"// Core {core_id} ROM - Petri-net Multi-core Execution",
            f"// Generated for {num_cores}-core system",
            f"// Operations: {len(operations)}",
            "//",
            f"// Memory Layout:",
            f"// @0-15: System registers",
            f"// @16-31: Core status flags (core_id + 16)",
            f"// @32-47: Core synchronization area", 
            f"// @256+: Optimized place memory",
            f"// @512+: Shared results area",
            "//",
            "",
            f"// Core {core_id} initialization",
            f"@{16 + core_id}",
            "M=0  // Set status to idle",
            "",
            f"(CORE_{core_id}_START)",
            f"// Core {core_id} execution begins",
            f"@{16 + core_id}",
            "M=1  // Set status to working",
            ""
        ]
        
        # Group operations by execution level for synchronization
        operations_by_level = {}
        for op_info in operations:
            level = op_info['level']
            if level not in operations_by_level:
                operations_by_level[level] = []
            operations_by_level[level].append(op_info)
        
        # Generate code for each level with synchronization
        for level in sorted(operations_by_level.keys()):
            level_ops = operations_by_level[level]
            
            rom_lines.extend([
                f"// === Level {level} Operations ===",
                f"// Wait for all cores to reach level {level}",
                f"(LEVEL_{level}_WAIT)",
            ])
            
            # Check if all cores are ready for this level
            # Simple protocol: each core sets bit in sync area when ready
            rom_lines.extend([
                f"// Signal ready for level {level}",
                f"@{32 + level}",  # Sync area for this level
                "D=M",
                f"@{1 << core_id}",  # Set bit for this core
                "D=D|A",
                f"@{32 + level}",
                "M=D",
                "",
                f"// Wait for all cores to be ready",
                f"(LEVEL_{level}_CHECK)",
                f"@{32 + level}",
                "D=M",
                f"@{(1 << num_cores) - 1}",  # All cores ready mask
                "D=D-A",
                f"@LEVEL_{level}_EXECUTE",
                "D;JEQ",  # All cores ready, proceed
                f"@LEVEL_{level}_CHECK",
                "0;JMP",  # Keep waiting
                "",
                f"(LEVEL_{level}_EXECUTE)"
            ])
            
            # Execute operations for this level
            for op_info in level_ops:
                operation = op_info['operation']
                transition = op_info['transition']
                
                rom_lines.extend([
                    f"// Operation: {operation}",
                    f"// Core {core_id} executing {operation}"
                ])
                
                # Generate memory-optimized operation code
                op_code = self._generate_core_operation_code(operation, transition, memory_map)
                rom_lines.extend(op_code)
                rom_lines.append("")
        
        # Core completion
        rom_lines.extend([
            f"// Core {core_id} completed all operations",
            f"@{16 + core_id}",
            "M=2  // Set status to done",
            "",
            f"(CORE_{core_id}_END)",
            f"@CORE_{core_id}_END",
            "0;JMP  // Halt core"
        ])
        
        return rom_lines
        
    def _generate_idle_core_rom(self, core_id, num_cores):
        """Generate ROM for cores with no operations assigned"""
        return [
            f"// Core {core_id} ROM - Idle Core",
            f"// No operations assigned in {num_cores}-core system",
            "//",
            f"@{16 + core_id}",
            "M=0  // Set status to idle",
            "",
            f"(CORE_{core_id}_IDLE)",
            "// Idle loop - could be used for other tasks",
            f"@CORE_{core_id}_IDLE", 
            "0;JMP"
        ]
        
    def _generate_core_operation_code(self, operation, transition, memory_map):
        """Generate assembly code for a specific operation on a core"""
        op_type = operation.split('_')[0]
        code_lines = []
        
        if op_type in ['add', 'sub', 'and', 'or', 'eq', 'lt', 'gt'] and len(transition.in_places) >= 2:
            # Binary operations
            loc_a = memory_map['location_map'][transition.in_places[0].name]
            loc_b = memory_map['location_map'][transition.in_places[1].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Binary operation: {op_type}",
                f"// Load operands from @{loc_a} and @{loc_b}",
                f"@{loc_a}",
                "D=M",
                f"@{loc_b}",
            ])
            
            if op_type == 'add':
                code_lines.append("D=D+M")
            elif op_type == 'sub':
                code_lines.append("D=D-M")
            elif op_type == 'and':
                code_lines.append("D=D&M")
            elif op_type == 'or':
                code_lines.append("D=D|M")
            elif op_type in ['eq', 'lt', 'gt']:
                # Comparison operations
                code_lines.extend([
                    "D=D-M  // Compare",
                    f"@{operation.upper()}_TRUE",
                    f"D;J{op_type.upper()}",
                    "D=0  // False",
                    f"@{operation.upper()}_DONE",
                    "0;JMP",
                    f"({operation.upper()}_TRUE)",
                    "D=-1  // True (-1)",
                    f"({operation.upper()}_DONE)"
                ])
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
            
        elif op_type in ['neg', 'not'] and len(transition.in_places) >= 1:
            # Unary operations
            loc_input = memory_map['location_map'][transition.in_places[0].name]
            loc_result = memory_map['location_map'][transition.out_places[0].name]
            
            code_lines.extend([
                f"// Unary operation: {op_type}",
                f"// Load operand from @{loc_input}",
                f"@{loc_input}",
                "D=M",
            ])
            
            if op_type == 'neg':
                code_lines.append("D=-D")
            elif op_type == 'not':
                code_lines.append("D=!D")
                
            code_lines.extend([
                f"// Store result to @{loc_result}",
                f"@{loc_result}",
                "M=D"
            ])
        
        return code_lines
        
    def _generate_shared_memory_init(self, memory_map, num_cores):
        """Generate shared memory initialization code"""
        init_lines = [
            f"// Shared Memory Initialization for {num_cores}-core system",
            "// Run this before starting any cores",
            "//",
            "// Initialize core status flags to idle",
        ]
        
        for core_id in range(num_cores):
            init_lines.extend([
                f"@{16 + core_id}",
                "M=0  // Core idle"
            ])
        
        init_lines.extend([
            "",
            "// Initialize synchronization area",
        ])
        
        # Initialize sync areas for each level (assuming max 10 levels)
        for level in range(10):
            init_lines.extend([
                f"@{32 + level}",
                "M=0  // Level sync"
            ])
        
        init_lines.extend([
            "",
            "// Initialize constants in optimized memory locations"
        ])
        
        # Initialize constants
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                init_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        
        init_lines.extend([
            "",
            "// Shared memory initialization complete",
            "(INIT_DONE)",
            "@INIT_DONE",
            "0;JMP"
        ])
        
        return init_lines
        
    def _generate_coordination_documentation(self, core_assignments, num_cores):
        """Generate documentation for the multi-core coordination protocol"""
        doc = f"""# Multi-Core Coordination Protocol

## System Overview
- **Cores**: {num_cores}
- **Coordination**: Level-based synchronization
- **Memory**: Shared optimized memory layout

## Memory Layout
- `@0-15`: System registers
- `@16-31`: Core status flags (0=idle, 1=working, 2=done)
- `@32-47`: Level synchronization area
- `@256+`: Optimized place memory (shared)
- `@512+`: Results collection area

## Core Assignments
"""
        
        for core_id, operations in core_assignments.items():
            doc += f"\n### Core {core_id}\n"
            if operations:
                doc += f"Operations: {len(operations)}\n"
                for op_info in operations:
                    doc += f"- Level {op_info['level']}: {op_info['operation']}\n"
            else:
                doc += "No operations assigned (idle core)\n"
        
        doc += f"""
## Synchronization Protocol

### Level-Based Execution
1. Each core waits at level barriers
2. Core sets ready bit in sync area (@32+level)
3. All cores wait for full ready mask: {(1 << num_cores) - 1}
4. When all ready, cores proceed with level operations
5. Repeat for next level

### Core Status Protocol
- **0**: Core idle/waiting
- **1**: Core working on operations  
- **2**: Core completed all operations

## Execution Flow
1. Run `shared_init.asm` to initialize shared memory
2. Start all core ROMs simultaneously
3. Cores synchronize at each level automatically
4. Final results available in optimized memory locations

## Files Generated
- `core0.asm` to `core{num_cores-1}.asm`: Individual core ROMs
- `shared_init.asm`: Shared memory initialization
- `coordination.md`: This documentation file
"""
        
        return doc
        
    def _analyze_execution_dependencies(self):
        """
        Analyze the Petri net to determine execution dependencies
        Returns a dependency graph and execution levels
        """
        # Build dependency graph
        dependencies = {}
        reverse_deps = {}
        
        for trans_name, transition in self.net.transitions.items():
            dependencies[trans_name] = []
            reverse_deps[trans_name] = []
            
        # Find dependencies based on place connections
        for trans_name, transition in self.net.transitions.items():
            for input_place in transition.in_places:
                # Find which transition produces this place
                for producer_name, producer in self.net.transitions.items():
                    if input_place in producer.out_places:
                        dependencies[trans_name].append(producer_name)
                        reverse_deps[producer_name].append(trans_name)
                        
        # Topological sort to find execution levels
        execution_levels = []
        remaining = set(self.net.transitions.keys())
        
        while remaining:
            # Find transitions with no unresolved dependencies
            ready = []
            for trans in remaining:
                if all(dep not in remaining for dep in dependencies[trans]):
                    ready.append(trans)
                    
            if not ready:
                # Handle cycles or isolated nodes
                ready = [next(iter(remaining))]
                
            execution_levels.append(ready)
            remaining -= set(ready)
            
        return {
            'dependencies': dependencies,
            'reverse_deps': reverse_deps,
            'execution_levels': execution_levels
        }
        
    def _assign_operations_to_cores(self, execution_plan, num_cores):
        """
        Assign operations to cores based on dependencies and load balancing
        """
        core_assignments = {i: [] for i in range(num_cores)}
        
        for level_idx, level in enumerate(execution_plan['execution_levels']):
            print(f"Level {level_idx}: {len(level)} parallel operations: {level}")
            
            # Assign operations in this level to cores (round-robin)
            for i, operation in enumerate(level):
                core_id = i % num_cores
                core_assignments[core_id].append({
                    'operation': operation,
                    'level': level_idx,
                    'transition': self.net.transitions[operation]
                })
                
        return core_assignments
        
    def _generate_assembly_code(self, core_assignments, num_cores):
        """
        Generate Hack assembly code for multi-core execution
        This method is kept for backward compatibility but now delegates to the new ROM generation
        """
        if num_cores == 1:
            memory_map = self._optimize_memory_allocation()
            return self._generate_single_core_assembly(core_assignments[0], memory_map)
        else:
            # For multi-core, return a summary instead of monolithic assembly
            roms = self._generate_multicore_roms(core_assignments, num_cores)
            
            # Return a summary of what was generated
            summary = [
                f"// Multi-core ROM generation completed",
                f"// Generated {num_cores} separate ROM files:",
            ]
            
            for core_id in range(num_cores):
                rom_size = len(roms[core_id]) if core_id in roms else 0
                summary.append(f"//   core{core_id}.asm: {rom_size} lines")
            
            summary.extend([
                f"// Plus shared_init.asm and coordination.md",
                f"// Check multicore_{num_cores}cores/ folder for files"
            ])
            
            return summary
            
    def _optimize_memory_allocation(self):
        """
        Simple memory optimization using Petri net structure
        Places can share memory if they can never have tokens simultaneously
        """
        print("\n--- Simple Memory Optimization ---")
        
        # Simple rule: if place A is consumed by a transition that produces place B,
        # then A and B can share memory (A dies when B is born)
        memory_map = {}
        location_to_places = {}
        next_location = 256
        
        # First pass: assign memory to all places
        for place_name, place in self.net.places.items():
            memory_map[place_name] = next_location
            location_to_places[next_location] = [place_name]
            next_location += 1
            
        # Second pass: find reuse opportunities
        for transition in self.net.transitions.values():
            # For each transition, input places can reuse memory from output places
            # (since inputs are consumed when outputs are produced)
            if len(transition.in_places) > 0 and len(transition.out_places) > 0:
                # Take the first output place's memory location
                output_place = transition.out_places[0]
                output_location = memory_map[output_place.name]
                
                # Reuse it for input places (except the first input which keeps its location)
                for i, input_place in enumerate(transition.in_places[1:], 1):  # Skip first input
                    old_location = memory_map[input_place.name]
                    
                    # Move input place to output's location
                    memory_map[input_place.name] = output_location
                    location_to_places[output_location].append(input_place.name)
                    
                    # Remove from old location
                    location_to_places[old_location].remove(input_place.name)
                    if not location_to_places[old_location]:  # If empty, remove
                        del location_to_places[old_location]
        
        # Clean up empty locations and renumber
        used_locations = sorted(location_to_places.keys())
        final_location_map = {}
        final_location_to_places = {}
        
        for i, old_location in enumerate(used_locations):
            new_location = 256 + i
            places = location_to_places[old_location]
            
            for place_name in places:
                final_location_map[place_name] = new_location
            final_location_to_places[new_location] = places
            
        print(f"Original places: {len(self.net.places)}")
        print(f"Memory locations needed: {len(final_location_to_places)}")
        print(f"Memory savings: {len(self.net.places) - len(final_location_to_places)} locations")
        
        # Show reuse details
        print(f"\nMemory Reuse Details:")
        for location, places in final_location_to_places.items():
            if len(places) > 1:
                print(f"  @{location}: {places} (SHARED)")
            else:
                print(f"  @{location}: {places}")
        
        return {
            'location_map': final_location_map,
            'location_to_places': final_location_to_places,
            'total_locations': len(final_location_to_places)
        }
        
    def _analyze_place_reachability(self):
        """
        Analyze which places can be reached simultaneously during execution
        Places that are never live at the same time can share memory
        """
        # Build execution dependency graph
        execution_plan = self._analyze_execution_dependencies()
        
        # Determine place lifetimes
        place_lifetimes = {}
        
        for place_name, place in self.net.places.items():
            # Find when place is produced (birth)
            birth_level = -1  # Constants are born at level -1
            if place_name.startswith("const_"):
                birth_level = -1
            else:
                # Find producing transition
                for producer in place.in_transitions:
                    for level_idx, level in enumerate(execution_plan['execution_levels']):
                        if producer.name in level:
                            birth_level = level_idx
                            break
                            
            # Find when place is consumed (death)
            death_level = float('inf')  # Final results live forever
            if place in self.result_places:
                death_level = float('inf')  # Result places live forever
            else:
                # Find consuming transitions
                min_death = float('inf')
                for consumer in place.out_transitions:
                    for level_idx, level in enumerate(execution_plan['execution_levels']):
                        if consumer.name in level:
                            min_death = min(min_death, level_idx)
                if min_death != float('inf'):
                    death_level = min_death
                    
            place_lifetimes[place_name] = {
                'birth': birth_level,
                'death': death_level,
                'lifetime': (birth_level, death_level)
            }
            
        return {
            'lifetimes': place_lifetimes,
            'execution_plan': execution_plan
        }
        
    def _allocate_memory_locations(self, reachability):
        """
        Allocate memory locations using interval graph coloring
        Places with non-overlapping lifetimes can share memory
        """
        lifetimes = reachability['lifetimes']
        
        # Sort places by birth time, then by death time
        sorted_places = sorted(lifetimes.items(), 
                             key=lambda x: (x[1]['birth'], x[1]['death']))
        
        # Greedy coloring algorithm for interval graphs
        location_map = {}  # place_name -> memory_location
        location_to_places = {}  # memory_location -> [place_names]
        active_locations = []  # [(end_time, location_id)]
        next_location = 256  # Start memory allocation at @256
        
        for place_name, lifetime_info in sorted_places:
            birth = lifetime_info['birth']
            death = lifetime_info['death']
            
            # Remove expired locations (locations that expire BEFORE this birth time)
            active_locations = [(end_time, loc_id) for end_time, loc_id in active_locations 
                              if end_time >= birth]
            
            # Try to reuse an existing location
            reused_location = None
            # Look for locations that expire at or before this birth time
            for end_time, loc_id in active_locations[:]:  # Copy list to avoid modification during iteration
                if end_time <= birth:  # This location is free at birth time
                    reused_location = loc_id
                    active_locations.remove((end_time, loc_id))
                    break
                        
            if reused_location is not None:
                # Reuse existing location
                location_map[place_name] = reused_location
                location_to_places[reused_location].append(place_name)
            else:
                # Allocate new location
                location_map[place_name] = next_location
                location_to_places[next_location] = [place_name]
                next_location += 1
                
            # Add this location to active set
            if death != float('inf'):
                active_locations.append((death, location_map[place_name]))
                
        return {
            'location_map': location_map,
            'location_to_places': location_to_places,
            'total_locations': next_location - 256
        }
        
    def _generate_single_core_assembly(self, operations, memory_map):
        """Generate assembly for single core execution with memory optimization"""
        assembly_lines = [
            "// Single-core sequential execution with memory optimization",
            "// Initialize stack pointer", 
            "@256",
            "D=A",
            "@SP",
            "M=D",
            "//"
        ]
        
        # Initialize constants in their allocated memory locations
        assembly_lines.append("// Initialize constants in optimized memory locations")
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                assembly_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
                
        assembly_lines.append("//")
        
        # Generate code for each operation in order
        for op_info in operations:
            operation = op_info['operation']
            transition = op_info['transition']
            
            assembly_lines.extend([
                f"// Operation: {operation}",
                f"// Level: {op_info['level']}"
            ])
            
            # Generate operation-specific assembly with memory locations
            op_type = operation.split('_')[0]
            
            if op_type in ['add', 'sub', 'and', 'or']:
                # Binary operations: load from memory locations, compute, store result
                input_places = transition.in_places
                output_places = transition.out_places
                
                if len(input_places) >= 2 and len(output_places) >= 1:
                    loc_a = memory_map['location_map'][input_places[0].name]
                    loc_b = memory_map['location_map'][input_places[1].name]
                    loc_result = memory_map['location_map'][output_places[0].name]
                    
                    assembly_lines.extend([
                        f"// Load operands from @{loc_a} and @{loc_b}",
                        f"@{loc_a}",
                        "D=M",
                        f"@{loc_b}",
                    ])
                    
                    if op_type == 'add':
                        assembly_lines.append("D=D+M")
                    elif op_type == 'sub':
                        assembly_lines.append("D=D-M")
                    elif op_type == 'and':
                        assembly_lines.append("D=D&M")
                    elif op_type == 'or':
                        assembly_lines.append("D=D|M")
                        
                    assembly_lines.extend([
                        f"// Store result to @{loc_result}",
                        f"@{loc_result}",
                        "M=D"
                    ])
                    
            elif op_type in ['neg', 'not']:
                # Unary operations
                input_places = transition.in_places
                output_places = transition.out_places
                
                if len(input_places) >= 1 and len(output_places) >= 1:
                    loc_input = memory_map['location_map'][input_places[0].name]
                    loc_result = memory_map['location_map'][output_places[0].name]
                    
                    assembly_lines.extend([
                        f"// Load operand from @{loc_input}",
                        f"@{loc_input}",
                        "D=M",
                    ])
                    
                    if op_type == 'neg':
                        assembly_lines.append("D=-D")
                    elif op_type == 'not':
                        assembly_lines.append("D=!D")
                        
                    assembly_lines.extend([
                        f"// Store result to @{loc_result}",
                        f"@{loc_result}",
                        "M=D"
                    ])
                    
            assembly_lines.append("//")
            
        # Push final results onto stack
        assembly_lines.extend([
            "// Push final results onto stack"
        ])
        
        for place in self.result_places:
            if place.name in memory_map['location_map']:
                memory_loc = memory_map['location_map'][place.name]
                assembly_lines.extend([
                    f"// Push result from @{memory_loc}",
                    f"@{memory_loc}",
                    "D=M",
                    "@SP",
                    "M=M+1",
                    "A=M-1",
                    "M=D"
                ])
                
        assembly_lines.extend([
            "//",
            "// End of program",
            "(END)",
            "@END", 
            "0;JMP"
        ])
        
        return assembly_lines
        
    def _generate_multi_core_assembly(self, core_assignments, num_cores, memory_map):
        """Generate assembly for multi-core execution with memory optimization and synchronization"""
        assembly_lines = [
            f"// Multi-core execution for {num_cores} cores with memory optimization",
            "// Core synchronization using shared memory",
            "//",
            "// Memory layout:",
            "// @16-31: Core status flags (0=idle, 1=working, 2=done)",
            "// @32-47: Core communication area",
            f"// @256+: Optimized place memory ({memory_map['total_locations']} locations)",
            "// @512+: Shared stack",
            "//",
            
            "// Initialize shared memory",
            "@512",  # Move stack higher to avoid optimized memory
            "D=A", 
            "@SP",
            "M=D",
            "//"
        ]
        
        # Initialize constants in optimized memory locations
        assembly_lines.append("// Initialize constants in optimized memory")
        for place_name, place in self.net.places.items():
            if place_name.startswith("const_") and place.has_token():
                value = place.tokens[0].value
                memory_loc = memory_map['location_map'][place_name]
                assembly_lines.extend([
                    f"// Constant {value} -> @{memory_loc}",
                    f"@{value}",
                    "D=A",
                    f"@{memory_loc}",
                    "M=D"
                ])
        
        # Generate core initialization
        for core_id in range(num_cores):
            assembly_lines.extend([
                f"// Initialize core {core_id}",
                f"@{16 + core_id}",  # Core status at @16+core_id
                "M=0",  # Set to idle
            ])
            
        assembly_lines.append("//")
        
        # Generate main execution coordinator with level-based synchronization
        assembly_lines.extend([
            "// Main execution coordinator with level synchronization",
            "(MAIN_LOOP)",
            
            # Check if all cores are done
            "// Check if all cores completed",
            "@0",
            "D=A",  # Counter for completed cores
        ])
        
        for core_id in range(num_cores):
            assembly_lines.extend([
                f"@{16 + core_id}",
                "D=D+M",  # Add core status (2 if done)
            ])
            
        assembly_lines.extend([
            f"@{2 * num_cores}",  # Expected sum if all cores done
            "D=D-A",
            "@END_PROGRAM",
            "D;JEQ",  # Jump to end if all done
            
            "// Continue execution",
            "@MAIN_LOOP", 
            "0;JMP",
            "//"
        ])
        
        # Generate code for each core with memory-optimized operations
        for core_id, operations in core_assignments.items():
            if not operations:
                continue
                
            assembly_lines.extend([
                f"// Core {core_id} execution with memory optimization",
                f"(CORE_{core_id})",
                f"@{16 + core_id}",
                "M=1",  # Set status to working
            ])
            
            # Generate operations for this core
            for op_info in operations:
                operation = op_info['operation']
                level = op_info['level']
                transition = op_info['transition']
                
                assembly_lines.extend([
                    f"// Core {core_id}: {operation} (Level {level})",
                    f"// Memory-optimized operation",
                ])
                
                # Generate memory-optimized operation code
                op_type = operation.split('_')[0]
                
                if op_type in ['add', 'sub', 'and', 'or'] and len(transition.in_places) >= 2:
                    # Binary operations with memory locations
                    loc_a = memory_map['location_map'][transition.in_places[0].name]
                    loc_b = memory_map['location_map'][transition.in_places[1].name]
                    loc_result = memory_map['location_map'][transition.out_places[0].name]
                    
                    assembly_lines.extend([
                        f"// Binary op: @{loc_a} {op_type} @{loc_b} -> @{loc_result}",
                        f"@{loc_a}",
                        "D=M",
                        f"@{loc_b}",
                    ])
                    
                    if op_type == 'add':
                        assembly_lines.append("D=D+M")
                    elif op_type == 'sub':
                        assembly_lines.append("D=D-M")
                    elif op_type == 'and':
                        assembly_lines.append("D=D&M")
                    elif op_type == 'or':
                        assembly_lines.append("D=D|M")
                        
                    assembly_lines.extend([
                        f"@{loc_result}",
                        "M=D"
                    ])
                    
                elif op_type in ['neg', 'not'] and len(transition.in_places) >= 1:
                    # Unary operations with memory locations
                    loc_input = memory_map['location_map'][transition.in_places[0].name]
                    loc_result = memory_map['location_map'][transition.out_places[0].name]
                    
                    assembly_lines.extend([
                        f"// Unary op: {op_type} @{loc_input} -> @{loc_result}",
                        f"@{loc_input}",
                        "D=M",
                    ])
                    
                    if op_type == 'neg':
                        assembly_lines.append("D=-D")
                    elif op_type == 'not':
                        assembly_lines.append("D=!D")
                        
                    assembly_lines.extend([
                        f"@{loc_result}",
                        "M=D"
                    ])
                        
                assembly_lines.append("//")
                
            assembly_lines.extend([
                f"// Core {core_id} finished",
                f"@{16 + core_id}",
                "M=2",  # Set status to done
                f"@CORE_{core_id}_END",
                "0;JMP",
                f"(CORE_{core_id}_END)",
                "//"
            ])
            
        # Final result collection
        assembly_lines.extend([
            "(END_PROGRAM)",
            "// Collect final results to stack",
        ])
        
        for place in self.result_places:
            if place.name in memory_map['location_map']:
                memory_loc = memory_map['location_map'][place.name]
                assembly_lines.extend([
                    f"// Push final result from @{memory_loc}",
                    f"@{memory_loc}",
                    "D=M",
                    "@SP",
                    "M=M+1",
                    "A=M-1",
                    "M=D"
                ])
        
        assembly_lines.extend([
            "// All cores completed",
            "@END_PROGRAM",
            "0;JMP"
        ])
        
        return assembly_lines
        
    def _analyze_concurrency(self):
        """Analyze potential for concurrent execution"""
        # Simple heuristic: count transitions that don't share input places
        independent_count = 0
        used_places = set()
        
        for transition in self.net.transitions.values():
            transition_places = set(place.name for place in transition.in_places)
            if not transition_places.intersection(used_places):
                independent_count += 1
                used_places.update(transition_places)
                
        return independent_count
        
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