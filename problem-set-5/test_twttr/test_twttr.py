"""
This module contains a set of tests for the `shorten` function in the `twttr` module.

The `shorten` function is tested to ensure that it correctly removes specified characters
from input strings. The tests cover scenarios involving vowels, capitalized vowels, symbols,
spaces, and numbers.
"""

from twttr import shorten


def test_vowels_replaced():
    """
    Test that the `shorten` function replaces vowels in a string with the characters specified.
    """
    assert shorten("hello") == "hll"


def test_capitalized_vowels_handled():
    """
    Test that the `shorten` function correctly handles capitalized vowels.
    """
    assert shorten("HELLO") == "HLL"


def test_symbols_ignored():
    """
    Test that the `shorten` function correctly handles symbols in the input string.
    """
    assert shorten("HELLO!") == "HLL!"


def test_spaces_ignored():
    """
    Test that the `shorten` function correctly handles spaces in the input string.
    """
    assert shorten("HEL LO") == "HL L"


def test_numbers_omitted():
    """
    Test that the `shorten` function omits numbers from the input string.
    """
    assert shorten("Hello3") == "Hll3"
