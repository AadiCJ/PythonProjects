from plates import is_valid


def test_hasSpecialChars():
    assert is_valid("CS5,") == False
    assert is_valid(",CS5") == False


def test_noLettersAfterNumbers():
    assert is_valid("AA513") == True
    assert is_valid("AAAA2A") == False
    assert is_valid("AA50A") == False


def test_firstNumberNotZero():
    assert is_valid("GSD152") == True
    assert is_valid("SET012") == False
    assert is_valid("DGFH01") == False


def test_startWithTwoLetters():
    assert is_valid("AA") == True
    assert is_valid("S3") == False
    assert is_valid("33") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("CS50135") == False
