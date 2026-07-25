def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: float, b: float, c: float, d: float, e: float) -> float:
    """
    Calculate the cumulative sum of the provided numeric arguments until the first falsy value.

    Parameters:
        a, b, c, d, e: numeric values (int or float). Truthy values are summed; the first falsy
        argument stops the accumulation.

    Returns:
        The sum of the consecutive truthy arguments, or 0.0 if the first argument is falsy.
    """
    for name, value in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be int or float, got {type(value).__name__}")
    total = 0.0
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