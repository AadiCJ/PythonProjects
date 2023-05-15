from jar import Jar
from pytest import raises


def test_deposit():
    j = Jar(10)
    with raises(ValueError):
        j.deposit(11)
    j = Jar(100)
    with raises(ValueError):
        j.deposit(111)

    j = Jar()
    j.deposit(5)
    assert j.size == 5


def test_withdraw():
    j = Jar(10)
    with raises(ValueError):
        j.withdraw(1)
    j = Jar(50)
    with raises(ValueError):
        j.withdraw(100)

    j = Jar()
    j.deposit(5)
    j.withdraw(2)
    assert j.size == 3
    j.withdraw(3)
    assert j.size == 0


def test_str():
    j = Jar()
    j.deposit(5)
    assert j.__str__().strip() == "🍪🍪🍪🍪🍪"
    j.deposit(2)
    assert j.__str__().strip() == "🍪🍪🍪🍪🍪🍪🍪"
    j.withdraw(5)
    assert j.__str__().strip() == "🍪🍪"


def test_capacity():
    j = Jar()
    assert j.capacity == 12
    j = Jar(100)
    assert j.capacity == 100
    j = Jar(50)
    assert j.capacity == 50
