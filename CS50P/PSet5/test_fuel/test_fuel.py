from fuel import gauge, convert
import pytest


def testConvert_valueError():
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ValueError):
        convert("124/22")


def testConvert_zeroDivError():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def testConvert_checkRounding():
    assert convert("2/3") == 67
    assert convert("1/3") == 33


def testGauge_returnsE():
    assert gauge(2) != "E"
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def testGauge_returnsF():
    assert gauge(98) != "F"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def testGauge_returnsPercentage():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
