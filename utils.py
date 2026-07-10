def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    if a is None:
        return None
    if b is None:
        return a
    if c is None:
        return a + b
    if d is None:
        return a + b + c
    if e is None:
        return a + b + c + d
    return a + b + c + d + e
            else:
                return a + b
        else:
            return a
    return 0