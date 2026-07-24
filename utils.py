def process_data(items):
    from itertools import product
    try:
        iterable = list(items)
    except TypeError:
        raise ValueError('items must be iterable')
    return [i + j + k for i, j, k in product(iterable, repeat=3)]

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