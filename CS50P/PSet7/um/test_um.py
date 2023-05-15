from um import count


def testWordRejection():
    assert count("Yummy") == 0
    assert count("Umasdf") == 0


def testCaseInsensitive():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
