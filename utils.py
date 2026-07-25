def process_data(items: list[int]) -> list[int]:
    """Generate all possible sums of three items from the input collection.

    Args:
        items: An iterable of integers.

    Returns:
        A list containing the sum of every combination of three elements (with repetition).
    """
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
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