from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, title, parameters):
        self.title = title
        self.parameters = parameters

    @property
    def type_cloth(self):
        print(f'Вы выбрали {self.title}')

    @abstractmethod
    def fabric_calculation(self):
        pass

class Coat(Clothes):

    def type_cloth(self):
        print(f'Определяем расход ткани для {self.title}')

    def fabric_calculation(self):
        print(f'Для пальто потребуется {self.parameters / 6.5 + 0.5:.2f} ткани')

class Suit(Clothes):

    def type_cloth(self):
        print(f'Определяем расход ткани для {self.title}')

    def fabric_calculation(self):
        print(f'Для костюма потребуется {2 * self.parameters + 0.3:.2f} ткани')


V = float(input('Введите размер (для пальто): '))
H = float(input('Введите рост (для костюма): '))

my_coat = Coat('пальто', V)
my_coat.type_cloth
my_coat.fabric_calculation()

my_suit = Suit('костюма', H)
my_suit.type_cloth
my_suit.fabric_calculation()
