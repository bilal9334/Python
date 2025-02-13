# numbers = {}  # will create a dict
# numbers = {*""}  # creating an empty set - avoid doing this
# numbers = {*{}}  # creates an empty set - avoid doing this too

numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers.add(next_value)
print(numbers)
