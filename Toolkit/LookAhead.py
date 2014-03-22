from itertools import tee, islice

class LookAhead:

    """Wrap an iterator with lookahead indexing

    >>> L = LookAhead([5, 3, 1, 5, 6, 3])

    >>> next(L)
    5
    >>> next(L)
    3
    >>> L[0]
    1
    >>> L[1]
    5
    >>> next(L)
    1
    """
    def __init__(self, iterator):
        self.t = tee(iterator, 1)[0]
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.t)
    def __getitem__(self, i):
        for value in islice(self.t.__copy__(), i, None):
            return value
        raise IndexError(i)
