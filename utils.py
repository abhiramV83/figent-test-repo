def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Calculate the sum of provided numeric arguments, treating None as zero.
    Zero values are included in the sum."""
    return sum(x for x in (a, b, c, d, e) if x is not None)
                return a + b
        else:
            return a
    return 0