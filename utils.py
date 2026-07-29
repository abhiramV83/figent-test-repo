def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: int | float | bool, b: int | float | bool, c: int | float | bool, d: int | float | bool, e: int | float | bool) -> int | float | None:
    """Return the sum of the arguments up to the first falsy value.

    Each parameter must be numeric (int, float, or bool); otherwise a ``TypeError`` is raised.
    """
    for name, value in (('a', a), ('b', b), ('c', c), ('d', d), ('e', e)):
        if not isinstance(value, (int, float, bool)):
            raise TypeError(f"Parameter {name} must be numeric")
    if not a:
        return None
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