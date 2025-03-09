cities = {"New York": 10, "London": 12, "Berlin": 5, "Tokyo": 20}

conversion = {city: (temp * (9 / 5) + 32) for city, temp in cities.items()}

print(conversion)