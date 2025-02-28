import pytest
from inventory import Product, Inventory


@pytest.fixture
def inventory():
    return Inventory()


def test_add_product(inventory):
    inventory.add_product("Apple", 10)
    assert inventory.get_product_quantity("Apple") == 10

    inventory.add_product("Apple", 5)
    assert inventory.get_product_quantity("Apple") == 15


def test_remove_products(inventory):
    inventory.add_product("Banana", 10)

    inventory.remove_product("Banana", 5)
    assert inventory.get_product_quantity("Banana") == 5

    inventory.remove_product("Banana", 5)
    with pytest.raises(KeyError, match="Product not found."):
        inventory.get_product_quantity("Banana")

    with pytest.raises(KeyError, match="Product not found."):
        inventory.remove_product("NonExisting", 2)


def test_get_product_quantity(inventory):
    inventory.add_product("Grapes", 20)
    assert inventory.get_product_quantity("Grapes") == 20


def test_get_all_products(inventory):
    inventory.add_product("Mango", 3)
    inventory.add_product("Orange", 3)

    products = inventory.get_all_products()
    assert products == {"Mango": 3, "Orange": 3}

    inventory.remove_product("Mango", 3)
    products = inventory.get_all_products()
    assert products == {"Orange": 3}
