# Creating list
fruits = ["apple", "banana", "orange", "pineapple", "elderberry"]
print(fruits)

# Accessing List
print(fruits[0])
print(fruits[4])

# Modifying the list
fruits[1] = "blueberry"
print(fruits)

# Adding and Removing elements
fruits.remove("pineapple")
fruits.append("grape")
print(fruits)

# Slicing
print(fruits[:3])

# Finding an element in the list
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

# Sorting and Reversing
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

# List Comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)
