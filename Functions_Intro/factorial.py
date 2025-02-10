def factorial(number: int) -> int:
    """
    Calculate the factorial of a given numbers as an argument

    :param number: The provided number for factorial
    :return: returns the factorial (0! = 1)
    """
    if number <= 1:
        return 1

    result = 2
    for x in range(3, number + 1):
        result *= x
    return result


for i in range(36):
    print(i, factorial(i))
 
