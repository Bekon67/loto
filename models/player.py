from models.card import Card
class Players:
    def __init__(self):
        self.players = []




class Player:
    def __init__(self,name):
        self.name = name
        self.card = Card()

    #
    # инициализация
    # определение типа игрока
    # присвоение игроку имени
    # получение игроком карточки
    # зачеркивание/незачеркивание номера в зависимости от типа игрока
