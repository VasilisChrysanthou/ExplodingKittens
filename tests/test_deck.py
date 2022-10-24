"""
Module for testing the deck class.
"""

from exploding_kittens import Deck


def test_deck_init():
    """
    Tests the initialisation of the deck class.
    """

    testdeck = Deck(num_of_players=2)

    assert testdeck.num_of_players == 2
    assert testdeck.expansion_1 == False
    assert testdeck.expansion_2 == False
    assert testdeck.expansion_3 == False
    assert type(testdeck.deck) == list
    assert len(testdeck.deck) == 46


def test_shuffle():
    """
    Tests the shuffle deck method of the class.
    """
    testdeck = Deck(num_of_players=2)
    deck1 = testdeck.deck.copy()
    testdeck.shuffle_deck()
    deck2 = testdeck.deck
    assert deck1 != deck2


def test_add_defuse_and_exploding_to_deck():
    """
    Tests the addition of defuse and exploding kitten cards
    method of the deck class.
    """
    testdeck = Deck(num_of_players=2)
    testlength1 = len(testdeck.deck)
    testdeck.add_defuse_and_exploding_to_deck()
    testlength2 = len(testdeck.deck)
    assert testlength1 == 46
    assert testlength2 == 51
    assert testlength1 != testlength2
