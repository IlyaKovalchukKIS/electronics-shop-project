import os
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создает экземпляры класса на основе таблицы хранящейся в items.csv
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/items.csv', encoding='utf-8') as csv_file:
            csv_reader = DictReader(csv_file)
            cls.all = []
            for (row) in csv_reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(number):
        """
        Преобразовывает строки-числа в числа
        """
        if "." in number:
            return int(float(number))
        else:
            return int(number)

    @property
    def name(self):
        """
        Геттер, который возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Сеттер, который проверяет длину названия товара,
        и если она не больше 10 символов то записывает ее
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина товара превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
