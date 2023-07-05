from abc import ABC, abstractmethod
from enum import Enum


class ChairTypeCatalog(Enum):
    """Тип каталога"""
    Office = 1
    Kitchen = 2
    Fishing = 3


class ICatalog(ABC):
    """
    Базовый класс, задающий
    интерфейс создаваемых меню
    """

    @abstractmethod
    def get_name(self):
        pass


class OfficeCatalog(ICatalog):
    def get_name(self):
        return "Каталог офисных стульев"


class KitchenCatalog(ICatalog):
    def get_name(self):
        return "Каталог кухонных стульев"


class FishingCatalog(ICatalog):
    def get_name(self):
        return "Каталог стульев для рыбалки"


class IClient(ABC):
    """
    Базовый класс, задающий
    интерфейс клиентов магазина
    """

    @abstractmethod
    def request_catalog(self, menu: ICatalog):
        ...

    @abstractmethod
    def form_order(self) -> dict:
        ...

    @abstractmethod
    def take_chair(self):
        ...

    @abstractmethod
    def get_name(self):
        ...


#####################################################


class Workshop:
    """
    Мастерская
    """

    def create_chair(self):
        print("Стул в процессе сборки!")

    def call_worker(self):
        print("Отдаем готовый стул продавцу")


class Worker:
    """
    Продавец-консультант
    """

    def take_order(self, client: IClient):
        print(f"Продавец принял заказ клиента {client.get_name()}")

    def send_to_workshop(self, workshop: Workshop):
        print("Продавец отнес заказ в мастерскую")

    def give_client(self, client: IClient):
        print(f"Стул готов и передан клиенту {client.get_name()}!")


class ChairShopFacade:
    """
    Пиццерия на основе паттерна 'Фасад'
    """

    def __init__(self):
        self.workshop = Workshop()
        self.worker = Worker()
        self.catalog = {ChairTypeCatalog.Office: OfficeCatalog,
                        ChairTypeCatalog.Kitchen: KitchenCatalog,
                        ChairTypeCatalog.Fishing: FishingCatalog}

    def get_catalog(self, type_catalog: ChairTypeCatalog) -> ICatalog:
        return self.catalog[type_catalog]()

    def take_order(self, client: IClient):
        self.worker.take_order(client)
        self.worker.send_to_workshop(self.workshop)
        self.__workshop_create()
        self.worker.give_client(client)

    def __workshop_create(self):
        self.workshop.create_chair()
        self.workshop.call_worker()


class Client(IClient):
    """
    Класс клиента пиццерии
    """

    def __init__(self, name: str):
        self.name = name

    def request_catalog(self, catalog: ICatalog):
        print(f"Клиент {self.name} ознакамливается с '{catalog.get_name()}'")

    def form_order(self) -> dict:
        print(f"Клиент {self.name} делает заказ")
        return {}

    def take_chair(self):
        print(f"Клиент {self.name} получил стул")

    def get_name(self):
        return self.name


if __name__ == "__main__":
    chair_shop = ChairShopFacade()
    client1 = Client("Роман")
    client2 = Client("Яков")
    client1.request_catalog(chair_shop.get_catalog(ChairTypeCatalog.Office))
    chair_shop.take_order(client1)
    client2.request_catalog(chair_shop.get_catalog(ChairTypeCatalog.Fishing))
    chair_shop.take_order(client2)
    client1.take_chair()
    client2.take_chair()
