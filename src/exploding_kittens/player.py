"""Module for the player class."""


class Player:
    """
    Class for the player object in the game.
    """

    def __init__(self, name=None):
        self.name = name
        self.hand = None

    def deal_hand(self, hand):
        """
        Deals the player a hand of cards.
        """
        self.hand = hand

    def player_turn(self):
        """
        The player's turn.
        """
        pass
