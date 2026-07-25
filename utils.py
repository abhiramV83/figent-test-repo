def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: int, b: int, c: int, d: int, e: int) -> int:
    """Calculate the sum of the arguments up to the first falsy value.

    The function validates that all inputs are numbers and that ``a`` is truthy.
    It returns the cumulative sum stopping at the first argument that evaluates
    to ``False``.
    """
    for name, value in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
    if not a:
        raise ValueError("Argument 'a' must be truthy")
    if not b:
        return a
    if not c:
        return a + b
    if not d:
        return a + b + c
    if not e:
        return a + b + c + d
    return a + b + c + d + e
            else:
                return a + b
        else:
            return a
    return 0