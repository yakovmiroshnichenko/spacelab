from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    """Интерфейсный класс для выполняемых операций"""

    @abstractmethod
    def execute(self) -> None:
        ...


class Master:
    def assemble_chair(self):
        print("Мастер собирает кресло из деталей")

    def make_markup(self):
        print("Мастер делает разметку для механизма обшивки")

    def put_in_machine(self):
        print("Мастер помещает заготовку в механизм")


class Apprentice:
    def prepare_billet(self):
        print("Ассистент подготавливает все детали кресла")

    def prepare_material(self):
        print("Ассистент подготавливает материал обшивки")


class Machine:
    def check(self):
        print("Механизм проверяет правильность сборки")

    def cover_material(self):
        print("Механизм обтягивает материалом заготовку ")


class PrepareBilletCommand(ICommand):
    """Класс команды для подготовки деталей кресла"""

    def __init__(self, executor: Apprentice):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_billet()


class PrepareMaterialCommand(ICommand):
    """Класс команды для подготовки материал обшивки"""

    def __init__(self, executor: Apprentice):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_material()


class AssembleChairCommand(ICommand):
    """Класс команды для сборки кресла"""

    def __init__(self, executor: Master):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.assemble_chair()


class MakeMarkupCommand(ICommand):
    """Класс команды для нанесения разметки"""

    def __init__(self, executor: Master):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_markup()


class PutMachineCommand(ICommand):
    """Класс команды для нанесения разметки"""

    def __init__(self, executor: Master):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.put_in_machine()


class CheckAssemblyCommand(ICommand):
    """Класс команды для проверки сборки"""

    def __init__(self, executor: Machine):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.check()


class CoverMaterialCommand(ICommand):
    """Класс команды для проверки сборки"""

    def __init__(self, executor: Machine):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cover_material()


class ChairWorkshop:
    """Класс агрегации всех команд для сборки кресла"""

    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def create(self) -> None:
        if not self.history:
            print("Не задана очередность выполнения"
                  " команд сборки кресла")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    master = Master()
    apprentice = Apprentice()
    machine = Machine()
    workshop = ChairWorkshop()
    # формируем последовательность команд для сборки кресла
    workshop.addCommand(PrepareBilletCommand(apprentice))
    workshop.addCommand(PrepareMaterialCommand(apprentice))
    workshop.addCommand(AssembleChairCommand(master))
    workshop.addCommand(MakeMarkupCommand(master))
    workshop.addCommand(PutMachineCommand(master))
    workshop.addCommand(CheckAssemblyCommand(machine))
    workshop.addCommand(CoverMaterialCommand(machine))
    # запускаем процесс сборки кресла
    workshop.create()
