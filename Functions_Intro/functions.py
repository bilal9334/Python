def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers

    The function multiplies two integers, but you can also use it to
    multiply a sequence. If you pass a string, for example, as the
    first argument, you'll get the string repeated 'y' times as the
    returned value.
    :param x: The first integer passed as an argument from the function call
    :param y: The second integer passed as an argument from the function call
    :return: The answer of two integers multiplied
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Get a string from Standard Input (stdin)

    A palindrome is a string that reads the same forwards as backwards.
    :param string: The text that the user will see,
        when prompted to enter a value.
    :return: The 'text' that the user enters
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Get a string from Standard Input (stdin)

    The function checks if the 'sentence' entered is a palindrome and
    loops through the sentence to check if a character is alphanumeric
    which means it ignores whitespaces, capitalisation and punctuation in
    the sentence.
    :param sentence: The text that the user will see, when prompted to
        enter a value.
    :return: The 'is_palindrome' function is called to check if the 'string'
        is a palindrome.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

# answer = multiply(2, 3)
# print(answer)
#
# print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

p = palindrome_sentence()
