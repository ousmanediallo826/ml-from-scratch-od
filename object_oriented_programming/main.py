# def hi(obj):
#     print("Hi, I am " + obj.name + "!")
#
# class Robot:
#     pass
# x = Robot()
# x.name = "Marvin"
# hi(x)
import weakref
# The __init__ Method
# class Robot:
#     def __init__(self, name=None, build_year=None):
#         self.name = name
#         self.build_year = build_year
#
#     def say_hi(self):
#         if self.name:
#             print("Hi, I am " + self.name)
#         else:
#             print("Hi, I am a robot without a name")
#         if self.build_year:
#             print(" I was built in " + str(self.build_year))
#         else:
#             print("It's not known, when I was created!")
#     def set_name(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def set_build_year(self, by):
#         self.build_year = by
#     def get_build_year(self):
#         return self.build_year
#
#
# x = Robot('Ousmane', 2000)
#
# x.say_hi()
# y = Robot()
# y.set_name("Marvin")
# y.say_hi()
# print(y.get_name())




# Public, - Protected-, and Private Attributes
# class A():
#     def __init__(self):
#         self.__priv = " I am private"
#         self._prot = " I am protected"
#         self.pub = "I am public"
#
# x = A()
# x.pub

#=========================2. Class vs. Instance Attributes==============================

# Class Attributes
# class Robot:
#     Three_Laws = (
#         """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
#         """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
#         """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
#     )
#     def __init__(self, name, build_year):
#         self.name = name
#         self.build_year = build_year
# for number, text in enumerate(Robot.Three_Laws):
#     print(str(number + 1) + ":\n " + text)
#
#
# class C:
#     counter = 0
#
#     def __init__(self):
#         type(self).counter += 1
#     def __del__(self):
#         type(self).counter -= 1
#
# if __name__ == "__main__":
#     x = C()
#     print("Number of instances: " + str(C.counter))
#     y= C()
#     print("Number of instances: " + str(C.counter))
#     del x
#     print("Number of instances: " + str(C.counter))
#     del y
#     print("Number of instances: " + str(C.counter))
#
# class Robots:
#     __counter = 0
#     def __init__(self):
#         type(self).__counter += 1
#     @classmethod
#     def RobotInstances(cls):
#         return cls, Robots.__counter
#
# if __name__ == "__main__":
#     print(Robots.RobotInstances())
#     x =Robots
#     print(x.RobotInstances())
#     y = Robots
#     print(y.RobotInstances())
#     print(Robots.RobotInstances())
#
#
# class Fraction(object):
#     def __init__(self, n, d):
#         self.numerator, self.denominator = Fraction.reduce(n, d)
#
#     @staticmethod
#     def gcd(a,b):
#         while b != 0:
#             a, b = b, a%b
#         return a
#
#     @classmethod
#     def reduce(cls, n1, n2):
#         g = cls.gcd(n1, n2)
#         return n1 // g, n2 // g
#
#     def __str__(self):
#         return str(self.numerator) + "/" + str(self.denominator)
#
# x = Fraction(8, 24)
# print(x)



#Class Methods vs. Static Methods and Instance Methods

# class Pet:
#     _class_info = "pet animals"
#     @classmethod
#     def about(cls):
#         print("This class is about " + cls._class_info + "!")
#
# class Dog(Pet):
#     _class_info = "man's best friend"
# class Cat(Pet):
#     _class_info = "all kinds of cats"
#
# Pet.about()
# Dog.about()
# Cat.about()


# Another Example of a Classmethod
# class Person:
#     total_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.total_people += 1
#
#     @classmethod
#     def display_total_people(cls):
#         print("Total number of people:" , cls.total_people)
#
# person1 = Person("Ousmane")
# person2 = Person("Twaambo")
# person3 = Person("Nazia")
#
# Person.display_total_people()



#=============================3. Properties vs. Getters and Setters==========================

# Properties
# class P:
#     def __init__(self, x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#     def set_x(self, x):
#         self.__x = x
#
# p1 = P(42)
# p2 = P(4711)
# print(p1.get_x())
# print(p2.get_x())
#
# p1.set_x(47)
# p1.set_x(p1.get_x() + p2.get_x())
# print(p1.get_x())
#
# class P:
#     def __init__(self, x):
#         self.set_x(x)
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
# p1 = P(1001)
# print(p1.get_x())
# p2 = P(15)
# print(p2.get_x())
# p3 = P(-2)
# print(p3.get_x())


# Public instead of Private Attributes
# class OurClass:
#     def __init__(self, a):
#         self.OurAtt = a
#     @property
#     def OurAtt(self):
#         return self.__OurAtt
#     @OurAtt.setter
#     def OurAtt(self, val):
#         if val < 0:
#             self.__OurAtt = 0
#         elif val > 1000:
#             self.__OurAtt = 1000
#         else:
#             self.__OurAtt = val
# x = OurClass(10)
# y = OurClass(2000)
# z = OurClass(-3)
# print(x.OurAtt)
# print(y.OurAtt)
# print(z.OurAtt)


# Generic Getters and Setters
# class Robot:
#     def __init__(self, name, build_year, city):
#         self.name = name
#         self.build_year = build_year
#         self.city = city
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def build_year(self):
#         return self.__build_year
#     @property
#     def city(self):
#         return self.__city
#     @name.setter
#     def name(self, value):
#         self.__name = value
#     @build_year.setter
#     def build_year(self, value):
#         self.__build_year = value
#     @city.setter
#     def city(self, value):
#         self.__city = value
#
# robot = Robot("RoboBot", 2022, "Tech Place")
# print(robot.name)
# print(robot.build_year)
# print(robot.city)


# class Robots:
#     def __init__(self, name, build_year, city):
#         self.name = name
#         self.build_year = build_year
#         self.city = city
#
#     def __getattr__(self, name):
#         return self.__dict__[f"__{name}"]
#
#     def __setattr__(self, name, value):
#         if name == 'name':
#             if value in ['Henry', 'Oscar']:
#                 raise ValueError("Not a decent Robot name")
#         elif value == 'build_year':
#             if int(value) < 2020:
#                 raise ValueError("Build has to be after 2019")
#         self.__dict__[f"__{name}"] = value
#
#
#     robot1 = Robot("Robot1", 2018, "Tech Place")
#     print(robot1.name)
#     print(robot1.build_year)
#     print(robot1.city)
#
#



#==================================4. Creating Immutable Classes In Python===================================
# Ways to Create Immutable Classes

#
# class ImmutableRObot:
#     def __init__(self, name, brandname):
#         self.__name = name
#         self.__brandname = brandname
#     @property
#     def get_name(self):
#         return self.__name
#     @property
#     def get_brandname(self):
#         return self.__brandname
#
# robot = ImmutableRObot("RoboX", brandname="TechBot")
# print(robot.get_name)
# print(robot.get_brandname)
#
#
# try:
#     robot.name = "RoboY"
# except AttributeError as e:
#     print(e)
#
#
# try:
#     robot.brandname = "TechBot"
# except AttributeError as e:
#     print(e)



#==========================================5. Dataclasses In Python=======================

# class Robot_traditional:
#     def __init__(self, model, serial_number, manufacturer):
#         self.model = model
#         self.serial_number = serial_number
#         self.manufacturer = manufacturer
#
#
# from dataclasses import dataclass
# @dataclass
# class Robot:
#     model: str
#     serial_number: str
#     manufacturer: str
#
# x = Robot_traditional("NanoGuardian XR-2000", "234-76", "Cyber Robotics Co.")
# y = Robot("MachinaMaster MM-42", "986-42", "Quantum Automations Inc.")
# print( repr(x) )
# print( repr(y) )


# Immutable Classes
# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class ImmutableRobot:
#     name: str
#     brand_name: str
#
# x1 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
# x2 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
# print(x1.__hash__(), x2.__hash__())
#
#
# class ImmutableRobot_traditional:
#     def __init__(self, name: str, brand_name:str):
#         self._name = name
#         self._brand_name = brand_name
#
#     @property
#     def name(self) -> str:
#         return self._name
#     @property
#     def brand_name(self) -> str:
#         return self._brand_name
#     def __eq__(self, other):
#         if not isinstance(other, ImmutableRobot_traditional):
#             return False
#         return self.name == other.name and self.brand_name == other.brand_name
#
#     def __hash__(self):
#         return hash((self.name, self.brand_name))
#
# x1 = ImmutableRobot_traditional("Marvin", "NanoGuardian XR-2000")
# x2 = ImmutableRobot_traditional("Marvin", "NanoGuardian XR-2000")
#
# print(x1 == x2)
#
#
#
# @dataclass(frozen=True)
# class ImmutableRobot1:
#     name: str
#     brand_name: str
#
#
# robot1 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
# robot2 = ImmutableRobot("R2D2", "QuantumTech Sentinel-7")
# robot3 = ImmutableRobot("Marva", "MachinaMaster MM-42")
#
# robots = {robot1,robot2, robot3}
# print("The robots in the set robots:")
# for robot in robots:
#     print(robot)
#
# activity = {robot1: 'activated', robot2: 'activated', robot3: 'deactivated'}
# print("\nAll the activated robots in the set robots:")
# for robo, mode in activity.items():
#     if mode == 'activated':
#         print(f"{robo}: is {mode}")



#===============================6. Implementing a Custom Property Class=================
# class Our_property:
#     """ emulation of the property class
#            for educational purposes """
#
#     def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#         """Attributes of 'our_decorator'
#                 fget
#                     function to be used for getting
#                     an attribute value
#                 fset
#                     function to be used for setting
#                     an attribute value
#                 fdel
#                     function to be used for deleting
#                     an attribute
#                 doc
#                     the docstring
#                 """
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#         print("\n__init__ called with:)")
#         print(f"fget={fget}, fset={fset}, fdel={fdel}, doc={doc}")
#         if doc is None and fget is not None:
#             print(f"doc set to docstring of {fget.__name__} method")
#             doc = fget.__doc__
#         self.__doc__ = doc
#
#     def __get__(self, obj, objType=None):
#         if obj is None:
#             return self
#         if self.fget is None:
#             raise AttributeError("unreadable attribute")
#         return self.fget(obj)
#
#
#     def __set__(self, obj, value):
#         if self.fset is None:
#             raise AttributeError("can't set attribute")
#         return self.fset(obj, value)
#
#     def __delete__(self, obj):
#         if self.fdel is None:
#             raise AttributeError("can't delete attribute")
#         return self.fdel(obj)
#
#     def getter(self, fget):
#         return type(self)(fget, self.fset, self.fdel, self.__doc__)
#
#     def setter(self, fset):
#         return type(self)(self.fget, fset, self.fdel, self.__doc__)
#
#     def deleter(self, fdel):
#         return type(self)(self.fget, self.fset, fdel, self.__doc__)
#
#
#
#
# class Robot:
#     def __init__(self, city):
#         self.city = city
#
#     @property
#     def city(self):
#         print("The Property 'city' will be returned now:")
#         return self.__city
#
#     @city.setter
#     def city(self, city):
#         print("City will be set now:")
#         self.__city = city
#
#
# print(type(Robot.city))
# print("Instantiating a Root and setting 'city' to 'Berlin'")
# robo = Robot("Berlin")
# print("The value is: ", robo.city)
# print("Our robot moves now to Frankfurt:")
# robo.city = "Frankfurt"
# print("The value is: ", robo.city)
#


#================================7. Magic Methods==============================
# class Length:
#     __metric = {
#         "mm": 0.001,
#         "cm": 0.01,
#         "m": 1,
#         "km": 1000,
#         "in": 0.0254,
#         "ft": 0.3048,
#         "yd": 0.0193,
#         "mi": 1609.344
#     }
#     def __init__(self, value, unit="m"):
#         self.value = value
#         self.unit = unit
#
#     def Converse2Meters(self):
#         return self.value * Length.__metric[self.unit]
#
#     def __add__(self, other):
#         l = self.Converse2Meters() + other.Converse2Meters()
#         return Length(l / Length.__metric[self.unit], self.unit)
#     def __str__(self):
#         return str(self.Converse2Meters())
#     def __repr__(self):
#         return "Length(" + str(self.value) + ", '" + self.unit + "')"
#
#
#
# if __name__ == "__main__":
#     x = Length(4)
#     print(x)
#     y = eval(repr(x))
#     z = Length(4.5, "yd") + Length(1)
#     print(repr(z))
#     print(z)



#Standard Classes as Base Classes

# class Plist(list):
#     def __init__(self, l):
#         list.__init__(self, l)
#     def push(self, item):
#         self.append(item)
#
#
# if __name__ == "__main__":
#     x = Plist([3, 4])
#     x.push(47)
#     print(x)


#=====================================8. Dynamic Data Transformation==========================
# Product Class Example
# class Product:
#     conversion_rates = {'USD': 1, 'EUR': 0.91, 'CHF': 0.90, 'GBP': 0.79}
#
#     def __init__(self, name, price, shipping_cost, currency='USD'):
#         self.name = name
#         self._price = price
#         self._shipping_cost = shipping_cost
#         self.currency = currency
#         self._used_currency = currency
#
#
#     def set_currency(self, new_currency, adapt_data=False):
#         if self.currency != new_currency:
#             self.currency = new_currency
#         if adapt_data:
#             self._price = self.price
#             self._shipping_cost = self.shipping_cost
#             self._used_currency = new_currency
#
#     @property
#     def price(self):
#         return self._convert_currency(self._price)
#
#     @property
#     def shipping_cost(self):
#         return self._convert_currency(self._shipping_cost)
#
#     def _convert_currency(self, amount):
#         factor =  Product.conversion_rates[self.currency] / Product.conversion_rates[self._used_currency]
#         return round(amount * factor, 2)
#
#     def __str__(self):
#         return f"Product: {self.name}, Price: {self.price} {self.currency}, Shipping Cost: {self.shipping_cost} {self.currency}"
#
#
#     def show_saved_data(self):
#         outstr = f"Saved Data: {self.name=}, {self.currency=}, {self._used_currency=} {self._price=}, {self._shipping_cost=}"
#         print(outstr)
#
#
# class Products:
#     def __init__(self):
#         self.products_list = []
#
#
#     def add_product(self, product):
#         self.products_list.append(product)
#
#     def view_products(self, currency="USD", ):
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # product = Product(name='Phone', price=500, shipping_cost=10, currency='USD')
# # print(product)
# # product.show_saved_data()
# # product1 = Product(name='Tablet', price=600, shipping_cost=20, currency='EUR')
# # print(product1)
# # product1.show_saved_data()
# # product.set_currency('GBP')
# # print(product)
# # product.show_saved_data()
# # product.set_currency('EUR', adapt_data=True)
# # print(product)
# # product.show_saved_data()





#=================9. Introduction to Descriptors====================
# class A:
#     ca_A = "class attribute of A"
#     def __init__(self):
#         self.ia_A = "instance attribute of A instance"
#
#
# class B(A):
#     ca_B = "class attribute of B"
#     def __init__(self):
#         super().__init__()
#         self.ia_B = "instance attribute of B"
#
#
# x = B()
# print(x.ia_B)
# print(x.ca_B)
# print(x.ia_A)
# print(x.ca_A)
#
#
# class SimpleDescriptor(object):
#     def __init__(self, initval=None):
#         print("__init__ of SimpleDecorator called with initval: ", initval)
#         self.__set__(self, initval)
#
#     def __get__(self, instance, owner):
#         print(instance, owner)
#         print('Getting (Retrieving) self.val: ', self.val)
#         return self.val
#
#     def __set__(self, instance, value):
#         print('Setting self.val to ', value)
#         self.val = value
#
#     def __getattribute__(self, key):
#         v = type.__getattribute__(self, key)
#         if hasattr(v, '__get__'):
#             return v.__get__(None, self)
#         return v
#
#
# class MyClass(object):
#     x = SimpleDescriptor("Green")
#
# m = MyClass()
# print(m.x)
# m.x = "Yellow"
# print(m.x)
#
# print(m.__dict__)
# print(MyClass.__dict__)
# print(SimpleDescriptor.__dict__)
# m.__getattribute__("x")

#
#
# from weakref import WeakKeyDictionary
# class Voter:
#     required_age = 18 # in Germany
#     def __init__(self):
#         self.age = WeakKeyDictionary()
#     def __get__(self, instance_obj, objtype):
#         return self.age.get(instance_obj)
#     def __set__(self, instance, new_age):
#         if new_age < Voter.required_age:
#             msg = '{name} is not old enough to vote in Germany'
#             raise Exception(msg.format(name=instance.name))
#         self.age[instance] = new_age
#         print('{name} can vote in Germany'.format(
#             name=instance.name))
#     def __delete__(self, instance):
#         del self.age[instance]
# class Person:
#     voter_age = Voter()
#     def __init__(self, name, age):
#         self.name = name
#         self.voter_age = age
# p1 = Person('Ben', 23)
# p2 = Person('Emilia', 22)
# p2.voter_age




#=============================10. Inheritance=====================
# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print("Hi, I am " + self.name)
#
#
# class PhysicianRobot(Robot):
#     pass
#
# x = Robot("Marvin")
# y = PhysicianRobot("James")
#
# y.say_hi()
#
#
#
# print(isinstance(x, Robot), isinstance(y, Robot))
# print(isinstance(x, PhysicianRobot))
# print(isinstance(y, PhysicianRobot))
#
# print(type(y) == Robot, type(y) == PhysicianRobot)


# Overriding
# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("Hi, I am " + self.name)
# class PhysicianRobot(Robot):
#
#     def say_hi(self):
#         print("Everything will be okay! ")
#         print(self.name + " takes care of you!")
#
# y = PhysicianRobot("James")
# y.say_hi()


# import random
#
# class Robot:
#     def __init__(self, name):
#         self.name = name
#         self.health_level = random.random()
#
#     def say_hi(self):
#         print("Hi, I am " + self.name)
#
#     def need_a_doctor(self):
#         if self.health_level < 0.5:
#             return True
#         else:
#             return False
#
# class PhysicianRobot(Robot):
#     def say_hi(self):
#         print("Everything will be okay! ")
#         print(self.name + " takes care of you!")
#
#     def heal(self, robo):
#         robo.health_level = random.uniform(robo.health_level, 1)
#         print(robo.name + " has been healed by " + self.name)
#
# doc = PhysicianRobot("Dr. Frankenstein")
#
# rob_list = []
#
# for i in range(10):
#     x = Robot("Marvin " + str(i))
#     if x.need_a_doctor():
#         print("health_level of " + x.name + " before healing: ", x.health_level)
#         doc.heal(x)
#         print("health_level of " + x.name + " after healing: ", x.health_level)
#     rob_list.append((x.name, x.health_level))
# print(rob_list)




#==============================11. Multiple Inheritance=================================
# Example: CalendarClock
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.set_Clock(hours, minutes, seconds)
#
#     def set_Clock(self, hours, minutes, seconds):
#         if type(hours) == int and 0 <= hours and hours < 24:
#             self.__hours = hours
#         else:
#             raise TypeError("Hours must be an integer between 0 and 24")
#
#         if type(minutes) == int and 0 <= minutes and minutes < 60:
#             self.__minutes = minutes
#         else:
#             raise TypeError("Minutes must be an integer between 0 and 60")
#
#         if type(seconds) == int and 0 <= seconds and seconds < 60:
#             self.__seconds = seconds
#         else:
#             raise TypeError("Seconds must be an integer between 0 and 60")
#
#     def __str__(self):
#         return "{0:02d}:{1:02d}:{2:02d}".format(self.__hours, self.__minutes, self.__seconds)
#
#     def tick(self):
#         if self.__seconds == 59:
#             self.__seconds = 0
#             if self.__minutes == 59:
#                 self.__minutes = 0
#                 if self.__hours == 23:
#                     self.__hours = 0
#                 else:
#                     self.__hours += 1
#             else:
#                 self.__minutes += 1
#         else:
#             self.__seconds += 1
#
#
#
# x = Clock(23,59,59)
# print(x)
# x.tick()
# print(x)
# y = str(x)
# print(type(y))
#
# class Calendar(object):
#     months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     date_style = "British"
#
#     @staticmethod
#     def leap_year(year):
#         if not year % 4 == 0:
#             return False
#         elif not year % 100 == 0:
#             return True
#         elif not year % 400 == 0:
#             return False
#         else:
#             return True
#
#     def __init(self, d, m, y):
#         if type(d) == int and type(m) == int and type(y) == int:
#             self.__days = d
#             self.__months = m
#             self.__years = y
#         else:
#             raise TypeError("d, m, y must be an integer")
#
#     def __str__(self):
#         if Calendar.date_style == "British":
#             return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
#                                                    self.__months,
#                                                    self.__years)
#         else:
#             return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
#                                                    self.__days,
#                                                    self.__years)
#
#     def advanced(self):
#         max_days = Calendar.months[self.__months]
#         if self.__months == 2 and Calendar.leap_year(self.__years):
#             max_days += 1
#         if self.__days == max_days:
#             self.__days = 1
#             if self.__months == 12:
#                 self.__months = 1
#                 self.__years += 1
#             else:
#                 self.__months += 1
#         else:
#             self.__days += 1
#
#
#
#
# x = Calendar(31,12,2012)
# print(x, end=" ")
# x.advance()
# print("after applying advance: ", x)
# print("2012 was a leapyear:")
# x = Calendar(28,2,2012)
# print(x, end=" ")
# x.advance()
# print("after applying advance: ", x)
# x = Calendar(28,2,2013)
# print(x, end=" ")
# x.advance()
# print("after applying advance: ", x)
# print("1900 no leapyear: number divisible by 100 but not by 400: ")
# x = Calendar(28,2,1900)
# print(x, end=" ")
# x.advance()
# print("after applying advance: ", x)
# print("2000 was a leapyear, because number divisibe by 400: ")
# x = Calendar(28,2,2000)
# print(x, end=" ")
# x.advance()
# print("after applying advance: ", x)
# print("Switching to American date style: ")
# Calendar.date_style = "American"
# print("after applying advance: ", x)

#
# class A:
#     def m(self):
#         print("m of A called")
#
#
# class A:
#     def m(self):
#         print("m of A called")
#
#
# class B(A):
#     def m(self):
#         print("m of B called")
#
#
# class C(A):
#     def m(self):
#         print("m of C called")
#
#
# class D(B, C):
#     def m(self):
#         print("m of D called")
#         B.m(self)
#         C.m(self)
#         A.m(self)
#
# x = D()
# x.m()

# class A:
#     def m(self):
#         print("m of A called")
#
#
# class B(A):
#     def m(self):
#         print("m of B called")
#         super().m()
#
#
# class C(A):
#     def m(self):
#         print("m of C called")
#         super().m()
#
#
# class D(B, C):
#     def m(self):
#         print("m of D called")
#         super().m()
#
#
# x = D()
# x.m()
#
#
# class A:
#     def __init__(self):
#         print("A.__init__")
#
#
# class B(A):
#     def __init__(self):
#         print("B.__init__")
#         super().__init__()
#
#
# class C(A):
#     def __init__(self):
#         print("C.__init__")
#         super().__init__()
#
#
# class D(B, C):
#     def __init__(self):
#         print("D.__init__")
#         super().__init__()
#
#
# d = D()
#
#
# # Polymorphism
#
# def f(x, y):
#     print("values: ", x, y)
#
# f(42, 43)
# f(42, 43.7)
# f(42.3, 43)
# f(42.0, 43.9)


#====================12. Multiple Inheritance: Example===========================
# import random
#
# class Robot():
#     __illegal_name = {"Henry", "Oscar"}
#     __crucial_health_level = 0.6
#     def __init__(self, name):
#         self.name = name
#         self.health_level = random.random()
#
#     @property
#     def name(self):
#         return self.__name
#
#
#     @name.setter
#     def name(self, name):
#         if name in self.__illegal_name:
#             self.__name = "Marvin"
#         else:
#             self.__name = name
#
#     def __str__(self):
#         return self.name + " , Robot"
#
#     def __add__(self, other):
#         first = self.name.split("-")[0]
#         second = other.name.split("-")[0]
#         return type(self)(first + "-" + second)
#
#     def need_a_nurse(self):
#         if self.health_level < Robot.__crucial_health_level:
#             return True
#         else:
#             return False
#
#     def say_hi(self):
#         print("Hi, I am " + self.name)
#         print("My health level is: " + str(self.health_level))
#
#
#
# first_generation = (Robot("Marvin"),
#                     Robot("Anchita"),
#                     Robot("Twaambo"))
# gen1 = first_generation
# babies = [gen1[0] + gen1[1], gen1[1] + gen1[2]]
# babies.append(babies[0] + babies[1])
# for baby in babies:
#     baby.say_hi()
#
#
#
# class NursingRObot(Robot):
#     def __init__(self, name="Hubert", healing_power=None):
#         super().__init__(name)
#         if healing_power is None:
#             self.healing_power = random.uniform(0.8, 1)
#         else:
#             self.healing_power = healing_power
#     def say_hi(self):
#         print("Well, well, everything will be fine ... " + self.name + " takes care of you!")
#
#     def say_hi_doc(self):
#         Robot.say_hi(self)
#
#     def heal(self, robo):
#         if robo.health_level > self.healing_power:
#             print(self.name + " not strong enough to heal " + robo.name)
#         else:
#             robo.health_level = random.uniform(robo.health_level, self.healing_power)
#             print(robo.name + " has been healed by " + self.name + "!")
#
#
#
# from itertools import chain
#
# nurses = [NursingRObot("Hubert"),
#           NursingRObot("Anchita", healing_power=1)]
#
# for nurse in nurses:
#     print("Healing power of " + nurse.name,
#           nurse.healing_power)
#
# print("\nLet's start the healing")
# for robo in chain(first_generation, babies):
#     robo.say_hi()
#     if robo.need_a_nurse():
#         nurse = random.choice(nurses)
#         nurse.heal(robo)
#         print("New health level: ", robo.health_level)
#     else:
#         print(robo.name + " is healthy enough!")
#         print()
#
#
#
# x = nurses[0] + nurses[1]
# x.say_hi()
# print(type(x))
#

#=============================13. Callable Instances of Classes================================
class FoodSupply:

    def __init__(self, *ingredients):
        self.incredients = ingredients


    def __call__(self):
        result = " ".join(self.incredients) + " plus delicious spam!"
        return result


f = FoodSupply("fish", "rice")
print(f())
g = FoodSupply("vegetables")
print(g())



#============================14. Slots: Avoiding Dynamically Created Attributes===================
class S(object):
    __slots__ = ['val']
    def __init__(self,v):
        self.val = v

x = S(42)
print(x.val)


#==========================15. Polynomial Class===========================================
class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return "Polynomial" + str(tuple(self.coefficients))

    def __str__(self):
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^" + str(degree)
            return res
        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            if abs(coeff) == 1 and i < degree:
                res += f"{'+' if coeff > 0 else '-'}{x_expr(degree - i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree - i)}"
        return res.lstrip('+')


polys = [Polynomial(1, 0, -4, 3, 0),
         Polynomial(2, 0),
         Polynomial(4, 1, -1),
         Polynomial(3, 0, -5, 2, 7),
         Polynomial(-42)]
for count, poly in enumerate(polys):
    print(f"$p_{count} = {str(poly)}$")
