def find_max(a: int, b: int, c: int) -> int:
    """
    Returns the maximum of three integers.

    :param a: The first `integer`.
    :param b: The second `integer`.
    :param c: The third `integer`.
    :return: The largest number between `a`, `b`, or `c`.
    """
    # if a > b and a > c:
    #     return a
    # elif b > a and b > c:
    #     return b
    # elif c > a and c > b:
    #     return c
    # else:
    #     return 0
    maximum = max(a, b, c)

    if maximum == a:
        print(f"{a} is the maximum number")
    elif maximum == b:
        print(f"{b} is the maximum number")
    else:
        print(f"{c} is the maximum number")

    return maximum


# Taking user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calling the function
largest = find_max(num1, num2, num3)
