from project import get_word, display_word, display_hangman
from words import word_list


def test_get_word():
    assert get_word() in word_list


def test_display_word():
    assert display_word("PYTHON", []) == "______"
    assert display_word("BANANA", ["B", "A", "N"]) == "BANANA"
    assert display_word("BANANA", ["B", "N"]) == "B_N_N_"
    assert display_word("banana", ["B", "N"]) == "______"


def test_display_hangman():
    expected_output = """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
    assert display_hangman(0) == expected_output
