import random


def get_integer(prompt: str) -> None:
    """
    Get an integer from Standard Input (stdin)

    The function will continue looping, and prompting the user, until a valid
    'int' is entered.

    :param prompt: The String that the user will see, when they're prompted to
    enter the value.
    :type prompt: str
    :return: The integer that the user enters.
    :rtype: None
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print(f"{temp} is not a valid number")


# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)
help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0  # initialise to any number that doesn't equal the answer
print("Please guess a numbers between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
            # guess = int(input())
else:
    print("Sorry, you have not guessed it correctly")
