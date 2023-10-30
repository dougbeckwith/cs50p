from plates import is_valid


def test_valid_length():
    assert is_valid("AA") == True
    assert is_valid("AAA3") == True
    assert is_valid("AAAB33") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAAAAAA") == False


def test_valid_first_num():
    assert is_valid("AA0000") == False
    assert is_valid("AA1111") == True
    assert is_valid("11") == False


def test_symbols():
    assert is_valid("AAD33!") == False
    assert is_valid("AAD33.") == False
    assert is_valid("AAD33 4") == False
    

def test_valid_number_placement():
    assert is_valid("33DD") == False
    assert is_valid("D454") == False
    assert is_valid("BB45") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

    