class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrower = None

    def borrow(self, borrower):
        if self.borrower:
            return f"{self.title} is already borrowed."
        self.borrower = borrower
        return f"{self.title} has been borrowed by {borrower}."

    def return_book(self):
        if self.borrower is None:
            return f"{self.title} was not borrowed."
        borrower = self.borrower
        self.borrower = None
        return f"{self.title} has been returned."

    def __str__(self):
        return f"Book - Title:{self.title}, Author: {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        print(f"Adding book: {book.title}")
        self.books.append(book)

    def remove_book(self, book):
        print(f"Removing book: {book.title}")
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError(f"{book.title} not found in library!")

    def check_book(self, book):
        print(f"Checking if book exists: {book.title}")
        if book in self.books:
            return True
        return f"{book.title} not found!"

    def borrow_book(self, title, borrower):
        print(f"Attempting to borrow: {title} by {borrower}")
        for book in self.books:
            print(f"Checking book: {book.title}")
            if book.title == title:
                return book.borrow(borrower)
        return f"Book '{title}' not found in library."

    def return_book(self, title):
        print(f"Attempting to return: {title}")
        for book in self.books:
            print(f"Checking book: {book.title}")
            if book.title == title:
                return book.return_book()
        return f"Book '{title}' not found in library."
