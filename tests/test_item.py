"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
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


def test_items_name():
    item2 = Item('Телефон', 25_000, 4)
    assert item2.name == 'Телефон'
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'


def test_items_len_name():
    items2 = Item('Телефон', 25_000, 4)
    assert items2.name == 'Телефон'
    with pytest.raises(Exception):
        items2.name = 'СуперПуперТелефон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.0') == 5


def test_items_repr():
    item1 = Item("Смартфон", 10_000, 20)
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"


def test_items_str():
    item1 = Item("Смартфон", 10_000, 20)
    assert item1.__str__() == 'Смартфон'
