def process_data(items):
    """Generate sums of all ordered triples from the iterable `items`.
    Parameters:
        items (iterable): An iterable of numeric values.
    Returns:
        list: A list containing the sum of each combination (i, j, k)."""
    try:
        iter(items)
    except TypeError:
        raise ValueError("items must be an iterable")
    items_list = list(items)
    from itertools import product
    return [i + j + k for i, j, k in product(items_list, repeat=3)]

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