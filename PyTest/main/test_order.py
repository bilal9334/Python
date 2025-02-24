import pytest
from order import Product, Order


@pytest.fixture
def order():
    return Order()


@pytest.fixture
def sample_product():
    return Product("Laptop", 1000)


@pytest.fixture
def another_product():
    return Product("Phone", 500)


def test_add_product(order, sample_product):
    order.add_product(sample_product)
    assert len(order.products) == 1
    assert order.products[0] == sample_product


def test_total_price(order, sample_product, another_product):
    order.add_product(sample_product)
    order.add_product(another_product)
    assert order.total_price() == 1500


def test_apply_discount(order, sample_product):
    order.add_product(sample_product)
    assert order.apply_discount(10) == 900


def test_checkout(order):
    with pytest.raises(ValueError, match="Order is empty! Failed to checkout"):
        order.checkout()
