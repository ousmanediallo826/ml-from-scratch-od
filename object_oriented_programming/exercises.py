# Exercise 1: Book Information
# Create a Book class using dataclass to represent information about books. Each book should have the following attributes:
#
# Title
# Author
# ISBN (International Standard Book Number)
# Publication Year
# Genre
# Write a program that does the following:
#
# Define the Book class using dataclass.
# Create instances of several books.
# Print out the details of each book, including its title, author, ISBN, publication year, and genre.
# You can use this exercise to practice defining dataclass, creating instances, and accessing attributes of dataclass objects. Additionally, you can explore how to add methods or customizations to the Book class, such as implementing a method to calculate the age of the book based on the publication year or adding validation for ISBN numbers.


from dataclasses import dataclass
@dataclass(frozen=True)
class Book_info:
    title: str
    author: str
    ISBN: int
    year: int
    genre: str

    def display_info(self):
        return f"{self.title} - {self.author} - {self.ISBN} - {self.year}"


book1 = Book_info(
    title = "Atomic Habits",
    author = "James Clear",
    ISBN = 9780735211292,
    year= 2018,
    genre = "Self-improvement/Productivity"
)
book2 = Book_info(
   title= "Clean Code: A Handbook of Agile Software Craftsmanship",
    author = "Robert C. Martin",
    ISBN = 9780132350884,
    year= 2008,
    genre = "Programming / Software Engineer"
)
book3 = Book_info(
    title= "The Pragmatic Programmer",
    author = "Andrew Hunt & David Thomas",
    ISBN = 9780135957059,
    year= 1999,
    genre = "Programming / Career Development"
)
book4 = Book_info(
    title= "Deep Work",
    author = "Cal Newport",
    ISBN= 9781455586691,
    year= 2016,
    genre= "Productivity / Personal Development"

)

books = [book1, book2, book3, book4]
for book in books:
    print(book.display_info())
