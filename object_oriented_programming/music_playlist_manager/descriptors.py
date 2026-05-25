

class SongDuration:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name


    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value < 0 and type(value) != int or type(value) != float:
            raise ValueError(
                "duration must be greater than 0"
            )
        setattr(obj, self.private_name, value)


class PlayCount:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objType=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if type(value) != int and value >= 0:
            raise ValueError(
                "play_count must be a non-negative integer"
            )

        setattr(obj, self.private_name, value)
