from models.keg import Keg


class Bag:
    def __init__(self, count):
        self.kegs = [Keg(item) for item in range(1, count + 1)]

    def __len__(self):
        return len(self.kegs)

    def __getitem__(self, item):
        return self.kegs[item]
