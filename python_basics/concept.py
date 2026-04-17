# from math import sqrt
#
# n = input("Maximum Number: ")
# n = int(n) + 1
# for i in range(1, n):
#     for b in range(i, n):
#         c_square = i ** 2 + b ** 2
#         c = int(sqrt(c_square))
#         if ((c_square - c**2 ) == 0):
#             print(i, b, c)
#
#

# Assignment Expressions

def f(x):
    return x + 4


numbers = [3, 7, 2, 9, 12]
odd_numbers = [result for x in numbers if(result := f(x)) % 2]
print(odd_numbers)


#List Manipulation

colours = ["red", "green", "blue", "green", "yellow"]
colours.remove("green")
print(colours)
print(colours.index("green"))


lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)


#deepcopy

from copy import deepcopy

person1 = ["Swen", ["Seestrasse", "Konstanz"]]
person2 = deepcopy(person1)
print(id(person1), id(person2))



# Dictionary in Python

person = {
    'name': 'Fnu Anchita',
    'age': 18,
    'city': 'Berlin',
    'email': 'anna@example.de'
}

name = person['name']
age = person['age']

print("Name:", name)
print("Age:", age)
person["city"] = "New York"
print(person)
person['sex'] = 'female'
person['favorite_hobbies'] = ['reading', 'music', 'programming']
print(person)
del person["sex"]
print(person)




city_population = {
    'Berlin': (3769495, 'Germany'),
    'Paris': (2161000, 'France'),
    'Vienna': (1921641, 'Austria'),
    'Hamburg': (1841179, 'Germany'),
    'Amsterdam': (872680, 'Netherlands'),
    'Rotterdam': (651446, 'Netherlands'),
    'Stuttgart': (634830, 'Germany'),
    'Zurich': (415215, 'Switzerland'),
    'Graz': (290571, 'Austria'),
    'Strasbourg': (280966, 'France'),
    'Freiburg': (230241, 'Germany'),
    'Geneva': (201818, 'Switzerland'),
    'Basel': (178128, 'Switzerland'),
    'Salzburg': (155031, 'Austria'),
    'Luxembourg City': (124528, 'Luxembourg'),
    'Metz': (117619, 'France')
}
city_population['Munich'] = (1471508, 'Germany')
city_population['Cologne'] = (1085664, 'Germany')
print(city_population)


#Convert Dictionaries to Lists
city_population_list = list(city_population.items())
print(city_population_list)
print(city_population_list[0])


city_name = input("Please enter your city name: ")
population = None

for city, (pop, _) in city_population_list:
    if city_name.lower() == city.lower():
        population = pop
        break
if population is None:
    print(f"The population of {city_name} is {population}")
else:
    print(f"Population data for {city_name} is not available.")