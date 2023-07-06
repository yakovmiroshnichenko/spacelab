from abc import ABCMeta, abstractmethod


class IWorker(metaclass=ABCMeta):
    """Абстрактный класс с обязанности рабочих"""

    @abstractmethod
    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        pass


class AbsWorker(IWorker):
    """Абстрактный класс реализующий интерфейс IWorker"""

    def __init__(self):
        self.__next_worker: IWorker = None

    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        self.__next_worker = worker
        return worker

    def execute(self, command: str) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        return ''


class Designer(AbsWorker):
    """Класс конкретного работника (Проектировщик)"""

    def execute(self, command: str) -> str:
        if command == 'design a chair':
            return 'The designer executed the command: ' + command
        else:
            return super().execute(command)


class Mechanic(AbsWorker):
    """Класс конкретного работника (Слесарь)"""
    def execute(self, command: str) -> str:
        if command == 'сreate a chair base':
            return 'The mechanic executed the command: ' + command
        else:
            return super().execute(command)


class Carpenter(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'sheathe an armchair':
            return 'The carpenter executed the command: ' + command
        else:
            return super().execute(command)


def give_command(worker: IWorker, command: str):
    string: str = worker.execute(command)
    if string == '':
        print(command + ' - there are no necessary specialists')
    else:
        print(string)


if __name__ == '__main__':
    designer = Designer()
    mechanic = Mechanic()
    carpenter = Carpenter()

    designer.set_next_worker(mechanic).set_next_worker(carpenter)

    give_command(designer, 'design a chair')
    give_command(designer, 'сreate a chair base')
    give_command(designer, 'sheathe an armchair')
    give_command(designer, 'add chair adjustment')
