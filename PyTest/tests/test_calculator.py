import pytest
from main.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    assert calc.add(2, 3) == 5


def test_subtraction(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply(calc):
    assert calc.multiply(3, 5) == 15


def test_division(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calc.divide(10, 0)
