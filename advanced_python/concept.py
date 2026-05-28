#===========================1. Recursive Functions===========================
from typing import Iterator


#Recursive Functions in Python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = 5
print(factorial(n))


def iterative_factorial(n):
    result = 1
    if n == 0:
        return 1
    for i in range(2, n + 1):
        result *= i
    return result


for i in range(5):
    print(i,iterative_factorial(i))




#=================================2. Iterators and Iterables==========================

for city in ["Berlin", "Vienna", "Zurich"]:
    print(city)

def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

for element in [34, [4,5], (4,5), {"a": 1}, "dsfdd", 4.5]:
    print(element, "iterable", iterable(element))



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


class RangeIterator:
    def __init__(self, start: int, stop: int):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


it = RangeIterator(1, 4)
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# Basic generator function

def my_range(start: int, stop: int):
    current = start
    while current <= stop:
        yield current
        current += 1

for n in my_range(1, 10):
    print(n)

nums = list(my_range(1, 10))
print(nums)

a,b,c = my_range(10, 12)
print(a,b,c)

# Infinite sequence

def neutral():
    n = 0
    while True:
        yield n
        n += 1

def take(n, iterable):
    for i, value in enumerate(iterable):
        if i >= n:
            return
        yield value
def evens(iterable):
    for value in iterable:
        if value % 2 == 0:
            yield value

results = list(take(5, evens(neutral())))
print(results)

from itertools import islice, count, filterfalse
result2 = list(islice(
    (n for n in count() if n % 2 == 0), 5
))
print(result2)
