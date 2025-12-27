"""
Token represents a value flowing through the Petri net.
Each token carries a value payload and represents an independent thread of execution.
Enhanced with level-based and continuation support for trampolined recursion.
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
        self.is_continuation = False

class ContinuationToken(Token):
    """Token representing a continuation (function call to be executed)"""
    def __init__(self, function_name, args, level=0):
        super().__init__(None, level, {'type': 'continuation'})
        self.function_name = function_name
        self.args = args
        self.is_continuation = True
        
    def __repr__(self):
        return f"ContinuationToken({self.function_name}, {len(self.args)} args, level={self.level})"