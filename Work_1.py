class Data:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def number_data(cls, day_month_year):
        new_data = []
        for i in day_month_year.split():
            if i != '-':
                i = int(i)
                new_data.append(i)
        print(f'Дата: {new_data[0]} число {new_data[1]} месяц {new_data[2]} год\n{type(new_data[0]), type(new_data[1]), type(new_data[2])}')

    @staticmethod
    def true_data(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2055:
                    print(f'Дата верная')
                else:
                    print(f'Перепроверьте год')
            else:
                print(f'Перепроверьте месяц')
        else:
            print(f'Перепроверьте число')


# Пример ввода: 08 - 03 - 2022 (неверно: 08-03-2022)
data_d_m_y = str(input('Введите дату через знак " - " (обязательно использовать пробелы между знаком "-"): '))
my_data = Data(data_d_m_y)
my_data.number_data(data_d_m_y)
my_day = int(input('Введите день: '))
my_month = int(input('Введите месяц: '))
my_year = int(input('Введите год: '))
my_data.true_data(my_day, my_month, my_year)
