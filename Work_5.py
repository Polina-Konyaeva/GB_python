new_list = [150, 150, 101, 100, 100, 10, 1]
new_elem = int(input('Введите новый элемент: '))
for i in range(len(new_list)):
    if new_list[i] < new_elem:
        new_list.insert(i, new_elem)
        break
print(new_list)

