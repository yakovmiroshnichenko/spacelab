from abc import ABC, abstractmethod
from typing import List


class Chair:
    """Класс изделия"""

    def __init__(self):
        self.__state: List[str] = ['base']

    def add_element(self, element: str) -> None:
        print(f"Добавлен элемент: {element}")
        self.__state.append(element)

    def __str__(self):
        return f"Элементы кресла: {self.__state}"


class ChairMaker(ABC):
    """Базовый класс шаблонного метода"""

    def make_chair(self, chair: Chair) -> None:
        self.sheathe_material(chair)
        self.add_improvement(chair)
        self.create(chair)

    @abstractmethod
    def sheathe_material(self, chair: Chair) -> None:
        ...

    @abstractmethod
    def add_improvement(self, chair: Chair) -> None:
        ...

    @abstractmethod
    def create(self, chair: Chair) -> None:
        ...


class OfficeChairMaker(ChairMaker):
    """Класс изготовления офисного стула"""

    def sheathe_material(self, chair: Chair) -> None:
        chair.add_element('Leather')

    def add_improvement(self, chair: Chair) -> None:
        chair.add_element('Headrest')
        chair.add_element('Armrest')
        chair.add_element('Glass-holder')

    def create(self, chair: Chair) -> None:
        print("Кресло будет изготовлено через 3 часа")


class KitchenChairMaker(ChairMaker):
    """Класс изготовления кухонного стула"""

    def sheathe_material(self, chair: Chair) -> None:
        chair.add_element('')

    def add_improvement(self, chair: Chair) -> None:
        chair.add_element('Headrest')
        chair.add_element('Armrest')
        chair.add_element('Height adjuster')

    def create(self, chair: Chair) -> None:
        print("Кресло будет изготовлено через 3 часа")


class Master:
    """Класс мастера по изготовлению мебели"""

    def __init__(self, template_chair: ChairMaker):
        self.__create = template_chair

    def set_template(self, template_chair: ChairMaker):
        self.__create = template_chair

    def make_chair(self) -> Chair:
        chair = Chair()
        self.__create.make_chair(chair)
        return chair


if __name__ == "__main__":
    master = Master(OfficeChairMaker())
    print("~" * 8 + "Мастер изготавливает стул 'Офис'" + 8 * "~")
    print(master.make_chair())
    print("*" * 8 + "Мастер изготавливает стул 'Кухонный'" + 8 * "*")
    master.set_template(KitchenChairMaker())
    print(master.make_chair())
