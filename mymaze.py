import random
import logging
import sys

logging.getLogger(__name__)


class Maze:

    def __init__(self):
        self.mapa: list = [
            [False, False, False, False, True, True, True, True],
            [False, False, True, False, False, True, False, False],
            [False, True, True, True, False, True, True, False],
            [True, True, False, True, True, True, False, False]
        ]
        self.road_position: list = [(x, y) for x in range(4) for y in range(8) if self.mapa[x][y]]
        self.key_position: tuple = (1, 2)
        self.safe_position: list = [(0, 4), (2, 6), (1, 2), (7, 0)]

    def generate_fire(self) -> list:
        """Генерация клеток с огнём"""
        random.shuffle(self.road_position)
        dangerous_cells = [f for f in self.road_position if f not in self.safe_position]
        fire_cells = dangerous_cells[:4]
        logging.info(f"\nКоординаты клеток с огнём:{fire_cells}\n")
        return fire_cells


class Hero:
    maze = Maze()

    def __init__(self, name, x=3, y=0, has_key=False, lives=5, heals=3):
        self.name: str = name
        self.x: int = x
        self.y: int = y
        self.has_key = has_key
        self.lives: int = lives
        self.max_lives: int = 5
        self.heals: int = heals
        self.next_x: int = x
        self.next_y: int = y
        self.prev_x: int = x
        self.prev_y: int = y
        self.h: list = []

    def move(self):
        """Передвижение героя"""
        logging.info("Введите направление движения (up, down, left, right):")
        match input():
            case 'up':
                self.next_x -= 1
                self.check_move()
                return True
            case 'left':
                self.next_y -= 1
                self.check_move()
                return True
            case 'down':
                self.next_x += 1
                self.check_move()
                return True
            case 'right':
                self.next_y += 1
                self.check_move()
                return True
            case _:
                logging.info("Недоступное направление движения, возврат к выбору команды")
                return False

    def check_move(self):
        """Проверка передвижения героя"""
        if (self.next_x, self.next_y) == (self.prev_x, self.prev_y):
            logging.info(f"Герой {self.name} испугался и побежал к началу лабиринта, но попал в ловушку.")
            self.lives = 0
            return None
        if (self.next_x, self.next_y) == (0, 7):
            if self.has_key:
                logging.info(f"\nГерой {self.name} победил голема и вышел из лабиринта!")
                sys.exit()
            else:
                logging.info(f"\n Героя {self.name} съел голем.")
                self.lives = 0
        try:
            if self.next_x < 0 or self.next_y < 0 or self.maze.mapa[self.next_x][self.next_y] is not True:
                logging.info(f"Стена, герой {self.name} потерял жизнь.")
                self.lives -= 1
                self.next_x, self.next_y = self.x, self.y
            else:
                if (self.next_x, self.next_y) in self.maze.safe_position or (self.x, self.y) in self.maze.safe_position:
                    self.x, self.y = self.next_x, self.next_y
                else:
                    self.prev_x, self.prev_y = self.x, self.y
                    self.x, self.y = self.next_x, self.next_y
        except IndexError:
            logging.info(f"Стена, герой {self.name} потерял жизнь.")
            self.lives -= 1
            self.next_x, self.next_y = self.x, self.y
            return
        if (self.x, self.y) == (2, 6) or (self.x, self.y) == (0, 4):
            logging.info(f"{self.name} на клетке лечения, здоровье полностью восстановлено.")
            self.lives = 5
        if (self.x, self.y) == self.maze.key_position:
            logging.info(f"Герой {self.name} обнаружил ключ!")

    def heal(self):
        """Лечение героя"""
        if self.heals != 0 and self.lives != self.max_lives:
            self.lives += 1
            self.heals -= 1
            logging.info(
                f"Герой {self.name} использовал аптечку. "
                f"Теперь у {self.name} {self.lives} жизней и {self.heals} аптечки.")
            return 'win'
        if self.heals == 0:
            logging.info("Аптечки закончились.")
            return False
        if self.lives == self.max_lives:
            logging.info("У героя максимальное здоровье, выберите другое действие:")
            return False

    def pick(self):
        """Подъем ключа"""
        if (self.x, self.y) == self.maze.key_position:
            self.has_key = True
            logging.info(f"{self.name} поднял ключ.")
            self.maze.key_position = (0, 0)
            return True
        else:
            return False


class Game:
    maze = Maze()

    def __init__(self):
        self.heroes = {}
        self.dead_heroes = []

    def start_game(self):
        """Начало игры, ввод имён"""
        logging.info("Введите количество героев:")
        try:
            amount = int(input())
            for i in range(amount):
                logging.info(f"Введите имя героя №{i + 1}:")
                hero_name: str = input()
                if hero_name in self.heroes.keys():
                    logging.info("Данное имя занято! Введите другое имя героя(герои-дубликаты будут удалены):")
                    hero_name = input()
                    self.heroes[hero_name] = Hero(name=hero_name)
                else:
                    self.heroes[hero_name] = Hero(name=hero_name)
        except ValueError:
            logging.critical('Недопустимое значения, попробуйте снова.')
            sys.exit()

        while True:
            """Начало нового хода, герои ходят по очереди."""
            for hero in self.heroes.values():
                if len(self.dead_heroes) == len(self.heroes):
                    logging.info(f"Все герои погибли, игра окончена!")
                    return False
                if hero.name in self.dead_heroes:
                    continue
                if hero.lives <= 0:
                    if hero.has_key:
                        hero.maze.key_position = hero.x, hero.y
                    logging.info(f"Герой {hero.name} погиб!")
                    self.dead_heroes.append(hero.name)
                    continue
                fire_cells = self.maze.generate_fire()
                hero_here_list = []
                for h in self.heroes.values():
                    if h != hero and (hero.x, hero.y) == (h.x, h.y) and h.lives != 0:
                        logging.info(f"Герой {h.name} находится на этой клетке.")
                        hero_here_list.append(h)
                logging.info(f"Ходит герой: {hero.name}\n"
                             f"Количество жизней: {hero.lives}\n"
                             f"Координаты героя {hero.name}: {(hero.x, hero.y)}\n")
                if (hero.x, hero.y) == hero.maze.key_position:
                    logging.info("Ключ здесь")
                logging.info("Выберите действие. Для справки введите 'rules'")
                while True:
                    """Выбор действия"""
                    active = input()
                    match active:
                        case 'rules':
                            logging.info("Доступные команды: move, attack, heal, pick\n"
                                         "Команда 'move' даёт возможность передвигается по карте лабиринта.\n"
                                         "Команда 'attack' позволяет выбрать определённого героя и атаковать его.\n"
                                         "Команда 'pick' для поднятия ключа(если он находится в клетке с героем).\n"
                                         "Команда 'heal' добавляет герою одну жизни(Максимум 3 раза за игру).\n"
                                         "Герой не может пропустить ход.\n"
                                         "Выберите действие:")

                        case 'move':
                            if hero.move():
                                if (hero.x, hero.y) in fire_cells:
                                    logging.info(f"Герой {hero.name} попал на клетку с огнём и потерял одну жизнь.")
                                    hero.lives -= 1
                                break
                            else:
                                continue
                        case 'attack':
                            if self.attack(hero):
                                break
                            else:
                                continue
                        case 'heal':
                            if hero.heal():
                                break
                            else:
                                continue
                        case 'pick':
                            if hero.pick():
                                break
                            else:
                                logging.info("На этой клетке нет ключа, выберите другое действие!")
                                continue
                        case _:
                            logging.info("Недоступное действие!")

                if hero.lives <= 0:
                    """Проверяем, жив ли герой."""
                    if hero.has_key:
                        hero.maze.key_position = hero.x, hero.y
                    logging.info(f"Герой {hero.name} погиб!")
                    self.dead_heroes.append(hero.name)
                    continue

    def attack(self, hero):
        """Атака других героев"""
        hero_here_list: list = []
        for h in self.heroes.values():
            if h != hero and (hero.x, hero.y) == (h.x, h.y) and h.lives != 0:
                hero_here_list.append(h)
        targets: list = []
        for h in hero_here_list:
            if h != hero:
                targets.append(h.name)
        if len(targets):
            while True:
                logging.info(f"Для атаки доступны: {targets}")
                choise = input()
                if choise not in targets:
                    logging.error(f"Героя нет в списке для атаки, выберите из доступных!")
                    continue
                else:
                    for target in hero_here_list:
                        if choise == target.name:
                            target.lives -= 1
                            logging.info(f"{hero.name} ударил героя {target.name} и {target.name} потерял 1 жизнь.")
                            return True
                break
        else:
            logging.error(f"Нет целей для атаки, выберите другое действие!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    game = Game()
    game.start_game()
