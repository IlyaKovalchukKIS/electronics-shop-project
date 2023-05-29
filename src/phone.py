from src.item import Item


class Phone(Item):
    """Класс Phone"""

    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим карт в телефоне
        """
        super().__init__(name, price, quantity)
        super().__repr__() + str(number_of_sim)
        self.__number_of_sim = number_of_sim
        self.__name = name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """
        Getter для атрибута number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity: int) -> None:
        """
        Setter для атрибута number_of_sim, который проверяет,
        является ли quantity экземпляром класса int и условие,
        что количество сим-карт должно быть больше 0
        """
        if quantity > 0 and isinstance(quantity, int):
            self.__number_of_sim = quantity
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
