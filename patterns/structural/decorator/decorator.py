from abc import ABC, abstractmethod


class Base(ABC):
    """Интерфейс декорируемого объекта"""
    @abstractmethod
    def cost(self) -> float:
        pass


class ChairBase(Base):
    """Класс декорируемого объекта"""
    def __init__(self, cost):
        self.cost = cost

    def cost(self) -> float:
        return self.cost


class IDecorator(Base):
    """Интерфейс декоратора"""
    @abstractmethod
    def name(self) -> str:
        pass


class ChairBasePlastic(IDecorator):
    def __init__(self, wrapped: Base, chair_cost: float):
        self.wrapped = wrapped
        self.cost = chair_cost
        self.name = "Plastic"

    def cost(self) -> float:
        return self.cost+self.wrapped.cost()

    def name(self) -> str:
        return self.name


class ChairBaseIron(IDecorator):
    def __init__(self, wrapped: Base, chair_cost: float):
        self.wrapped = wrapped
        self.cost = chair_cost
        self.name = "Iron"

    def cost(self) -> float:
        return self.cost+self.wrapped.cost()

    def name(self) -> str:
        return self.name


if __name__ == "__main__":
    def print_chair(chair: IDecorator) -> None:
        print(f"{chair.name()} chair cost = {chair.cost()}")

    chair_base = ChairBase(3.4)
    print(f"Chair base price: = {chair_base.cost()}")
    plastic = ChairBasePlastic(chair_base, 10)
    print_chair(plastic)
    iron = ChairBaseIron(chair_base, 7)
    print_chair(iron)
