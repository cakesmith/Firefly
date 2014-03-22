from itertools import count

class LabelGenerator:
    def __init__(self, name, joinchar="."):
        self.labels = {None:self._makeiterator(name, joinchar)}
        self.name = name
        self.joinchar = joinchar

    def _makeiterator(self, tag, joinchar):
        
        def iterator():
            for i in count(0):
                yield joinchar.join((tag,str(i)))
        return iterator()

    def add(self, tag):
        self.labels.update({tag:self._makeiterator(self.joinchar.join((self.name, tag)), self.joinchar)})

    def next(self, tag=None):
        if tag in self.labels.keys():
            return next(self.labels[tag])
        else:
            self.add(tag)
            return self.next(tag)
            
    def reset(self, tag):
        if tag in self.labels.keys():
            self.labels[tag] = self._makeiterator(self.joinchar.join((self.name, tag)), self.joinchar)
