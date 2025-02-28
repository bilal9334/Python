import pytest
from libraray_system import Book, Library


@pytest.fixture
def library():
    return Library()


def test_add_book(library):
    library.add_book("Python Programming", "John Doe")
    assert library.is_available("Python Programming")


def test_remove_book(library):
    library.add_book("Oliver Twist", "Charles Dickens")
    library.remove_book("Oliver Twist")

    assert not library.is_available("Oliver Twist")

    with pytest.raises(KeyError, match="Book not found in library"):
        library.remove_book("Non-existing Book")


def test_is_available(library):
    library.add_book("Python Programming", "John Doe")
    assert library.is_available("Python Programming")

    assert not library.is_available("Oliver Twist")


def test_list_books(library):
    library.add_book("Python Programming", "John Doe")
    library.add_book("Oliver Twist", "Charles Dickens")

    books = library.list_book()
    assert "Book - Title: Python Programming, Author: John Doe" in books
    assert "Book - Title: Oliver Twist, Author: Charles Dickens" in books
