list_1 = input('Введите числа в список: ').split()
# map выполняет функцию int для каждого элемента
list_1 = list(map(int, list_1))
print(list_1)
list_2 = [i for i in list_1 if list_1.count(i) == 1]
print(list_2)