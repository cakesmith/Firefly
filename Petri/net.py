class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = {}
        self.arcs = []
        
    def add_place(self, name):
        from .Place import Place
        place = Place(name)
        self.places[name] = place
        return place
        
    def add_transition(self, name, operation=None):
        from .Transition import Transition
        transition = Transition(name, operation)
        self.transitions[name] = transition
        return transition
        
    def add_arc(self, source, target):
        """Add arc between place and transition or transition and place"""
        self.arcs.append((source.name, target.name))
        
        # Handle different connection types
        if hasattr(source, 'tokens'):  # source is a Place
            source.connect_to_transition(target)
        else:  # source is a Transition
            source.connect_to_place(target)
        
    def execute_step(self):
        """Execute one step of the Petri net"""
        fired = []
        for transition in self.transitions.values():
            if transition.can_fire():
                transition.fire()
                fired.append(transition.name)
        return fired