import pytest
from src.phone import Phone


def test_phone_init():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_setter_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

    with pytest.raises(ValueError):
        phone.number_of_sim = 0

    with pytest.raises(ValueError):
        phone_fail_sim = Phone("Test", 15_000, 4, 0)


def test_phone_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
