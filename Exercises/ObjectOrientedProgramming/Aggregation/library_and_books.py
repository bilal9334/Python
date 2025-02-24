class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book - Title: {self.title}, Author: {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "Library is empty!"
        else:
            for book in self.books:
                print(f"{book} - Available")


if __name__ == '__main__':
    book1 = Book("Oliver Twist", "Charles Dickens")
    book2 = Book("The Adventure of Tom Sawyer", "Mark Twain")

    library = Library()

    # Adding Books to Library
    library.add_books(book1)
    library.add_books(book2)

    # Output
    library.list_books()
