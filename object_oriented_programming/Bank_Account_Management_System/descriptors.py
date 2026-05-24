"""
Topic 9 — Introduction to Descriptors
--------------------------------------
A descriptor is any object that defines __get__, __set__, or __delete__.
When assigned as a *class attribute*, Python routes all attribute access
through those special methods instead of the normal instance __dict__ lookup.
"""


class PositiveNumber:
    """Ensures an attribute is always a number >= 0."""

    def __set_name__(self, owner, name):
        self.public_name  = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{self.public_name!r} must be a number, got {type(value).__name__!r}"
            )
        if value < 0:
            raise ValueError(
                f"{self.public_name!r} cannot be negative (got {value})"
            )
        setattr(obj, self.private_name, round(float(value), 2))

    def __delete__(self, obj):
        raise AttributeError(
            f"Cannot delete {self.public_name!r} — reset it to 0 instead."
        )


class BoundedRate:
    """Ensures a rate stays strictly inside (0, 1]. Useful for interest rates."""

    def __set_name__(self, owner, name):
        self.public_name  = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, 0.0)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{self.public_name!r} must be a float, got {type(value).__name__!r}"
            )
        if not (0 < value <= 1):
            raise ValueError(
                f"{self.public_name!r} must be between 0 (exclusive) and 1 (inclusive), got {value}"
            )
        setattr(obj, self.private_name, float(value))

    def __delete__(self, obj):
        raise AttributeError(f"Cannot delete {self.public_name!r}.")