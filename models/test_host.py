from pytest import raises
from models.host import Host, EmptyBagError
from models.player import Player
from models.card import Card
from models.cardrow import CardRow


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

            # def announces_results_round(self,
            #                             players):  # объявить результат очередного круга   # объявить итоговый результат
            #     list_winner = [player for player in players if player.card.is_card_cross_out()]
            #     return list_winner

    def test_announces_results_round(self):
        list_players = [Player('one'), Player('two')]
        list_winner = self.test_host.announces_results_round(list_players)
        assert not list_winner
        count = 0
        for player in list_players:
            count += 1
            assert not player.card.is_card_cross_out()
            for k in range(3):
                assert not player.card.is_card_cross_out()
                for cell in player.card[k]:
                    if cell.value != '  ':
                        assert not player.card[k].is_row_cross_out()
                        cell.is_cross_out = True
                assert player.card[k].is_row_cross_out()
            assert player.card.is_card_cross_out()
            list_winner = self.test_host.announces_results_round(list_players)
            assert list_winner
            assert len(list_winner) == count
            assert player.name in list_winner

    # def mistakes_players(self, players, bag):  # проверка, где накосячили человек и Валенок
    #     dict_mistake = {}
    #     for player in players:
    #         mistake_player = []
    #         for keg in test_bag:
    #             for row in player.card.rows:
    #                 for cell in row.cells:
    #                     if str(cell) == str(keg):
    #                         mistake_player.append(keg.number)
    #         dict_mistake[player] = mistake_player
    #     return dict_mistake

    def test_mistakes_players(self):
        list_players = [Player('one'), Player('two')]


