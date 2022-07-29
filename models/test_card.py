from pytest import raises

from models.card import Card
from models.cardrow import CardRow


class TestCard:
    def test_init(self):
        test_card = Card()
        assert test_card[0]
        assert test_card[1]
        assert test_card[2]
        with raises(IndexError):
            str(test_card[3])
        assert str(type(test_card[0])) == "<class 'models.cardrow.CardRow'>"
        # Проверяем, что в карточке  генерируется 15 различных чисел по 5 в строке и пустые ячейки
        set_card_value = []
        for k in range(3):
            set_card_value.append(set([test_card[k].cells[i].value for i in range(9)]))
            assert len(set_card_value[k]) == 6
        assert len(set_card_value[0] | set_card_value[1] | set_card_value[2]) == 16

    def setup(self):
        self.rows = [CardRow([1, 17, None, 34, None, 56, None, None, 81]),
                     CardRow([None, 19, None, 39, None, 52, None, 79, 83]),
                     CardRow([7, None, 29, None, 43, 56, None, 77, None])]

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
