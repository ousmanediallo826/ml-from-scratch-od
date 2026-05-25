class PositivePrice:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name


    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value < 0 and type(value) is not int and type(value) is not float:
            raise TypeError(
                "price must be greater than 0"
            )
        setattr(obj, self.private_name, value)


class ShareCount:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if type(value) is not int and value < 0:
            raise TypeError(
                "price must be greater than 0 and a positive integer"
            )

        setattr(obj, self.private_name, value)