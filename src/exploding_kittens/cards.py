"""Module that consists of all card classes"""


class Cards:
    """
    This is the generic class for all Cards, which all other cards will inherit from.
    """

    def __init__(self):
        self.discarded = False
        self.getid()

    def getid(self):
        """
        Gets the id of the card.
        """
        self.id = None


class ExplodingKitten(Cards):
    """
    This is the class for the Exploding Kitten card.
    """

    def getid(self):
        self.id = 0

    def __repr__(self):
        return "Exploding Kitten"


class Defuse(Cards):
    """
    Defuse card class.
    """

    def getid(self):
        self.id = 1

    def __repr__(self):
        return "Defuse"


class Catermelon(Cards):
    """
    Catermelon card class.
    """

    def getid(self):
        self.id = 2

    def __repr__(self):
        return "Catermelon"


class HairyPotatoCat(Cards):
    """
    Hairy potato cat card class.
    """

    def getid(self):
        self.id = 3

    def __repr__(self):
        return "Hairy Potato Cat"


class RainbowCat(Cards):
    """
    Rainbow cat card class.
    """

    def getid(self):
        self.id = 4

    def __repr__(self):
        return "Rainbow Cat"


class BeardCat(Cards):
    """
    Beard cat card class.
    """

    def getid(self):
        self.id = 5

    def __repr__(self):
        return "Beard Cat"


class Tacocat(Cards):
    """
    Tacocat card class.
    """

    def getid(self):
        self.flavortext = "I'm a Palindrome"
        self.id = 6

    def __repr__(self):
        return "Tacocat"


class Favor(Cards):
    """
    Favor card class.
    """

    def getid(self):
        self.id = 7

    def __repr__(self):
        return "Favor"


class Skip(Cards):
    """
    Skip card class.
    """

    def getid(self):
        self.id = 8

    def __repr__(self):
        return "Skip"


class Attack(Cards):
    """
    Attack card class.
    """

    def getid(self):
        self.id = 9

    def __repr__(self):
        return "Attack"


class SeeTheFuture(Cards):
    """
    See the future card class.
    """

    def getid(self):
        self.id = 10

    def __repr__(self):
        return "See The Future"


class Nope(Cards):
    """
    Nope card class.
    """

    def getid(self):
        self.id = 11

    def __repr__(self):
        return "Nope"


class Shuffle(Cards):
    """
    Shuffle card class.
    """

    def getid(self):
        self.id = 12

    def __repr__(self):
        return "Shuffle"
