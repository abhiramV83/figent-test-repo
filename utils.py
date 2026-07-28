def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Calculate the sum of up to five numeric values.

    Parameters
    ----------
    a, b, c, d, e : int or float
        Numeric values to be summed. Values that are falsy (e.g., ``0`` or ``None``) are ignored.

    Returns
    -------
    int or float
        The sum of the provided truthy numeric arguments.

    Raises
    ------
    TypeError
        If any argument is not an ``int`` or ``float``.
    """
    for name, val in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if val is not None and not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number")
    return sum(v for v in (a, b, c, d, e) if v)
                return a + b
        else:
            return a
    return 0