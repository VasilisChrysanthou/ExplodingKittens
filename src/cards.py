
class Cards:
    """
    This is the generic class for all Cards, which all other cards will inherit from.
    """
    def __init__(self):
        self.discarded = False
        self.getid()
    
    def getid(self):
        pass

class ExplodingKitten(Cards):
    def getid(self):
        self.id = 0

    def __repr__(self):
        return "Exploding Kitten"

class Defuse(Cards):
    def getid(self):
        self.id = 1

    def __repr__(self):
        return "Defuse"

class Catermelon(Cards):
    def getid(self):
        self.id = 2

    def __repr__(self):
        return "Catermelon"

class HairyPotatoCat(Cards):
    def getid(self):
        self.id = 3

    def __repr__(self):
        return "Hairy Potato Cat"
    
class RainbowCat(Cards):
    def getid(self):
        self.id = 4
    
    def __repr__(self):
        return "Rainbow Cat"

class BeardCat(Cards):
    def getid(self):
        self.id = 5

    def __repr__(self):
        return "Beard Cat"

class Tacocat(Cards):    
    def getid(self):
        self.flavortext = "I'm a Palindrome"
        self.id = 6
    
    def __repr__(self):
        return "Tacocat"

class Favor(Cards):
    def getid(self):
        self.id = 7

    def __repr__(self):
        return "Favor"

class Skip(Cards):
    def getid(self):
        self.id = 8

    def __repr__(self):
        return "Skip"

class Attack(Cards):
    def getid(self):
        self.id = 9

    def __repr__(self):
        return "Attack"

class SeeTheFuture(Cards):
    def getid(self):
        self.id = 10

    def __repr__(self):
        return "See The Future"

class Nope(Cards):
    def getid(self):
        self.id = 11

    def __repr__(self):
        return "Nope"

class Shuffle(Cards):
    def getid(self):
        self.id = 12

    def __repr__(self):
        return "Shuffle"