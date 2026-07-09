def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Calculate sum based on truthiness of parameters.
    Returns sum of parameters up to the first falsy one, matching the original logic.
    """
    if not a:
        return None
    if not b:
        return None
    if not c:
        return None
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