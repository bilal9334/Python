import pytest
from countries import get_capital

def test_get_capital():
    capitals = {
        "Germany": "Berlin",
        "France": "Paris",
        "Italy": "Rome",
        "Spain": "Madrid",
    }

    assert get_capital("Germany", capitals) == "Berlin"
    assert get_capital("France", capitals) == "Paris"
    assert get_capital("Italy", capitals) == "Rome"
    assert get_capital("Spain", capitals) == "Madrid"
    assert get_capital("USA", capitals) == "Country not found"