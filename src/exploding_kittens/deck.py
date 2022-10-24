"""Module for the Deck class"""

import random

from .constants import (
    NUM_OF_DEFUSE_CARDS_IN_BASE_GAME,
    NUM_OF_ATTACK_CARDS_IN_BASE_GAME,
    NUM_OF_SHUFFLE_CARDS_IN_BASE_GAME,
    NUM_OF_SEE_FUTURE_CARDS_IN_BASE_GAME,
    NUM_OF_NOPE_CARDS_IN_BASE_GAME,
    NUM_OF_SKIP_CARDS_IN_BASE_GAME,
    NUM_OF_FAVOR_CARDS_IN_BASE_GAME,
    NUM_OF_TACOCAT_CARDS_IN_BASE_GAME,
    NUM_OF_CATERMELON_CARDS_IN_BASE_GAME,
    NUM_OF_HAIRY_POTATO_CAT_CARDS_IN_BASE_GAME,
    NUM_OF_BEARD_CAT_CARDS_IN_BASE_GAME,
    NUM_OF_RAINBOW_RALPHING_CAT_CARDS_IN_BASE_GAME,
)
from .cards import (
    ExplodingKitten,
    Defuse,
    Catermelon,
    HairyPotatoCat,
    RainbowCat,
    BeardCat,
    Tacocat,
    Favor,
    Skip,
    Attack,
    SeeTheFuture,
    Nope,
    Shuffle,
)


class Deck:
    """
    Class containing all methods needed to utilise a deck of cards.
    """

    def __init__(
        self, num_of_players=2, expansion_1=False, expansion_2=False, expansion_3=False
    ):
        self.num_of_players = num_of_players
        self.expansion_1 = expansion_1
        self.expansion_2 = expansion_2
        self.expansion_3 = expansion_3
        self.initialise_deck()

    def initialise_deck(self):
        """
        Initialises the deck based on the card set specified apart from
        Defuse cards and Exploding Kittens
        """
        self.cards = []
        self.cards += (
            NUM_OF_ATTACK_CARDS_IN_BASE_GAME * [Attack()]
            + NUM_OF_SHUFFLE_CARDS_IN_BASE_GAME * [Shuffle()]
            + NUM_OF_SEE_FUTURE_CARDS_IN_BASE_GAME * [SeeTheFuture()]
            + NUM_OF_NOPE_CARDS_IN_BASE_GAME * [Nope()]
            + NUM_OF_SKIP_CARDS_IN_BASE_GAME * [Skip()]
            + NUM_OF_FAVOR_CARDS_IN_BASE_GAME * [Favor()]
            + NUM_OF_TACOCAT_CARDS_IN_BASE_GAME * [Tacocat()]
            + NUM_OF_CATERMELON_CARDS_IN_BASE_GAME * [Catermelon()]
            + NUM_OF_HAIRY_POTATO_CAT_CARDS_IN_BASE_GAME * [HairyPotatoCat()]
            + NUM_OF_BEARD_CAT_CARDS_IN_BASE_GAME * [BeardCat()]
            + NUM_OF_RAINBOW_RALPHING_CAT_CARDS_IN_BASE_GAME * [RainbowCat()]
        )
        self.shuffle_deck()

    def add_defuse_and_exploding_to_deck(self):
        """
        Adds the Defuse cards and Exploding Kittens cards in the deck after giving
        each player their hand
        """
        self.cards += (NUM_OF_DEFUSE_CARDS_IN_BASE_GAME - self.num_of_players) * [
            Defuse()
        ] + (self.num_of_players - 1) * [ExplodingKitten()]
        self.shuffle_deck()

    def shuffle_deck(self):
        """
        Shuffles the deck
        """
        random.shuffle(self.cards)
