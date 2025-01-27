name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 <= age < 31:
    print("Welcome to the club 18-30 holiday, {0}".format(name))
else:
    print("Please come back when you are right age")
