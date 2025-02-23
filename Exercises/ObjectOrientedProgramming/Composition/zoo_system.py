class Animal:

    def make_sound(self):
        return "Animals make sounds"

    def __str__(self):
        return self.__class__.__name__


class Lion(Animal):

    def make_sound(self):
        return "Lion makes a Roar"


class Monkey(Animal):

    def make_sound(self):
        return "Monkey makes a OO--oo--aa--aa"


class Zoo:

    def __init__(self):
        self._animals = []

    def add_animals(self, animal):
        self._animals.append(animal)

    def list_animals(self):
        if not self._animals:
            print("No animals in the zoo!")
        else:
            print("\nAnimals in the Zoo")
            for animal in self._animals:
                print(f"{animal} - {animal.make_sound()}")


if __name__ == '__main__':
    lion = Lion()
    monkey = Monkey()

    zoo = Zoo()

    zoo.add_animals(lion)
    zoo.add_animals(monkey)
    zoo.list_animals()
