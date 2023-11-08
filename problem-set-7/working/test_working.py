import pytest
from working import convert

def main():
    test_proper_time()
    test_wrong_format()
    test_wrong_hour()
    test_wrong_minute()


def test_proper_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("11:40 PM to 8:15 AM") == "23:40 to 08:15"


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("15 AM to 13 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")
