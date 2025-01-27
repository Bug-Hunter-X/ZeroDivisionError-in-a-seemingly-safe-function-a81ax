def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0  # Or raise a more specific exception, e.g., ValueError
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_solution(0, 0)