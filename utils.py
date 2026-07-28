from typing import Iterable, Iterator

def process_data(items: Iterable[int]) -> Iterator[int]:
    """
    Generate the sum of every ordered triple (i, j, k) from the input iterable.
    Returns a generator to avoid O(n³) memory usage.
    """
    seq = list(items)
    if not all(isinstance(x, (int, float)) for x in seq):
        raise TypeError("All items must be numeric")
    return (i + j + k for i in seq for j in seq for k in seq)

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