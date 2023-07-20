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

    def __init__(self, players=("Player 1", "Player 2")):
        self.deck = Deck(num_of_players=len(players))
        self.discard_pile = []
        self.dead_players = []
        self.players = []
        for pl in players:
            self.players.append(Player(pl))
            self.players[-1].deal_hand(
                [self.deck.cards.pop(0) for _ in range(5)] + [Defuse()]
            )
            self.players[-1].hand.sort(key=lambda x: x.id)
        self.deck.add_defuse_and_exploding_to_deck()

    def update_discard_pile(self, played_card):
        """
        Add the played card to the discard pile.
        """
        if played_card is not None:
            self.discard_pile += [played_card]

    def execute_all_turns_for_a_player(self):
        """
        For the current player:

            while the player is still required to draw:
                while the player wants to play a card:
                    - Choose what card to play
                    - If a card is chosen
                        - Update the discard pile
                        - Perform the card's action
                    - Otherwise, set the stopping criteria to True
                - The player draws a card to end their turn
                - Check if the player exploded and resolve it
        """
        self.next_player_cards_to_draw = 1
        while self.cards_to_draw != 0:
            end_turn = False

            while not end_turn:
                played_card = self.current_player.choose_card_to_play()
                if played_card is not None:
                    print(f"Player {self.current_player} plays {played_card}")
                    self.update_discard_pile(played_card)
                    played_card.action(self)  # Pass the game class into the Cards class
                    if self.cards_to_draw == 0:
                        break
                else:
                    end_turn = True

            # TODO: Nope implementation here as well?
            if self.cards_to_draw == 0:
                break

            drawn_card = self.current_player.draw_to_end_turn(self)

            # A.K.A. "The Narrator" muahahahahaha
            print(f"Player {self.current_player} draws {drawn_card}")
            if drawn_card.id == 0:
                exploded = self.current_player.explode()
                if exploded:
                    self.dead_players.append(self.current_player)
                    self.players.pop(self.current_player.id)
                    self.update_discard_pile(drawn_card)
                    input(f"Bye bye player {self.current_player}")
                    self.cards_to_draw = 1

            self.cards_to_draw -= 1

    def play_game(self):
        end_of_game = False
        self.turn_count = 0
        self.cards_to_draw = 1
        while not end_of_game:
            # TODO: Solve the problem where a player explodes and SOMETIMES
            #       the next player's turn is skipped. This happens because
            #       when modulo changes from 3 to 2 the outcome changes as well
            player_id = self.turn_count % len(self.players)
            self.current_player = self.players[player_id]
            self.current_player.id = player_id

            self.execute_all_turns_for_a_player()
            self.cards_to_draw = self.next_player_cards_to_draw

            if len(self.players) == 1:
                end_of_game = True

            self.turn_count += 1
