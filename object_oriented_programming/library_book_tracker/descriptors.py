class StartingRating:

    def __set_name__(self, owner, name):
        self.public = name
        self.private = "_" + name


    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if value < 1 and value > 5:
            raise ValueError("Value must be between 1 and 5")
        setattr(obj, self.private, value)

    def __delete__(self, obj):
        delattr(obj, self.private)



