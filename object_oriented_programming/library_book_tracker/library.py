from book import *
class Library:

    name = "Diallo Library"
    _total_libraries = 0

    def __init__(self, owner):
        self.owner = owner
        self._books = []

    def __str__(self):
        return f"{self.name} - owned by {self.owner} ({len(self._books)} books)"


    def __len__(self):
        return len(self._books)

    def __contains__(self, item):
        return item in self._books

    def __iter__(self):
        return iter(self._books)

    def add_book(self, book):
        self._books.append(book)

    def find_by_author(self):
        for book in self._books:
            if book.author == self.owner:
                return book
    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)


