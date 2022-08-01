from models.cardrow import CardRow
import random


class Card:

    def __init__(self):
        # генерируем по при случайных числа в каждом десятке
        numbers = [random.sample(range(1 + 10 * i, 10 + 10 * i), k=3) for i in range(9)]
        # распределяем по трем строкам
        rows = [[numbers[k][i] for k in range(9)] for i in range(3)]
        for i in range(len(rows)):  # В каждой строке четыре случайных ячейки заменяем None
            list_index_none = random.sample(range(9), k=4)
            for k in list_index_none:
                rows[i][k] = None
        self.rows = [CardRow(item) for item in rows]

    def __getitem__(self, item):
        return self.rows[item]


    def printcard(self):  # вывод карточки в терминал
        print('*' * 27)
        print(*self.rows[0])
        print(*self.rows[1])
        print(*self.rows[2])
        print('*' * 27)

    def is_card_cross_out(self):  # полное заполнение карточки
        count = 0
        for k in range(3):
            if self.rows[k].is_row_cross_out():
                count += 1
        return count == 3


if __name__ == '__main__':
    # генерируем по при случайных числа в каждом десятке
    # распределяем по трем строкам

    numbers = [random.sample(range(1 + 10 * i, 10 + 10 * i), k=3) for i in range(9)]
    rows = [[numbers[k][i] for k in range(9)] for i in range(3)]
    print(rows)

    for i in range(len(rows)):
        # list_index_none = random.sample(range(9), k=4)
        # print(list_index_none)
        for k in random.sample(range(9), k=4):
            rows[i][k] = None
    print(rows)
    rows_test = [CardRow(item) for item in rows]
    print('*' * 27)
    print(*rows_test[0])
    print(*rows_test[1])
    print(*rows_test[2])
    print('*' * 27)
    print('X' * 27)

    card = Card()
    print(type(card[0]))
    print('*' * 27)
    print(*card[0])
    print(*card[1])
    print(*card[2])
    print('*' * 27)
    card.printcard()

    print('O' * 27)
    for cell in card[0]:
        if cell.value != '  ':
            print(cell)
            cell.is_cross_out = True
            print(cell)

    print(card[0].is_row_cross_out())

    print('T' * 27)
    card[0].cells[3].is_cross_out = True
    card[1].cells[5].is_cross_out = True
    print('*' * 27)
    print(*card[0])
    print(*card[1])
    print(*card[2])
    print('*' * 27)
    card.printcard()

    print(card[0].is_row_cross_out())
    card[0].cells[0].is_cross_out = True
    card[0].cells[1].is_cross_out = True
    card[0].cells[2].is_cross_out = True
    card[0].cells[4].is_cross_out = True
    card[0].cells[5].is_cross_out = True
    card[0].cells[6].is_cross_out = True
    card[0].cells[7].is_cross_out = True
    card[0].cells[8].is_cross_out = True
    card.printcard()
    print(card[0].is_row_cross_out())
    card[0].cells[5].is_cross_out = False
    card[0].cells[6].is_cross_out = False
    card[0].cells[7].is_cross_out = False
    card[0].cells[8].is_cross_out = False
    card.printcard()
    print(card[0].is_row_cross_out())
