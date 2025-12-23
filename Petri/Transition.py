class Transition:
    def __init__(self, fn):
        self.fn = fn
        self.out = []
        self.in = []

    def connect(place):
        self.out.append(place)
        place.in.append(self)
    
