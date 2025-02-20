class LibraryItem:

    def __init__(self, title, author):
        self._title = title
        self._author = author

    def display_info(self):
        return "Title: {0._title}, Author: {0._author}".format(self)


class Book(LibraryItem):

    def __init__(self, title, author, pages):
        super().__init__(title=title, author=author)
        self.pages = pages

    def display_info(self):
        return super().display_info() + ", No. of pages: {0.pages}".format(self)


class Magazine(LibraryItem):

    def __init__(self, title, author, issue_number):
        super().__init__(title=title, author=author)
        self.issue_number = issue_number

    def display_info(self):
        return super().display_info() + ", Issue Number: {0.issue_number}".format(self)


if __name__ == '__main__':

    book = Book("Oliver Twist", "Frank", 300)
    print(book.display_info())

    mag = Magazine("Aldi Süd", "Aldi", 500)
    print(mag.display_info())
