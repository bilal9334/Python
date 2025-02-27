import pytest
from shoppingcart import Item, ShoppingCart


@pytest.fixture
def item():
    return Item("Laptop", 1000)


@pytest.fixture
def another_item():
    return Item("Mouse", 500)


@pytest.fixture
def cart():
    return ShoppingCart()


def test_add_item(cart, item):
    cart.add_item(item.item, item.price)
    assert len(cart.items) == 1


def test_remove_item(cart, item):
    cart.add_item(item.item, item.price)
    cart.remove_item(item.item)
    assert item.item not in cart.items


def test_remove_product_not_in_cart(cart, item):
    with pytest.raises(ValueError, match="Item not found!"):
        cart.remove_item(item.item)


def test_total_price(cart, item, another_item):
    cart.add_item(item.item, item.price)
    cart.add_item(another_item.item, another_item.price)
    assert cart.get_total() == 1500


def test_get_items(cart, item, another_item):
    cart.add_item(item.item, item.price)
    cart.add_item(another_item.item, another_item.price)
    assert cart.get_items() == {"Laptop": 1000, "Mouse": 500}
