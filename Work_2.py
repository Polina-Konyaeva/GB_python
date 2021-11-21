with open('file_task_2.txt', 'r') as file_2:
    lines = file_2.readlines()
    print(f'Количество строк в файле {len(lines)}')
    for i in range(len(lines)):
        line_new = lines[i].split()
        print(f'Строка {i + 1}: количество слов = {len(line_new)}')



