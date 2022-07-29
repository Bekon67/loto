from models.keg import Keg


class Bag:
    #
    #    наполнить мешок бочонками
    # уменьшить количество бочонков в мешке на один при извлечении

    def __init__(self, count):
        self._kegs = list(range(1, count + 1))

    def __len__(self):
        return len(self._kegs)

    # def get_random_numbers(self, count):
    #     result = random.sample(self._kegs, count)
    #     return result

    def get_next_number(self):
        try:
            result = random.choice(self._kegs)
        except IndexError:
            raise EmptyBagError
        else:
            self._kegs.remove(result)
            return result
