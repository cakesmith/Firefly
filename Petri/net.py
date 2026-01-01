from .Place import Place
from .Transition import Transition

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = {}
        self.arcs = []
        
    def add_place(self, place):
        self.places[place.name] = place
        return place
        
    def add_transition(self, transition):
        self.transitions[transition.name] = transition
        return transition
        
    def add_arc(self, source, target):
        """Add arc between place and transition or transition and place"""
        self.arcs.append((source.name, target.name))
        
        if isinstance(source, Transition):  
            source.out_places.append(target)
        else:
            target.in_places.append(source)
        
    def execute_step(self):
        """Execute one step of the Petri net"""
        # First, collect all transitions that can fire BEFORE any firing happens
        # This prevents transitions enabled by firings within this step from also firing
        enabled = [t for t in self.transitions.values() if t.can_fire()]
        
        # Now fire all the enabled transitions
        fired = []
        for transition in enabled:
            transition.fire()
            fired.append(transition.name)
        return fired

    def allocate_memory(self, next_slot=0):
        """
        Proper memory allocation with liveness analysis and interference detection.
        Uses graph coloring to assign memory slots safely.
        """
        # Reset all memory addresses
        for place in self.places.values():
            place.memory_address = None
        
        # Step 1: Perform liveness analysis to find interference
        interference_graph = self._build_interference_graph()
        
        # Step 2: Use graph coloring to assign memory slots
        slot_assignment = self._color_interference_graph(interference_graph)
        
        # Step 3: Assign memory addresses based on coloring
        max_slot = 0
        for place_name, slot in slot_assignment.items():
            self.places[place_name].memory_address = slot
            max_slot = max(max_slot, slot)
        
        return max_slot + 1
    
    def _build_interference_graph(self):
        """
        Build interference graph: places that can be alive simultaneously
        must have different memory slots (connected by edges)
        """
        interference = {name: set() for name in self.places.keys()}
        
        # For each transition, analyze which places can be alive together
        for transition in self.transitions.values():
            # All input places of a transition can be alive together
            # (they must all have tokens for the transition to fire)
            input_names = [p.name for p in transition.in_places]
            for i, place1 in enumerate(input_names):
                for j, place2 in enumerate(input_names):
                    if i != j:
                        interference[place1].add(place2)
                        interference[place2].add(place1)
            
            # NOTE: We do NOT assume all output places interfere with each other
            # because a transition might produce tokens to only some outputs
            # based on its operation logic
        
        # Additional analysis: places in parallel paths and pipeline overlaps
        self._analyze_parallel_paths(interference)
        
        return interference
    
    def _analyze_parallel_paths(self, interference):
        """
        Analyze parallel execution paths and pipeline overlaps to find additional interferences.
        """
        # 1. Fork analysis: Places in different branches of a fork can be alive simultaneously
        for transition in self.transitions.values():
            if len(transition.out_places) > 1:
                branches = []
                for output_place in transition.out_places:
                    branch_places = self._get_reachable_places(output_place.name, max_depth=3)
                    branches.append(branch_places)
                
                # Places in different branches can be alive simultaneously
                for i, branch1 in enumerate(branches):
                    for j, branch2 in enumerate(branches):
                        if i != j:
                            for place1 in branch1:
                                for place2 in branch2:
                                    interference[place1].add(place2)
                                    interference[place2].add(place1)
        
        # 2. Pipeline analysis: Adjacent stages in a pipeline can overlap during execution
        self._analyze_pipeline_overlaps(interference)
    
    def _analyze_pipeline_overlaps(self, interference):
        """
        In pipelined execution, adjacent stages can be active simultaneously.
        For example: A->T1->B->T2->C, when T2 fires, both B and C can be active.
        """
        # Find all linear chains (pipelines)
        chains = self._find_linear_chains()
        
        for chain in chains:
            # In a pipeline, adjacent places can be alive simultaneously
            for i in range(len(chain) - 1):
                place1 = chain[i]
                place2 = chain[i + 1]
                interference[place1].add(place2)
                interference[place2].add(place1)
    
    def _find_linear_chains(self):
        """Find linear chains (pipelines) in the network"""
        chains = []
        visited = set()
        
        # Start from places with no predecessors
        start_places = []
        for place_name in self.places.keys():
            has_predecessor = False
            for transition in self.transitions.values():
                if any(p.name == place_name for p in transition.out_places):
                    has_predecessor = True
                    break
            if not has_predecessor:
                start_places.append(place_name)
        
        # Trace each chain from start places
        for start_place in start_places:
            if start_place not in visited:
                chain = self._trace_linear_chain(start_place, visited)
                if len(chain) > 1:  # Only consider chains with multiple places
                    chains.append(chain)
        
        return chains
    
    def _trace_linear_chain(self, start_place, visited):
        """Trace a linear chain starting from a given place"""
        chain = [start_place]
        visited.add(start_place)
        current_place = start_place
        
        while True:
            # Find the unique next place in the chain (if any)
            next_places = []
            
            # Look for transitions that consume from current_place
            for transition in self.transitions.values():
                if (len(transition.in_places) == 1 and 
                    transition.in_places[0].name == current_place and
                    len(transition.out_places) == 1):
                    
                    next_place = transition.out_places[0].name
                    if next_place not in visited:
                        next_places.append(next_place)
            
            # Continue chain only if there's exactly one next place
            if len(next_places) == 1:
                next_place = next_places[0]
                chain.append(next_place)
                visited.add(next_place)
                current_place = next_place
            else:
                break
        
        return chain
    
    def _get_reachable_places(self, start_place, max_depth=3):
        """Get places reachable from start_place within max_depth steps"""
        if max_depth <= 0:
            return {start_place}
        
        reachable = {start_place}
        current_level = {start_place}
        
        for depth in range(max_depth):
            next_level = set()
            for place_name in current_level:
                # Find transitions that consume from this place
                for transition in self.transitions.values():
                    if any(p.name == place_name for p in transition.in_places):
                        # Add all output places of this transition
                        for output_place in transition.out_places:
                            if output_place.name not in reachable:
                                next_level.add(output_place.name)
                                reachable.add(output_place.name)
            
            if not next_level:
                break
            current_level = next_level
        
        return reachable
    
    def _color_interference_graph(self, interference):
        """
        Use graph coloring to assign memory slots.
        Places connected by edges get different colors (slots).
        """
        place_names = list(self.places.keys())
        coloring = {}
        
        # Sort places by degree (most constrained first)
        sorted_places = sorted(place_names, 
                             key=lambda p: len(interference[p]), 
                             reverse=True)
        
        for place in sorted_places:
            # Find the lowest color not used by neighbors
            used_colors = set()
            for neighbor in interference[place]:
                if neighbor in coloring:
                    used_colors.add(coloring[neighbor])
            
            # Assign the lowest available color
            color = 0
            while color in used_colors:
                color += 1
            coloring[place] = color
        
        return coloring
    def assign_cpu_cores(self, num_cores):
        """
        Assign CPU cores to transitions using graph coloring based on level system.
        Transitions at the same level that can execute in parallel get different cores.
        """
        self.cpu_cores = num_cores
        
        # Step 1: Compute levels for all transitions
        self._compute_transition_levels()
        
        # Step 2: Build conflict graph for transitions at each level
        conflict_graph = self._build_transition_conflict_graph()
        
        # Step 3: Use graph coloring to assign CPU cores
        self.cpu_assignments = self._color_transition_graph(conflict_graph, num_cores)
        
        return self.cpu_assignments
    
    def _compute_transition_levels(self):
        """
        Compute the level of each transition based on longest path from start.
        Transitions at the same level can potentially execute in parallel.
        """
        self.transition_levels = {}
        
        # Find starting transitions (no input places or input from init)
        start_transitions = []
        for transition in self.transitions.values():
            if (not transition.in_places or 
                (len(transition.in_places) == 1 and transition.in_places[0].name == "init")):
                start_transitions.append(transition)
        
        # BFS to assign levels
        visited = set()
        queue = [(t, 0) for t in start_transitions]  # (transition, level)
        
        while queue:
            transition, level = queue.pop(0)
            
            if transition.name in visited:
                # Update level if we found a longer path
                if level > self.transition_levels.get(transition.name, -1):
                    self.transition_levels[transition.name] = level
                    # Re-queue successors with updated level
                    for successor in self._get_successor_transitions(transition):
                        if successor.name not in visited or level + 1 > self.transition_levels.get(successor.name, -1):
                            queue.append((successor, level + 1))
                continue
            
            visited.add(transition.name)
            self.transition_levels[transition.name] = level
            
            # Add successor transitions to queue
            for successor in self._get_successor_transitions(transition):
                queue.append((successor, level + 1))
    
    def _get_successor_transitions(self, transition):
        """Get transitions that can execute after the given transition"""
        successors = []
        
        # Find transitions that consume from this transition's output places
        for output_place in transition.out_places:
            for other_transition in self.transitions.values():
                if output_place in other_transition.in_places:
                    successors.append(other_transition)
        
        return successors
    
    def _build_transition_conflict_graph(self):
        """
        Build conflict graph for transitions.
        Transitions conflict if they:
        1. Are at the same level AND
        2. Share input or output places (resource conflicts)
        """
        conflict_graph = {name: set() for name in self.transitions.keys()}
        
        # Group transitions by level
        levels = {}
        for trans_name, level in self.transition_levels.items():
            if level not in levels:
                levels[level] = []
            levels[level].append(trans_name)
        
        # For each level, find conflicts between transitions
        for level, trans_names in levels.items():
            for i, trans1_name in enumerate(trans_names):
                for j, trans2_name in enumerate(trans_names):
                    if i != j:
                        trans1 = self.transitions[trans1_name]
                        trans2 = self.transitions[trans2_name]
                        
                        # Check for resource conflicts
                        if self._transitions_conflict(trans1, trans2):
                            conflict_graph[trans1_name].add(trans2_name)
                            conflict_graph[trans2_name].add(trans1_name)
        
        return conflict_graph
    
    def _transitions_conflict(self, trans1, trans2):
        """
        Check if two transitions conflict (cannot execute simultaneously).
        They conflict if they share input or output places.
        """
        # Check shared input places
        trans1_inputs = set(p.name for p in trans1.in_places)
        trans2_inputs = set(p.name for p in trans2.in_places)
        if trans1_inputs & trans2_inputs:
            return True
        
        # Check shared output places
        trans1_outputs = set(p.name for p in trans1.out_places)
        trans2_outputs = set(p.name for p in trans2.out_places)
        if trans1_outputs & trans2_outputs:
            return True
        
        # Check if one's output is another's input
        if trans1_outputs & trans2_inputs or trans2_outputs & trans1_inputs:
            return True
        
        return False
    
    def _color_transition_graph(self, conflict_graph, num_cores):
        """
        Use graph coloring to assign CPU cores to transitions.
        Conflicting transitions get different cores (colors).
        Also distribute non-conflicting transitions across cores for load balancing.
        With shared ROM, control flow operations can be on any core.
        """
        assignments = {}
        
        # Sort transitions by conflict degree (most constrained first), then by level
        sorted_transitions = sorted(self.transitions.keys(),
                                  key=lambda t: (len(conflict_graph[t]), self.transition_levels.get(t, 0)),
                                  reverse=True)
        
        for trans_name in sorted_transitions:
            # Find cores used by conflicting transitions
            used_cores = set()
            for conflicting_trans in conflict_graph[trans_name]:
                if conflicting_trans in assignments:
                    used_cores.add(assignments[conflicting_trans])
            
            # If there are no conflicts, distribute across cores for load balancing
            if not used_cores:
                # Count current assignments per core
                core_counts = {}
                for core in range(num_cores):
                    core_counts[core] = 0
                
                for assigned_core in assignments.values():
                    if assigned_core < num_cores:
                        core_counts[assigned_core] += 1
                
                # Assign to the core with the least work
                core = min(core_counts.keys(), key=lambda c: core_counts[c])
            else:
                # Find the lowest available core not used by conflicts
                core = 0
                while core in used_cores and core < num_cores:
                    core += 1
                
                # If all cores are used by conflicts, use round-robin assignment
                if core >= num_cores:
                    # Count assignments per core excluding conflicts
                    core_counts = {}
                    for c in range(num_cores):
                        if c not in used_cores:
                            core_counts[c] = sum(1 for assigned_core in assignments.values() if assigned_core == c)
                    
                    if core_counts:
                        core = min(core_counts.keys(), key=lambda c: core_counts[c])
                    else:
                        # All cores have conflicts, use modulo assignment
                        core = len(assignments) % num_cores
            
            assignments[trans_name] = core
        
        return assignments
    
    def generate_shared_rom(self):
        """
        Generate a single shared ROM that all CPU cores can access.
        Each CPU maintains its own PC (Program Counter) to track execution position.
        
        The ROM contains:
        1. All transition assembly code with labels
        2. Synchronization checks for Petri net semantics
        3. Jump targets that any CPU can reach
        
        Returns:
            List of assembly instructions forming the shared ROM
        """
        if not self.cpu_assignments:
            raise RuntimeError("CPU cores not assigned. Call assign_cpu_cores() first.")
        
        shared_rom = []
        
        # Add initialization code
        shared_rom.append("// Shared ROM for multi-CPU Petri net execution")
        shared_rom.append("// Each CPU has its own PC register")
        shared_rom.append("")
        
        # Generate ROM sections for each CPU core's transitions
        # But place them all in the shared ROM space
        for core in range(self.cpu_cores):
            core_transitions = [
                trans_name for trans_name, assigned_core in self.cpu_assignments.items()
                if assigned_core == core
            ]
            
            if not core_transitions:
                continue
            
            # Sort transitions by level within each core
            core_transitions.sort(key=lambda t: self.transition_levels.get(t, 0))
            
            shared_rom.append(f"// === CPU Core {core} Transitions ===")
            shared_rom.append(f"(CORE_{core}_START)")
            
            for trans_name in core_transitions:
                transition = self.transitions[trans_name]
                
                # Add transition label
                shared_rom.append(f"({trans_name})")
                
                # Add synchronization check
                sync_check = self._generate_sync_check(transition)
                shared_rom.extend(sync_check)
                
                # Add the transition's assembly code
                assembly = transition.emit_assembly()
                if isinstance(assembly, list):
                    shared_rom.extend(assembly)
                else:
                    shared_rom.append(assembly)
                
                # Add synchronization signal
                sync_signal = self._generate_sync_signal(transition)
                shared_rom.extend(sync_signal)
                
                shared_rom.append("")  # Blank line for readability
        
        # Add all labels from the label registry
        if hasattr(self, 'labels'):
            shared_rom.append("// === Program Labels ===")
            for label_name, label_place in self.labels.items():
                shared_rom.append(f"({label_name})")
        
        # Add CPU-specific entry points
        shared_rom.append("// === CPU Entry Points ===")
        for core in range(self.cpu_cores):
            shared_rom.append(f"(CPU_{core}_ENTRY)")
            shared_rom.append(f"@CORE_{core}_START")
            shared_rom.append("0;JMP")
        
        return shared_rom
    
    def generate_roms(self):
        """
        Generate ROM programs for each CPU core.
        
        With shared ROM architecture:
        - Returns a single shared ROM that all cores can access
        - Each core gets an entry point in the shared ROM
        - Cores use individual PC registers to track their position
        """
        if not self.cpu_assignments:
            raise RuntimeError("CPU cores not assigned. Call assign_cpu_cores() first.")
        
        # Generate the shared ROM
        shared_rom = self.generate_shared_rom()
        
        # Return the shared ROM for all cores
        # Each core will start at its own entry point: CPU_0_ENTRY, CPU_1_ENTRY, etc.
        roms = {}
        for core in range(self.cpu_cores):
            # Each core gets the same shared ROM but starts at different entry point
            roms[core] = [
                f"// CPU {core} - Shared ROM with individual PC",
                f"@CPU_{core}_ENTRY",
                "0;JMP"
            ] + shared_rom
        
        return roms
    
    def _generate_core_rom(self, transition_names):
        """
        Generate ROM program for a specific core's transitions.
        """
        rom = []
        
        for trans_name in transition_names:
            transition = self.transitions[trans_name]
            
            # Add synchronization check (wait for input places to have tokens)
            rom.extend(self._generate_sync_check(transition))
            
            # Add the transition's assembly code
            assembly = transition.emit_assembly()
            if isinstance(assembly, list):
                rom.extend(assembly)
            else:
                rom.append(assembly)
            
            # Add synchronization signal (mark output places as ready)
            rom.extend(self._generate_sync_signal(transition))
        
        return rom
    
    def _generate_sync_check(self, transition):
        """
        Generate assembly code to check if transition can fire.
        Wait for all input places to have tokens.
        """
        sync_code = []
        
        if not transition.in_places:
            return sync_code
        
        # For each input place, check if it has a token
        for place in transition.in_places:
            if place.name == "init":
                continue  # Init place is always ready
            
            # Wait loop for this place to be ready
            sync_code.append(f"// Wait for {place.name}")
            sync_code.append(f"({place.name}_WAIT)")
            if place.memory_address is not None:
                sync_code.append(f"@R{place.memory_address + 1000}")  # Use high memory for flags
                sync_code.append("D=M")
                sync_code.append(f"@{place.name}_WAIT")
                sync_code.append("D;JEQ")  # Jump back if not ready
        
        return sync_code
    
    def _generate_sync_signal(self, transition):
        """
        Generate assembly code to signal that transition has completed.
        Mark output places as having tokens.
        """
        sync_code = []
        
        # For each output place, set its ready flag
        for place in transition.out_places:
            sync_code.append(f"// Signal {place.name} ready")
            if place.memory_address is not None:
                sync_code.append("@1")  # Set ready flag
                sync_code.append("D=A")
                sync_code.append(f"@R{place.memory_address + 1000}")  # Use high memory for flags
                sync_code.append("M=D")
        
        return sync_code