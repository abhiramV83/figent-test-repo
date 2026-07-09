def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Return the sum of arguments up to the first falsy value.

    The function adds each argument in order (a, b, c, d, e) and stops
    when it encounters a falsy value, returning the accumulated sum.
    """
    total = 0
    if a:
        total += a
    else:
        return total
    if b:
        total += b
    else:
        return total
    if c:
        total += c
    else:
        return total
    if d:
        total += d
    else:
        return total
    if e:
        total += e
    return total
                return a + b
        else:
            return a
    return 0