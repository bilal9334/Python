def is_palindrome(w: str) -> bool:
    """
    Check whether a given string is a palindrome

    A palindrome is a string that reads the same forwards as backwards.

    :param w: The text that the user will see,
            when prompted to enter a value.
    :return: The `text` that the user enters.
    """
    return w[::-1].casefold() == w.casefold()


word = input("Please enter a text: ")
if is_palindrome(word):
    print(f"{word} is Palindrome")
else:
    print(f"{word} is not a Palindrome")
