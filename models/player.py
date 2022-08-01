from models.card import Card


class Player:
    def __init__(self, name):
        self.name = name
        # self.profile = 1
        self.card = Card()

    def __str__(self):
        return str(self.name)

    # инициализация
    # определение типа игрока
    # присвоение игроку имени
    # получение игроком карточки
    # зачеркивание/незачеркивание номера в зависимости от типа игрока
