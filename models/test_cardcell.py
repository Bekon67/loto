# from models.bag import Bag
# from models.card import Card
from models.cardcell import CardCell


# from models.cardrow import CardRow
# from models.host import Host
from models.keg import Keg
# from models.player import Player


class TestCardCell:

    def test_init(self):
        cell_none = CardCell(None)
        assert cell_none.value == '  '
        assert not cell_none.is_cross_out
        cell_25 = CardCell(25)
        assert cell_25.value == '25'
        assert not cell_25.is_cross_out

    def setup(self):
        self.cell_39 = CardCell(39)
        self.cell_40 = CardCell(40)
        self. keg_40 = Keg(40)

    def test_get_number(self):
        assert self.cell_40.value == '40'
        assert not self.cell_40.is_cross_out
        self.cell_40.is_cross_out = True
        assert self.cell_40.value == '40'

    def test_cross_out(self):
        self.cell_40.cross_out(40)
        assert self.cell_40.is_cross_out
        assert not self.cell_39.is_cross_out

#
# if __name__ == '__main__':
#     pass
