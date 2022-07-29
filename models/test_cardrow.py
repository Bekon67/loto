# from models.bag import Bag
# from models.card import Card
from models.cardcell import CardCell

from models.cardrow import CardRow
# from models.host import Host
from models.keg import Keg


# from models.player import Player

class TestCardRow:
    def test_init(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        test_row = CardRow(line)
        assert test_row.cells[0].value == ' 1'
        assert str(test_row.cells[0]) == ' 1'
        assert test_row.cells[6].value == '  '
        assert str(test_row.cells[6]) == '  '

        # assert test_row.cells == [' 1', '17', '  ', '34', '43', '56', '  ', '77', '81']

    def test_cross_out(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        test_row = CardRow(line)
        assert test_row.cells[8].value == '81'
        assert str(test_row.cells[8]) == '81'
        test_row.cells[8].is_cross_out = True
        assert test_row.cells[8].is_cross_out
        assert test_row.cells[8].value == '81'
        assert str(test_row.cells[8]) == '--'

    def test_is_all_cross_out(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        test_row = CardRow(line)
        assert not test_row.is_all_cross_out()
        test_row.cells[0].is_cross_out = True
        test_row.cells[1].is_cross_out = True
        test_row.cells[3].is_cross_out = True
        test_row.cells[5].is_cross_out = True
        assert not test_row.is_all_cross_out()
        test_row.cells[8].is_cross_out = True
        assert test_row.is_all_cross_out()

