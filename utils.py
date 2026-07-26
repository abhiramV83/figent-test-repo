def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(value1: float, value2: float, value3: float, value4: float, value5: float) -> float:
    # Validate that all inputs are numeric
    for name, val in (('value1', value1), ('value2', value2), ('value3', value3), ('value4', value4), ('value5', value5)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric type")
    # If the first value is falsy, return 0 (mirrors original behavior of returning nothing)
    if not value1:
        return 0
    total = 0
    for val in (value1, value2, value3, value4, value5):
        if val:
            total += val
        else:
            break
    return total
                return a + b
        else:
            return a
    return 0