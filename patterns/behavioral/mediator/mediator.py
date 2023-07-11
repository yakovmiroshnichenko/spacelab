from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, emp: "Employee", msg: str):
        pass


class Employee(metaclass=ABCMeta):
    def __init__(self, mediators: IMediator):
        self._mediator = mediators

    def set_mediator(self, med: IMediator):
        self._mediator = med


class Master(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__is_working = False

    def execute_work(self):
        print('<-Мастер в работе')
        self._mediator.notify(self, 'Мастер собирает кресло')

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print("<-Мастер освобождён от работы")
        else:
            print('<-Мастер занят')


class Director(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__text: str = ''

    def give_command(self, txt: str):
        self.__text = txt
        if txt == '':
            print("->Директор знает, что мастер уже работает")
        else:
            print("->Директор дал команду:" + txt)
        self._mediator.notify(self, txt)


class Controller(IMediator):
    def __init__(self, masters: Master, directors: Director):
        self.__master = masters
        self.__director = directors
        master.set_mediator(self)
        director.set_mediator(self)

    def notify(self, emp: "Employee", msg: str):
        if isinstance(emp, Director):
            if msg == '':
                self.__master.set_work(False)
            else:
                self.__master.set_work(True)
        if isinstance(emp, Master):
            if msg == 'Мастер собирает кресло':
                self.__director.give_command('')


if __name__ == '__main__':
    master = Master()
    director = Director()

    mediator = Controller(master, director)
    director.give_command("Собирать кресло")

    print("~~~~~~~~~~~")

    master.execute_work()
