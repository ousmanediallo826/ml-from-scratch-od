class ValidScores:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name


    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value < 0 or value > 100:
            raise ValueError(
                f"{self.private_name} is not a valid score range. Must be between 0 and 100"
            )
        if type(value) is not int or type(value) is not float:
            raise TypeError(
                f"{self.private_name} is not a valid type for the grade. Must be an int or float"
            )
        return setattr(obj, self.private_name, value)

    def __delete__(self, obj):
        delattr(obj, self.private_name)