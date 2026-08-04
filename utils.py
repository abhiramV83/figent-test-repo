def process_data(items):
    """Compute the sum of every ordered triple (i, j, k) from *items*.

    Parameters
    ----------
    items : Iterable[Number]
        An iterable containing numeric values (int or float).

    Returns
    -------
    Iterator[Number]
        An iterator yielding ``i + j + k`` for each possible triple.
    """
    # Validate that items is iterable and contains only numbers
    try:
        values = list(items)
    except TypeError:
        raise TypeError("items must be an iterable of numbers")
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("items must contain only numeric values")
    # Generate sums lazily to avoid O(n³) memory usage
    for i in values:
        for j in values:
            for k in values:
                yield i + j + k

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