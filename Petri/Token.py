"""
Token represents a value flowing through the Petri net.
Each token carries a value payload and represents an independent thread of execution.
"""

class Token:
    def __init__(self, value=None, level=0, metadata=None):
        self.value = value
        self.level = level  # Execution level for level-based recursion
        self.metadata = metadata or {}
        
    def __repr__(self):
        return f"Token({self.value}, level={self.level})"
        
    def __str__(self):
        return str(self.value)

class ValueToken(Token):
    """Token representing a computed value (final result)"""
    def __init__(self, value, level=0):
        super().__init__(value, level, {'type': 'value'})