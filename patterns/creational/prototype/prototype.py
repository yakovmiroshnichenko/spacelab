from abc import abstractmethod, ABC
# import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Chair(Prototype):
    def __init__(self, base_material, material, creation_time):
        self.base_material = base_material
        self.material = material
        self.creation_time = creation_time  # in hours

    def __str__(self):
        return f"- Base material: {self.base_material}\n- Sheathing material: {self.material}\n" \
               f"- Creation time: {self.creation_time}\n"

    def clone(self):
        return type(self)(self.base_material, self.material, self.creation_time)


if __name__ == '__main__':
    print("Chair number 1:")
    chair1 = Chair("Plastic", "Fabric", "4")
    print(chair1)

    print("\nChair number 2:")
    chair2 = chair1.clone()
    chair2.base_material = "Iron"
    chair2.material = "Leather"
    print(chair2)
    print(id(chair1), id(chair2))
