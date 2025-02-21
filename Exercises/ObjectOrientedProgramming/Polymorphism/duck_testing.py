class Car:

    def move(self):
        return "Move Car"


class Bicycle:

    def move(self):
        return "Move Bicycle"


def make_it_move(movement):
    print(movement.move())


if __name__ == '__main__':
    make_it_move(Car())
    make_it_move(Bicycle())
