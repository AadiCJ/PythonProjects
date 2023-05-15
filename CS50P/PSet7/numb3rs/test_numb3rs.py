from numb3rs import validate


def testHighNumberRejection():
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False
    assert validate("275.3.6.28") == False


def testAlphaRejection():
    assert validate("192.168.0.1") == True
    assert validate("a.letter.is.here") == False
    assert validate("these.are.13.letters") == False


def testFormatIncorrectRejection():
    assert validate("192.168.0.1") == True
    assert validate("192,168,0,1") == False


def testFirstByteCheckOnly():
    assert validate("192.168.0.1") == True
    assert validate("192.1245.32.42") == False
    assert validate("134.256.353.12") == False
