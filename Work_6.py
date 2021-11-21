new_dict = {}
with open('file_task_6.txt', encoding='utf-8') as file_6:
    for i in file_6:
        subject, mark = i.split(':')
        new_list = ([j for j in mark if ('0' <= j <= '9') or j == ' '])
        new_list = ''.join(new_list).split()
        new_list = sum(list(map(int, new_list)))
        new_dict[subject] = new_list
    print(f'Словарь, содержащий название предмета и общее количество занятий по нему:\n{new_dict}')