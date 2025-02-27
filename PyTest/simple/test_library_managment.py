import pytest
from library_management import Book, Library


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


def test_borrow_book(library, book):
    library.add_book(book)
    response = library.borrow_book("Python Programming")
    assert response == "Book borrowed!"


def test_borrow_book_already_borrowed(library, book):
    library.add_book(book)
    library.borrow_book("Python Programming")
    response = library.borrow_book("Python Programming")
    assert response == "Book is already borrowed!"


def test_return_book(library, book):
    library.add_book(book)
    library.borrow_book("Python Programming")
    response = library.return_book("Python Programming")
    assert response == "Python Programming has been returned."


def test_borrow_non_existent_book(library):
    response = library.borrow_book("Oliver Twist")
    assert response == "Book 'Oliver Twist' not found in library."
