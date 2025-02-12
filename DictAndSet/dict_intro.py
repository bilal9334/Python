vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'cam-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]

result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# my_car = vehicles['fiesta']
# print(my_car)
#
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)

# for key in vehicles:
#     print(key, vehicles[key], sep=": ")
for key, value in vehicles.items():  # Python 3 used .item() to loop over dictionaries.
    print(key, value, sep=": ")
