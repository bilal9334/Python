import pytest
from employee_mgm_system import EmployeeManager


@pytest.fixture
def manager():
    emp_manager = EmployeeManager()
    emp_manager.add_employee("Alice", 2500)
    emp_manager.add_employee("Bob", 5000)
    return emp_manager


def test_add_employee(manager):
    manager.add_employee("Charlie", 6000)
    assert manager.get_salary("Charlie") == 6000

    with pytest.raises(ValueError, match="Employee already exists."):
        manager.add_employee("Alice", 2500)

    with pytest.raises(ValueError, match="Salary cannot be negative."):
        manager.add_employee("David", -1000)


def test_remove_employee(manager):
    manager.remove_employee("Alice")
    with pytest.raises(KeyError, match="Employee not found"):
        manager.get_salary("Alice")

    with pytest.raises(KeyError, match="Employee not found"):
        manager.remove_employee("Emmanuel")


def test_update_salary(manager):
    manager.update_salary("Alice", 5000)
    assert manager.get_salary("Alice")

    with pytest.raises(KeyError, match="Employee not found"):
        manager.get_salary("Raza")

    with pytest.raises(KeyError, match="Salary cannot be negative"):
        manager.update_salary("Alice", -7000)


def test_get_salary(manager):
    assert manager.get_salary("Alice") == 2500
    assert manager.get_salary("Bob") == 5000

    with pytest.raises(KeyError, match="Employee not found"):
        manager.get_salary("Unknown")


def test_list_all_employees(manager):
    employees = manager.get_all_employees()
    assert employees == {"Alice": 2500, "Bob": 5000}

    manager.add_employee("Charlie", 8000)
    employees = manager.get_all_employees()
    assert employees == {"Alice": 2500, "Bob": 5000, "Charlie": 8000}
