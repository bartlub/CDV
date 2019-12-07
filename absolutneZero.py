from liczba import Number

class AbsolutZero(Number):
    def __init__(self):
        self.value = 0
    def __str__(self):
        return "Jestem zerem!"
    def reklama(self):
        print('Ucz się!')


zero = AbsolutZero()
print(zero)
