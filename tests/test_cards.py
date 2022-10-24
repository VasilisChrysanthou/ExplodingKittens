"""
Module for testing the Cards class.
"""

from exploding_kittens import (
    Cards,
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


def test_cards_class():
    """
    Tests the Cards class.
    """

    testcard = Cards()
    assert testcard.discarded is False
    assert testcard.getid() is None


def test_explodingkitten():
    """
    Tests the Exploding Kitten class.
    """

    testcard = ExplodingKitten()
    assert testcard.discarded is False
    assert testcard.id == 0
    assert type(testcard) == ExplodingKitten
    assert str(testcard) == "Exploding Kitten"


def test_defuse():
    """
    Tests the Defuse Card class.
    """

    testcard = Defuse()
    assert testcard.discarded is False
    assert testcard.id == 1
    assert type(testcard) == Defuse
    assert str(testcard) == "Defuse"


def test_catermelon():
    """
    Tests the Catermelon Card class.
    """
    testcard = Catermelon()
    assert testcard.discarded is False
    assert testcard.id == 2
    assert type(testcard) == Catermelon
    assert str(testcard) == "Catermelon"


def test_hairypotatocat():
    """
    Tests the Hairy Potato Cat Card class.
    """
    testcard = HairyPotatoCat()
    assert testcard.discarded is False
    assert testcard.id == 3
    assert type(testcard) == HairyPotatoCat
    assert str(testcard) == "Hairy Potato Cat"


def test_rainbowcat():
    """
    Tests the Rainbow Cat Card class.
    """
    testcard = RainbowCat()
    assert testcard.discarded is False
    assert testcard.id == 4
    assert type(testcard) == RainbowCat
    assert str(testcard) == "Rainbow Cat"


def test_beardcat():
    """
    Tests the Beard Cat Card class.
    """
    testcard = BeardCat()
    assert testcard.discarded is False
    assert testcard.id == 5
    assert type(testcard) == BeardCat
    assert str(testcard) == "Beard Cat"


def test_tacocat():
    """
    Tests the Tacocat Card class.
    """
    testcard = Tacocat()
    assert testcard.discarded is False
    assert testcard.id == 6
    assert type(testcard) == Tacocat
    assert str(testcard) == "Tacocat"
    assert testcard.flavortext == "I'm a Palindrome"


def test_favor():
    """
    Tests the Favor Card class.
    """
    testcard = Favor()
    assert testcard.discarded is False
    assert testcard.id == 7
    assert type(testcard) == Favor
    assert str(testcard) == "Favor"


def test_skip():
    """
    Tests the Skip Card class.
    """
    testcard = Skip()
    assert testcard.discarded is False
    assert testcard.id == 8
    assert type(testcard) == Skip
    assert str(testcard) == "Skip"


def test_attack():
    """
    Tests the Attack Card class.
    """
    testcard = Attack()
    assert testcard.discarded is False
    assert testcard.id == 9
    assert type(testcard) == Attack
    assert str(testcard) == "Attack"


def test_seethefuture():
    """
    Tests the See The Future Card class.
    """
    testcard = SeeTheFuture()
    assert testcard.discarded is False
    assert testcard.id == 10
    assert type(testcard) == SeeTheFuture
    assert str(testcard) == "See The Future"


def test_nope():
    """
    Tests the Nope Card class.
    """
    testcard = Nope()
    assert testcard.discarded is False
    assert testcard.id == 11
    assert type(testcard) == Nope
    assert str(testcard) == "Nope"


def test_shuffle():
    """
    Tests the Shuffle Card class.
    """
    testcard = Shuffle()
    assert testcard.discarded is False
    assert testcard.id == 12
    assert type(testcard) == Shuffle
    assert str(testcard) == "Shuffle"

