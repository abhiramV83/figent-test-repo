def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(a, b, c, d, e):
    """Calculate the sum of provided numeric arguments based on truthiness.
    
    Parameters:
        a, b, c, d, e (int or float): Numeric values to be summed.
    
    Returns:
        int or float or None: Sum of arguments up to the first falsy value after a,
        or None if `a` is falsy.
    
    Raises:
        TypeError: If any argument is not a number.
    """
    for name, value in (('a', a), ('b', b), ('c', c), ('d', d), ('e', e)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Argument {name} must be a number")
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