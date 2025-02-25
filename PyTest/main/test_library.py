import pytest
from library import Book, Library


@pytest.fixture
def book():
    return Book("Python Programming", "John Doe")


@pytest.fixture
def another_book():
    return Book("Data Science", "Jane Smith")


@pytest.fixture
def library():
    return Library()


def test_add_book(library, book):
    library.add_book(book)
    assert book in library.books
    assert len(library.books) == 1


def test_remove_book(library, book):
    library.add_book(book)
    library.remove_book(book)
    assert book not in library.books


def test_remove_non_existing_book(library, book):
    with pytest.raises(ValueError, match="Python Programming not found in library!"):
        library.remove_book(book)


def test_check_book(library, book):
    library.add_book(book)
    assert library.check_book(book)


def test_check_non_existent_book(library):
    book = Book("Oliver Twist", "Charles Dickens")
    assert library.check_book(book) == "Oliver Twist not found!"


def test_borrow_book(library, book):
    library.add_book(book)
    response = library.borrow_book("Python Programming", "Bilal")
    assert response == "Python Programming has been borrowed by Bilal."


def test_borrow_book_already_borrowed(library, book):
    library.add_book(book)
    library.borrow_book("Python Programming", "Bilal")
    response = library.borrow_book("Python Programming", "Asad")
    assert response == "Python Programming is already borrowed."


def test_return_book(library, book):
    library.add_book(book)
    library.borrow_book("Python Programming", "Bilal")
    response = library.return_book("Python Programming")
    assert response == "Python Programming has been returned."


def test_return_non_existent_book(library):
    response = library.return_book("Nonexistent Book")
    assert response == "Book 'Nonexistent Book' not found in library."


def test_borrow_non_existent_book(library):
    response = library.borrow_book("Nonexistent Book", "Alice")
    assert response == "Book 'Nonexistent Book' not found in library."
