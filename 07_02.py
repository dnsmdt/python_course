from abc import abstractmethod, ABC


class Cloth:
    @abstractmethod
    def __init__(self):
        name = 'clothing'


class Coat(Cloth):
    def __init__(self, v):
        super().__init__()
        self.name = 'Coat'
        self.v = v

    @property
    def textile_need(self):
        return round(self.v / (6.5 + 0.5), 2)


class Suit(Cloth):
    def __init__(self, h):
        super().__init__()
        self.name = 'Coat'
        self.h = h

    @property
    def textile_need(self):
        return round(2 * self.h + 0.3, 2)


coat_1 = Coat(40)
suit_1 = Suit(30)
print(f'Расход ткани для пальто - {coat_1.textile_need}')
print(f'Расход ткани для костюма - {suit_1.textile_need}')
