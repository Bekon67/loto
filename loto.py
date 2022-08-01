from models.cardcell import CardCell
from models.cardrow import CardRow
from models.card import Card
from models.keg import Keg
from models.bag import Bag
from models.host import Host
from models.player import Player

host = Host(input('Введтите имя ведущего: '))
count_players = int(input('Введите количество участников: '))
players = []
for i in range(count_players):
    players.append(Player(input(f'Введите имя {i+1}-го игрока: ')))
    print(f'{players[i].name}, это Ваша карточка:')
    players[i].card.printcard()
bag = Bag(90)
game_over = False
# while not game_over:
#     keg = host.get_next_keg(bag)
#     for player in players:
#         player.card.printcard()
#         if str(keg) in player.card:
#             print(player.card.index(str(keg)))