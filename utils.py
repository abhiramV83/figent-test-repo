def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: int, b: int, c: int, d: int, e: int) -> int:
    """Calculate the sum of consecutive arguments until the first falsy value.
    
    Parameters:
        a, b, c, d, e (int): Integer values to be summed.
    
    Returns:
        int: Sum of all arguments up to (and including) the first falsy argument.
        If the first argument ``a`` is falsy, returns 0.
    """
    total = 0
    for value in (a, b, c, d, e):
        if value:
            total += value
        else:
            break
    return total
                return a + b
        else:
            return a
    return 0