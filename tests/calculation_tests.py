import pytest

from src.calculations import add, average, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 9) == -6


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(8, 2) == 4
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([10, 20]) == 15


def test_average_empty_list():
    with pytest.raises(ValueError, match="No values provided"):
        average([])
