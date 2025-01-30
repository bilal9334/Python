low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press the ENTER to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    highLow = input(
        "My guess is {}. Should I guess higher or lower? Enter h or lo, or c if my guess was correct  ".format(
            guess)).casefold()

    if highLow == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif highLow == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif highLow == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1  # Augmented Assignment
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
