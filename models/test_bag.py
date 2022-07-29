from models.keg import Keg
from models.bag import Bag


class TestBag:

    def test_init(self):
        test_bag = Bag(90)
        assert test_bag
        assert len(test_bag) == 90

    #
    # def __len__(self):
    #     return len(self._numbers)
    #
    # def get_random_numbers(self, count):
    #     result = random.sample(self._numbers, count)
    #     return result
    #
    # def get_next_number(self):
    #     try:
    #         result = random.choice(self._numbers)
    #     except IndexError:
    #         raise EmptyBagError
    #     else:
    #         self._numbers.remove(result)
    #         return result
