from bank import value


def test_cisStartsWithH():
    assert value("Hey") == value("hey")


def test_cisStartsWithHello():
    assert value("Hello, Greetings") == value("hello, Greetings")


def test_cisElse():
    assert value("Other Greetings") == value("other Greetings")


def test_startsWithH():
    assert value("Hey") == 20


def test_startsWithHello():
    assert value("Hello, Greetings") == 0


def test_else():
    assert value("Other Greetings") == 100
