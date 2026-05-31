#===========================1. Recursive Functions===========================
from typing import Iterator


#Recursive Functions in Python
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# n = 5
# print(factorial(n))
#
#
# def iterative_factorial(n):
#     result = 1
#     if n == 0:
#         return 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# for i in range(5):
#     print(i,iterative_factorial(i))
#
#


#=================================2. Iterators and Iterables==========================

# for city in ["Berlin", "Vienna", "Zurich"]:
#     print(city)
#
# def iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except TypeError:
#         return False
#
# for element in [34, [4,5], (4,5), {"a": 1}, "dsfdd", 4.5]:
#     print(element, "iterable", iterable(element))



#=================================3. Generators and Iterators==========================
# other_cities = ["Strasbourg", "Freiburg", "Stuttgart",
#                 "Vienna / Wien", "Hannover", "Berlin",
#                 "Zurich"]
#
# city_iterator = iter(other_cities)
# while city_iterator:
#     try:
#         city = next(city_iterator)
#         print(city)
#     except StopIteration:
#         break
#
#
#
# # Implementing an Iterator as a Class
#
# class Cycle(object):
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.iterator = iter(iterable)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while True:
#             try:
#                 element = next(self.iterator)
#                 return element
#             except StopIteration:
#                 self.iterator = iter(self.iterable)
#
#
# x = Cycle("abc")
#
# for i in range(10):
#     print(next(x), end=", ")
#
#
#
# # Generators
# def count(firstval=0, step=1):
#     x = firstval
#     while True:
#         yield x
#         x += step
#
# counter = count()
# for i in range(10):
#     print(next(counter), end=", ")
#
# start_value = 2.1
# stop_value = 0.3
# print("\nNew counter:")
# counter = count(start_value, stop_value)
# for i in range(10):
#     new_value = next(counter)
#     print(f"{new_value:2.2f}", end=", ")



#Manual Iterators


# class RangeIterator:
#     def __init__(self, start: int, stop: int):
#         self.current = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.stop:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
#
#
# it = RangeIterator(1, 4)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
#

# Basic generator function
#
# def my_range(start: int, stop: int):
#     current = start
#     while current <= stop:
#         yield current
#         current += 1
#
# for n in my_range(1, 10):
#     print(n)
#
# nums = list(my_range(1, 10))
# print(nums)
#
# a,b,c = my_range(10, 12)
# print(a,b,c)
#
# # Infinite sequence
#
# def neutral():
#     n = 0
#     while True:
#         yield n
#         n += 1
#
# def take(n, iterable):
#     for i, value in enumerate(iterable):
#         if i >= n:
#             return
#         yield value
# def evens(iterable):
#     for value in iterable:
#         if value % 2 == 0:
#             yield value
#
# results = list(take(5, evens(neutral())))
# print(results)
#
# from itertools import islice, count, filterfalse
# result2 = list(islice(
#     (n for n in count() if n % 2 == 0), 5
# ))
# print(result2)




#============================4. Lambda Operator, filter, reduce and map=========================
# square  = lambda x: x * x
# print(square(5))
#
#
# prices = [10, 20, 30, 40, 50]
# taxed_prices = map(lambda p: p * 1.10, prices)
# print(list(taxed_prices))
#
#
# scores = [55, 82, 67, 90, 74, 43]
# passing_scores = filter(lambda s: s >= 70, scores)
# print(list(passing_scores))
#
# from functools import reduce
#
# numbers = [2, 3, 5, 6, 7]
# total_product = reduce(lambda x, y: x * y, numbers)
# print(total_product)
#
#
# salaries = [40000, 65000, 32000, 80000, 50000]
#
# high_salary = filter(lambda s: s > 45000, salaries)
# print(list(high_salary))
#



#=====================5. zip introduction and examples====================
#
# heroes = ["Batman", "Superman", "Spider-Man"]
# identities = ["Bruce Wayne", "Clark Kent", "Peter Parker"]
#
# zipped_heros = zip(heroes, identities)
# for name, identity in zipped_heros:
#     print(f"{name} is secretly {identity}")
#
# pairs = [("Apples", 2.50), ("Bananas", 1.20), ("Cherries", 4.00)]
# items, prices = zip(*pairs)
# print(items)
# print(prices)
#
#
# keys = ["username", "email", "role"]
# values = ["dev_pro", "pro@email.com", "Admin"]
#
# user_profile = dict(zip(keys, values))
# print(user_profile)
#
#
#
# students = ["Alex", "Blair", "Charlie", "Drew"]
# scores = [85, 92, 78, 95]
#
# result = zip(students, scores)
# for name, score in result:
#     print(f"{name} scores {score}/100")


#===================6. Decorators and Decoration==================================
# def shout(text):
#     return text.upper()
#
# def print_msg(func_to_run):
#     print("Starting process...")
#     print(func_to_run("hello"))
#
# print(print_msg(shout))
#
#
# def polite_decorator(original_func):
#
#     def wrapper():
#         print("Bonjour! Nice to meet you.")  # Code before
#         original_func()  # The original function runs!
#         print("Au revoir! Have a nice day.")
#
#     return wrapper
# @polite_decorator
# def say_name():
#     print("My name is Gemini.")
#
#
# print(say_name())
#
#
#
# import time
# def time_decorator(original_func):
#     def wrapper():
#         start_time = time.time()
#         original_func()
#         end_time = time.time()
#
#         print(f"⏱️ Execution time: {end_time - start_time:.4f} seconds")
#     return wrapper
#
# @time_decorator
# def heavy_calculator():
#     print("Running a massive loop...")
#     time.sleep(1.2)
#
# print(heavy_calculator())
#
#
# def security_bypassed_check(func):
#     def wrapper(*args, **kwargs):
#         print("--- Doing something before ---")
#         print("⚠️ WARNING: Accessing sensitive data account...")
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
#
# @security_bypassed_check
# def view_bank_vault():
#     print("🔓 Vault Opened! Accessing $1,000,000.")
#
# view_bank_vault()
#
#
# def universal_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("--- Doing something before ---")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @universal_decorator
# def greet_name(name, age):
#     print(f"Hello, {name}! I am {age} years old.")
#
# greet_name("Ousmane", 18)






#===============================7. Memoization and Decorators=========================
# def fetch_user_data(user_id):
#     print(f"📡 Fetching user {user_id} from slow database...")
#     return {"id": user_id, "status": "Active"}
#
#
# fetch_user_data(101)
# fetch_user_data(102)
# fetch_user_data(101)
#
#
#
# notepad = {}
#
# def calculate_expensive_bonus(worker_name):
#     if worker_name in notepad:
#         print(f"⚡ [CACHE HIT] Found {worker_name} in the notepad. Skipping math!")
#         return notepad[worker_name]
#
#     print(f"📡 [MATH DETECTED] Calculating bonus for {worker_name}...")
#
#     calculate_bonus = 5000 * 1.15
#
#     notepad[worker_name] = calculate_bonus
#     return calculate_bonus
#
#
# print(calculate_expensive_bonus("Alice"))
# print(calculate_expensive_bonus("Bob"))
# print(calculate_expensive_bonus("Alice")) # Calling Alice again!
#
#
#
#
# # Our secret notepad to store downloaded images
#
# image_cache = {}
#
# def download_profile_pic(username):
#     if username in image_cache:
#         print(f"⚡ [CACHE HIT] Already have {username}'s photo in memory. Displaying instantly!")
#         return image_cache[username]
#
#     print(f"🌐 [NETWORK DOWNLOAD] Connecting to server to get {username}'s photo...")
#     raw_image_data = f"📸 Raw_Data_Of_{username}_Photo.png"
#
#     image_cache[username] = raw_image_data
#     return raw_image_data
#
#
# download_profile_pic("alex_travels")
# download_profile_pic("coding_pro")
# download_profile_pic("alex_travels") # Clicking Alex again!
#
#
#
# def memoize_image(original_download_function):
#     notepad = {}
#
#     def wrapper(username):
#         if username in image_cache:
#             print(f"⚡ [DECORATOR CACHE] Found {username} in memory!")
#             return image_cache[username]
#
#         result = original_download_function(username)
#         notepad[username] = result
#         return result
#     return wrapper
#
# @memoize_image
# def download_profile_pic(username):
#     print(f"🌐 Downloading {username}'s photo from the web...")
#     return f"📸 {username}_image.png"
#
# download_profile_pic("sarah_sky") # Runs the download code
# download_profile_pic("sarah_sky")
#
#
#
# def universal_memoize(func):
#     notepad = {}
#
#     def wrapper(*args):
#         if args in notepad:
#             print("⚡ [CACHE HIT] Answer found in notepad!")
#             return notepad[args]
#
#         result = func(*args)
#         notepad[args] = result
#         return result
#     return wrapper
#
#
# def memoize_flights(func):
#
#     notepad = {}
#     def wrapper(*args):
#         if args in notepad:
#             print("⚡ [CACHE HIT] Answer found in notepad!")
#             return notepad[args]
#         result = func(*args)
#         notepad[args] = result
#         return result
#     return wrapper
#
# @memoize_flights
# def get_flight_price(destination):
#     print(f"✈️ Searching airline databases for flights to {destination}...")
#     return 450.00
#
#
# print(get_flight_price("Tokyo"))
# print(get_flight_price("Paris"))
# print(get_flight_price("Tokyo"))
#
#
#
#
#
#======================8. Functional Programming OOP==============================
# class ImmutableEmployee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def apply_raise(self, amount):
#         return ImmutableEmployee(self.name, self.salary + amount)
#
#
# emp1 = ImmutableEmployee("Bob", 50000)
# emp2 = emp1.apply_raise(5000)
#
# print(emp1.salary)
# print(emp2.salary)
#
#
#
# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#
#
# catalog = [
#     Product("Laptop", 1200, "Electronics"),
#     Product("Shirt", 40, "Clothing"),
#     Product("Headphones", 150, "Electronics"),
#     Product("Book", 20, "Media")
# ]
#
# electronics = filter(lambda x: x.category == "Electronics", catalog)
# price = map(lambda x: x.price, electronics)
# total_cost = sum(price)
# print(total_cost)
#
#
#
#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#
#     def deposit(self, amount):
#         return BankAccount(self.owner, self.balance + amount)
#     def withdraw(self, amount):
#         return BankAccount(self.owner, self.balance - amount)
#
# acc1 = BankAccount("Charlie", 1000)
# acc2 = acc1.deposit(500)
# acc3 = acc2.withdraw(700)
#
# print(acc1.balance)
# print(acc2.balance)
# print(acc3.balance)
#
#
# #=====Problem 2: The Fleet Tracker Pipeline========
# class Vehicle:
#     def __init__(self, vin, status, mileage):
#         self.vin = vin
#         self.status = status
#         self.mileage = mileage
#
# fleet = [
#     Vehicle("V101", "Active", 50000),
#     Vehicle("V102", "Maintenance", 120000),
#     Vehicle("V103", "Active", 35000),
#     Vehicle("V104", "Active", 80000),
#     Vehicle("V105", "Maintenance", 15000)
# ]
#
# active = filter(lambda x: x.status == "Active", fleet)
# active_mileages = map(lambda x: x.mileage, active)
# mileage_list = list(active_mileages)
#
# average_mileage = sum(mileage_list) / len(mileage_list)
# print(f"Active Vehicle Mileages: {mileage_list}")
# print(f"Average Fleet Mileage: {average_mileage} miles")
#
#
# #Problem 3: The RPG Character Inventory Reducer
# from functools import reduce
# class Item:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
# inventory = [
#     Item("Iron Sword", 12.5),
#     Item("Health Potion", 0.5),
#     Item("Steel Shield", 22.0),
#     Item("Magic Scroll", 0.2)
# ]
#
# total_weight = reduce(lambda x, y: x + y.weight, inventory, 0)
# print(total_weight)




#===========================9. List Comprehension====================================
numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number * number)
print(squares)


squares = [number * number for number in numbers]
print(squares)

even_squares = [number for number in numbers if number % 2 == 0]
print(even_squares)


words = ["apple", "banana", "cherry"]
shouting = [w.upper() for w in words]
print(shouting)



# Problem 1: The Email Cleaner
dirty_emails = [" user1@gmail.com ", "admin@site.com   ", "  hello@yahoo.com "]
clean_emails = [email.strip() for email in dirty_emails]
print(clean_emails)

# Problem 2: High-Score Filter
all_scores = [45, 120, 88, 200, 99, 105, 30]

elite_scores = [score for score in all_scores if score >= 100]
print(elite_scores)


# Problem 3: The VIP Guest Initializer
guests = ["Alex", "Alexander", "Bo", "Cassandra", "Ed"]
badge_initials = [name[0] for name in guests if len(name) > 4]
print(badge_initials)


scores = [40, 85, 30, 92]
results = ["pass" if s >= 50 else "fail" for s in scores]
print(results)

order_totals = [25.0, 140.5, 99.0, 300.0, 12.0]
shipping_cost = [0 if s >= 100 else 15 for s in order_totals]
print(shipping_cost)