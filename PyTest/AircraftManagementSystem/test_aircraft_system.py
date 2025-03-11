import pytest
from aircraft_system import Aircraft

@pytest.fixture
def aircraft():
    return Aircraft("A320-001")

def test_take_off(aircraft):
    aircraft.take_off(5000)
    assert aircraft.get_status() == "ascending"

    aircraft.take_off(40000)
    assert aircraft.get_status() == "cruising"

def test_descend(aircraft):

    aircraft.descend(0)
    assert aircraft.get_status() == "on ground"

def test_take_off_when_in_air(aircraft):
    aircraft.take_off(4000)
    assert aircraft.get_status() == "ascending"
    aircraft.take_off(6000)
    assert aircraft.get_status() == "cruising"

def test_descend_when_on_ground(aircraft):
    aircraft.descend(0)
    assert aircraft.get_status() == "on ground"

    aircraft.descend(1000)
    assert aircraft.get_status() == "on ground"
    