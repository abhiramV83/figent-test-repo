def process_data(items):
    """Generate sums of all triples from the iterable `items`.

    Args:
        items: An iterable of numbers.

    Returns:
        A list of sums for each combination of three elements (with repetition).

    Raises:
        ValueError: If `items` is None.
        TypeError: If `items` is not iterable.
    """
    if items is None:
        raise ValueError("items must not be None")
    try:
        seq = list(items)
    except TypeError:
        raise TypeError("items must be iterable")
    import itertools
    return [i + j + k for i, j, k in itertools.product(seq, repeat=3)]

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