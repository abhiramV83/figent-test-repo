def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    # Validate that all inputs are numeric
    for name, val in (('a', a), ('b', b), ('c', c), ('d', d), ('e', e)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number")
    # Flattened logic using early returns
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