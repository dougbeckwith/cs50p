from um import count

def main():
    test_count()
    test_count_um_in_word()
    test_count_um_then_period()
    test_count_capitals()

def test_count():
    assert count('um') == 1


def test_count_um_in_word():
    assert count("um album") == 1
    assert count("um um album") == 2


def test_count_um_then_period():
    assert count("um. um. album") == 2


def test_count_capitals():
    assert count("UM i have a dog") == 1
    assert count("UM, Um i have a dog") == 2