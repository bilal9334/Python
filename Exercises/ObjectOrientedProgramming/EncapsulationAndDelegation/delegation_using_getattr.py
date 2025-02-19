class Printer:
    """Class to show the working of a printer"""

    def print_document(self):
        return "Printing document..."

    def scan_document(self):
        return "Scanning document..."


class Office:
    """Office has printer which is used for printing or scanning documents"""

    def __init__(self):
        self.printer = Printer()

    def __getattr__(self, attr):
        return getattr(self.printer, attr)


if __name__ == '__main__':
    my_office = Office()
    print(my_office.print_document())
    print(my_office.scan_document())
