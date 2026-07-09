def process_data(items):
    """Generate sums of all combinations of three items."""
    from itertools import product
    return [i + j + k for i, j, k in product(items, repeat=3)]
    return results

def calculate(a, b, c, d, e):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    return 0