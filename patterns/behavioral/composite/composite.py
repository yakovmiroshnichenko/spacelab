from abc import ABC, abstractmethod


class IElement(ABC):
    """Интерфейс элементов кресла"""

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Element(IElement):
    """Класс элемента"""

    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundElement(IElement):
    """Класс компонуемых элементов"""

    def __init__(self, name: str):
        self.__name = name
        self.elem = []

    def cost(self):
        cost = 0
        for it in self.elem:
            cost += it.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_element(self, element: IElement):
        self.elem.append(element)

    def remove_element(self, element: IElement):
        self.elem.remove(element)

    def clear(self):
        self.elem = []


class Chair(CompoundElement):
    """Класс мебели"""

    def __init__(self, type: str):
        super(Chair, self).__init__(type)

    def cost(self):
        cost = 0
        for it in self.elem:
            cost_it = it.cost()
            print(f"Стоимость '{it.name()}' = {cost_it}$")
            cost += cost_it
        print(f"Стоимость кресла '{self.name()}' = {cost}$")
        return cost


if __name__ == "__main__":
    base = CompoundElement("Base")
    base.add_element(Element("Wheels", 3))
    base.add_element(Element("Leg", 2.3))
    seat = CompoundElement("Seat")
    seat.add_element(Element("Armrest", 7.3))
    seat.add_element(Element("Headrest", 5.3))
    seat.add_element(Element("Skin", 15.54))
    chair = Chair("Office")
    chair.add_element(base)
    chair.add_element(seat)
    chair.cost()
