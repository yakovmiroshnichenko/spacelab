class MyDBBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyDBBaseClass, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


class MyDataBase(metaclass=MyDBBaseClass):
    def __init__(self):
        self.name = "DataBase"
        self.value_a = 3
        self.value_b = 5

    def add_a_b(self) -> int:
        return self.value_a+self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    my_db1 = MyDataBase()
    my_db2 = MyDataBase()
    print("DataBase name: " + my_db1.get_name())
    my_db1.set_name("New DataBase")
    print("DataBase2 name: " + my_db2.get_name())
    print(my_db1)
    print(my_db2)
    my_db2.value_b = 3
    print(my_db2.value_b, my_db1.value_b)
    print(my_db1.add_a_b())
    print(id(my_db1) == id(my_db2))
