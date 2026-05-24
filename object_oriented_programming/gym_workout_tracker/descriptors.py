

class PositiveInt:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name


    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(
                "'reps' must be a positive integer"
            )
        setattr(obj, self.private_name, value)


class WeightValue:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if type(value) != int or type(value) != float and value >= 0:
            raise ValueError(
                "Weight value must be a positive integer or float"
            )
        setattr(obj, self.private_name, value)
