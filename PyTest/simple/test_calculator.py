import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5


def test_subtract(calc):
    assert calc.subtract(3, 2) == 1


def test_multiply(calc):
    assert calc.multiply(5, 3) == 15


def test_division_by_zero(calc):
    with pytest.raises(ValueError, match="Division by zero not possible."):
        calc.divide(10, 0)


def test_division(calc):
    assert calc.divide(6, 3) == 2
