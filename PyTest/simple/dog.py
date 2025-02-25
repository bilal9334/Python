class Dog:

    def __init__(self, name, age, breed):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

    def get_human_age(self):
        return self.age * 7

    def describe(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old."


class DogHouse:

    def __init__(self):
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def list_dogs(self):
        return [dog.name for dog in self.dogs]
