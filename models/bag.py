from models.keg import Keg
class Bag:

    инциализация
    наполнить мешок бочонками
    уменьшить количество бочонков в мешке на один при извлечении


    def __init__(self, count):
        self.kegs = list(range(1, count + 1))

    def __len__(self):
        return len(self._numbers)

    def get_random_numbers(self, count):
        result = random.sample(self._numbers, count)
        return result

    def get_next_number(self):
        try:
            result = random.choice(self._numbers)
        except IndexError:
            raise EmptyBagError
        else:
            self._numbers.remove(result)
            return result
