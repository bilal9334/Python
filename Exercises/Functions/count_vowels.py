def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string.

    :param text: The input string.
    :return: The count of vowels (a, e, i, o, u) in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# Get user input
user_text = input("Enter some text: ")
vowel_count = count_vowels(user_text)

# Display the result
print(f"Number of vowels in the text are {vowel_count}")
