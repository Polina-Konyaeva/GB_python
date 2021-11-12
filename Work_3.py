month = int(input('Введите номер месяца (от 1 до 12): '))
#1
month_list = ['зима','весна','лето','осень']
if 1 <= month <= 2 or month == 12:
    print(month_list[0])
elif 3 <= month <= 5:
    print(month_list[1])
elif 6 <= month <= 8:
    print(month_list[2])
else:
    print(month_list[3])

#2
month_dict = {
    'зима':(1, 2, 12),
    'весна':(3, 4, 5),
    'лето':(6, 7, 8),
    'осень':(9, 10, 11)
}
for key in month_dict.keys():
    if month in month_dict[key]:
        print(key)
