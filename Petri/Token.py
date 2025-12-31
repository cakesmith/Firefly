"""
Token represents a value flowing through the Petri net.
Each token carries a value payload and represents an independent thread of execution.
"""

class Token:
    def __init__(self, value=None, metadata=None):
        self.value = value
        self.metadata = metadata or {}
        
    def __repr__(self):
        return f"Token({self.value}, metadata={self.metadata})"
        
    def __str__(self):
        return str(self.value)