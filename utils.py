from itertools import product

def process_data(items: list[int]) -> list[int]:
    """Return a list of sums for all 3‑element combinations (with replacement) from *items*.
    """
    return [i + j + k for i, j, k in product(items, repeat=3)]

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