from models.keg import Keg
from collections import Counter


class Bag:
    def __init__(self, count):
        self.kegs = [Keg(item) for item in range(1, count + 1)]

    def __len__(self):
        return len(self.kegs)

    def __getitem__(self, item):
        return self.kegs[item]


if __name__ == '__main__':
    bag_90 = Bag(90)
    print(*bag_90)
    bag_2 = Bag(2)

    print(*bag_2)
    bag_89 = Bag(89)
    # bag = list((Counter(bag_90) - Counter(bag_2)).elements())
    bag = set(bag_90) - set(bag_89)
    print(*bag)
    # df = 2 - 4
    array_1 = ['one', 'two']
    array_2 = ['one', 'two', 'one', 'three', 'four']
    array_3 = list((Counter(array_2) - Counter(array_1)).elements())

    print(array_3)
