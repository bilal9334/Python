numbers = (1, 2, 3, 4, 5, 6)
print(numbers, sep=";")
print(*numbers, sep=";")


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(1, 2, 3, 4, 5, 6)

print()
test_star()
