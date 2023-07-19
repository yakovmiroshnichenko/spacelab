from abc import ABC, abstractmethod
from typing import List


class OrderItemVisitor(ABC):
    """Интерфейс посетителя"""

    @abstractmethod
    def visit(self, item) -> float:
        ...


class ItemElement(ABC):
    """Интерфейс для заказываемых изделий"""

    @abstractmethod
    def accept(self, visitor: OrderItemVisitor) -> float:
        ...


class Chair(ItemElement):
    """Класс кресла"""

    def __init__(self, type: str, price: float):
        self.type = type
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class Table(ItemElement):
    """Класс стола"""

    def __init__(self, type: str, price: float, square: float):
        self.type = type
        self.price = price
        self.square = square

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class WithOutDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    без учета скидки"""

    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Chair):
            cost = item.get_price()
        elif isinstance(item, Table):
            cost = item.get_price()
        return cost


class ChairDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    учетом скидки на все стулья в 15%"""

    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Chair):
            cost = item.get_price()
            cost -= cost * 0.15
        elif isinstance(item, Table):
            cost = item.get_price()
        return cost


class TableDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    учетом скидки на все столы в 35%"""

    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Chair):
            cost = item.get_price()
        elif isinstance(item, Table):
            cost = item.get_price()
            cost -= cost * 0.35
        return cost


class Master:
    def __init__(self, discounts: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discounts

    def set_order(self, orders: List[ItemElement]) -> None:
        self.order = orders

    def set_discount(self, discounts: OrderItemVisitor) -> None:
        self.discount_calculator = discounts

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price


if __name__ == "__main__":
    order: List[ItemElement] = [Chair("Office", 12.3),
                                Table("Working", 45, 1),
                                Chair("Kitchen", 10.5),
                                Chair("Game", 20),
                                Table("Dining", 50, 2)]
    discount = WithOutDiscountVisitor()
    master = Master(discount)
    master.set_order(order)
    print(f"Сумма заказа без учета скидок: "
          f"{master.calculate_finish_price()}$")
    discount = ChairDiscountVisitor()
    master.set_discount(discount)
    print(f"Сумма заказа c учетом скидки на стулья: "
          f"{master.calculate_finish_price()}$")
    discount = TableDiscountVisitor()
    master.set_discount(discount)
    print(f"Сумма заказа c учетом скидки на столы: "
          f"{master.calculate_finish_price()}$")

