from abc import ABC, abstractmethod
from enum import Enum, auto


class ChairType(Enum):
    KITCHEN = auto()
    OFFICE = auto()


class ChairBaseMaterial(Enum):
    WOODEN = auto()
    PLASTIC = auto()
    IRON = auto()


class ChairMaterial(Enum):
    LEATHER = auto()
    FABRIC = auto()


class ChairEquipment(Enum):
    ARMREST = auto()
    HEADREST = auto()
    CUPHOLDER = auto()
    RHINESTONES = auto()


"""
Класс компонуемого изделия
"""


class Chair:
    def __init__(self, type):
        self.type = type
        self.base_material = None
        self.material = None
        self.equipment = []
        self.creation_time = None  # in hours

    def __str__(self):
        info: str = f"Chair type: {self.type} \n" \
                    f"Material: {self.base_material.name} & " \
                    f"{self.material.name}\n" \
                    f"Equipment: {[it for it in self.equipment]} \n" \
                    f"Creation time: {self.creation_time} hours"

        return info


"""
Абстрактный класс, задающий интерфейс строителя
"""


class Builder(ABC):

    @abstractmethod
    def make_base(self) -> None: pass

    @abstractmethod
    def sheathe_material(self) -> None: pass

    @abstractmethod
    def add_equipment(self) -> None: pass

    @abstractmethod
    def get_chair(self) -> Chair: pass


"""
Реализация конкретных строителей для сборки
"""


class KitchenChairBuilder(Builder):

    def __init__(self):
        self.chair = Chair("Kitchen")
        self.chair.creation_time = 4  # in hours

    def make_base(self) -> None:
        self.chair.base_material = ChairBaseMaterial.IRON

    def sheathe_material(self) -> None:
        self.chair.material = ChairMaterial.FABRIC

    def add_equipment(self) -> None:
        self.chair.equipment.extend([ChairEquipment.ARMREST.name, ChairEquipment.RHINESTONES.name])

    def get_chair(self) -> Chair:
        return self.chair


class OfficeChairBuilder(Builder):

    def __init__(self):
        self.chair = Chair("Office")
        self.chair.creation_time = 6  # in hours

    def make_base(self) -> None:
        self.chair.base_material = ChairBaseMaterial.PLASTIC

    def sheathe_material(self) -> None:
        self.chair.material = ChairMaterial.LEATHER

    def add_equipment(self) -> None:
        self.chair.equipment.extend([ChairEquipment.ARMREST.name, ChairEquipment.HEADREST.name])

    def get_chair(self) -> Chair:
        return self.chair


"""
Класс Director, отвечающий за процесс поэтапной сборки
"""


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, constructor: Builder):
        self.builder = constructor

    def make_chair(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.make_base()
        self.builder.sheathe_material()
        self.builder.add_equipment()


if __name__ == '__main__':
    director = Director()
    for this in (KitchenChairBuilder, OfficeChairBuilder):
        builder = this()
        director.set_builder(builder)
        director.make_chair()
        chair = builder.get_chair()
        print(chair)
        print('~~~~~~~~~~~~~~~~~')
