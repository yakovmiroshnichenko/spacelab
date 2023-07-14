from typing import List


class Memento:
    """Класс Хранитель, фиксирующий
    текущие модификации кресла"""

    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Chair:
    """Класс изделия(кресла)"""

    def __init__(self):
        self.__state: List[str] = ['base']

    def add_element(self, element: str) -> None:
        print(f"Добавлен элемент: {element}")
        self.__state.append(element)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Текущее состояние: {self.__state}"


class Master:
    def __init__(self, chairs: Chair):
        self.chair = chairs
        self.chair_states: List[Memento] = []

    def add_element_to_chair(self, element: str):
        self.chair_states.append(self.chair.create_memento())
        self.chair.add_element(element)

    def undo_add_element(self):
        if len(self.chair_states) == 1:
            self.chair.set_memento(self.chair_states[0])
            print("Кресло вернулось в своё исходное состояние!")
            print(self.chair)
        else:
            print("Отмена предыдущего действия")
            state = self.chair_states.pop()
            self.chair.set_memento(state)
            print(self.chair)


if __name__ == "__main__":
    chair = Chair()
    master = Master(chair)
    print(chair)
    print("*" * 8 + "Добавляем элементы:" + 8 * "*")
    master.add_element_to_chair('стразы')
    master.add_element_to_chair('подголовник')
    master.add_element_to_chair('держатель стакана')
    print(chair)
    print("*" * 4 + "Отменяем произведенные ранее действия" + 4 * "*")
    master.undo_add_element()
    master.undo_add_element()
    master.undo_add_element()
    print("*" * 5 + "Вновь добавляем элементы:" + 5 * "*")
    master.add_element_to_chair('регулятор высоты')
    master.add_element_to_chair('сетка МЕШ')
    print(chair)
