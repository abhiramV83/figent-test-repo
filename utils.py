import itertools

def process_data(items: list[int]) -> list[int]:
    """Generate sum of all triples from items.

    Args:
        items: List of integers.

    Returns:
        List of sums for each combination (i, j, k).
    """
    if not isinstance(items, list):
        raise TypeError("items must be a list")
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