""" Module for the main game """

from .deck import Deck, Defuse
from .player import Player


class Game:
    """
    Class for the main functionality of the game. Upon initialisation,
    the deck is created and each player is dealt a hand of 5 cards
    plus one Defuse card. Then the remaining Defuse cards and the
    Exploding Kittens are shuffled into the deck.
    """

    def __init__(self, players=["Player 1", "Player 2"]):
        self.deck = Deck(num_of_players=len(players))
        self.players = []
        for pl in players:
            self.players.append(Player(pl))
            self.players[-1].deal_hand(
                [self.deck.cards.pop(0) for _ in range(5)] + [Defuse()]
            )
            self.players[-1].hand.sort(key=lambda x: x.id)
        self.deck.add_defuse_and_exploding_to_deck()

