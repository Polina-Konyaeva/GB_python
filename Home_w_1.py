def division (a, b):
    if b != 0:
        return (a / b)
    else:
        return('Деление на 0 невозможно')
number_1 = float(input('Введите число 1: '))
number_2 = float(input('Введите число 2: '))
print(division(number_1, number_2))
