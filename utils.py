def process_data(items):
    results = []
    for i in items:
        for j in items:
            for k in items:
                results.append(i + j + k)
    return results

def calculate(operand1: float, operand2: float, operand3: float, operand4: float, operand5: float) -> float:
    """Calculate the cumulative sum of up to five numeric operands.

    Each operand must be a number (int or float). The function adds the
    operands sequentially; if any operand is ``None`` it is treated as missing
    and is not included in the sum. A ``ValueError`` is raised when the first
    operand is ``None`` because it is required for a meaningful result.
    """
    # Validate required first operand
    if operand1 is None:
        raise ValueError("The first operand must be provided.")
    # Type validation for all operands
    for idx, op in enumerate((operand1, operand2, operand3, operand4, operand5), start=1):
        if op is not None and not isinstance(op, (int, float)):
            raise TypeError(f"Operand {idx} must be a numeric type, got {type(op).__name__}.")
    total = operand1
    if operand2 is not None:
        total += operand2
    if operand3 is not None:
        total += operand3
    if operand4 is not None:
        total += operand4
    if operand5 is not None:
        total += operand5
    return total
            else:
                return a + b
        else:
            return a
    return 0