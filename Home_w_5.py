def numbers_sum():
    summa = 0
    while True:
        num = input('Введите строку чисел: ').split()
        for i in num:
            if i == '!':
                print('Программа завершена')
                return
            else:
                summa += int(i)
        print(f'Сумма всех чисел равна {summa}')
print(numbers_sum())

