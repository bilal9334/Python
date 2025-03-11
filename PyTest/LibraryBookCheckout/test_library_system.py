import pytest
from library_system import Book, LibrarySystem

@pytest.fixture
def book():
    return Book("The Great Gatsby")

@pytest.fixture
def another_book():
    return Book("1984")

def test_check_out_book(book):
    book.check_out()
    assert book.is_checked_out == True

def test_return_book(book):
    book.check_out()
    book.return_book()
    assert book.is_checked_out == False

def test_return_book_not_checked_out(book):
    book.return_book()
    assert book.is_checked_out == False

def test_check_out_already_checked_out_book(book):
    book.check_out()
    book.check_out()
    assert book.is_checked_out == True


# Test for Library
def test_add_book_to_library(book):
    library = LibrarySystem()
    library.add_books(book)
    library.add_books(another_book)
    assert len(library.books) == 2

# def test_checkout_book_from_library(book):
#     library = LibrarySystem()
#     library.add_books(book)
#     library.checkout_book(book)
#     assert book.is_checked_out() == True

def test_checkout_book_not_in_library(another_book):
    library = LibrarySystem()
    library.checkout_book(another_book)

def test_return_book_to_library(book):
    library = LibrarySystem()
    library.add_books(book)
    library.checkout_book(book)
    library.return_book(book)
    assert book.is_checked_out == False

def test_return_book_not_in_library(book):
    library = LibrarySystem()
    library.return_book(book)