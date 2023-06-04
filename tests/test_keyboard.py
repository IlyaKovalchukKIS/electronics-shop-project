import pytest

from src.keyboard import KeyBoard


def test_init():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_error_setter_language():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'