from .Place import Place
from .Transition import Transition

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = {}
        self.arcs = []
        self._potentially_enabled = set()  # Transitions that might be enabled
        self._initialized = False
        
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
            # Register this transition as a consumer of the place
            source.consumers.append(target)
    
    def initialize_enabled_set(self):
        """Initialize the set of potentially enabled transitions based on current tokens."""
        self._potentially_enabled = set()
        for place in self.places.values():
            if place.has:
                for consumer in place.consumers:
                    self._potentially_enabled.add(consumer.name)
        self._initialized = True
    
    def notify_token_added(self, place):
        """Called when a token is added to a place - mark consumers as potentially enabled."""
        for consumer in place.consumers:
            self._potentially_enabled.add(consumer.name)
    
    def execute_step(self):
        """Execute one step of the Petri net using event-driven approach."""
        if not self._initialized:
            self.initialize_enabled_set()
        
        # Check only potentially enabled transitions
        enabled = []
        still_potentially_enabled = set()
        
        for trans_name in self._potentially_enabled:
            transition = self.transitions[trans_name]
            if transition.can_fire():
                enabled.append(transition)
            else:
                # Check if it still has potential (at least one input has token)
                if any(p.has for p in transition.in_places):
                    still_potentially_enabled.add(trans_name)
        
        # Fire all enabled transitions
        fired = []
        for transition in enabled:
            # Double-check before firing (another transition might have stolen token)
            if transition.can_fire():
                transition.fire()
                fired.append(transition.name)
                
                # Add consumers of output places to potentially enabled set
                for out_place in transition.out_places:
                    if out_place.has:
                        for consumer in out_place.consumers:
                            still_potentially_enabled.add(consumer.name)
        
        self._potentially_enabled = still_potentially_enabled
        return fired
    
    def execute_step_single(self):
        """Execute one transition (first enabled) - more deterministic."""
        if not self._initialized:
            self.initialize_enabled_set()
        
        # Find first enabled transition from potentially enabled set
        for trans_name in list(self._potentially_enabled):
            transition = self.transitions[trans_name]
            if transition.can_fire():
                transition.fire()
                
                # Update potentially enabled set
                # Remove this transition if its inputs are now empty
                if not all(p.has for p in transition.in_places):
                    self._potentially_enabled.discard(trans_name)
                
                # Add consumers of output places
                for out_place in transition.out_places:
                    if out_place.has:
                        for consumer in out_place.consumers:
                            self._potentially_enabled.add(consumer.name)
                
                return [trans_name]
            else:
                # Check if still potentially enabled
                if not any(p.has for p in transition.in_places):
                    self._potentially_enabled.discard(trans_name)
        
        return []

    # High memory base for place storage (below screen at 16384)
    # This leaves room for stack (256-2047) and heap (2048-~16000)
    PLACE_MEMORY_BASE = 15000
    
    def allocate_memory(self, start_address=None, verbose=False):
        """
        Proper memory allocation with liveness analysis and interference detection.
        Uses graph coloring to assign memory slots safely.
        
        Places are allocated in high memory (starting at PLACE_MEMORY_BASE by default)
        to avoid conflicts with:
        - Special registers (0-15)
        - Static variables (16-255) 
        - Stack (256-2047)
        - Heap (2048+)
        
        Args:
            start_address: Starting address for place memory (default: PLACE_MEMORY_BASE)
            verbose: Print debug info
            
        Returns:
            Number of slots used
        """
        if start_address is None:
            start_address = self.PLACE_MEMORY_BASE
            
        # Reset all memory addresses
        for place in self.places.values():
            place.memory_address = None
        
        # Step 1: Perform liveness analysis to find interference
        if verbose:
            print(f"  Building interference graph for {len(self.places)} places...")
        interference_graph = self._build_interference_graph(verbose=verbose)
        if verbose:
            total_edges = sum(len(v) for v in interference_graph.values()) // 2
            print(f"  Interference graph has {total_edges} edges")
        
        # Step 2: Use graph coloring to assign memory slots
        if verbose:
            print(f"  Coloring interference graph...")
        slot_assignment = self._color_interference_graph(interference_graph, verbose=verbose)
        if verbose:
            print(f"  Assigned {len(slot_assignment)} places to slots")
        
        # Step 3: Assign memory addresses based on coloring (offset by start_address)
        max_slot = 0
        for place_name, slot in slot_assignment.items():
            self.places[place_name].memory_address = start_address + slot
            max_slot = max(max_slot, slot)
        
        if verbose:
            print(f"  Memory range: {start_address} - {start_address + max_slot}")
            if start_address + max_slot >= 16384:
                print(f"  WARNING: Place memory overlaps with screen memory!")
        
        return max_slot + 1
    
    def _build_interference_graph(self, verbose=False):
        """
        Build interference graph: places that can be alive simultaneously
        must have different memory slots (connected by edges)
        """
        interference = {name: set() for name in self.places.keys()}
        
        if verbose:
            print(f"    Analyzing {len(self.transitions)} transitions for interference...")
        
        # For each transition, analyze which places can be alive together
        for idx, transition in enumerate(self.transitions.values()):
            if verbose and idx % 1000 == 0 and idx > 0:
                print(f"    Processed {idx}/{len(self.transitions)} transitions...")
            
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
        if verbose:
            print(f"    Analyzing parallel paths...")
        self._analyze_parallel_paths(interference, verbose=verbose)
        
        return interference
    
    def _analyze_parallel_paths(self, interference, verbose=False):
        """
        Analyze parallel execution paths and pipeline overlaps to find additional interferences.
        """
        # 1. Fork analysis: Places in different branches of a fork can be alive simultaneously
        fork_count = 0
        total_branch_pairs = 0
        for idx, transition in enumerate(self.transitions.values()):
            if verbose and idx % 500 == 0 and idx > 0:
                print(f"    Fork analysis: processed {idx}/{len(self.transitions)} transitions...")
            
            if len(transition.out_places) > 1:
                fork_count += 1
                branches = []
                for output_place in transition.out_places:
                    branch_places = self._get_reachable_places(output_place.name, max_depth=3)
                    branches.append(branch_places)
                
                # Places in different branches can be alive simultaneously
                for i, branch1 in enumerate(branches):
                    for j, branch2 in enumerate(branches):
                        if i < j:
                            total_branch_pairs += len(branch1) * len(branch2)
                            for place1 in branch1:
                                for place2 in branch2:
                                    interference[place1].add(place2)
                                    interference[place2].add(place1)
        
        if verbose:
            print(f"    Analyzed {fork_count} fork transitions, {total_branch_pairs} branch place pairs")
        
        # 2. Pipeline analysis: Adjacent stages in a pipeline can overlap during execution
        if verbose:
            print(f"    Analyzing pipeline overlaps...")
        self._analyze_pipeline_overlaps(interference, verbose=verbose)
    
    def _analyze_pipeline_overlaps(self, interference, verbose=False):
        """
        In pipelined execution, adjacent stages can be active simultaneously.
        For example: A->T1->B->T2->C, when T2 fires, both B and C can be active.
        """
        # Find all linear chains (pipelines)
        if verbose:
            print(f"    Finding linear chains...")
        chains = self._find_linear_chains()
        if verbose:
            print(f"    Found {len(chains)} chains")
        
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
    
    def _color_interference_graph(self, interference, verbose=False):
        """
        Use graph coloring to assign memory slots.
        Places connected by edges get different colors (slots).
        """
        place_names = list(self.places.keys())
        coloring = {}
        
        # Sort places by degree (most constrained first)
        if verbose:
            print(f"    Sorting {len(place_names)} places by degree...")
        sorted_places = sorted(place_names, 
                             key=lambda p: len(interference[p]), 
                             reverse=True)
        
        if verbose:
            print(f"    Assigning colors...")
        
        for idx, place in enumerate(sorted_places):
            if verbose and idx % 1000 == 0 and idx > 0:
                print(f"    Colored {idx}/{len(sorted_places)} places...")
            
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
    def assign_cpu_cores(self, num_cores, verbose=False):
        """
        Assign CPU cores to transitions using graph coloring based on level system.
        Transitions at the same level that can execute in parallel get different cores.
        """
        self.cpu_cores = num_cores
        
        # Step 1: Compute levels for all transitions
        if verbose:
            print(f"  Computing transition levels for {len(self.transitions)} transitions...")
        self._compute_transition_levels(verbose=verbose)
        if verbose:
            print(f"  Computed {len(self.transition_levels)} levels")
        
        # Step 2: Build conflict graph for transitions at each level
        if verbose:
            print(f"  Building conflict graph...")
        conflict_graph = self._build_transition_conflict_graph(verbose=verbose)
        if verbose:
            total_conflicts = sum(len(v) for v in conflict_graph.values()) // 2
            print(f"  Found {total_conflicts} conflict pairs")
        
        # Step 3: Use graph coloring to assign CPU cores
        if verbose:
            print(f"  Coloring graph with {num_cores} cores...")
        self.cpu_assignments = self._color_transition_graph(conflict_graph, num_cores, verbose=verbose)
        if verbose:
            print(f"  Assigned {len(self.cpu_assignments)} transitions to cores")
        
        return self.cpu_assignments
    
    def _compute_transition_levels(self, verbose=False):
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
        
        if verbose:
            print(f"    Found {len(start_transitions)} starting transitions")
        
        # Use a simpler approach: assign levels based on topological order
        # For cycles (from goto/label), just use the first visit level
        visited = set()
        queue = [(t, 0) for t in start_transitions]
        
        while queue:
            transition, level = queue.pop(0)
            
            if transition.name in visited:
                continue  # Skip already visited (handles cycles)
            
            visited.add(transition.name)
            self.transition_levels[transition.name] = level
            
            # Add successor transitions to queue
            for successor in self._get_successor_transitions(transition):
                if successor.name not in visited:
                    queue.append((successor, level + 1))
        
        # Assign level 0 to any unvisited transitions (disconnected or only reachable via back-edges)
        for trans_name in self.transitions.keys():
            if trans_name not in self.transition_levels:
                self.transition_levels[trans_name] = 0
        
        if verbose:
            max_level = max(self.transition_levels.values()) if self.transition_levels else 0
            print(f"    Assigned levels 0-{max_level} to {len(self.transition_levels)} transitions")
    
    def _get_successor_transitions(self, transition):
        """Get transitions that can execute after the given transition"""
        successors = []
        
        # Find transitions that consume from this transition's output places
        for output_place in transition.out_places:
            for other_transition in self.transitions.values():
                if output_place in other_transition.in_places:
                    successors.append(other_transition)
        
        return successors
    
    def _build_transition_conflict_graph(self, verbose=False):
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
        
        if verbose:
            print(f"    Grouped into {len(levels)} levels")
            max_level_size = max(len(v) for v in levels.values()) if levels else 0
            print(f"    Largest level has {max_level_size} transitions")
        
        # For each level, find conflicts between transitions
        comparisons = 0
        for level, trans_names in levels.items():
            level_size = len(trans_names)
            if verbose and level_size > 100:
                print(f"    Processing level {level} with {level_size} transitions...")
            
            for i, trans1_name in enumerate(trans_names):
                for j, trans2_name in enumerate(trans_names):
                    if i < j:  # Only check each pair once
                        comparisons += 1
                        trans1 = self.transitions[trans1_name]
                        trans2 = self.transitions[trans2_name]
                        
                        # Check for resource conflicts
                        if self._transitions_conflict(trans1, trans2):
                            conflict_graph[trans1_name].add(trans2_name)
                            conflict_graph[trans2_name].add(trans1_name)
        
        if verbose:
            print(f"    Made {comparisons} pairwise comparisons")
        
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
    
    def _color_transition_graph(self, conflict_graph, num_cores, verbose=False):
        """
        Use graph coloring to assign CPU cores to transitions.
        Conflicting transitions get different cores (colors).
        Also distribute non-conflicting transitions across cores for load balancing.
        With shared ROM, control flow operations can be on any core.
        """
        assignments = {}
        
        # Sort transitions by conflict degree (most constrained first), then by level
        if verbose:
            print(f"    Sorting {len(self.transitions)} transitions...")
        sorted_transitions = sorted(self.transitions.keys(),
                                  key=lambda t: (len(conflict_graph[t]), self.transition_levels.get(t, 0)),
                                  reverse=True)
        
        if verbose:
            print(f"    Assigning cores...")
        
        for idx, trans_name in enumerate(sorted_transitions):
            if verbose and idx % 1000 == 0 and idx > 0:
                print(f"    Assigned {idx}/{len(sorted_transitions)} transitions...")
            
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
        Generate optimized ROM programs with shared code segments.
        
        This method:
        1. Generates assembly for each transition
        2. Finds common instruction sequences across transitions
        3. Creates shared ROM segments for common code
        4. Returns per-core ROMs that reference shared segments
        
        Returns:
            Dictionary with:
            - 'shared': List of shared ROM segments (common code)
            - 'cores': Dictionary mapping core_id to core-specific ROM
            - 'stats': Statistics about ROM sharing
        """
        if not self.cpu_assignments:
            raise RuntimeError("CPU cores not assigned. Call assign_cpu_cores() first.")
        
        # Step 1: Generate assembly for each transition
        transition_assembly = {}
        for trans_name, transition in self.transitions.items():
            assembly = transition.emit_assembly()
            if isinstance(assembly, str):
                assembly = [assembly]
            transition_assembly[trans_name] = assembly
        
        # Step 2: Find common instruction sequences
        shared_segments, segment_refs = self._find_shared_segments(transition_assembly)
        
        # Step 3: Generate optimized ROMs
        roms = self._generate_optimized_roms(transition_assembly, shared_segments, segment_refs)
        
        return roms
    
    def _find_shared_segments(self, transition_assembly, min_length=4):
        """
        Find common instruction sequences that can be shared across transitions.
        
        Args:
            transition_assembly: Dict mapping transition name to assembly list
            min_length: Minimum sequence length to consider for sharing (default 4 to ensure savings)
        
        Returns:
            shared_segments: Dict mapping segment_id to instruction list
            segment_refs: Dict mapping (trans_name, start_idx) to segment_id
        """
        shared_segments = {}
        segment_refs = {}
        segment_id = 0
        
        # Build a map of instruction sequences to transitions that use them
        sequence_map = {}  # tuple(instructions) -> [(trans_name, start_idx), ...]
        
        for trans_name, assembly in transition_assembly.items():
            # Look for sequences of min_length or more
            for length in range(min_length, len(assembly) + 1):
                for start in range(len(assembly) - length + 1):
                    seq = tuple(assembly[start:start + length])
                    
                    # Skip sequences with labels (they're position-dependent)
                    if any(line.strip().startswith('(') for line in seq):
                        continue
                    
                    # Skip sequences that are just comments
                    if all(line.strip().startswith('//') or not line.strip() for line in seq):
                        continue
                    
                    if seq not in sequence_map:
                        sequence_map[seq] = []
                    sequence_map[seq].append((trans_name, start))
        
        # Find sequences used by multiple transitions
        for seq, usages in sequence_map.items():
            # Get unique transitions using this sequence
            unique_trans = set(trans for trans, _ in usages)
            
            # Only share if savings > overhead (call takes ~4 instructions)
            # Savings = (len(seq) - 4) * (num_usages - 1)
            call_overhead = 4
            potential_savings = (len(seq) - call_overhead) * (len(unique_trans) - 1)
            
            if len(unique_trans) >= 2 and potential_savings > 0:
                # This sequence is shared - create a shared segment
                seg_name = f"SHARED_{segment_id}"
                shared_segments[seg_name] = list(seq)
                
                # Record references
                for trans_name, start_idx in usages:
                    segment_refs[(trans_name, start_idx, len(seq))] = seg_name
                
                segment_id += 1
        
        # Remove overlapping/subsumed segments (keep longest)
        segment_refs = self._remove_overlapping_segments(segment_refs)
        
        return shared_segments, segment_refs
    
    def _remove_overlapping_segments(self, segment_refs):
        """Remove overlapping segment references, keeping the longest ones."""
        # Group by transition
        by_trans = {}
        for (trans_name, start, length), seg_name in segment_refs.items():
            if trans_name not in by_trans:
                by_trans[trans_name] = []
            by_trans[trans_name].append((start, length, seg_name))
        
        # For each transition, remove overlapping segments
        cleaned_refs = {}
        for trans_name, segments in by_trans.items():
            # Sort by length descending, then start ascending
            segments.sort(key=lambda x: (-x[1], x[0]))
            
            used_ranges = []
            for start, length, seg_name in segments:
                end = start + length
                
                # Check if this overlaps with any used range
                overlaps = False
                for used_start, used_end in used_ranges:
                    if not (end <= used_start or start >= used_end):
                        overlaps = True
                        break
                
                if not overlaps:
                    used_ranges.append((start, end))
                    cleaned_refs[(trans_name, start, length)] = seg_name
        
        return cleaned_refs
    
    def _generate_optimized_roms(self, transition_assembly, shared_segments, segment_refs):
        """
        Generate optimized ROMs with level-based execution loop.
        
        The execution model:
        1. Group transitions by level
        2. For each level, all assigned transitions on a core execute
        3. After each level, synchronize before moving to next level
        4. Loop through all levels until complete
        
        Returns:
            Dictionary with 'shared', 'cores', and 'stats' keys
        """
        # Build shared ROM section
        shared_rom = []
        shared_rom.append("// === SHARED CODE SEGMENTS ===")
        shared_rom.append("// Common instruction sequences used by multiple transitions")
        shared_rom.append("")
        
        for seg_name, instructions in shared_segments.items():
            shared_rom.append(f"({seg_name})")
            shared_rom.extend(instructions)
            shared_rom.append(f"({seg_name}_RET)")  # Return point label
            shared_rom.append("")
        
        # Group transitions by level
        levels = {}
        for trans_name, level in self.transition_levels.items():
            if level not in levels:
                levels[level] = []
            levels[level].append(trans_name)
        
        max_level = max(levels.keys()) if levels else 0
        
        # Build per-core ROMs with execution loop
        core_roms = {}
        total_original = 0
        total_optimized = 0
        
        for core in range(self.cpu_cores):
            core_transitions = [
                trans_name for trans_name, assigned_core in self.cpu_assignments.items()
                if assigned_core == core
            ]
            
            if not core_transitions:
                core_roms[core] = [f"// CPU {core} - No transitions assigned"]
                continue
            
            # Group this core's transitions by level
            core_levels = {}
            for trans_name in core_transitions:
                level = self.transition_levels.get(trans_name, 0)
                if level not in core_levels:
                    core_levels[level] = []
                core_levels[level].append(trans_name)
            
            rom = []
            rom.append(f"// CPU {core} ROM - {len(core_transitions)} transitions across {len(core_levels)} levels")
            rom.append(f"(CORE_{core}_START)")
            rom.append("")
            
            # Generate code for each level in order
            for level in range(max_level + 1):
                level_transitions = core_levels.get(level, [])
                
                if not level_transitions:
                    continue
                
                rom.append(f"// === Level {level} ===")
                rom.append(f"(CORE_{core}_LEVEL_{level})")
                
                for trans_name in level_transitions:
                    transition = self.transitions[trans_name]
                    assembly = transition_assembly[trans_name]
                    
                    total_original += len(assembly)
                    
                    rom.append(f"// Transition: {trans_name}")
                    rom.append(f"({trans_name})")
                    
                    # Add the transition's assembly code
                    optimized_assembly = self._replace_with_shared_calls(
                        trans_name, assembly, segment_refs
                    )
                    rom.extend(optimized_assembly)
                    total_optimized += len(optimized_assembly)
                    
                    rom.append("")
                
                # After all transitions at this level, signal level complete
                rom.append(f"// Level {level} complete - signal ready for next level")
                rom.append(f"@1")
                rom.append(f"D=A")
                rom.append(f"@R{13 + core}")  # Use R13-R20 for core level flags
                rom.append(f"M=D")
                rom.append("")
            
            # End of execution
            rom.append(f"(CORE_{core}_END)")
            rom.append(f"@CORE_{core}_END")
            rom.append("0;JMP")
            
            core_roms[core] = rom
        
        # Calculate stats
        stats = {
            'shared_segments': len(shared_segments),
            'total_shared_instructions': sum(len(s) for s in shared_segments.values()),
            'original_instructions': total_original,
            'optimized_instructions': total_optimized,
            'savings_percent': ((total_original - total_optimized) / max(total_original, 1)) * 100,
            'num_levels': max_level + 1
        }
        
        return {
            'shared': shared_rom,
            'cores': core_roms,
            'stats': stats
        }
    
    def _replace_with_shared_calls(self, trans_name, assembly, segment_refs):
        """
        Replace instruction sequences with calls to shared segments.
        """
        # Find segments for this transition
        trans_segments = []
        for (t_name, start, length), seg_name in segment_refs.items():
            if t_name == trans_name:
                trans_segments.append((start, length, seg_name))
        
        if not trans_segments:
            return assembly
        
        # Sort by start position
        trans_segments.sort(key=lambda x: x[0])
        
        # Build optimized assembly
        result = []
        current_pos = 0
        
        for start, length, seg_name in trans_segments:
            # Add instructions before this segment
            result.extend(assembly[current_pos:start])
            
            # Add call to shared segment
            result.append(f"// Call shared segment {seg_name}")
            result.append(f"@{seg_name}")
            result.append("0;JMP")
            result.append(f"({trans_name}_{seg_name}_RETURN)")
            
            current_pos = start + length
        
        # Add remaining instructions
        result.extend(assembly[current_pos:])
        
        return result
    
    def get_shareable_transitions(self):
        """
        Analyze which transitions can share ROM segments.
        
        Returns a graph showing which transitions have common code
        that could be shared.
        """
        # Generate assembly for each transition
        transition_assembly = {}
        for trans_name, transition in self.transitions.items():
            assembly = transition.emit_assembly()
            if isinstance(assembly, str):
                assembly = [assembly]
            transition_assembly[trans_name] = assembly
        
        # Build sharing graph
        sharing_graph = {name: set() for name in self.transitions.keys()}
        
        # Compare each pair of transitions
        trans_names = list(transition_assembly.keys())
        for i, trans1 in enumerate(trans_names):
            for trans2 in trans_names[i+1:]:
                asm1 = transition_assembly[trans1]
                asm2 = transition_assembly[trans2]
                
                # Find common subsequences
                common = self._find_common_subsequences(asm1, asm2)
                
                if common:
                    sharing_graph[trans1].add(trans2)
                    sharing_graph[trans2].add(trans1)
        
        return sharing_graph
    
    def _find_common_subsequences(self, asm1, asm2, min_length=3):
        """Find common instruction subsequences between two assembly lists."""
        common = []
        
        for i in range(len(asm1)):
            for j in range(len(asm2)):
                # Find longest common sequence starting at i, j
                length = 0
                while (i + length < len(asm1) and 
                       j + length < len(asm2) and
                       asm1[i + length] == asm2[j + length]):
                    length += 1
                
                if length >= min_length:
                    common.append(asm1[i:i+length])
        
        return common
    
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