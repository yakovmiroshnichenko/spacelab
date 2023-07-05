from abc import ABC, abstractmethod
import time


class Chair:
    """Класс изделия"""

    def __init__(self, type: str, material: str, creation_time: int):
        self.type = type
        self.material = material
        self.creation_time = creation_time  # in hours
        self.__isReady = False

    def make(self) -> None:
        self.__isReady = True

    def isReady(self) -> bool:
        return self.__isReady


class IMachineImplementor(ABC):
    """Интерфейс для реализации станков различного типа"""

    @abstractmethod
    def set_material(self, material: str) -> None:
        pass

    @abstractmethod
    def create_chair(self, chair: Chair) -> None:
        pass

    @abstractmethod
    def get_material(self) -> str:
        pass

    @abstractmethod
    def get_machine_type(self) -> str:
        pass


class ManualMachineImplementor(IMachineImplementor):

    def __init__(self, material: str):
        self.material = material
        self.type = "Manual"

    def set_material(self, material: str) -> None:
        self.material = material

    def create_chair(self, chair: Chair) -> None:
        time.sleep(chair.creation_time)
        chair.make()

    def get_machine_type(self) -> str:
        return self.type

    def get_material(self) -> str:
        return self.material


class AutoMachineImplementor(IMachineImplementor):

    def __init__(self, material: str):
        self.material = material
        self.type = "Auto"

    def set_material(self, material: str) -> None:
        self.material = material

    def create_chair(self, chair: Chair) -> None:
        time.sleep(chair.creation_time/2)
        chair.make()

    def get_machine_type(self) -> str:
        return self.type

    def get_material(self) -> str:
        return self.material


class Machine:
    """Класс станка"""

    def __init__(self, implementor: IMachineImplementor):
        self.__implementor = implementor

    def __prepare_material(self, material: str):
        if self.__implementor.get_material() != material:
            print("Material replacement, please wait...")
            time.sleep(2)
            self.__implementor.set_material(material)
        else:
            print("Correct material")
        print("Machine prepared!")

    def make_chair(self, chair: Chair) -> None:
        self.__prepare_material(chair.material)
        print(f"Making {chair.type} chair for {chair.creation_time}"
              f" hours at {chair.material} material")
        self.__implementor.create_chair(chair)
        if chair.isReady():
            print("Chair is ready!!!")
        else:
            print("O_o ... some wrong ...")
        print("~~~~~~~~~~~~~~")

    def change_implementor(self, implementor: IMachineImplementor) -> None:
        self.__implementor = implementor
        print("Implementor changed")

    def get_material(self) -> str:
        return self.__implementor.get_material()

    def get_implementor_name(self) -> str:
        return self.__implementor.get_machine_type()


if __name__ == "__main__":
    first_chair = Chair("Kitchen", 'Fabric', 4)
    second_chair = Chair("Office", 'Leather', 6)

    implementor = ManualMachineImplementor(first_chair.material)
    machine = Machine(implementor)
    print(f"Implementor type: {machine.get_implementor_name()}")
    machine.make_chair(first_chair)
    machine.make_chair(second_chair)
    # замена реализации
    new_implementor = AutoMachineImplementor(machine.get_material())
    machine.change_implementor(new_implementor)
    machine.make_chair(first_chair)
    machine.make_chair(second_chair)
    print(f"Implementor type: {machine.get_implementor_name()}")
