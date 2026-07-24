def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a: int, b: int, c: int, d: int, e: int) -> int | None:
    """Calculate sum based on truthiness of parameters.
    Returns a+b+c+d+e if all are truthy, a+b+c+d if e is falsy, a+b+c if d is falsy.
    Returns None if a, b, or c are falsy.
    """
    if not a or not b or not c:
        return None
    if d:
        return a + b + c + d + (e if e else 0)
    return a + b + c
            else:
                return a + b
        else:
            return a
    return 0