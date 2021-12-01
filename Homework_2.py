class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.massa = 35
        self.num_sm = 10

    def mass_asphalt(self):
        print(f'Масса асфальта составляет: {self._lenght * self._width * self.massa * self.num_sm} кг для покрытия всего дорожного полотна')

l = float(input('Введите длину дороги в метрах (lenght): '))
h = float(input('Введите ширину дороги в метрах (width): '))

asph_road = Road(l, h)
asph_road.mass_asphalt()
