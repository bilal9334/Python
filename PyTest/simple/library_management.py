class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            return "Book is already borrowed!"
        else:
            self.borrowed = True
            return "Book borrowed!"

    def return_book(self):
        if not self.borrowed:
            return f"{self.title} was not borrowed."
        self.borrowed = False
        return f"{self.title} has been returned."

    def __str__(self):
        return f"Book - Title: {self.title}, Author: {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError(f"{book.title} not found in library!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return f"Book '{title}' not found in library."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return f"Book '{title}' not found in library."
