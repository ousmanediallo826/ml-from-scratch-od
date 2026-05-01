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
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableRobot:
    name: str
    brand_name: str

x1 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
x2 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
print(x1.__hash__(), x2.__hash__())


class ImmutableRobot_traditional:
    def __init__(self, name: str, brand_name:str):
        self._name = name
        self._brand_name = brand_name

    @property
    def name(self) -> str:
        return self._name
    @property
    def brand_name(self) -> str:
        return self._brand_name
    def __eq__(self, other):
        if not isinstance(other, ImmutableRobot_traditional):
            return False
        return self.name == other.name and self.brand_name == other.brand_name

    def __hash__(self):
        return hash((self.name, self.brand_name))

x1 = ImmutableRobot_traditional("Marvin", "NanoGuardian XR-2000")
x2 = ImmutableRobot_traditional("Marvin", "NanoGuardian XR-2000")

print(x1 == x2)



@dataclass(frozen=True)
class ImmutableRobot1:
    name: str
    brand_name: str


robot1 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
robot2 = ImmutableRobot("R2D2", "QuantumTech Sentinel-7")
robot3 = ImmutableRobot("Marva", "MachinaMaster MM-42")

robots = {robot1,robot2, robot3}
print("The robots in the set robots:")
for robot in robots:
    print(robot)

activity = {robot1: 'activated', robot2: 'activated', robot3: 'deactivated'}
print("\nAll the activated robots in the set robots:")
for robo, mode in activity.items():
    if mode == 'activated':
        print(f"{robo}: is {mode}")

