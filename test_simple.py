import pytest


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def times(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return 'cant divide by zero'
    return a / b


def test_sum():
    assert sum(5, 5) == 10


def test_sub():
    assert sub(10, 5) == 5


def test_times():
    assert times(2, 2) == 4


@pytest.mark.parametrize("n1, n2, result", [(10, 2, 5), (5, 5, 1), (10, 0, 'cant divide by zero')])
def test_division(n1, n2, result):
    assert division(n1, n2) == result
