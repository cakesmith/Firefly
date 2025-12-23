"""
Place can hold a token.


"""

class Place:

    def __init__(self, name):
        self.name = name
        self.has = False
        self.out_places = []
        self.in_places = []

    def put(self, token):
        if(~self.has):
            self.has = True
            self.token = token

    def get(self):
        if(self.has):
            self.has = False
            return self.token

    def connect(transition):
        self.out_places.append(transition)
        transition.in_places.append(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

                