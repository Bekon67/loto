from models.cardcell import CardCell
from models.cardrow import CardRow


class TestCardRow:
    def test_init(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        test_row = CardRow(line)
        assert test_row.cells[0].value == ' 1'
        assert str(test_row.cells[0]) == ' 1'
        assert test_row.cells[6].value == '  '
        assert str(test_row.cells[6]) == '  '

    def setup(self):
        self.cells = [CardCell(item) for item in [1, 17, None, 34, None, 56, None, None, 81]]

    def test_cross_out(self):
        # line = [1, 17, None, 34, None, 56, None, None, 81]
        # test_row = CardRow(line)
        assert self.cells[8].value == '81'
        assert str(self.cells[8]) == '81'
        self.cells[8].is_cross_out = True
        assert self.cells[8].is_cross_out
        assert self.cells[8].value == '81'
        assert str(self.cells[8]) == '--'

    def test_is_row_cross_out(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        test_row = CardRow(line)
        assert not test_row.is_row_cross_out()
        test_row.cells[0].is_cross_out = True
        test_row.cells[1].is_cross_out = True
        test_row.cells[3].is_cross_out = True
        test_row.cells[5].is_cross_out = True
        assert not test_row.is_row_cross_out()
        test_row.cells[8].is_cross_out = True
        assert test_row.is_row_cross_out()
