"""
Module for testing the Game class.
"""

from exploding_kittens import Game


def test_game_init_default():
    """
    Tests the initialisation of the game class.
    """
    testgame = Game()
    assert len(testgame.players) == 2
    assert testgame.players[0].name == "Player 1"
    assert testgame.players[1].name == "Player 2"
    assert len(testgame.players[0].hand) == 6
    assert len(testgame.players[1].hand) == 6
    assert len(testgame.deck.cards) == 41


def test_game_init_three_players():
    """
    Tests the initialisation of the game class with three players.
    """
    testgame = Game(["Vasos", "Mixas", "Kostas"])
    assert len(testgame.players) == 3
    assert testgame.players[0].name == "Vasos"
    assert testgame.players[1].name == "Mixas"
    assert testgame.players[2].name == "Kostas"
    assert len(testgame.players[0].hand) == 6
    assert len(testgame.players[1].hand) == 6
    assert len(testgame.players[2].hand) == 6
    assert len(testgame.deck.cards) == 36
