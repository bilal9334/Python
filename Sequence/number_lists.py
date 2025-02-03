empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)
# print(another_even)

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]  # Copying a list - Python 2
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)  # Not equal lists - False
print(numbers == more_numbers)  # Equal numbers of items in a list - True
