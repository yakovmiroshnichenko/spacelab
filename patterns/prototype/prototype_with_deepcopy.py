from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Chair(Prototype):
    __material: str = ''
    __creation_time: int = 4

    def __init__(self, donor: 'Chair' = None):
        if donor is not None:
            self.__material = donor.get_material()
            self.__creation_time = copy.deepcopy(donor.get_creation_time())

    def set_material(self, material: str):
        self.__material = material

    def get_material(self) -> str:
        return self.__material

    def get_creation_time(self) -> int:
        return self.__creation_time

    def set_creation_time(self, time: int):
        self.__creation_time = time  # in hours

    def clone(self):
        return Chair(self)

    def __str__(self):
        return f"Base material: {self.get_material()}; "\
               f"Creation time: {self.get_creation_time()} hours\n"


if __name__ == '__main__':
    chair1: Chair = Chair()
    chair1.set_material('Iron')
    chair2: Chair = chair1.clone()
    print(chair1, chair2)
    chair2.set_material('Plastic')
    chair2.set_creation_time(5)
    print('~~~~~~~~~~~~')
    print(chair1, chair2)
    print(id(chair1), id(chair2))
