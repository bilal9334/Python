for i in range(1, 21):
    print("i is now {}".format(i))

print("*" * 80)

# if we do not provide a start value then the python will take 0 as a default value
for a in range(10):
    print("a is now {}".format(a))

print("*" * 80)

# Providing a step to for loop
for b in range(0, 10, 2):
    print("b is now {}".format(b))

print("*" * 80)

# Providing a negative step (start value should be greater than the stop value)
for c in range(10, 0 ,-2):
    print("c is now {}".format(c))
