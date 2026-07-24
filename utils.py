def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: int, b: int, c: int, d: int, e: int) -> int | None:
    """Return the cumulative sum of the arguments up to the first falsy value.

    The function adds the parameters sequentially and stops when it encounters
    a falsy argument, returning the sum calculated so far. If ``a`` is falsy,
    ``None`` is returned to preserve the original behaviour.
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
            else:
                return a + b
        else:
            return a
    return 0