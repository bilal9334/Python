def is_even(number: int) -> bool:
    """
    Checks if a given number is even.

    :param number: The `integer` to check.
    :return: Returns `True` if number is even, otherwise `False`.
    """
    return number % 2 == 0


check_number = int(input("Enter a number: "))

if is_even(check_number):
    print(f"{check_number} is even")
else:
    print(f"{check_number} is odd")
