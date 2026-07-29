def process_data(items):
    """Return a list of sums of all ordered triples from *items*.
    """
    if not hasattr(items, '__iter__'):
        raise TypeError('items must be iterable')
    import itertools
    return [i + j + k for i, j, k in itertools.product(items, repeat=3)]

def calculate(a, b, c, d, e):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    return 0