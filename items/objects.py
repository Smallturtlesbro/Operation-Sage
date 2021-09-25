
class Weapon:
    def __str__(self):
        return self.name


class Consumable:
    def __str__(self):
        return self.name


class Furniture:
    def __str__(self):
        return self.name

#Weapon
class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust."
        self.damage = 10


class Iron_bar(Weapon):
    def __init__(self):
        self.name = "Iron bar"
        self.description = "A one foot iron bar, Suitable for bludgeoning."
        self.damage = 5


class Sword:
    def __init__(self):
        self.name = "Sword"
        self.description = "A short sword."
        self.damage = 12


class Rock:
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, could be used for bludgeoning"
        self.damage = 5


class Unarmed:
    def __init__(self):
        self.name = "Unarmed"
        self.description = "Just some trusty ol fists"
        self.damage = 3


#Furniture
class Bucket(Furniture):
    def __init__(self):
        self.name = "Bucket"
        self.description = "A small wooden bucket; your only source of relief."


#Consumable
class Bread(Consumable):
    def __init__(self):
        self.name = "Bread"
        self.description = "A stale piece of bread."


