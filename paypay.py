def isprime(n: int) -> bool:
    return True


def iseven(n: int) -> bool:
    return n % 2 == 0


def sqrt(n: float, threshold=1e-3) -> float:

    A = n
    L = A
    W = A / L

    while (W - L) / L > threshold:
        L = (L + W) / 2
        W = A / L

    return L

def ispalindrome(word):
    return None

