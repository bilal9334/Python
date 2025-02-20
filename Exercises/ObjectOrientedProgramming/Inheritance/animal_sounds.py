class Animal:

    def make_sound(self):
        return "Animals make sounds!"


class Dog(Animal):

    def make_sound(self):
        return "Bark!"


class Cat(Animal):

    def make_sound(self):
        return "Meow!"


if __name__ == '__main__':

    dog = Dog()
    print(dog.make_sound())

    cat = Cat()
    print(cat.make_sound())
