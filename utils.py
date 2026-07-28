def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: float, b: float, c: float, d: float, e: float) -> float:
    """Calculate the sum of the provided numeric arguments.

    Each argument is validated to be a number (int or float). Falsy values
    (e.g., 0, None) are ignored in the sum. Raises ``TypeError`` for non‑numeric
    inputs.
    """
    for name, value in (('a', a), ('b', b), ('c', c), ('d', d), ('e', e)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a numeric type, got {type(value).__name__}")
    total = 0.0
    if a:
        total += a
    if b:
        total += b
    if c:
        total += c
    if d:
        total += d
    if e:
        total += e
    return total
                return a + b
        else:
            return a
    return 0