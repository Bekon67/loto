from pytest import raises
from models.bag import Bag


class TestBag:
    def setup(self):
        self.count = 90
        self.test_bag = Bag(self.count)

    def test_init(self):
        assert self.test_bag
        assert len(self.test_bag.kegs) == 90

    def init_item(self):
        assert self.test_bag.kegs[5].number == 6
        assert self.test_bag.kegs[5] == 6  # TODO Почему? В Host такой тест не проходит
        assert self.test_bag[5].number == 6
        assert self.test_bag[5] == 6  # TODO Почему? В Host такой тест не проходит
        with raises(IndexError):
            str(self.test_bag.kegs[91])
        with raises(IndexError):
            str(self.test_bag[92])

    def test_len(self):
        assert len(self.test_bag.kegs) == 90
        assert len(self.test_bag) == 90
