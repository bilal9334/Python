def is_prime(n: int) -> bool:
    """
    Checks if the given non-negative number is a Prime.

    A prime number is a natural number greater than 1 that is only
    divisible by 1 and itself.

    :param n: The `integer` to check (must be greater than 1).
    :return: Returns `True` if the number is Prime, otherwise `False`.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


result = int(input("Enter a number: "))

if is_prime(result):
    print(f"{result} is a Prime number.")
else:
    print(f"{result} is not a Prime number.")
