# Exercise 1
# Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters.
# The values of both dictionaries are numerical.
# The function should return the merged sum dictionary m of those dictionaries.
# If a key k is both in d1 and d2, the corresponding values will be added and included
# in the dictionary m If k is only contained in one of the dictionaries,
# the k and the corresponding value will be included in m

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



#Exercise 2
# Given is the following simplified data of a supermarket:

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
# To be ready for an imminent crisis you decide to buy everything.
# This isn't particularly social behavior,
# but for the sake of the task, let's imagine it. The question is how much will you have to pay?


def total_price(d):
    sum = 0
    for k,v in d.items():
        sum += v["quantity"] * v["price"]
    return f"The total price of your grocery is ${sum}"

result = total_price(supermarket)
print(result)


# Exercise 4
# Given is the island of Vannoth

#Create a dictionary, where we get for every city of Vannoth the distance to the capital city of Rogeburgh

distance_from_capital = {'Rogerburgh': 0,
                         'Smithstad': 5.2,
                         'Scottshire': 12.3,
                         'Clarkhaven': 14.9,
                         'Dixonshire': 12.7,
                         'Port Carol': 3.4}



#Exercise 8
#Student Gradebook using Nested Dictionaries

#To solve this exercise you have to be familiar with functions in Python, see our introduction on functions in our python course.

#Create a Python program to manage a student gradebook using nested dictionaries. Follow these steps to implement the functionality:

#Initialize an empty dictionary to serve as the gradebook.
#Implement a function add_student(gradebook, student_name) that takes the gradebook dictionary and a student name as input and adds an empty dictionary for the student's grades to the gradebook.
#Implement a function add_grade(gradebook, student_name, subject, grade) that takes the gradebook dictionary, a student name, a subject name, and a grade as input. This function should add the grade for the specified subject to the grades dictionary of the specified student in the gradebook.
#Implement a function calculate_average_grade(gradebook, student_name) that takes the gradebook dictionary and a student name as input and calculates the average grade for the specified student.
#Implement a function display_gradebook(gradebook) that takes the gradebook dictionary as input and displays the contents of the gradebook, including student names, subjects, and grades, as well as the average grade for each student.
#Use the provided sample usage to demonstrate the functionality of your program.

#Note: You may assume that each student will have unique names, and subjects may have duplicate names but within the context of different students.

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

