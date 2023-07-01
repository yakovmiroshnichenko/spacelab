from abc import ABC, abstractmethod


class LengthM(ABC):

    @abstractmethod
    def get_length(self) -> int:
        pass

    @abstractmethod
    def set_length(self, lh: int) -> None:
        pass


class LengthCM(ABC):

    @abstractmethod
    def get_length_in_centimeters(self) -> int:
        pass


class Table(LengthM):
    def __init__(self, lh) -> None:
        self.length = lh

    def set_length(self, lh: int) -> None:
        self.length = lh

    def get_length(self) -> int:
        return self.length


class AdapterLength(LengthCM):
    def __init__(self, original_length: LengthM):
        self.original_length = original_length
        self.length = self.convert_length()

    def convert_length(self) -> int:
        return self.original_length.get_length() * 100

    def get_length_in_centimeters(self) -> int:
        return self.length


if __name__ == '__main__':
    table_length = Table(15)  # in meters
    table_length_in_centimeters = AdapterLength(table_length)
    print("Table length in meters: " + str(table_length.get_length()))
    print("~~~~~~~~~~~~~")
    print("Table length in centimeters: " + str(table_length_in_centimeters.get_length_in_centimeters()))
