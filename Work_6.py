from itertools import count, cycle
num_1 = int(input('Введите С какого числа: '))
num_2 = int(input('Введите ДО какого числа: '))
for i in count(num_1):
    if i > num_2:
        break
    print(i)

new_list = input('Введите элементы списка: ').split()
kol = 0
n = int(input('Введите количество повторений: '))
for i in cycle(new_list):
    kol += 1
    if kol > n:
        break
    print(i)
