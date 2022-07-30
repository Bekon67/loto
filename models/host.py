from models.player import Player, Players
from models.card import Card
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
            next_keg = choice(bag.kegs)
        except IndexError:
            raise EmptyBagError
        else:
            bag.kegs.remove(next_keg)
            return next_keg

    def announces_results_round(self, players):  # объявить результат очередного круга   # объявить итоговый результат
        list_winner = [player for player in players if player.card.is_card_cross_out()]
        return list_winner
#TODO можно проверить, где накосячили человек и Валенок
    # def announces_remaining_numbers(self): # объявить отставшиеся бочонки в мешке ОНИ ИЗВЕСТНЫ!!!




