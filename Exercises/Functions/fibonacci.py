def fibonacci(n: int) -> int:
    """
    Returns the nth fibonacci number for a non-negative integer n.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

    :param n: The position in the Fibonacci sequence (must be non-negative).
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(2, n):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
