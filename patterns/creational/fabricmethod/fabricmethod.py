from abc import ABC, abstractmethod
import logging
logging.getLogger(__name__)


class Furniture(ABC):
    @abstractmethod
    def release(self):
        pass


class Chair(Furniture):
    def release(self):
        logging.info("Выпущено кресло")


class Sofa(Furniture):
    def release(self):
        logging.info("Выпущен диван")


class FurnitureFactory(ABC):
    @abstractmethod
    def create(self) -> Furniture:
        pass


class ChairFactory(FurnitureFactory):
    def create(self):
        return Chair()


class SofaFactory(FurnitureFactory):
    def create(self):
        return Sofa()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    creator = ChairFactory()
    chair = creator.create()

    creator = SofaFactory()
    sofa = creator.create()

    chair.release()
    sofa.release()
