def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Return the cumulative sum of the arguments up to the first falsy value.

    The function evaluates the parameters in order a, b, c, d, e. It returns the sum of
    all preceding truthy arguments including the first falsy one (which is excluded).
    If *a* is falsy, ``None`` is returned to preserve the original implicit ``None``
    behavior.
    """
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
                return a + b
        else:
            return a
    return 0