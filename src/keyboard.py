from src.item import Item


class MixinLanguage:
    """Класс миксин для изменения раскладки клавиатуры"""
    __slots__ = ['__language']

    def __init__(self) -> None:
        self.__language: str = "EN"

    @property
    def language(self) -> str:
        """Геттер для атрибута language"""
        return self.__language

    def change_lang(self):
        """Метод для изменения раскладки клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class KeyBoard(Item, MixinLanguage):
    """Класс товара Клавиатуры"""
    __slots__ = ['name', 'price', 'quantity']

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
