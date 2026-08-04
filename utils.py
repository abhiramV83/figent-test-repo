def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: float, b: float, c: float, d: float, e: float) -> float:
    """Calculate the sum of the provided numeric arguments.

    The function adds arguments sequentially until it encounters the first
    falsy value (e.g., 0, False, None) and then stops, mirroring the original
    nested‑if behavior. Non‑numeric inputs raise a TypeError.
    """
    for name, value in zip(("a", "b", "c", "d", "e"), (a, b, c, d, e)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")
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