class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула на{direction}!')

    def show_speed(self):
        return self.speed

    def information_car(self):
        print(f'Марка {self.name} {self.color} цвета едет со скоростью {self.speed} км/ч')


class TownCar(Car):

    def information_car(self):
        super().information_car()

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена!')
        else:
            print('Нарушений по скорость нет')


class SportCar(Car):

    def information_car(self):
        super().information_car()


class WorkCar(Car):

    def information_car(self):
        super().information_car()

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена!')
        else:
            print('Нарушений по скорость нет')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def information_car(self):
        super().information_car()

print('Первая машина:')
my_car_town = TownCar(80, 'красного', 'BMW_F20')
my_car_town.information_car()
my_car_town.go()
my_car_town.show_speed()
my_car_town.turn("право")
my_car_town.stop()

print('\nВторая машина:')
my_car_sport = SportCar(150, 'черного', 'MCLAREN_720s')
my_car_sport.information_car()
my_car_sport.go()
my_car_sport.turn("лево")
my_car_sport.stop()

print('\nТретья машина: ')
my_car_work = WorkCar(30, 'белого', 'AUDI_RS6')
my_car_work.information_car()
my_car_work.go()
my_car_work.show_speed()
my_car_work.turn("лево")
my_car_work.turn("право")
my_car_work.stop()

print('\nЧетвертая машина:')
my_car_police = PoliceCar(90, 'синего', 'FORD_NYPD')
my_car_police.information_car()
my_car_police.go()
my_car_police.turn("право")
my_car_police.stop()
