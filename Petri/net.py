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
        fired = []
        for transition in self.transitions.values():
            if transition.can_fire():
                transition.fire()
                fired.append(transition.name)
        return fired
    def allocate_memory(self):
        """Simple memory allocation by analyzing graph structure"""
        next_slot = 0
        
        # Start with input places (no incoming arcs)
        for place in self.places.values():
            if not any(place in t.out_places for t in self.transitions.values()):
                # This is an input place
                place.memory_address = next_slot
                next_slot += 1
        
        # Process transitions in order, reusing slots
        for transition in self.transitions.values():
            # Get a free slot from consumed input places
            free_slot = None
            for input_place in transition.in_places:
                if input_place.memory_address is not None:
                    free_slot = input_place.memory_address
                    break
            
            # Assign output places to reused or new slots
            for output_place in transition.out_places:
                if free_slot is not None:
                    output_place.memory_address = free_slot
                    free_slot = None  # Use each free slot only once
                else:
                    output_place.memory_address = next_slot
                    next_slot += 1
                    
        return next_slot