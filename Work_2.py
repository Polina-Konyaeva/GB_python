from random import randint
list_1 = [randint(0, 550) for i in range (10)]
print(list_1)
list_2 = []
for i in range(len(list_1)):
    if list_1[i] > list_1[i-1]:
        list_2.append(list_1[i])
print(list_2)