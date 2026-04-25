from math import sqrt

n = input("Maximum Number: ")
n = int(n) + 1
for i in range(1, n):
    for b in range(i, n):
        c_square = i ** 2 + b ** 2
        c = int(sqrt(c_square))
        if ((c_square - c**2 ) == 0):
            print(i, b, c)



#Assignment Expressions

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



#Dictionary in Python

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



city_info_dict = {'Stuttgart': (207.35, 634830), 'Karlsruhe': (173.46, 313092), 'Mannheim': (144.96, 309370), 'Freiburg': (153.07, 230241), 'Heidelberg': (108.83, 160355), 'Heilbronn': (99.88, 125960)}
city_names = city_info_dict.keys()
print(city_names)

for city in city_names:
    print(city)

city_values = city_info_dict.values()

for area, population  in city_values:
    print("Area:", area, "sq. km, Population:", population)


# Turn Lists into Dictionaries

cities = ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt']
areas = [891.68, 755.3, 310.7, 405.02, 248.31]
populations = [3769495, 1841179, 1471508, 1085664, 753056]

city_areas_dicts = dict(zip(cities, areas))
print(city_areas_dicts)

city_info_dicts = {city: (area, population) for city, area, population in zip(cities, areas, populations)}
print(city_info_dicts)



#pop() and popitem()

capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam", "Switzerland":"Bern"}

capitals_dict = capitals.pop("Switzerland")
print(capitals_dict)
print(capitals)

capital = {"Springfield": "Illinois",
            "Augusta": "Maine",
            "Boston": "Massachusetts",
            "Lansing": "Michigan",
            "Albany": "New York",
            "Olympia": "Washington",
            "Toronto": "Ontario"}

(city, state) = capital.popitem()
print(city, state)
print(capital)


# Iterating over a Dictionary

d = {"a": 123, "b": 34, "c": 456, "d": 789}
for k in d:
    print(k, d[k])






#==============================13. Sets and Frozen Sets =========================================

x = set("A Python Tutorial")
print(x)
y = set(["Perl", "Java", "Python"])
print(y)

cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
# print(cities)

# Immutable Set

# city = set((["Python", "Java"], ["Paris", "London", "Berlin"]))
# print(city)
cities_cities = set((("Python", "Java"), ("Paris", "London", "Berlin")))
print(cities_cities)


Frozensets

the_cities = set(["Frankfurt", "Basel", "freiburg"])
the_cities.add("strasbourg")
print(the_cities)


# my_cities = frozenset(["Frankfurt", "Basel", "freiburg"])
# my_cities.add("strasbourg")
# print(my_cities)


# Improved notation
adjectives = {"cheap", "expensive", "inexpensive", "economical"}
print(adjectives)


# Set Operations
colours = {"green", "red"}
colours.add("blue")
print(colours)

cities.clear()
print(cities)


more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)



x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}

print(x.difference(y))

#============================14. Sets Examples========================
#Different Words of a Text
import re

ulysses_txt = open("sons_and_lovers_lawrence.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", ulysses_txt)
print("The novel ulysses contains " + str(len(words)))

for word in ["the", "while", "good", "bad", "ireland", "irish"]:
    print("The word '" + word + "' occurs " + \
          str(words.count(word)) + " times in the novel!")

diff_words = set(words)
print("'Ulysses' contains " + str(len(diff_words)) + " different words!")

novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']




#=========================15. Keyboard Input=========================
name = input("What's your name? ")
print("Nice to meet you " + name + "!")

age = input("Your age? ")
print("So, you are already " + age + " years old, " + name + "!")

city_in_usa = input("Largest city in the USA: ")
print(city_in_usa, type(city_in_usa))


#==============================16. Conditional Statements=============================

#Conditional statements in Python

language = input("Your Preferred Language: ").lower()
if language == "french":
    print("preferz-vous parlez français?")
if language == "italian":
    print("Preferisci parlare italiano?")
else:
    print("You are neither French nor Italian.")
    print("So, let us speak English!")


# Ternary if Statement

inside_city_limit = False

maximum_speed = 50 if inside_city_limit else 100
print(maximum_speed)



# ============================================================17. Structural Pattern Matching==============================


