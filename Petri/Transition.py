class Transition:
    def __init__(self, name, operation=None, emit_function=None, assembly_template=None):
        self.name = name
        self.operation = operation  # Function to execute when firing
        self.emit_function = emit_function  # Function to emit assembly code
        self.in_places = []
        self.out_places = []

        
    def can_fire(self):
        """Check if all input places have tokens and no output places have tokens"""
        return (all(place.has for place in self.in_places) and 
                not any(place.has for place in self.out_places))
        
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
            if i < len(output_tokens) and output_tokens[i] is not None:
                place.put_token(output_tokens[i])
                
        return True
    
    def emit_assembly(self, *args, **kwargs):
        """Emit assembly code for this transition"""
        if self.emit_function:
            return self.emit_function(self, *args, **kwargs)
        else:
            return f"// {self.name} - no assembly implementation"