class Book:

    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    def __str__(self):
        return f"Book - Title: {self._title}, Author: {self._author}, Pages: {self._pages}"


class Magazine:

    def __init__(self, title, editor, issue_number):
        self._title = title
        self._editor = editor
        self._issue_number = issue_number

    def __str__(self):
        return f"Magazine - Title: {self._title}, Editor: {self._editor}, Issue Number: {self._issue_number}"


class Library:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_item(self):
        if not self.items:
            print("Library is empty")
        else:
            for item in self.items:
                print(item)


if __name__ == '__main__':
    book1 = Book("Olivar Twist", "Charles Dickens", 300)
    book2 = Book("The Adventure of Tom Sawyer", "Mark Twain", 220)
    magazine = Magazine("National Geographic", "Susan Goldberg", 150)

    library = Library()

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine)

    library.list_item()
