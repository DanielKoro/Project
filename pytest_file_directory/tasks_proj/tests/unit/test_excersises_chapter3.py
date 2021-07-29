import pytest


@pytest.fixture(scope='module')
def number():
    print(number)
    yield 3
    print(number)


def test_number(number):
    assert number == 3


def test_number2(number):
    assert number == 4
