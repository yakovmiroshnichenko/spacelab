from abc import ABC, abstractmethod


class Strategy(ABC):
    """Интерфейс стратегии"""

    @abstractmethod
    def get_price(self):
        ...

    @abstractmethod
    def get_creation_time(self):
        ...


class SweetheartStrategy(Strategy):
    def __init__(self, price):
        self.price: int = price
        self.creation_time = 3  # in hours
        self.workshop = "Sweetheart"

    def get_price(self):
        return self.price

    def get_creation_time(self):
        return self.creation_time


class CheaplyStrategy(Strategy):
    def __init__(self, price):
        self.price: int = price
        self.creation_time = 6  # in hours
        self.workshop = "Cheaply"

    def get_price(self):
        return self.price

    def get_creation_time(self):
        return self.creation_time


class HomemadeStrategy(Strategy):
    def __init__(self, price):
        self.price: int = price
        self.creation_time = 6  # in hours
        self.workshop = "Home"

    def get_price(self):
        return self.price

    def get_creation_time(self):
        return self.creation_time


class Order:
    def __init__(self, type_order, cost_order, strategy: Strategy):
        self.type = type_order
        self.cost = cost_order
        self._strategy = strategy

    def set_workshop(self, delivery):
        self._strategy = delivery

    def __str__(self):
        return f"""Ваш заказ: {self.type}. Стоимость материалов: {self.cost}$ +
        работа мастера {self._strategy.get_price()}$
        Итого к оплате: {self.cost + self._strategy.get_price()}$
 """


if __name__ == "__main__":
    order1 = Order("Кресло", 50, SweetheartStrategy(40))
    print(order1)
    print("~" * 5)
    order2 = Order("Табурет", 25, CheaplyStrategy(15))
    print(order2)
    print("~" * 5)

    # Клієнт передумав та вирішив забрати самостійно товар з магазину
    order2.set_workshop(HomemadeStrategy(0))
    print(order2)
    print("~" * 5)
