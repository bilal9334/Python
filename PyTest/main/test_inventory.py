import pytest
from inventory import Item, Inventory


@pytest.fixture
def item():
    return Item("Laptop", 10)


@pytest.fixture
def another_item():
    return Item("Phone", 5)


@pytest.fixture
def inventory():
    return Inventory()


def test_add_item(inventory, item):
    inventory.add_item(item)
    assert item in inventory.items
    assert len(inventory.items) == 1


def test_remove_item(inventory, item):
    inventory.add_item(item)
    inventory.remove_item(item)
    assert item not in inventory.items


def test_remove_non_existent_item(inventory, item):
    with pytest.raises(ValueError, match="Laptop not found in inventory!"):
        inventory.remove_item(item)


def test_check_stock(inventory, item):
    inventory.add_item(item)
    assert inventory.check_stock(item) == 10


def test_check_stock_non_existent(inventory):
    item = Item("Mouse", 3)
    assert inventory.check_stock(item) == "Mouse not found!"


def test_update_stock(inventory, item):
    inventory.add_item(item)
    assert inventory.update_stock("Laptop", 5) == "Updated stock for Laptop: 15"


def test_update_stock_not_enough(inventory, item):
    inventory.add_item(item)
    assert inventory.update_stock("Laptop", -15) == "Error: Not enough stock to remove 15 items"


def test_update_stock_non_existent(inventory):
    assert inventory.update_stock("Tablet", 5) == "Error: Tablet not found in inventory"
