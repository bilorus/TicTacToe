import pytest

from TicTacToe import Cell, TicTacToe


def test_Cell_bool():
    c = Cell()
    assert bool(c) == True
    c.value = 1
    assert bool(c) == False
    c.value = 2
    assert bool(c) == False


def test_TicTacToe__init__():
    t = TicTacToe()
    assert len(t.pole) == 3, 'rows'
    for row in t.pole:
        assert len(row) == 3, 'cols'
    for i in range(3):
        for j in range(3):
            assert type(t.pole[i][j]) == Cell, 'all items are Cells'
            assert t.pole[i][j].value == 0
            assert t.pole[i][j].is_free == True


def test_check_index():
    check = TicTacToe._TicTacToe__check_index
    assert check((0, 0)) == None, 'OK coordinates'
    assert check((1, 1)) == None, 'OK coordinates'
    assert check((2, 2)) == None, 'OK coordinates'
    assert check((0, 2)) == None, 'OK coordinates'
    assert check((2, 0)) == None, 'OK coordinates'
    assert check((2, 0)) == None, 'OK coordinates'


def test_check_index_raises():
    check = TicTacToe._TicTacToe__check_index
    with pytest.raises(IndexError):
        check((1,))
    with pytest.raises(IndexError):
        check((1, 2, 3))
    with pytest.raises(IndexError):
        check((1, 3))
    with pytest.raises(IndexError):
        check((-2, -1))
    with pytest.raises(IndexError):
        check((3, 0))


def test_getitem():
    t = TicTacToe()
    assert t[0, 0] == 0


def test_setitem():
    t = TicTacToe()
    t[1, 1] = 1
    assert t[1, 1] == 1


if __name__ == '__main__':
    pytest.main()
