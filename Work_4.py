num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('file_task_4.txt', 'r', encoding='utf-8') as file_4:
    lines = file_4.readlines()
with open('new_file_task_4.txt', 'w', encoding='utf-8') as new_file_4:
    for i in lines:
        i = i.split(' — ')
        i[0] = num_dict[i[0]]
        print(' — '.join(i), file=new_file_4, end='')
