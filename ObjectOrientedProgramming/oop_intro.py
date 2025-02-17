class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):   # sets the initial state of the object by assigning values of the object's
        # properties. It initializes each new instance of a class. The first parameter will always be `self`.
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Model: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
# When a variable is bound to a class instance then it is referred to as an attribute
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5  # we can create attributes with class instances like this
print(kenwood.power)
# print(hamilton.power)  # this will return an error since the 'hamilton' instance of the class 'Kettle' does not
# have an attribute named 'power'.
print("Switching to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switching kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)

print("*" * 80)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
