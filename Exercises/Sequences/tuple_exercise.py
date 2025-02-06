# Create tuple
colors = ("red", "blue", "green", "white")
print(colors)

# Accessing Tuple Elements
print(colors[1])
print(colors[3])

# Tuple Unpacking
color_1, color_2, color_3, color_4 = colors
print(color_1, color_2, color_3, color_4)

# Converting tuple to list and back
color_list = list(colors)

# Modifying the list
color_list[3] = "purple"

# Converting list to tuple
color_tuple = tuple(color_list)
print(color_tuple)

# Counting occurrences in a tuple
nums = (1, 2, 3, 2, 4, 2, 5)
print(nums.count(2))

# Tuple Indexing
print(colors.index("blue"))

# Changing an element of tuple
# colors[0] = "white"
print(colors)
