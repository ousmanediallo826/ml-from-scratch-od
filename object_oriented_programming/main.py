# def hi(obj):
#     print("Hi, I am " + obj.name + "!")
#
# class Robot:
#     pass
# x = Robot()
# x.name = "Marvin"
# hi(x)


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
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    @property

