import random

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
                item.value = self.FREE_CELL
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
                cell.value = self.HUMAN_X
                cell.is_free = False
                break
            else:
                print('Клетка занята')

    def computer_go(self):
        while True:
            row = random.choice(self.pole)
            cell = random.choice(row)
            if cell:
                cell.value = self.COMPUTER_O
                cell.is_free = False
                break
            else:
                continue

    def _win_check(self, player):
        for row in self.pole:
            if all(map(lambda item: item.value == player, row)):
                return True
        for col in range(3):
            column = (self.pole[0][col], self.pole[1][col], self.pole[2][col])
            if all(map(lambda x: x.value == player, column)):
                return True
        gd = tuple(self.pole[i][i] for i in range(3))
        pd = tuple(self.pole[i][2 - i] for i in range(3))
        if all(map(lambda item: item.value == player, gd)) or all(map(lambda item: item.value == player, pd)):
            return True
        return False

    @property
    def is_human_win(self):
        return self._win_check(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self._win_check(self.COMPUTER_O)

    @property
    def is_draw(self):
        all_elem = (x for row in self.pole for x in row)
        if all(map(lambda item: item.is_free is False, all_elem)):
            return True
        return False

    def __bool__(self):
        if self.is_draw or self.is_human_win or self.is_computer_win:
            return False
        return True
