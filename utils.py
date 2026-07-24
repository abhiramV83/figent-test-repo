def process_data(items):
    """Generate sums of all combinations of three items.

    Args:
        items (Iterable[int]): Iterable of numeric items.

    Returns:
        list[int]: List containing the sum of each triple combination.
    """
    return [i + j + k for i in items for j in items for k in items]

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