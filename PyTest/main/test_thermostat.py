import pytest
from thermostat import SmartThermostat

@pytest.fixture
def smart_thermostat():
    return SmartThermostat(15)


def test_set_temperature(smart_thermostat):
    smart_thermostat.set_temperature(20)
    assert smart_thermostat.temperature == 20

    with pytest.raises(ValueError, match="Temperature must be between 10 and 30 degrees"):
        smart_thermostat.set_temperature(100)


def test_increase_temperature(smart_thermostat):
    smart_thermostat.increase_temperature(10)
    assert smart_thermostat.temperature == 25



def test_decrease_temperature(smart_thermostat):
    smart_thermostat.decrese_temperature(5)
    assert smart_thermostat.temperature == 10

    smart_thermostat.decrese_temperature(1)
    assert smart_thermostat.temperature == 10
    