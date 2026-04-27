# # Exercise 1
# # Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters.
# # The values of both dictionaries are numerical.
# # The function should return the merged sum dictionary m of those dictionaries.
# # If a key k is both in d1 and d2, the corresponding values will be added and included
# # in the dictionary m If k is only contained in one of the dictionaries,
# # the k and the corresponding value will be included in m
#
from math import factorial


def dict_merge_sum(d1, d2):
    m = {}

    for k in d1:
        m[k] = d1[k]

    for k in d2:
        if k in m:
            m[k] = m[k] + d2[k]
        else:
            m[k] = d2[k]
    return m

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 40}

result = dict_merge_sum(d1, d2)
print(result)


#
# #Exercise 2
# # Given is the following simplified data of a supermarket:
#
supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}
# # To be ready for an imminent crisis you decide to buy everything.
# # This isn't particularly social behavior,
# # but for the sake of the task, let's imagine it. The question is how much will you have to pay?
#

def total_price(d):
    sum = 0
    for k,v in d.items():
        sum += v["quantity"] * v["price"]
    return f"The total price of your grocery is ${sum}"

result = total_price(supermarket)
print(result)

#
# # Exercise 4
# # Given is the island of Vannoth
#
# #Create a dictionary, where we get for every city of Vannoth the distance to the capital city of Rogeburgh
#
distance_from_capital = {'Rogerburgh': 0,
                         'Smithstad': 5.2,
                         'Scottshire': 12.3,
                         'Clarkhaven': 14.9,
                         'Dixonshire': 12.7,
                         'Port Carol': 3.4}



# #Exercise 8
# #Student Gradebook using Nested Dictionaries
#
# #To solve this exercise you have to be familiar with functions in Python, see our introduction on functions in our python course.
#
# #Create a Python program to manage a student gradebook using nested dictionaries. Follow these steps to implement the functionality:
#
# #Initialize an empty dictionary to serve as the gradebook.
# #Implement a function add_student(gradebook, student_name) that takes the gradebook dictionary and a student name as input and adds an empty dictionary for the student's grades to the gradebook.
# #Implement a function add_grade(gradebook, student_name, subject, grade) that takes the gradebook dictionary, a student name, a subject name, and a grade as input. This function should add the grade for the specified subject to the grades dictionary of the specified student in the gradebook.
# #Implement a function calculate_average_grade(gradebook, student_name) that takes the gradebook dictionary and a student name as input and calculates the average grade for the specified student.
# #Implement a function display_gradebook(gradebook) that takes the gradebook dictionary as input and displays the contents of the gradebook, including student names, subjects, and grades, as well as the average grade for each student.
# #Use the provided sample usage to demonstrate the functionality of your program.
#
# #Note: You may assume that each student will have unique names, and subjects may have duplicate names but within the context of different students.
#
gradeBook = {}

def add_student(gradeBook, student_name):
    gradeBook[student_name] =  {}
    return gradeBook

def add_grade(gradeBook, student_name, subject, grade):
    gradeBook[student_name][subject] = grade
    return gradeBook

def calculate_average(gradeBook, student_name):
    total = 0
    for subject in gradeBook[student_name]:
        total += gradeBook[student_name][subject]
    result = total / len(gradeBook[student_name])
    return result
def display_gradebook(gradeBook):
    print("Gradebook:")
    for student, grades in gradeBook.items():
        print(student + ":")
        for subject, grade in grades.items():
            print("- {}: {}".format(subject, grade))
        average_grade = calculate_average(gradeBook, student)
        if average_grade is not None:
            print("  Average grade: {:.2f}".format(average_grade))
        print()
result = add_student(gradeBook, 'Anchita')
grade1 = add_grade(gradeBook,student_name="Anchita", subject='Math', grade=90)
grade2 = add_grade(gradeBook,student_name="Anchita", subject='Linear Algebra', grade=30)
grade3 = add_grade(gradeBook,student_name="Anchita", subject='Science', grade=100)
grade4 = add_grade(gradeBook,student_name="Anchita", subject='Engineering', grade=70)
average = calculate_average(gradeBook, 'Anchita')
print(display_gradebook(gradeBook))




#=============================16. Conditional Statements Execises ===========================

# Exercise 1
# Write a Python program that checks the temperature and provides a message based
# on the temperature value.
# If the temperature is above 27 degrees Celsius, it should print "It's a hot day."
# If the temperature is 27 degrees or below, it should print "It's not a hot day."

def check_temperature(temperature):
    if temperature == "" or type(temperature) != int:
        return "invalid input type"
    if temperature > 27:
        return "it's hot today 🌞"
    if temperature < 27:
        return "it's not a hot day."

temperature = int(input("Enter a temperature between 0 and 27: "))
print(check_temperature(temperature))



# Exercise 2
# Write a Python program that calculates and displays a letter grade for a given numerical score based on the following grading scale:
#
#     A: 90-100
#     B: 80-89
#     C: 70-79
#     D: 60-69
#     F: 0-59
#
def calculate_grade(grade):
    if grade > 0 and grade < 59:
        return "F"
    elif grade >= 60 and grade <= 69:
        return "D"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 90 and grade <= 100:
        return "A"
    else:
        return "invalid input"

#
#
# grade = int(input("Enter a grade: "))
# print(calculate_grade(grade))


# Exercise 3
# Write a Python program that classifies a person's age into one of the following categories: "Infant," "Child," "Teenager," "Adult," or "Senior." The program should ask the user for their age and then display the corresponding classification based on the following guidelines:
#
#     Infants: 0-2 years old
#     Children: 3-12 years old
#     Teenagers: 13-19 years old
#     Adults: 20-64 years old
#     Seniors: 65 years old and older


# def age_classification(age):
#     if age >= 65:
#         return "You're a seniors"
#     elif age >= 20 and age <= 64:
#         return "You're an adult"
#     elif age >= 13 and age < 19:
#         return "You're a teenagers"
#     elif age >= 3 and age <= 12:
#         return "You're a child"
#     elif age >= 0 and age <= 2:
#         return "You're an infant"
#     else:
#         return "invalid input"
#
#
# age = int(input("Enter a age: "))
# print(age_classification(age))



# Exercise 4
# A leap year is a calendar year containing an additional day added
# to keep the calendar year synchronized with the astronomical or seasonal year.
# In the Gregorian calendar, each leap year has 366 days instead of 365,
# by extending February to 29 days rather than the common 28.
# These extra days occur in years which are multiples of four (with the exception of centennial years not divisible by 400).
# Write a Python program, which asks for a year and calculates, if this year is a leap year or not.


# def leap_year(year):
#     if year % 4:
#         return f"{year} is not a leap year"
#     elif year % 100 == 0 and year % 400 != 0:
#         return f"{year} is not a leap year"
#     else:
#         return f"{year} is a leap year"
#
# year = int(input("Enter a year: "))
# print(leap_year(year))

# ======================================While Loops Exercise ======================

# Exercise 1: Dog Age to Human Age
# We had a program to convert a dog age to a human age in our chapter Conditional Statements.
#
# This was the program:
#
# while True:
#     dog_age = int(input("Age of the dog: "))
#     print()
#     if dog_age <= 0:
#         human_age = -1
#
#     elif dog_age == 1:
#         human_age = 14
#     else:
#         # this means: dog_age >= 2:
#         human_age = 22 + (dog_age - 2) * 5
#     if human_age > 0:
#         print("Corresponds to  " + str(human_age) + " human years!")
#     else:
#         print("Negative values or zero makes no sense for a dog age!")
#         break

# Write a version with a while loop so that people can keep on converting dog ages.
# 0 or a negative value means that they want to finish.


# Exercise 2: Factorial Calculator
# Write a Python program that calculates the factorial of a number entered by the user using a while loop.
# The factorial of a non-negative integer n, denoted in mathematics as n!,
# is the product of all positive integers from 1 to n.
# For example, 5! (read as "5 factorial") is equal to 5 * 4 * 3 * 2 * 1, which is 120.

#
# n = int(input("Enter a number: "))
# factorial = 1
# counter = 1
# while counter <= n:
#
#
#
#
#         factorial *= counter
#         counter += 1
# print(f"{n}! = {factorial}")



# Exercise 3: Password Checker
# Write a Python program that simulates a simple password checker.
# The program should ask the user to enter a password and continue
# to prompt them until they enter the correct password.
# Once the correct password is entered, the program should print a success message.

#
# maximum_attempt = 5
# while True:
#     password = input("Enter a password: ")
#     if maximum_attempt == 0:
#         print("You exceeded the maximum number of attempts.")
#         break
#     else:
#         if password == "Anchitafnu826$":
#             print("Congrats! You guessed the password correctly!")
#             break
#         else:
#             print("Invalid input. Try again.")
#     if maximum_attempt == 2:
#         print('You only have 2 attempts left.')
#     maximum_attempt -= 1
#



#===================================29. File Management ========================

# Exercise 1
# Write a function which reads in a text from file and returns a list of the paragraphs.
# You may use one of the following books:

def read_books():
    paragraphs = []

    with open("./files/Virginia_wolf.txt", "r") as file:
        text= file.read()
    raw_paragraphs = text.split("\n\n")
    for paragraph in raw_paragraphs:
        paragraphs.append(paragraph)
    return paragraphs


print(read_books())