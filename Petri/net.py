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