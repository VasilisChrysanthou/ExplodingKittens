"""
Module for testing the player class
"""

from exploding_kittens import Player


def test_player():
    """
    Tests the player class.
    """

    p1 = Player(name="Vasilis")
    p1.deal_hand(hand=12345)
    p1.player_turn()
    assert p1.name == "Vasilis"
    assert p1.hand == 12345
