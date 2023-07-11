from typing import List
from collections.abc import Iterable, Iterator


class ChairItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кресло под номером: {self.number}"


class ChairIterator(Iterator):
    def __init__(self, chair: List[ChairItem],
                 reverse: bool = False):
        self._chair = chair
        self._index: int = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self) -> ChairItem:
        try:
            chair_item = self._chair[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return chair_item


class ChairGroup(Iterable):
    def __init__(self, amount_chairs: int = 10):
        self._chairs = [ChairItem(it+1) for it in range(amount_chairs)]
        print(f"Ряд состоит из "
              f"{amount_chairs} кресел")

    def amount_chairs(self) -> int:
        return len(self._chairs)

    def __iter__(self) -> ChairIterator:
        return ChairIterator(self._chairs)

    def get_reverse_iterator(self) -> ChairIterator:
        return ChairIterator(self._chairs, True)


if __name__ == "__main__":
    chairs = ChairGroup(5)
    for item in chairs:
        print("Это " + str(item))
    print("*" * 8 + "Обход в обратную сторону" + "*" * 8)
    iterator = chairs.get_reverse_iterator()
    for item in iterator:
        print("Это " + str(item))
