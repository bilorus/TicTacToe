from class_Cell import Cell


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    @staticmethod
    def __check_index(indx):
        if any(map(lambda x: type(x) is not int or x not in (0, 1, 2), indx)):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False

    def init(self):
        for row in self.pole:
            for item in row:
                item.value = 0
                item.is_free = True

    def show(self):
        for i, row in enumerate(self.pole):
            for j, item in enumerate(row):
                print(item.value, end='')
                print(' | ' if j != 2 else '\n', end='')
            print('─────────' if i != 2 else '')

    def human_go(self):
        while True:
            coords = tuple(map(int, input('Введите координаты для Х через пробел: ').split()))
            cell = self.pole[coords[0]][coords[1]]
            if cell:
                cell.value = 1
                cell.is_free = False
                break
            else:
                print('Клетка занята')


