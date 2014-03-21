
import collections    


def func(entry):
    for x in entry:
        if isinstance(x, collections.Iterable):
            for x in func(x):
                yield x
        else:
            yield x
        
def testfunc():
    s = yield somefunc(1234)
    
    yield 567 + s

def somefunc(z):
    return z+17
