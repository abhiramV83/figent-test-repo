def process_data(items: list[int]) -> list[int]:
    """Compute the sum of every combination of three items from the input list.

    Args:
        items: A list of numeric values.

    Returns:
        A list containing the sums of all possible triples (i, j, k) from ``items``.
        Note: This operation has O(n³) time and memory complexity.
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