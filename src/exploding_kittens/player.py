"""Module for the player class."""

import random


class Player:
    """
    Class for the player object in the game.
    """

    # TODO: Possible idea is to include a strategy argument
    # where `strategy = interactive, random, logic_1, logic_2`
    def __init__(self, name=None):
        self.name = name
        self.id = None
        self.hand = None
        self.active = True

    def deal_hand(self, hand):
        """
        Deals the player a hand of cards.
        """
        self.hand = hand

    def choose_card_to_play(self):
        """
        The player's turn.
        """
        # TODO: Add check to ensure valid card_id is selected

        #### Pezontas me ton Mixa ####
        if self.name == "Mixas":
            card_id = input([self.name, self.hand])        
            if card_id == "":
                return None
            return self.hand.pop(int(card_id))

        #### Pezontas random
        if random.random() < 0.3:
            return self.hand.pop(random.randint(0, len(self.hand) - 1))
        return None

    def draw_to_end_turn(self, game):
        """
        Draw a card and end player's turn.
        """
        drawn_card = game.deck.cards.pop(0)
        if drawn_card.id != 0:
            self.hand += [drawn_card]
        return drawn_card

    def explode(self):
        # TODO: Implement explosion
        return True

    def __repr__(self):
        return f"{self.name}"
