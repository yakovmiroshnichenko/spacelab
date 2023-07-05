class ChairFlyweight:
    def __init__(self, type, material, color):
        self._type: str = type
        self._material: str = material
        self._color: str = color

    def __str__(self):
        return f"Type: {self._type}\nMaterial: {self._material}\nColor: {self._color}"


class ChairFactory:
    def __init__(self):
        self.chairs = {}

    def get_car(self, type, material, color):
        if (type, material, color) not in self.chairs:
            self.chairs[(type, material, color)] = ChairFlyweight(type, material, color)
        return self.chairs[(type, material, color)]


if __name__ == '__main__':
    factory = ChairFactory()

    chair1 = factory.get_car("Office", "Leather", "Black")
    chair2 = factory.get_car("Office", "Leather", "Black")
    print("Chair #1:\n" + str(chair1))
    print("ID:" + str(id(chair1)))

    print()

    print("Chair #2:\n" + str(chair2))
    print("ID:" + str(id(chair2)))

    print()
    print(factory.chairs)