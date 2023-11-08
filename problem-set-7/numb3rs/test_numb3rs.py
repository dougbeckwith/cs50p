from numb3rs import validate


def main():
    test_ip_letters()
    test_ip_numbers()


def test_ip_letters():
    assert validate("a.a.a.a") == False
    assert validate("aa.aa.aa.aa") == False
    assert validate("aaa.aaa.aaa.aaa") == False


def test_ip_numbers():
    assert validate("0.0.0.0") == True
    assert validate("10.10.30.80") == True
    assert validate("104.10.30.80") == True
    assert validate("100.150.130.120") == True
    assert validate("255.255.255.255") == True
    assert validate("1000.1.1.1") == False
    assert validate("10.10.100.900") == False


if __name__ == "__main__":
    main()
