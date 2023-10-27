from bank import value

def test_proper_greeting():
    assert value("hello") == 0


def test_starts_with_h():
    assert value("hi") == 20


def test_capital_greeting():
    assert value("HELLO") == 0


def test_incorrect_greeting():
    assert value("What's up") == 100
