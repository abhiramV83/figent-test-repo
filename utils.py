def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: float, b: float, c: float, d: float, e: float) -> float:
    """Calculate the sum of consecutive numeric arguments.

    The function adds the arguments in order until it encounters the first
    falsy value (e.g., ``0``, ``None``, ``False``). All provided arguments must
    be numbers; otherwise a ``TypeError`` is raised.

    Parameters:
        a, b, c, d, e: numeric values (int or float).

    Returns:
        The sum of the arguments up to (but not including) the first falsy
        value. If all arguments are truthy, the sum of all five is returned.
    """
    for name, val in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number")
    total = 0.0
    for val in (a, b, c, d, e):
        if not val:
            break
        total += val
    return total
                return a + b
        else:
            return a
    return 0