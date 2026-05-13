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

#
# from dataclasses import dataclass
# @dataclass(frozen=True)
# class Book_info:
#     title: str
#     author: str
#     ISBN: int
#     year: int
#     genre: str
#
#     def display_info(self):
#         return f"{self.title} - {self.author} - {self.ISBN} - {self.year}"
#
#
# book1 = Book_info(
#     title = "Atomic Habits",
#     author = "James Clear",
#     ISBN = 9780735211292,
#     year= 2018,
#     genre = "Self-improvement/Productivity"
# )
# book2 = Book_info(
#    title= "Clean Code: A Handbook of Agile Software Craftsmanship",
#     author = "Robert C. Martin",
#     ISBN = 9780132350884,
#     year= 2008,
#     genre = "Programming / Software Engineer"
# )
# book3 = Book_info(
#     title= "The Pragmatic Programmer",
#     author = "Andrew Hunt & David Thomas",
#     ISBN = 9780135957059,
#     year= 1999,
#     genre = "Programming / Career Development"
# )
# book4 = Book_info(
#     title= "Deep Work",
#     author = "Cal Newport",
#     ISBN= 9781455586691,
#     year= 2016,
#     genre= "Productivity / Personal Development"
#
# )
#
# books = [book1, book2, book3, book4]
# for book in books:
#     print(book.display_info())










# Exercise 1
# Write a class with the name Ccy, similar to the previously defined Length class.Ccy should contain values in various currencies, e.g. "EUR", "GBP" or "USD". An instance should contain the amount and the currency unit. The class, you are going to design as an exercise, might be best described with the following example session:
#
# from currencies import Ccy
# v1 = Ccy(23.43, "EUR")
# v2 = Ccy(19.97, "USD")
# print(v1 + v2)
# print(v2 + v1)
# print(v1 + 3) # an int or a float is considered to be a EUR value
# print(3 + v1)

class Ccy:
    currencies = {
        'CHF': 1.0821202355817312,
        'CAD': 1.488609845538393,
        'GBP': 0.8916546282920325,
        'JPY': 114.38826536281809,
        'EUR': 1.0,
        'USD': 1.11123458162018
    }

    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def changeTo(self, new_unit):
        """
            An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
            Defines the '+' operator.
            If other is a CCy object the currency values
            are added and the result will be the unit of
            self. If other is an int or a float, other will
            be treated as a Euro value.
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        return Ccy(x + self.value, self.unit)

    def __iadd__(self, other):
        """
            Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res
    
    


x = Ccy(10,"USD")
y = Ccy(11)
z = Ccy(12.34, "JPY")
z = 7.8 + x + y + 255 + z
print(z)
lst = [Ccy(10,"USD"), Ccy(11), Ccy(12.34, "JPY"), Ccy(12.34, "CAD")]
z = sum(lst)
print(z)