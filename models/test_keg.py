from pytest import raises
from models.keg import Keg


class TestKeg:

    def setup(self):
        # 40
        self.keg = Keg(40)

    def test_init(self):
        # 1, 2, 3
        assert self.keg.number == 40
