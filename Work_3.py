with open('file_task_3.txt', 'r', encoding='utf-8') as file_3:
    lines = file_3.read().split('\n')
    surname = []
    summa = 0
    for i in lines:
        i = i.split()
        if int(i[1]) < 20000:
            surname.append(i[0])
        summa += int(i[1])
    print(f'Оклад менее 20000 получает: {", ".join(surname)}')
    print(f'Средняя величина дохода сотрудников составляет {summa / len(lines)}')
