from models.keg import Keg


class TestKeg:
    def setup(self):
        self.keg = Keg(40)

    def test_init(self):
        keg_15 = Keg(15)
        assert keg_15.number == 15
        assert self.keg.number == 40



