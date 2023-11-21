import pytest
from seasons import check_birth_date


def main():
    test_check_birth_date()


def test_check_birth_date():
    assert check_birth_date("1987-01-15") == ("1987", "01", "15")
    assert check_birth_date("1987-01-153") == None
    assert check_birth_date("Jan 15th 1987") == None
