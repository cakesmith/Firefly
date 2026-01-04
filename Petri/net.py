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
        Build interference graph using happens-before analysis.
        
        Two places DON'T interfere only if one is ALWAYS consumed before the other
        is produced (strict ordering). Otherwise, they might be alive together.
        
        This is conservative but correct - we only allow memory sharing when
        we can PROVE the places can't be alive simultaneously.
        """
        place_names = list(self.places.keys())
        num_places = len(place_names)
        
        if verbose:
            print(f"    Computing happens-before ordering for {num_places} places...")
        
        # Build lookup tables
        place_to_consumers = {name: [] for name in place_names}
        place_to_producers = {name: [] for name in place_names}
        
        for transition in self.transitions.values():
            for p in transition.in_places:
                place_to_consumers[p.name].append(transition)
            for p in transition.out_places:
                place_to_producers[p.name].append(transition)
        
        # Compute "happens-before" relation using topological ordering
        # Place A happens-before Place B if A must be consumed before B is produced
        happens_before = self._compute_happens_before(place_to_consumers, place_to_producers, verbose)
        
        # Build interference: places interfere unless one strictly happens-before the other
        interference = {name: set() for name in place_names}
        
        if verbose:
            print(f"    Building interference from ordering...")
        
        for i, p1 in enumerate(place_names):
            for j, p2 in enumerate(place_names):
                if i < j:
                    # Places interfere unless one strictly precedes the other
                    p1_before_p2 = p2 in happens_before.get(p1, set())
                    p2_before_p1 = p1 in happens_before.get(p2, set())
                    
                    if not p1_before_p2 and not p2_before_p1:
                        # No ordering - they can be alive together
                        interference[p1].add(p2)
                        interference[p2].add(p1)
        
        if verbose:
            total_edges = sum(len(v) for v in interference.values()) // 2
            print(f"    Interference graph has {total_edges} edges")
        
        return interference
    
    def _compute_happens_before(self, place_to_consumers, place_to_producers, verbose=False):
        """
        Compute happens-before relation between places.
        
        Place A happens-before Place B if:
        - A is consumed by a transition T, and
        - B is produced by T or by a transition reachable from T's outputs
        
        Returns dict mapping place -> set of places that happen after it.
        """
        happens_after = {name: set() for name in self.places.keys()}
        
        # For each place, find all places that are produced after it's consumed
        for place_name in self.places.keys():
            # Find transitions that consume this place
            consumers = place_to_consumers.get(place_name, [])
            
            for consumer_trans in consumers:
                # All outputs of this transition happen after this place
                for out_place in consumer_trans.out_places:
                    happens_after[place_name].add(out_place.name)
                
                # Transitively, anything reachable from outputs also happens after
                visited = set()
                frontier = [p.name for p in consumer_trans.out_places]
                
                while frontier:
                    current = frontier.pop()
                    if current in visited:
                        continue
                    visited.add(current)
                    happens_after[place_name].add(current)
                    
                    # Follow consumers of current place
                    for trans in place_to_consumers.get(current, []):
                        for out_p in trans.out_places:
                            if out_p.name not in visited:
                                frontier.append(out_p.name)
        
        return happens_after
    
    def _analyze_parallel_paths_optimized(self, interference, place_to_consumers, place_to_producers, verbose=False):
        """
        Optimized parallel path analysis using pre-built lookup tables.
        
        CRITICAL: For correctness, we need to ensure that places in different
        parallel branches don't share memory. We use a deeper analysis to
        capture all places that can be alive simultaneously.
        """
        num_transitions = len(self.transitions)
        
        # 1. Fork analysis: Places in different branches of a fork can be alive simultaneously
        fork_count = 0
        total_branch_pairs = 0
        
        for idx, transition in enumerate(self.transitions.values()):
            if verbose and idx % 1000 == 0 and idx > 0:
                print(f"    Fork analysis: processed {idx}/{num_transitions} transitions...")
            
            if len(transition.out_places) > 1:
                fork_count += 1
                branches = []
                for output_place in transition.out_places:
                    # Use deeper analysis to capture all reachable places
                    # max_depth=10 should be enough for most computations
                    branch_places = self._get_reachable_places_optimized(
                        output_place.name, place_to_consumers, max_depth=10)
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
        
        # 2. Pipeline analysis: Adjacent stages in a pipeline can overlap
        if verbose:
            print(f"    Analyzing pipeline overlaps...")
        self._analyze_pipeline_overlaps_optimized(interference, place_to_consumers, place_to_producers, verbose=verbose)
    
    def _analyze_pipeline_overlaps_optimized(self, interference, place_to_consumers, place_to_producers, verbose=False):
        """
        Optimized pipeline overlap analysis.
        """
        # Find linear chains using lookup tables
        if verbose:
            print(f"    Finding linear chains...")
        chains = self._find_linear_chains_optimized(place_to_consumers, place_to_producers)
        if verbose:
            print(f"    Found {len(chains)} chains")
        
        for chain in chains:
            # In a pipeline, adjacent places can be alive simultaneously
            for i in range(len(chain) - 1):
                place1 = chain[i]
                place2 = chain[i + 1]
                interference[place1].add(place2)
                interference[place2].add(place1)
    
    def _get_reachable_places_optimized(self, start_place, place_to_consumers, max_depth=2):
        """Get places reachable from start_place using pre-built lookup table."""
        if max_depth <= 0:
            return {start_place}
        
        reachable = {start_place}
        current_level = {start_place}
        
        for depth in range(max_depth):
            next_level = set()
            for place_name in current_level:
                # Use lookup table instead of scanning all transitions
                for transition in place_to_consumers.get(place_name, []):
                    for output_place in transition.out_places:
                        if output_place.name not in reachable:
                            next_level.add(output_place.name)
                            reachable.add(output_place.name)
            
            if not next_level:
                break
            current_level = next_level
        
        return reachable
    
    def _find_linear_chains_optimized(self, place_to_consumers, place_to_producers):
        """Find linear chains using pre-built lookup tables."""
        chains = []
        visited = set()
        
        # Start from places with no predecessors (using lookup table)
        start_places = [name for name, producers in place_to_producers.items() if not producers]
        
        # Trace each chain from start places
        for start_place in start_places:
            if start_place not in visited:
                chain = self._trace_linear_chain_optimized(start_place, visited, place_to_consumers)
                if len(chain) > 1:
                    chains.append(chain)
        
        return chains
    
    def _trace_linear_chain_optimized(self, start_place, visited, place_to_consumers):
        """Trace a linear chain using pre-built lookup table."""
        chain = [start_place]
        visited.add(start_place)
        current_place = start_place
        
        while True:
            next_places = []
            
            # Use lookup table
            for transition in place_to_consumers.get(current_place, []):
                if (len(transition.in_places) == 1 and len(transition.out_places) == 1):
                    next_place = transition.out_places[0].name
                    if next_place not in visited:
                        next_places.append(next_place)
            
            if len(next_places) == 1:
                next_place = next_places[0]
                chain.append(next_place)
                visited.add(next_place)
                current_place = next_place
            else:
                break
        
        return chain
    
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
        
        Level = max(predecessor levels) + 1
        This ensures a transition is at a higher level than ALL its predecessors.
        """
        self.transition_levels = {}
        
        # Build predecessor map: transition -> list of predecessor transitions
        predecessors = {t.name: [] for t in self.transitions.values()}
        for transition in self.transitions.values():
            for successor in self._get_successor_transitions(transition):
                predecessors[successor.name].append(transition.name)
        
        # Find starting transitions (no predecessors or only from init)
        start_transitions = []
        for trans_name, preds in predecessors.items():
            if not preds:
                start_transitions.append(trans_name)
        
        if verbose:
            print(f"    Found {len(start_transitions)} starting transitions")
        
        # Compute levels using dynamic programming
        # Level of a transition = max(level of predecessors) + 1
        def compute_level(trans_name, visited_stack=None):
            if visited_stack is None:
                visited_stack = set()
            
            # Already computed
            if trans_name in self.transition_levels:
                return self.transition_levels[trans_name]
            
            # Cycle detection
            if trans_name in visited_stack:
                return 0  # Break cycle with level 0
            
            visited_stack.add(trans_name)
            
            preds = predecessors.get(trans_name, [])
            if not preds:
                level = 0
            else:
                max_pred_level = -1
                for pred in preds:
                    pred_level = compute_level(pred, visited_stack)
                    max_pred_level = max(max_pred_level, pred_level)
                level = max_pred_level + 1
            
            visited_stack.discard(trans_name)
            self.transition_levels[trans_name] = level
            return level
        
        # Compute levels for all transitions
        for trans_name in self.transitions.keys():
            compute_level(trans_name)
        
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
        
        STRATEGY: Only split work across cores when transitions can truly run in parallel
        (same level, no conflicts). Sequential chains stay on the same core to avoid
        inter-core synchronization overhead.
        """
        assignments = {}
        
        # Group transitions by level
        levels = {}
        for trans_name, level in self.transition_levels.items():
            if level not in levels:
                levels[level] = []
            levels[level].append(trans_name)
        
        if verbose:
            print(f"    Processing {len(levels)} levels...")
        
        # Process level by level
        for level in sorted(levels.keys()):
            trans_at_level = levels[level]
            
            # Find independent groups at this level (no conflicts between them)
            # These can be assigned to different cores
            independent_groups = []
            assigned_in_level = set()
            
            for trans_name in trans_at_level:
                if trans_name in assigned_in_level:
                    continue
                
                # Start a new group with this transition
                group = [trans_name]
                assigned_in_level.add(trans_name)
                
                # Find all transitions that conflict with this one (same group)
                for other_trans in trans_at_level:
                    if other_trans in assigned_in_level:
                        continue
                    if other_trans in conflict_graph[trans_name]:
                        # Conflicts - must be on different core, not same group
                        continue
                    # Check if conflicts with anyone in the group
                    conflicts_with_group = False
                    for g_trans in group:
                        if other_trans in conflict_graph[g_trans]:
                            conflicts_with_group = True
                            break
                    if not conflicts_with_group:
                        # Can be in same group (will go to same core)
                        # But we want parallelism, so keep separate
                        pass
                
                independent_groups.append(group)
            
            # Assign each independent transition to a different core (round-robin)
            # This maximizes parallelism at each level
            for i, trans_name in enumerate(trans_at_level):
                # Check if predecessor is assigned - prefer same core to reduce sync
                predecessors_cores = set()
                trans = self.transitions[trans_name]
                for in_place in trans.in_places:
                    for other_trans in self.transitions.values():
                        if in_place in other_trans.out_places and other_trans.name in assignments:
                            predecessors_cores.add(assignments[other_trans.name])
                
                # Check conflicts at this level
                conflicts_cores = set()
                for other_trans in trans_at_level:
                    if other_trans in assignments and other_trans in conflict_graph[trans_name]:
                        conflicts_cores.add(assignments[other_trans])
                
                if len(trans_at_level) > 1 and not conflicts_cores:
                    # Multiple transitions at this level with no conflicts - parallelize
                    core = i % num_cores
                    # Avoid conflict cores
                    while core in conflicts_cores and core < num_cores:
                        core = (core + 1) % num_cores
                elif predecessors_cores and not conflicts_cores:
                    # Has predecessor, no conflicts - use same core as predecessor
                    core = list(predecessors_cores)[0]
                else:
                    # Use round-robin avoiding conflicts
                    core = len(assignments) % num_cores
                    while core in conflicts_cores:
                        core = (core + 1) % num_cores
                
                assignments[trans_name] = core
        
        if verbose:
            # Count per core
            core_counts = {}
            for core in range(num_cores):
                core_counts[core] = sum(1 for c in assignments.values() if c == core)
            print(f"    Core distribution: {core_counts}")
        
        return assignments
    
    def generate_shared_rom(self):
        """
        Generate a single shared ROM for multi-core execution with Petri net semantics.
        
        EVENT-DRIVEN EXECUTION:
        When a transition fires and decrements a consumer's counter, immediately check
        if that counter hit 0. If so, jump directly to check/fire that transition.
        
        This eliminates polling - execution flows directly from producer to consumer
        when data is ready.
        
        Memory layout:
        - R0-R99: Reserved (stack pointers, etc.)
        - R100+i: Countdown counter for transition i (0 = ready to fire)
        - R200+i: Valid flags for places (1 = has token)
        - R15000+: Data slots (allocated by allocate_memory)
        
        Returns:
            Tuple of (assembly_lines, entry_points, initial_valid_addrs, initial_counters)
        """
        if not self.cpu_assignments:
            raise RuntimeError("CPU cores not assigned. Call assign_cpu_cores() first.")
        
        COUNTER_BASE = 1000     # Countdown counters for transitions
        VALID_FLAG_BASE = 2000  # Valid flags for places
        
        # Assign addresses
        trans_list = list(self.transitions.keys())
        trans_counter_addr = {name: COUNTER_BASE + i for i, name in enumerate(trans_list)}
        
        place_valid_addr = {}
        for i, place_name in enumerate(self.places.keys()):
            place_valid_addr[place_name] = VALID_FLAG_BASE + i
        
        # Build consumer map: place -> list of transitions that consume from it
        place_consumers = {p: [] for p in self.places.keys()}
        for trans_name, trans in self.transitions.items():
            for in_place in trans.in_places:
                place_consumers[in_place.name].append(trans_name)
        
        # Initial counter values (will be adjusted for initial marking)
        trans_input_count = {}
        for trans_name, trans in self.transitions.items():
            trans_input_count[trans_name] = len(trans.in_places)
        
        # Find initial marking - adjust counters for places that start with tokens
        initial_marking = []
        for place_name, place in self.places.items():
            if place.has:
                initial_marking.append(place_valid_addr[place_name])
                # Transitions consuming from this place start with counter-1
                for consumer in place_consumers[place_name]:
                    trans_input_count[consumer] -= 1
        
        # Find termination places
        termination_addrs = []
        for place_name in self.places.keys():
            if place_name.startswith('return_dispatch') or place_name == 'end':
                termination_addrs.append(place_valid_addr[place_name])
        
        # Get transition info
        transition_asm = {}
        transition_outputs = {}
        
        for trans_name, trans in self.transitions.items():
            asm = trans.emit_assembly()
            transition_asm[trans_name] = [asm] if isinstance(asm, str) else asm
            
            outputs = [(p.name, p.memory_address, place_valid_addr[p.name]) 
                      for p in trans.out_places]
            transition_outputs[trans_name] = outputs
        
        # Group transitions by core, sorted by level
        core_transitions = {core_id: [] for core_id in range(self.cpu_cores)}
        
        for trans_name, core_id in self.cpu_assignments.items():
            level = self.transition_levels.get(trans_name, 0)
            core_transitions[core_id].append((level, trans_name))
        
        for core_id in core_transitions:
            core_transitions[core_id].sort()
            core_transitions[core_id] = [name for (_, name) in core_transitions[core_id]]
        
        # Build reverse map: transition -> core
        trans_to_core = {t: c for c, ts in core_transitions.items() for t in ts}
        
        # Generate ROM with event-driven execution
        rom_lines = []
        entry_points = {}
        
        def instr_count(lines):
            return sum(1 for l in lines if l.strip() and not l.strip().startswith('//') 
                      and not l.strip().startswith('('))
        
        for core_id in range(self.cpu_cores):
            entry_points[core_id] = instr_count(rom_lines)
            rom_lines.append(f"(CORE_{core_id}_START)")
            
            # Check for termination
            for term_addr in termination_addrs:
                rom_lines.extend([
                    f"@R{term_addr}",
                    "D=M",
                    f"@CORE_{core_id}_HALT",
                    "D;JNE"
                ])
            
            transitions = core_transitions.get(core_id, [])
            
            for idx, trans_name in enumerate(transitions):
                counter_addr = trans_counter_addr[trans_name]
                outputs = transition_outputs.get(trans_name, [])
                input_count = len(self.transitions[trans_name].in_places)
                
                # Label for checking this transition (jump here to check counter + outputs)
                rom_lines.append(f"(CORE_{core_id}_CHECK_{trans_name})")
                
                # Skip label - next transition or loop end
                skip_label = (f"CORE_{core_id}_CHECK_{transitions[idx+1]}" 
                             if idx + 1 < len(transitions) 
                             else f"CORE_{core_id}_LOOP_END")
                
                # Check counter == 0 (ready to fire)
                rom_lines.extend([
                    f"@R{counter_addr}",
                    "D=M",
                    f"@{skip_label}",
                    "D;JNE"  # Skip if counter != 0
                ])
                
                # Check outputs are empty (Petri semantics)
                for place_name, data_addr, valid_addr in outputs:
                    rom_lines.extend([
                        f"@R{valid_addr}",
                        "D=M",
                        f"@{skip_label}",
                        "D;JNE"
                    ])
                
                # FIRE: Reset counter to input count (for re-firing in loops)
                rom_lines.extend([
                    f"@{input_count}",
                    "D=A",
                    f"@R{counter_addr}",
                    "M=D"
                ])
                
                # Execute transition assembly
                rom_lines.extend(transition_asm.get(trans_name, []))
                
                # Set output valid flags AND decrement consumer counters
                # Process ALL outputs first, then check for ready consumers
                for place_name, data_addr, valid_addr in outputs:
                    rom_lines.extend([
                        "@1",
                        "D=A",
                        f"@R{valid_addr}",
                        "M=D"
                    ])
                    
                    # Decrement counters of all consumers
                    for consumer in place_consumers[place_name]:
                        consumer_counter = trans_counter_addr[consumer]
                        rom_lines.extend([
                            f"@R{consumer_counter}",
                            "M=M-1"
                        ])
                
                # Now check if any same-core consumer became ready (counter == 0)
                # Jump to the first one found
                for place_name, data_addr, valid_addr in outputs:
                    for consumer in place_consumers[place_name]:
                        consumer_core = trans_to_core.get(consumer, -1)
                        if consumer_core == core_id:
                            consumer_counter = trans_counter_addr[consumer]
                            rom_lines.extend([
                                f"@R{consumer_counter}",
                                "D=M",
                                f"@CORE_{core_id}_CHECK_{consumer}",
                                "D;JEQ"  # Jump to check if counter == 0
                            ])
            
            # Loop back to start
            rom_lines.extend([
                f"(CORE_{core_id}_LOOP_END)",
                f"@CORE_{core_id}_START",
                "0;JMP",
                f"(CORE_{core_id}_HALT)",
                f"@CORE_{core_id}_HALT",
                "0;JMP"
            ])
        
        # Return initial counter values along with marking
        initial_counters = [(trans_counter_addr[t], trans_input_count[t]) for t in trans_list]
        return rom_lines, entry_points, initial_marking, initial_counters
    
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