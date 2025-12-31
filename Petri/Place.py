"""
Place can hold tokens with values.
Each token represents an independent thread of execution.
"""

class Place:
    def __init__(self, name):
        self.name = name
        self.token = None
        self.has = False
        self.memory_address = None  # Will be assigned during allocation pass
        self.is_live = True  # For liveness analysis

    def put_token(self, token):
        self.has = True
        self.token = token

    def get_token(self):
        self.has = False
        return self.token

if __name__ == "__main__":
    import doctest
    doctest.testmod()

                