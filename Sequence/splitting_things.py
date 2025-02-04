panagram = """The quick brown
for jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
value_list = values.split()
print(value_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# replace the values in place
for index in range(len(value_list)):
    value_list[index] = int(value_list[index])

print(value_list)

# create a new list
integer_values = []
for value in value_list:
    integer_values.append(int(value))

print(integer_values)
