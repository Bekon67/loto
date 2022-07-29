from models.keg import Keg


class TestKeg:

    def test_init(self):
        keg_1 = Keg(1)
        keg_15 = Keg(15)
        assert keg_1.number == 1
        assert keg_15.number == 15

    def setup(self):
        self.keg = Keg(40)
