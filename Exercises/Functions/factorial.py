def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    The factorial of 0 is 1 (0! = 1)

    :param n: A non-negative integer.
    :return: Returns the factorial `n`.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n <= 1:
        return 1

    return n * factorial(n-1)


result = int(input("Please enter a number: "))
for i in range(result):
    print(i, factorial(i))
