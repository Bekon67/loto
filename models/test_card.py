from pytest import raises

from models.card import Card
from models.cardrow import CardRow


class TestCard:
    def setup(self):
        self.card = Card()
        self.card.rows = [CardRow([1, 17, None, 34, None, 56, None, None, 81]),
                          CardRow([None, 19, None, 39, None, 52, None, 79, 83]),
                          CardRow([7, None, 29, None, 43, 58, None, 77, None])]

    def test_init(self):
        test_card = Card()
        assert test_card[0]
        assert test_card[1]
        assert test_card[2]
        with raises(IndexError):
            str(test_card[3])
        assert str(type(test_card[0])) == "<class 'models.cardrow.CardRow'>"
        # Проверяем, что в карточке  генерируется 15 различных чисел по 5 в строке и пустые ячейки
        card_values = []
        for k in range(3):
            card_values.append(set([str(test_card[k].cells[i]) for i in range(9)]))
            assert len(card_values[k]) == 6
        assert len(card_values[0] | card_values[1] | card_values[2]) == 16
        card_values = []
        for k in range(3):
            card_values.append(set([str(self.card[k].cells[i]) for i in range(9)]))
            assert len(card_values[k]) == 6
        assert len(card_values[0] | card_values[1] | card_values[2]) == 16

    def test_is_card_cross_out(self):
        test_card = Card()
        assert not test_card.is_card_cross_out()
        for k in range(3):
            assert not test_card.is_card_cross_out()
            for cell in test_card[k]:
                if cell.value != '  ':
                    assert not test_card[k].is_row_cross_out()
                    cell.is_cross_out = True
            assert test_card[k].is_row_cross_out()
        assert test_card.is_card_cross_out()
