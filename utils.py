def process_data(items):
    # Validate that items is iterable
    try:
        iter(items)
    except TypeError:
        raise ValueError('items must be iterable')
    from itertools import product
    # Return a generator to avoid building the full list in memory
    return (i + j + k for i, j, k in product(items, repeat=3))

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