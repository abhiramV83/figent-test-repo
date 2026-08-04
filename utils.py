def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Compute the sum of up to five numeric values.

    Parameters
    ----------
    a, b, c, d, e : int, float, or None
        Values to be summed. ``None`` values are ignored; zero is treated as a
        valid numeric value.

    Returns
    -------
    int or float
        The sum of the provided non‑None arguments. If ``a`` is ``None`` the
        function returns ``0``.
    """
    # Validate types
    for name, val in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if val is not None and not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be int or float, got {type(val).__name__}")
    # If the first argument is missing, return 0 (mirrors original intent)
    if a is None:
        return 0
    # Sum all non‑None arguments, treating zero as a valid value
    return sum(v for v in (a, b, c, d, e) if v is not None)
                return a + b
        else:
            return a
    return 0