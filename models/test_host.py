from pytest import raises
from models.host import Host, EmptyBagError


class TestHost:
    def setup(self):
        name_host = 'Якубович'
        self.test_host = Host(name_host)
        self.test_bag = self.test_host.took_out_bag()
        self.count = 90

    def test_init(self):
        assert self.test_host
        assert self.test_host.name == 'Якубович'
        assert str(type(self.test_host.name)) == "<class 'str'>"

    def test_took_out_bag(self):
        assert self.test_bag
        assert len(self.test_bag) == 90
        assert self.test_bag.kegs[5].number == 6
        assert self.test_bag[5].number == 6
        with raises(IndexError):
            test = self.test_bag.kegs[91]
        with raises(IndexError):
            str(self.test_bag[92])

    def test_get_next_keg(self):
        next_keg = self.test_host.get_next_keg(self.test_bag)
        assert len(self.test_bag.kegs) == 89
        assert len(self.test_bag) == 89
        assert next_keg not in self.test_bag
        assert next_keg.number in range(1, self.count + 1)
        for _ in range(88):
            next_keg = self.test_host.get_next_keg(self.test_bag)
        assert len(self.test_bag) == 1
        next_keg = self.test_host.get_next_keg(self.test_bag)
        assert not len(self.test_bag)
        with raises(EmptyBagError):
            next_keg = self.test_host.get_next_keg(self.test_bag)
