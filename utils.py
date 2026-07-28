def process_data(items):
    """Compute the sum of every ordered triple (i, j, k) from *items*.

    The function returns a list containing i + j + k for each combination.
    It validates that *items* is iterable and limits the input size to avoid
    excessive memory consumption.
    """
    try:
        seq = list(items)
    except TypeError:
        raise TypeError("items must be an iterable")
    if len(seq) > 1000:
        raise ValueError("items size too large; may cause excessive memory usage")
    results = [i + j + k for i in seq for j in seq for k in seq]
    return results

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