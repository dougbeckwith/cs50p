from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar_two = Jar(2)
    assert jar_two.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(2) == None
    with pytest.raises(ValueError):
        jar.deposit(11)
    assert jar.deposit(5) == None


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(11)
    jar.deposit(1)
    assert jar.withdraw(1) == None
