number = int(input("Please enter a number: "))

if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("Number is zero")


# Check odd or even
if number % 2 == 0:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))
