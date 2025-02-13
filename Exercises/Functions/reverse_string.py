def reverse_string(string: str) -> str:
    """
    Returns the given string in reverse order.

    :param string: The string as input to the function to be reversed.
    :return: The reversed string, preserving spaces and capitalization.
    """
    return string[::-1]


text = input("Please enter a text: ")
print(f"Original text: {text}")
print()
print(f"Reversed text: {reverse_string(text)}")
