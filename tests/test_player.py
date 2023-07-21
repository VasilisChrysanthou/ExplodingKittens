"""
Module for testing the player class
"""
import random
from exploding_kittens import Player, Game, Cards


def test_player():
    """
    Tests the player class.
    """

    p1 = Player(name="Vasilis")
    p1.deal_hand(hand=12345)
    assert p1.name == "Vasilis"
    assert p1.hand == 12345
    assert p1.active == True

def test_choose_card_to_play():
    p1 = Player(name="Mixas")
    p1.deal_hand(hand=["Cat","Taco","Rainbow"])
    assert p1.name == "Mixas"
    #TODO: finish later

def test_choose_card_to_play_random():
    pass
    #TODO later

# too complicating, might not be needed.
# def test_draw_to_end_turn_generic():
#    game = Game()
#    test_player = game.players[0]
#    test_card_drawn = test_player.draw_to_end_turn(game)
#    assert test_card_drawn == Cards

def test_draw_to_end_turn_specific():
    random.seed(0)
    game = Game()
    test_player = game.players[0]
    assert game.players[0].draw_to_end_turn(game)
