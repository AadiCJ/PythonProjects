from twttr import shorten


def test_caseInsensitivity():
    assert shorten("TwITteR").lower() == shorten("twitter")


def test_shortening():
    assert shorten("Sentence") == "Sntnc"


def test_ignoreNumbers():
    assert shorten("23423512") == "23423512"


def test_ignorePunctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
