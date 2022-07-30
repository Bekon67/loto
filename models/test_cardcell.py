from models.cardcell import CardCell
from models.keg import Keg


class TestCardCell:
    def setup(self):
        self.cell_39 = CardCell(39)
        self.cell_40 = CardCell(40)
        self.cell_none = CardCell(None)
        self.keg_39 = Keg(39)
        self.keg_40 = Keg(40)

    def test_init(self):
        assert self.cell_none.value == '  '
        assert not self.cell_none.is_cross_out
        assert self.cell_39.value == '39'
        assert not self.cell_39.is_cross_out

    def test_get_number(self):
        assert self.cell_40.value == '40'
        assert not self.cell_40.is_cross_out
        self.cell_40.is_cross_out = True
        assert self.cell_40.value == '40'

    def test_cross_out(self):
        self.cell_40.cross_out(self.keg_40.number)
        assert self.cell_40.is_cross_out
        assert not self.cell_39.is_cross_out
