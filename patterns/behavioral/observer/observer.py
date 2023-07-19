from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderType(Enum):
    """Типы возможных заказов"""
    SOFA = 1
    CHAIR = 2
    TABLE = 3


class Order:
    """Класс заказа"""
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ под #{self.id} ({self.type.name})"


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...


class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)


class Master(Subject):
    def __init__(self):
        super().__init__()
        self.__orders: List[Order] = []
        self.__finish_order: List[Order] = []

    def take_order(self, order: Order) -> None:
        print(f"Мастер принял {order}")
        self.__orders.append(order)

    def get_order(self, order_id: int) -> Order:
        order = None
        for it in self.__finish_order:
            if it.id == order_id:
                order = it
                break
        self.__finish_order.remove(order)
        return order

    def processing_order(self):
        if self.__orders:
            order = choice(self.__orders)
            self.__orders.remove(order)
            self.__finish_order.append(order)
            print(f"Мастер выполнил {order}")
            self.notify(order.id)
        else:
            print("Мастер совершает уборку в мастерской")


class Client(Observer):
    def __init__(self, name: str, master: Master):
        self.__master = master
        self.__name = name
        self.order: Order = None

    def update(self, order_id: int) -> None:
        """Принимаем номер текущего выполненного заказа
        и "отписываемся" от оповещения мастера"""
        if self.order is not None:
            if order_id == self.order.id:
                print(f"Клиент {self.__name} забрал(а) "
                      f"{self.__master.get_order(order_id)}")
                self.__master.detach(self)

    def create_order(self) -> None:
        """Метод для формирования заказа
        и подписки на оповещения от мастера
        по выполненному заказу"""
        order_type = choice([OrderType.SOFA,
                             OrderType.CHAIR,
                             OrderType.TABLE])
        self.order = Order(order_type)
        print(f"Клиент {self.__name} сделал(а) {self.order}")
        self.__master.attach(self)
        self.__master.take_order(self.order)


if __name__ == "__main__":
    names = ['Яков', 'Роман',
             'Богдан', 'Ростислав', 'Андрей']
    master = Master()
    clients = [Client(name, master) for name in names]
    for client in clients:
        print("~"*30)
        client.create_order()
    print("*" * 4 + "Мастер приступает к выполнению заказов" + 4 * "*")
    for _ in range(6):
        print("~"*30)
        master.processing_order()
