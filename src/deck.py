"""Module for the Deck class"""

import random

from constants import *


class Deck:
    def __init__(
        self, num_of_players=2, expansion_1=False, expansion_2=False, expansion_3=False
    ):
        self.num_of_players = num_of_players
        self.expansion_1 = expansion_1
        self.expansion_2 = expansion_2
        self.expansion_3 = expansion_3
        self.initialise_deck()
        self.shuffle_deck()

    def initialise_deck(self):
        """
        Initialises the deck based on the card set specified
        """
        self.deck = []
        self.deck += (
            NUM_OF_DEFUSE_CARDS_IN_BASE_GAME * ["Defuse"]
            + NUM_OF_ATTACK_CARDS_IN_BASE_GAME * ["Attack"]
            + NUM_OF_SHUFFLE_CARDS_IN_BASE_GAME * ["Shuffle"]
            + NUM_OF_SEE_FUTURE_CARDS_IN_BASE_GAME * ["See The Future"]
            + NUM_OF_NOPE_CARDS_IN_BASE_GAME * ["Nope"]
            + NUM_OF_SKIP_CARDS_IN_BASE_GAME * ["Skip"]
            + NUM_OF_FAVOR_CARDS_IN_BASE_GAME * ["Favor"]
            + NUM_OF_TACOCAT_CARDS_IN_BASE_GAME * ["Tacocat"]
            + NUM_OF_CATERMELON_CARDS_IN_BASE_GAME * ["Catermelon"]
            + NUM_OF_HAIRY_POTATO_CAT_CARDS_IN_BASE_GAME * ["Hairy cat"]
            + NUM_OF_BEARD_CAT_CARDS_IN_BASE_GAME * ["Beard cat"]
            + NUM_OF_RAINBOW_RALPHING_CAT_CARDS_IN_BASE_GAME * ["Rainbow cat"]
            + (self.num_of_players - 1) * ["Exploding Kitten"]
        )

    def shuffle_deck(self):
        """
        Shuffles the deck
        """
        random.shuffle(self.deck)
