def multiply(x, y):
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers, you can also use
    it to multiply a sequence. If you pass a string, for example, as the first
    argument, you'll get the string repeated 'y' times as the returned value.

    :param x: The first number to multiply.
    :type x: float or int
    :param y: The number to multiply by 'x'.
    :type y: float or int
    :return: The product of 'x' and 'y'
    :rtype: float or int
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check
    :type string: string
    :return: True if 'string' is a palindrome, False otherwise.
    :rtype: string
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome.

    :param sentence: The function ignores whitespace, capitalisation and 
    punctuation in the sentence.
    :type sentence: The sentence to check.
    :return: True if 'sentence' is a palindrome, False otherwise.
    :rtype: string
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return is_palindrome(string)

# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print(f"'{word}' is a palindrome.")
# else:
#     print(f"'{word}' is not a palindrome.")

answer = multiply(18, 3)
print(answer)
