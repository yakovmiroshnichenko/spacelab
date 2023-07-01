from abc import ABC, abstractmethod
import logging
logging.getLogger(__name__)

"""
Базовые классы мебели
"""


class Sofa(ABC):
    def __init__(self, furniture: str):
        self._furniture = furniture

    @abstractmethod
    def create(self): pass


class Chair(ABC):
    def __init__(self, furniture: str):
        self._furniture = furniture

    @abstractmethod
    def create(self): pass


class Table(ABC):
    def __init__(self, furniture: str):
        self._furniture = furniture

    @abstractmethod
    def create(self): pass


"""
Производные классы мебели в готическом стиле
"""


class GothicSofa(Sofa):
    def __init__(self):
        super().__init__("Gothic")

    def create(self):
        logging.info(f'Created sofa in {self._furniture} style')


class GothicChair(Chair):
    def __init__(self):
        super().__init__("Gothic")

    def create(self):
        logging.info(f'Create chair in {self._furniture} style')


class GothicTable(Table):
    def __init__(self):
        super().__init__("Gothic")

    def create(self):
        logging.info(f'Created table in {self._furniture} style')


"""
Производные классы мебели в стиле модерн
"""


class ModernSofa(Sofa):
    def __init__(self):
        super().__init__("Modern")

    def create(self):
        logging.info(f'Created sofa in {self._furniture} style')


class ModernChair(Chair):
    def __init__(self):
        super().__init__("Modern")

    def create(self):
        logging.info(f'Create chair in {self._furniture} style')


class ModernTable(Table):
    def __init__(self):
        super().__init__("Modern")

    def create(self):
        logging.info(f'Created table in {self._furniture} style')


"""
Базовый класс абстрактной фабрики
"""


class FurnitureAbstractFactory(ABC):
    @abstractmethod
    def getSofa(self) -> Sofa: pass

    @abstractmethod
    def getChair(self) -> Chair: pass

    @abstractmethod
    def getTable(self) -> Table: pass


"""
Производные классы абстрактной фабрики,
конкретные реализации для каждого стиля мебели
"""


class GothicFactory(FurnitureAbstractFactory):
    def getSofa(self) -> Sofa:
        return GothicSofa()

    def getChair(self) -> Chair:
        return GothicChair()

    def getTable(self) -> Table:
        return GothicTable()


class ModernFactory(FurnitureAbstractFactory):
    def getSofa(self) -> Sofa:
        return ModernSofa()

    def getChair(self) -> Chair:
        return ModernChair()

    def getTable(self) -> Table:
        return ModernTable()


"""
Клиентский класс, использующий фабрику для создания мебели
"""


class Creation:
    def __init__(self, factory: FurnitureAbstractFactory):
        self._furniture_factory = factory

    def create_furniture(self):
        sofa = self._furniture_factory.getSofa()
        chair = self._furniture_factory.getChair()
        table = self._furniture_factory.getTable()
        sofa.create()
        chair.create()
        table.create()


def create_factory(style: str) -> FurnitureAbstractFactory:
    factory_dict = {
        "Gothic": GothicFactory,
        "Modern": ModernFactory
    }
    return factory_dict[style]()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    furniture_style = "Modern"
    furn = create_factory(furniture_style)
    add = Creation(furn)
    add.create_furniture()
