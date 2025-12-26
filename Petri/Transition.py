class Transition:
    def __init__(self, name, operation=None):
        self.name = name
        self.operation = operation  # Function to execute when firing
        self.in_places = []
        self.out_places = []

    def connect_to_place(self, place):
        """Connect this transition output to a place"""
        self.out_places.append(place)
        place.in_transitions.append(self)
        
    def can_fire(self):
        """Check if all input places have tokens"""
        return all(place.has_token() for place in self.in_places)
        
    def fire(self):
        """Execute the transition if it can fire"""
        if not self.can_fire():
            return False
            
        # Consume tokens from input places
        input_tokens = []
        for place in self.in_places:
            token = place.get_token()
            input_tokens.append(token)
            
        # Execute operation if defined
        if self.operation:
            output_tokens = self.operation(input_tokens)
        else:
            # Default: pass through first token
            output_tokens = input_tokens[:1] if input_tokens else [None]
            
        # Produce tokens to output places
        if not isinstance(output_tokens, list):
            output_tokens = [output_tokens]
            
        for i, place in enumerate(self.out_places):
            if i < len(output_tokens):
                place.put_token(output_tokens[i])
                
        return True
    
