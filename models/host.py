from models.bag import Bag
from models.keg import Keg
from random import choice
from models.bag import Bag


class EmptyBagError(Exception):
    def __str__(self):
        return 'В мешке больше нет чисел'


class Host:
    def __init__(self, name):
        self.name = name

    def took_out_bag(self):  # достать мешок
        return Bag(90)

    def get_next_keg(self, bag):  # достать случайный бочонок
        try:
            result = choice(bag.kegs)
        except IndexError:
            raise EmptyBagError
        else:
            bag.kegs.remove(result)
            return result
    # объявить результат очередного круга
    # объявить итоговый результат
    # объявить отставшиеся бочонки в мешке
