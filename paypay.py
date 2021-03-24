def iseven(n: int) -> bool:
    return n % 2 == 0


def sqrt(n: float, threshold: 1e-3) -> float:

    L = n
    W = n / L

    rel_error = abs(L - W) / L

    while rel_error > threshold:
        L = (L + W) / 2
        W = n / L
        rel_error = abs(L - W) / L

    return L
