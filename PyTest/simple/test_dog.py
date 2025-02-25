import pytest
from dog import Dog, DogHouse


def test_bark():
    dog = Dog("Buddy", 3, "Golden Retriever")
    assert dog.bark() == "Buddy says woof!"


def test_get_human_age():
    dog = Dog("Buddy", 3, "Golden Retriever")
    assert dog.get_human_age() == 21


def test_negative_age():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        Dog("Buddy", -1, "Golden Retriever")


def test_dog_breed():
    dog = Dog("Buddy", 3, "Golden Retriever")
    assert dog.breed == "Golden Retriever"


def test_dog_description():
    dog = Dog("Buddy", 3, "Golden Retriever")
    assert dog.describe() == "Buddy is a Golden Retriever and is 3 years old."


def test_add_dog():
    house = DogHouse()
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    dog2 = Dog("Max", 2, "Beagle")

    house.add_dog(dog1)
    house.add_dog(dog2)

    assert dog1 in house.dogs
    assert dog2 in house.dogs


def test_list_dogs():
    house = DogHouse()
    house.add_dog(Dog("Buddy", 2, "Golden Retriever"))
    house.add_dog(Dog("Max", 2, "Beagle"))

    assert house.list_dogs() == ["Buddy", "Max"]
