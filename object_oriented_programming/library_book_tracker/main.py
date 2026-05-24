from book import Book
from library import Library
lib = RatedLibrary("Alice")

lib.add_book(Book("Dune", "Frank Herbert", 412))
lib.add_book(Book("1984", "George Orwell", 328))
lib.add_book(Book("Sapiens", "Yuval Noah Harari", 443))

# Mark one as done and rate it
lib._books[0].status = "done"
lib._books[0].rating = 5

print(lib)                  # uses __str__
print(len(lib))             # uses __len__
print("Dune" in lib)        # uses __contains__
print(lib.avg_rating)       # uses @property
print(lib.top_rated(2))     # uses inheritance

for book in lib:            # uses __iter__
    print(book)