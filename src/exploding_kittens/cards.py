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

    def action(self, game):
        pass


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

    def action(self, game):
        """
        The Skip card end the players current turn and
        reduces the amount of cards required to be drawn
        for the player by 1.
        """
        game.cards_to_draw -= 1


class Attack(Cards):
    """
    Attack card class.
    """

    def getid(self):
        self.id = 9

    def __repr__(self):
        return "Attack"

    def action(self,game):
        """
        The attack card ends all remaining turns of the player and
        makes the next player play twice. In the event when a player
        plays an attack and have more than one turns remaining then
        it adds two more turns to the next player.
        """
        if game.cards_to_draw == 1:
            game.next_player_cards_to_draw = 2
        else:
            game.next_player_cards_to_draw = game.cards_to_draw + 2
        game.cards_to_draw = 0

class SeeTheFuture(Cards):
    """
    See the future card class.
    """

    def getid(self):
        self.id = 10

    def __repr__(self):
        return "See The Future"

    def action(self, game):
        """
        This card allows the player to see the top 3 cards
        of the drawing pile.
        """
        ### TODO: depending on strategy the below print function
        # should have different functionality.
        # e.g. when another player in the games plays this,
        # you should not be able to see what the top 3 cards are.
        print(game.deck.cards[0:3])

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

    def action(self, game):
        game.deck.shuffle_deck()