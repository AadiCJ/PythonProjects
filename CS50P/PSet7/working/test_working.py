import working
from pytest import raises


def testInvalidMinutes():
    with raises(ValueError):
        working.convert("9:60 PM to 5:60 AM")
    with raises(ValueError):
        working.convert("9:68 AM to 5:12 PM")
    with raises(ValueError):
        working.convert("9 AM to 5:79 PM")


def testCorrectOutput():
    assert working.convert("9 PM to 5 PM").strip() == "21:00 to 17:00".strip()
    assert working.convert("9 AM to 5 PM").strip() == "09:00 to 17:00".strip()
    assert working.convert("9:30 AM to 5:30 PM").strip() == "09:30 to 17:30".strip()


def testIncorrectFormat():
    with raises(ValueError):
        working.convert("9 PM - 5 PM")
    with raises(ValueError):
        working.convert("9 PM from 5 AM")
