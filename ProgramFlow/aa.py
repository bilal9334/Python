x = 23

x += 1
print(x)  # 24

x -= 4
print(x)  # 20

x *= 5
print(x)  # 100

x //= 4  # 25
print(x)

x /= 5  # 5.0 - not conversion from int to float
print(x)

x **= 2  # 25.0 - x still represents float
print(x)

x %= 5
print(x)  # 0.0 - 25 is exactly divisible by 5

greeting = "Good "

greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)
