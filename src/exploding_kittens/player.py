"""Module for the player class"""


class Player:
    def __init__(self, name=None):
        self.name = name

    def deal_hand(self, hand):
        self.hand = hand

    def player_turn(self):
        pass
