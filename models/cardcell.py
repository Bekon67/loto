class CardCell:
    def __init__(self, number):
        if isinstance(number, int):
            if number < 10:
                self.value = ' ' + str(number)
            else:
                self.value = str(number)
        elif number is None:
            self.value = '  '
        self.is_cross_out = False

    def __str__(self):
        return '--' if self.is_cross_out else self.value


    # # зачеркивание цифры правильно
    def cross_out(self, keg_number):
        if self.value == str(keg_number):
            self.is_cross_out = True
