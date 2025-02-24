import pytest
from shopping_cart import Product, ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart()


@pytest.fixture
def sample_product():
    return Product("Laptop", 1000)


@pytest.fixture
def another_product():
    return Product("Phone", 500)


def test_add_product(cart, sample_product):
    cart.add_product(sample_product)
    assert len(cart.products) == 1
    assert cart.products[0] == sample_product


def test_remove_product(cart, sample_product):
    cart.add_product(sample_product)
    cart.remove_product(sample_product)
    assert len(cart.products) == 0


def test_remove_product_not_in_cart(cart, sample_product):
    with pytest.raises(ValueError, match="Product not in cart!"):
        cart.remove_product(sample_product)


def test_total_price(cart, sample_product, another_product):
    cart.add_product(sample_product)
    cart.add_product(another_product)
    assert cart.total_price() == 1500


def test_cart_is_empty(cart):
    assert cart.is_empty() == True
    cart.add_product(Product("Tablet", 300))
    assert cart.is_empty() == False
