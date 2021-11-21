with open('file_task_5.txt', 'w') as file_5:
    numbers = input('Введите набор чисел через пробел: ')
    file_5.write(numbers + ' ')
    numbers = numbers.split()
    summa = 0
    for i in numbers:
        summa += int(i)
    print(f'Сумму чисел в файле: {summa}')
