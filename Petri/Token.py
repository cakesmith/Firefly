"""
Token represents a value flowing through the Petri net.
Each token carries a value payload and represents an independent thread of execution.
"""

class Token:
    # Class-level configuration for bit width (default: 16-bit signed)
    BIT_WIDTH = 16
    
    def __init__(self, value=None, metadata=None):
        self.metadata = metadata or {}
        self._value = None
        self.value = value  # Use setter for normalization
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        """Set value with overflow handling for signed integers."""
        if val is None or isinstance(val, str):
            # Symbolic values (like "local[0]") pass through unchanged
            self._value = val
        elif isinstance(val, (int, float)):
            # Normalize to signed integer within bit width
            self._value = Token.normalize(int(val))
        else:
            self._value = val
    
    @classmethod
    def normalize(cls, value):
        """Normalize value to signed integer within configured bit width."""
        if not isinstance(value, int):
            return value
        
        max_val = (1 << (cls.BIT_WIDTH - 1)) - 1   # e.g., 32767 for 16-bit
        min_val = -(1 << (cls.BIT_WIDTH - 1))      # e.g., -32768 for 16-bit
        modulo = 1 << cls.BIT_WIDTH                 # e.g., 65536 for 16-bit
        
        # Wrap around using two's complement semantics
        value = value % modulo
        if value > max_val:
            value -= modulo
        
        return value
    
    @classmethod
    def set_bit_width(cls, bits):
        """Configure the bit width for all tokens (default: 16)."""
        cls.BIT_WIDTH = bits
        
    def __repr__(self):
        return f"Token({self._value}, metadata={self.metadata})"
        
    def __str__(self):
        return str(self._value)