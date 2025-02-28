class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book - Title: {self.title}, Author: {self.author}"


class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            raise ValueError("Book already exists in library.")
        self.books[title] = Book(title, author)

    def remove_book(self, title):
        if title not in self.books:
            raise KeyError("Book not found in library.")
        del self.books[title]

    def is_available(self, title):
        return title in self.books

    def list_book(self):
        return [str(book) for book in self.books.values()]
