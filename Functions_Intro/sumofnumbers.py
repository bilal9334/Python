def sum_numbers(*args: float) -> float:
    """
    Calculate the sum of all numbers.
    :param args: Numbers to be summed.
    :return: The sum of all numbers passed as an argument.
    """

    result = 0
    for num in args:
        result += num
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
