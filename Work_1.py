with open('file_task_1.txt', 'w', encoding='utf-8') as file_1:
    text = input('Введите текст: ')
    while text:
        file_1.write(text + '\n')
        text = input('Введите текст: ')
        if text == '':
            break