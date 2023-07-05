from abc import ABCMeta, abstractmethod
from typing import Dict


class ISite(metaclass=ABCMeta):
    @abstractmethod
    def make_order(self, num: int) -> str:
        pass


class ChairWebSite(ISite):

    def make_order(self, num: int) -> str:
        return f'Заказ {num} принят в обработку'


class WebSiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def make_order(self, num: int) -> str:
        order: str = ''
        if self.__cache.get(num) is not None:
            order = self.__cache[num]
            order = 'Из кеша: ' + order
        else:
            order = self.__site.make_order(num)
            self.__cache[num] = order
        return order


if __name__ == '__main__':
    my_site: ISite = WebSiteProxy(ChairWebSite())

    print(my_site.make_order(1))
    print(my_site.make_order(2))
    print(my_site.make_order(3))

    print(my_site.make_order(2))
