from models.player import Player
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
        list_winner = [player.name for player in players if player.card.is_card_cross_out()]
        return list_winner

    def mistakes_players(self, players, bag):  # проверка, где накосячили человек и Валенок
        dict_mistake = {}
        for player in players:
            mistake_player = []
            for keg in bag:
                for row in player.card.rows:
                    for cell in row.cells:
                        if str(cell) == str(keg):
                            mistake_player.append(keg.number)
            dict_mistake[player] = mistake_player
        return dict_mistake

# def announces_remaining_numbers(self): # объявить отставшиеся бочонки в мешке ОНИ ИЗВЕСТНЫ!!!

# if __name__ in '__main__':
#     test_host = Host('Якубович')
#     test_bag = test_host.took_out_bag()
#     players = [Player('df'), Player('dde')]
#     list_mistakes = test_host.mistakes_players(players, test_bag)
#     # print(list_mistakes)
#
#     for player in players:
#         print(f'{player} не зачеркнул {list_mistakes[player]}')
