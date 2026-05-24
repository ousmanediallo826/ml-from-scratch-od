

class Account:
    def __init__(self, balance) :
        self._balance = balance

    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

Acc = Account(100)
print(Acc.balance)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return 3.14159 * self._radius ** 2


c = Circle(10)
print(c.radius)
