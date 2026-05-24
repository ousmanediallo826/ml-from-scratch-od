class PositiveNumber:
    def __set_name__(self, owner, name):
        self.public = name
        self.private = "_" + name


    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Negative numbers are not allowed")
        setattr(obj, self.private, value)

    def __delete__(self, obj):
        delattr(obj, self.private)


class Person:
    age = PositiveNumber()
class Product:
    price = PositiveNumber()
    stock = PositiveNumber()


p = Person()
p.age = 12
p.age = 2
print(p.age)



