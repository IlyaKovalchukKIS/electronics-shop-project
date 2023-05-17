"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_items_total_price():
    item1 = Item("Смартфон", 10_000, 20)
    assert item1.calculate_total_price() == 200_000


def test_items_init():
    item1 = Item("Смартфон", 10_000, 20)
    assert isinstance(item1, Item)


def test_items_discount():
    item1 = Item("Смартфон", 10_000, 20)
    Item.pay_rate = 0.85
    item1.apply_discount()
    assert item1.price == 8_500
