new_list = input('Введите элементы: ').split()
print('Данный список:   ', new_list)
for i in range (len(new_list)):
    if len(new_list) % 2 == 0:
        if i % 2 == 0:
            a = new_list[i]
            new_list[i] = new_list[i+1]
            new_list[i+1] = a
    else:
        for i in range(len(new_list)-1):
                if i % 2 == 0:
                    a = new_list[i]
                    new_list[i] = new_list[i + 1]
                    new_list[i + 1] = a
print('Получаем список: ', new_list)