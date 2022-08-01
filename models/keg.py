class Keg:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number) if len(str(self.number)) == 2 else ' ' + str(self.number)



if __name__ == '__main__':
    keg_9 = Keg(9)
    keg_89 = Keg(89)
    print(type(keg_89))
    print(keg_89)

