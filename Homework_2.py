# 2 номер
time = int(input('Введите время в секундах: '))
if time >= 0:
    hour = time // 3600
    h = time - 3600 * hour
    minute = h // 60
    second = (time - 3600 * hour) - 60 * minute
    print(f'{time} секунд = {hour:02}:{minute:02}:{second:02}')
else:
    print('Время не может быть отрицательным')
