"""
Token represents an independent execution thread in the Petri net.

Each token owns its complete execution state:
- pc: program counter (current position)
- stack_frames: LIFO structure of call frames (per-token, NOT global)
- sp: stack pointer
- value: data payload

This design enables true multicore execution where multiple tokens
can execute function calls concurrently without serialization.

Key invariant: Return order is defined per-token, not globally.
A return resumes only the caller of that same token.
"""

class StackFrame:
    """
    Represents a single call frame on a token's stack.
    
    Each frame contains:
    - return_pc: where to resume after return
    - saved_lcl: caller's LCL pointer
    - saved_arg: caller's ARG pointer  
    - saved_this: caller's THIS pointer
    - saved_that: caller's THAT pointer
    - locals: local variables for this frame
    - arguments: arguments passed to this call
    """
    __slots__ = ['return_pc', 'saved_lcl', 'saved_arg', 'saved_this', 
                 'saved_that', 'locals', 'arguments', 'function_name']
    
    def __init__(self, return_pc, saved_lcl=0, saved_arg=0, 
                 saved_this=0, saved_that=0, n_locals=0, n_args=0,
                 function_name=None):
        self.return_pc = return_pc
        self.saved_lcl = saved_lcl
        self.saved_arg = saved_arg
        self.saved_this = saved_this
        self.saved_that = saved_that
        self.locals = [0] * n_locals
        self.arguments = [0] * n_args
        self.function_name = function_name
    
    def __repr__(self):
        return f"StackFrame(ret={self.return_pc}, fn={self.function_name})"


class Token:
    """
    Token represents an independent thread of execution.
    
    Each token MUST own:
    - token_id: stable identifier for debugging/scheduling
    - stack_frames: LIFO structure of call frames (per-token stack)
    - value: data payload for the current operation
    
    CRITICAL: No stack data may be shared across tokens.
    Stack frames are indexed by (token_id, frame_depth), NOT by global order.
    """
    
    # Class-level configuration
    BIT_WIDTH = 16
    _next_token_id = 0
    
    def __init__(self, value=None, metadata=None, token_id=None):
        # Assign unique token ID
        if token_id is None:
            self.token_id = Token._next_token_id
            Token._next_token_id += 1
        else:
            self.token_id = token_id
            
        self.metadata = metadata or {}
        self._value = None
        self.value = value  # Use setter for normalization
        
        # Per-token execution state
        self.stack_frames = []  # LIFO stack of StackFrame objects
        self.sp = 0  # Stack pointer within this token's context
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        """Set value with overflow handling for signed integers."""
        if val is None or isinstance(val, str):
            self._value = val
        elif isinstance(val, (int, float)):
            self._value = Token.normalize(int(val))
        else:
            self._value = val
    
    @classmethod
    def normalize(cls, value):
        """Normalize value to signed integer within configured bit width."""
        if not isinstance(value, int):
            return value
        
        max_val = (1 << (cls.BIT_WIDTH - 1)) - 1
        min_val = -(1 << (cls.BIT_WIDTH - 1))
        modulo = 1 << cls.BIT_WIDTH
        
        value = value % modulo
        if value > max_val:
            value -= modulo
        
        return value
    
    @classmethod
    def set_bit_width(cls, bits):
        """Configure the bit width for all tokens."""
        cls.BIT_WIDTH = bits
    
    @classmethod
    def reset_token_ids(cls):
        """Reset token ID counter (useful for testing)."""
        cls._next_token_id = 0

    # =========================================================================
    # Per-Token Stack Frame Management
    # =========================================================================
    
    def push_frame(self, return_pc, saved_lcl=0, saved_arg=0,
                   saved_this=0, saved_that=0, n_locals=0, n_args=0,
                   function_name=None):
        """
        Push a new stack frame for a function call.
        
        This is called when executing CALL on this token.
        The frame is owned by THIS token only.
        """
        frame = StackFrame(
            return_pc=return_pc,
            saved_lcl=saved_lcl,
            saved_arg=saved_arg,
            saved_this=saved_this,
            saved_that=saved_that,
            n_locals=n_locals,
            n_args=n_args,
            function_name=function_name
        )
        self.stack_frames.append(frame)
        return frame
    
    def pop_frame(self):
        """
        Pop the top stack frame on return.
        
        Returns the popped frame, or None if stack is empty.
        This is called when executing RETURN on this token.
        """
        if self.stack_frames:
            return self.stack_frames.pop()
        return None
    
    def current_frame(self):
        """Get the current (top) stack frame, or None if empty."""
        if self.stack_frames:
            return self.stack_frames[-1]
        return None
    
    @property
    def call_depth(self):
        """Return current call depth (number of frames on stack)."""
        return len(self.stack_frames)
    
    def get_local(self, index):
        """Get a local variable from the current frame."""
        frame = self.current_frame()
        if frame and 0 <= index < len(frame.locals):
            return frame.locals[index]
        return 0
    
    def set_local(self, index, value):
        """Set a local variable in the current frame."""
        frame = self.current_frame()
        if frame:
            while len(frame.locals) <= index:
                frame.locals.append(0)
            frame.locals[index] = Token.normalize(value)
    
    def get_argument(self, index):
        """Get an argument from the current frame."""
        frame = self.current_frame()
        if frame and 0 <= index < len(frame.arguments):
            return frame.arguments[index]
        return 0
    
    def set_argument(self, index, value):
        """Set an argument in the current frame."""
        frame = self.current_frame()
        if frame:
            while len(frame.arguments) <= index:
                frame.arguments.append(0)
            frame.arguments[index] = Token.normalize(value)

    # =========================================================================
    # Legacy Compatibility - Call Stack as Value
    # =========================================================================
    # These methods provide backward compatibility with the old call stack
    # representation where the stack was stored in token.value as a tuple.
    # New code should use push_frame/pop_frame instead.
    
    def get_call_stack_from_value(self):
        """
        Extract call stack from legacy value format.
        Legacy format: ("callstack", [addr1, addr2, ...])
        """
        if isinstance(self._value, tuple) and len(self._value) == 2:
            if self._value[0] == "callstack":
                return list(self._value[1])
        return []
    
    def set_call_stack_to_value(self, stack):
        """
        Set call stack in legacy value format.
        """
        if stack:
            self._value = ("callstack", list(stack))
        else:
            self._value = []
    
    # =========================================================================
    # Cloning for Fork Operations
    # =========================================================================
    
    def clone(self, new_value=None):
        """
        Create a new token with independent execution state.
        
        Used when forking execution (e.g., parallel branches).
        The new token gets its own token_id and stack frames.
        """
        new_token = Token(
            value=new_value if new_value is not None else self._value,
            metadata=dict(self.metadata),
            token_id=None  # Get new unique ID
        )
        # Deep copy stack frames
        for frame in self.stack_frames:
            new_token.stack_frames.append(StackFrame(
                return_pc=frame.return_pc,
                saved_lcl=frame.saved_lcl,
                saved_arg=frame.saved_arg,
                saved_this=frame.saved_this,
                saved_that=frame.saved_that,
                n_locals=len(frame.locals),
                n_args=len(frame.arguments),
                function_name=frame.function_name
            ))
            # Copy local values
            if new_token.stack_frames:
                new_token.stack_frames[-1].locals = list(frame.locals)
                new_token.stack_frames[-1].arguments = list(frame.arguments)
        new_token.sp = self.sp
        return new_token
        
    def __repr__(self):
        return f"Token(id={self.token_id}, value={self._value}, depth={self.call_depth})"
        
    def __str__(self):
        return str(self._value)
