from models.cardrow import CardRow


class TestCardRow:
    def setup(self):
        line = [1, 17, None, 34, None, 56, None, None, 81]
        self.test_row = CardRow(line)

    def test_init(self):
        assert self.test_row
        assert self.test_row.cells
        assert self.test_row.cells[8].value == '81'
        assert str(self.test_row.cells[8]) == '81'
        assert self.test_row[8].value == '81'
        assert str(self.test_row[8]) == '81'
        assert self.test_row.cells[6].value == '  '
        assert str(self.test_row.cells[6]) == '  '
        assert self.test_row[6].value == '  '
        assert str(self.test_row[6]) == '  '
        assert not self.test_row.cells[8].is_cross_out
        assert not self.test_row[6].is_cross_out

    def test_cross_out(self):
        self.test_row[8].is_cross_out = True
        assert self.test_row[8].is_cross_out
        assert self.test_row[8].value == '81'
        assert str(self.test_row[8]) == '--'

    def test_is_row_cross_out(self):
        assert not self.test_row.is_row_cross_out()
        for cell in self.test_row:
            if str(cell) != '  ':
                cell.is_cross_out = True
        assert self.test_row.is_row_cross_out()
        self.test_row[7].is_cross_out = True
        assert not self.test_row.is_row_cross_out()
