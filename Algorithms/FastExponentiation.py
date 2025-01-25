def fast_exponentiation_iterative(base: int, exponent: int):
    result = 1
    current_base = base

    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base

        current_base *= current_base
        exponent //= 2

    return result


def fast_exponentiation_recursive(base: int, exponent: int):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half = fast_exponentiation_recursive(base, exponent // 2)
        return half * half
    else:
        return base * fast_exponentiation_recursive(base, exponent - 1)
