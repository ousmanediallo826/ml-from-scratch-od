import pytest

@pytest.fixture
def fresh_cart():
    print("\n🛒 [Setup] Creating fresh cart...")
    cart = ["apple", "banana"]

    yield cart

    print("\n🧹 [Teardown] Clearing cart out of memory...")
    cart.clear()


def test_fresh_cart(fresh_cart):
    assert len(fresh_cart) == 2
    assert "apple" in fresh_cart
