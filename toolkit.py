from re import compile
from itertools import count
from collections import namedtuple, Iterable

class LabelGenerator:
    
    def __init__(self, name, joinchar="."):
        self.labels = {None:self._makeiterator(name, joinchar)}
        self.name = name
        self.joinchar = joinchar
    
    def _makeiterator(self, tag, joinchar):
        
        def iterator():
            for i in itertools.count(0):
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

    def resetAll(self):
        self.__init__(self.name, self.joinchar)



def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for x in flatten(x):
                yield x
        else:
            yield x
            

def scanpattern(pattern, text, ignore_types=None):
    """ Takes a master pattern and scans a text with it, returning match values
        if the match type is not in ignore_types.
    """ 
    
    scanmatch = collections.namedtuple('scanmatch', ('type', 'value', 'loc'))
        
    master_pat = re.compile(pattern)
    
    scanner = master_pat.scanner(text)
    
    # iterating over a string breaks everything, so let's make sure that we have a list.
    
    if isinstance(ignore_types, str):
        ignore_types = [ignore_types]
        
    for type, value, loc in ((m.lastgroup, m.group(), m.start()) for m in iter(scanner.match, None) if m.lastgroup not in ignore_types):
        yield scanmatch(type, value, loc)
    
def safewrite(lines, file, sep="\n"):

    if isinstance(lines, str):
        file.write(lines)
        file.write(sep)
    else:
        for i in lines:
            file.write(i)
            file.write(sep)
    

    

def loctoline(text):
    """Take a given text and produce a function L such that
    L(loc) will yield the line number N in text.
    
    >>> L = loctoline("foo\\nbar")
    
    >>> L(0)
    1
    >>> L(3)
    1
    >>> L(4)
    2
    >>> L(7)

    """

    line = []
    num = 1
    
    for char in text:
        line.append(num)
        if char == "\n":
            num += 1
    
    def lookup(location):
        try:
            return line[location]
        except IndexError:
            return None
    # return a closure to generate the data structure on demand and only when necessary.
    return lookup


if __name__ == "__main__":
    import doctest
    doctest.testmod()
