class Book:
    def __init__(self, title: str):
        self.title = title
        self.is_checked_out = False
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checkout out.")
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")


class LibrarySystem:
    def __init__(self):
        self.books = []
    
    def add_books(self, book: Book):
        self.books.append(book)
    
    def checkout_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                book.check_out()
                return
        print(f"Book {book_title} not found in library.")
    
    def return_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                book.return_book()
                return
            
        print(f"Book {book_title} not found in library")

library = LibrarySystem()
library.add_books(Book("The Great Gatsby"))
library.add_books(Book("1984"))
library.add_books(Book("To Kill a Mockingbird"))

library.checkout_book("1984")
library.checkout_book("The Great Gatsby")
library.checkout_book("1984")

library.return_book("1984")
library.return_book("1984")