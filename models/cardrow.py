from models.cardcell import CardCell


class CardRow:

    # инициализация
    def __init__(self, line):
        self.cells = [CardCell(item) for item in line]

    def __getitem__(self, item):
        return self.cells[item]

    def is_all_cross_out(self):  # полное заполнение строки
        count = 0
        for k in self.cells:
            if str(k) == '--':
                count += 1
        return count == 5


if __name__ == '__main__':
    test_row = CardRow([1, 17, None, 34, None, 56, None, None, 81])
    test_row2 = CardRow([None, 19, None, 39, None, 52, None, 79, 83])
    test_row3 = CardRow([7, None, 29, None, 43, 56, None, 77, None])

    print(len(test_row.cells))
    print(range(len(test_row.cells)))

    print('*' * 100)
    print(*test_row.cells)
    print(*str(test_row.cells))
    print('*' * 100)

    print(type(test_row), test_row)
    print(type(test_row.cells[1].value), test_row.cells[1].value)
    print(type(test_row.cells[1].is_cross_out), test_row.cells[1].is_cross_out)

    print(type(test_row[0]), test_row[0])
    print(type(test_row.cells[0]), test_row.cells[0])

    print('*' * 27)
    print(*test_row)
    print(*test_row2)
    print(*test_row3)
    print('*' * 27)

    test_row.cells[3].is_cross_out = True
    test_row.cells[5].is_cross_out = True

    print('*' * 27)
    print(*test_row)
    print(*test_row2)
    print(*test_row3)
    print('*' * 27)

    for l in test_row.cells:
        print(l)
