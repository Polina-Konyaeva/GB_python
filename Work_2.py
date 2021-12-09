class CheckingDivision(Exception):

    def __init__(self, number):
        self.number = number


try:
    my_number_1 = float(input('Введите число: '))
    my_number_2 = float(input('Введите число: '))
    if my_number_2 == 0:
        raise CheckingDivision('Деление на ноль!')
    print(f'Деление {my_number_1} на {my_number_2} равно {my_number_1/my_number_2}')
except CheckingDivision as number:
    print(number)


