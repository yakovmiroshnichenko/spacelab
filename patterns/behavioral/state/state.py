from abc import ABC, abstractmethod
from enum import Enum


class OrderState(Enum):
    """Возможные состояния заказа на сайте-каталоге"""
    ADD_TO_CART = 1  #
    RECEIVE_PAYMENT = 2  # Очікує оплати
    SEND_ORDER = 3  # Передано перевізнику


class Catalog:
    """Класс магазина-каталога для заказов мебели"""

    def __init__(self):
        self.money: int = 0
        self.__states: dict[OrderState, State] = {
            OrderState.ADD_TO_CART: ADD_TO_CART_State(),
            OrderState.RECEIVE_PAYMENT: RECEIVE_PAYMENT_State(),
            OrderState.SEND_ORDER: SEND_ORDER_State()
        }
        self.__now_state: State = self.__states[OrderState.ADD_TO_CART]

    def get_state(self):
        return self.__now_state

    def set_state(self, state: OrderState):
        self.__now_state = self.__states[state]

    def insert_money(self, money: int) -> None:
        self.money += money
        print(f"Баланс пополнен на {self.money}$")
        self.__now_state.insert_money(self)

    def make_order(self) -> None:
        self.__now_state.make_order(self)

    def end_shopping(self) -> None:
        self.__now_state.send_order(self)


class State(ABC):
    """Базовый класс состояние заказа"""

    @abstractmethod
    def make_order(self, machine) -> None:  # Зробити замовлення
        ...

    @abstractmethod
    def insert_money(self, machine) -> None:  # Очікує оплати
        ...

    @abstractmethod
    def send_order(self, machine) -> None:  # Відправляє замовлення
        ...

    def __str__(self):
        return self.__class__.__name__


class ADD_TO_CART_State(State):
    """Статус добавление заказа"""

    def make_order(self, catalog) -> None:
        cost = 50  # Вартість товару
        print(f"Спасибо за заказ, ожидаем оплату в размере {cost}$")
        catalog.set_state(OrderState.RECEIVE_PAYMENT)

    def insert_money(self, machine) -> None:
        print("Вы пополнили баланс с пустой корзиной, выберите товар")

    def send_order(self, machine) -> None:
        print("Пожалуйста, выберите товар")


class RECEIVE_PAYMENT_State(State):
    """Статус ожидания оплаты"""

    def make_order(self, machine) -> None:
        cost = 307  # Вартість товару
        print(f'Товар добавлен в корзину, стоимость {cost}$')

    def insert_money(self, machine) -> None:
        cost = 105
        if machine.money >= cost:
            print("Заказ оплачен")
            machine.set_state(OrderState.SEND_ORDER)
            machine.end_shopping()
        else:
            print("Недостаточно средств")

    def send_order(self, coffee_machine) -> None:
        print("Товар не оплачен, ожидаем оплату!")


class SEND_ORDER_State(State):
    """Статус завершения оформления заказа и совершения отправки"""

    def make_order(self, coffee_machine) -> None:
        print(f"Заказ оформлен, ожидайте SMS уведомления")

    def insert_money(self, coffee_machine) -> None:
        print("Баланс пополнен")

    def send_order(self, coffee_machine) -> None:
        print("Спасибо за заказ, он уже в пути к вам!")


if __name__ == "__main__":
    online_catalog = Catalog()
    print(f"~~~~Текущее состояние заказа:  {online_catalog.get_state()}")
    online_catalog.make_order()
    print(f"~~~~Текущее состояние заказа:  {online_catalog.get_state()}")
    online_catalog.insert_money(70)
    print(f"~~~~Текущее состояние заказа:  {online_catalog.get_state()}")
    online_catalog.insert_money(230)
    print(f"~~~~Текущее состояние заказа:  {online_catalog.get_state()}")
