class Dog:
    species = "Canis lupus"
    def __init__(self, name):
        self.name = name

rex = Dog("REX")
luna = Dog("Luna")
print(rex.species)
print(luna.species)
print(rex.name)
rex.species = "Wolf"
print(rex.species)
print(luna.species)
