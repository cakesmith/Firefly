"""
Control Flow Manager for Petri Net VM
Manages control flow constructs (labels, goto, if-goto) in Petri net semantics
Handles function-scoped labels and control flow places
"""

from .Token import Token

class ControlFlowManager:
    """
    Manages control flow constructs (labels, goto, if-goto) in Petri net semantics
    Handles function-scoped labels and control flow places
    """
    def __init__(self, net):
        self.net = net
        self.labels = {}  # label_name -> control_place
        self.function_labels = {}  # function_name -> {label_name -> control_place}
        self.pending_jumps = []  # Jumps waiting for label resolution
        self.place_counter = 0
        
    def get_unique_place_name(self, prefix="control"):
        self.place_counter += 1
        return f"{prefix}_{self.place_counter}"
        
    def define_label(self, label_name, function_name=None):
        """
        Create a control flow place for this label
        Labels are scoped to their containing function
        """
        if function_name:
            # Function-scoped label
            scoped_label_name = f"{function_name}.{label_name}"
            if function_name not in self.function_labels:
                self.function_labels[function_name] = {}
        else:
            # Global label (for main program)
            scoped_label_name = label_name
            
        # Check if label already exists
        if scoped_label_name in self.labels:
            print(f"Label '{label_name}' already defined in function '{function_name}', reusing existing place")
            return self.labels[scoped_label_name]
            
        # Create control flow place for this label
        control_place = self.net.add_place(self.get_unique_place_name(f"label_{scoped_label_name}"))
        
        # Store label mapping
        if function_name:
            self.function_labels[function_name][label_name] = control_place
        self.labels[scoped_label_name] = control_place
        
        print(f"Defined label '{label_name}' in function '{function_name}' -> {control_place.name}")
        return control_place
        
    def get_label_place(self, label_name, function_name=None):
        """
        Get the control flow place for a label
        Handles function scoping
        """
        if function_name:
            scoped_label_name = f"{function_name}.{label_name}"
            # First try function-scoped label
            if function_name in self.function_labels and label_name in self.function_labels[function_name]:
                return self.function_labels[function_name][label_name]
        else:
            scoped_label_name = label_name
            
        # Try global label
        if scoped_label_name in self.labels:
            return self.labels[scoped_label_name]
            
        # Label not found
        raise RuntimeError(f"Undefined label: {label_name} in function {function_name}")
        
    def is_label_defined(self, label_name, function_name=None):
        """Check if a label is defined in the given scope"""
        try:
            self.get_label_place(label_name, function_name)
            return True
        except RuntimeError:
            return False
            
    def get_function_labels(self, function_name):
        """Get all labels defined in a function"""
        return self.function_labels.get(function_name, {})
        
    def clear_function_labels(self, function_name):
        """Clear labels for a function (cleanup)"""
        if function_name in self.function_labels:
            # Remove from global labels too
            for label_name in self.function_labels[function_name]:
                scoped_name = f"{function_name}.{label_name}"
                if scoped_name in self.labels:
                    del self.labels[scoped_name]
            del self.function_labels[function_name]