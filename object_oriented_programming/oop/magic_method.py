class Money:
    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Money({self.amount}, {self.currency})"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Can't add money with different currency")

        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        return self.amount < other.amount

    def __len__(self):
        return len(self.amount)

    def __bool__(self):
        return self.amount > 0

    def __contains__(self, item):
        return item == self.currency



a = Money(50)
b = Money(100)
print(a + b)
print(a > b)
print(bool(a))
print("USD" in a)
print(sorted([a,b]))