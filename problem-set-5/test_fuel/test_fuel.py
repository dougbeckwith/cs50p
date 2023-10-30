import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    with pytest.raises(ValueError):
        convert("4 divided 5")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("4/2")
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(55) == "55%"
