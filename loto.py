from models.cardcell import CardCell
from models.cardrow import CardRow
from models.card import Card
from models.keg import Keg
from models.bag import Bag
from models.host import Host
from models.player import Player
from random import choices

host = Host(input('Введтите имя ведущего: '))
count_players = int(input('Введите количество участников: '))
players = []
for i in range(count_players):
    players.append(Player(input(f'Введите имя {i + 1}-го игрока: '),
                   int(input(f'Введите тип {i + 1}-го игрока: '))))
    print(f'{players[i].name}, это Ваша карточка:')
    players[i].card.printcard()
bag = Bag(90)
list_winner = []
while not list_winner:
    keg = host.get_next_keg(bag)
    print(f'Достали бочонок {keg}!')
    for player in players:
        print(keg)
        player.card.printcard()
        if player.profile == 1:
            answer = 'да'
            # print('Ура! Имеется')
        elif player.profile == 2:
            answer = input('У Вас в карточке есть это число? (да/нет): ')
        else:
            answer = choices(['да', 'нет'], weights=[0.9, 0.1], k=1)[0]
        print(answer)
        for row in player.card.rows:
            for cell in row.cells:
                if str(cell) == str(keg) and answer == 'да':
                    cell.cross_out(keg)
        player.card.printcard()
    list_winner = host.announces_results_round(players)
print('Победитель:' if len(list_winner) == 1 else 'Победители:')

print(*list_winner)
print(f'Количество оставшихся в мешке бочонков - {len(bag)}:')
print(*bag)
# list_mistakes = host.mistakes_players(players, bag)
# # print(list_mistakes)
#
# for player in players:
#     if list_mistakes[player]:
#         print(f'{player} не зачеркнул {list_mistakes[player]}')

# data = random.choices(values, weights=[0.2, 0.3, 0.5], k=1000)
