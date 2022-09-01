class Cell:
    """
    Object for game pole in class TicTacToe
    """
    def __init__(self):
        self.value = 0  # 1 == x, 2 == 0
        self.is_free = True

    def __bool__(self):
        return self.is_free



