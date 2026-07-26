def process_data(items: Iterable[Union[int, float]]) -> List[float]:
    """
    Compute the sum of every possible triple combination of numeric items.

    Args:
        items: An iterable of numbers (int or float).

    Returns:
        A list containing the sum of each triple (i, j, k) from the input.
    """
    # Convert to list to allow multiple passes over the data
    try:
        items_list = list(items)
    except TypeError:
        raise TypeError("items must be an iterable of numbers")
    for element in items_list:
        if not isinstance(element, (int, float)):
            raise TypeError("All elements in items must be int or float")
    results: List[float] = []
    for i in items_list:
        for j in items_list:
            for k in items_list:
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