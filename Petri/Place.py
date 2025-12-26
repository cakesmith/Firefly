"""
Place can hold tokens with values.
Each token represents an independent thread of execution.
"""

class Place:
    def __init__(self, name):
        self.name = name
        self.tokens = []  # Can hold multiple tokens
        self.out_transitions = []
        self.in_transitions = []

    def put_token(self, token):
        """Add a token to this place - only one token allowed"""
        if self.has_token():
            # Replace existing token instead of accumulating
            self.tokens = [token]
        else:
            self.tokens.append(token)

    def get_token(self):
        """Remove and return a token from this place"""
        if self.tokens:
            return self.tokens.pop(0)
        return None
        
    def has_token(self):
        """Check if place has at least one token"""
        return len(self.tokens) > 0
        
    def token_count(self):
        """Return number of tokens in this place"""
        return len(self.tokens)

    def connect_to_transition(self, transition):
        """Connect this place as input to a transition"""
        self.out_transitions.append(transition)
        transition.in_places.append(self)
        
    def connect_from_transition(self, transition):
        """Connect this place as output from a transition"""
        self.in_transitions.append(transition)
        transition.out_places.append(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

                