class Warehouse:
    def __init__(self, list_quantity):
        self.list_quantity = list_quantity

    def adding_warehouse(self, technic):
        self.list_quantity.append(technic)
        return f'На складе есть следующая техника: {self.list_quantity}'

    def give_company(self, company, technic):
        if self.list_quantity.count(technic) > 0:
            self.list_quantity.remove(technic)
            print(f'{technic} передаем в компанию {company}')
        else:
            print('На складе нет такой техники')

    def add_quantity_of_one_technic(self, technic, kol):
        try:
            for _ in range(kol):
                self.list_quantity.append(technic)
        except:
            print('Неправильное использование типа данных, перепроверьте!')


class OfficeEquipment:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title


class Printer(OfficeEquipment):
    def __init__(self, title, paint):
        super().__init__(title)
        self.paint = paint

    @property
    def inform_printer(self):
        print(f'{self.title} имеет {self.paint} печать.')


class Scanner(OfficeEquipment):
    def __init__(self, title, resolution):
        super().__init__(title)
        self.resolution = resolution

    @property
    def inform_scanner(self):
        print(f'{self.title} имеет {self.resolution} dpi (разрешающую способность).')


class Xerox(OfficeEquipment):
    def __init__(self, title, speed):
        super().__init__(title)
        self.speed = speed

    @property
    def inform_xerox(self):
        print(f'{self.title} имеет {self.speed} скорость сканирования.')


new_printer_1 = Printer('Принтер1', 'цветноую')
new_printer_2 = Printer('Принтер2', 'ч/б')

new_scanner_1 = Scanner('Сканер1', '300')
new_scanner_2 = Scanner('Сканер2', '470')
new_scanner_3 = Scanner('Сканер3', '650')

new_xerox_1 = Xerox('Ксерокс1', 'высокую')

print(f'Данные о технике:')
new_printer_1.inform_printer
new_printer_2.inform_printer
new_scanner_1.inform_scanner
new_scanner_2.inform_scanner
new_scanner_3.inform_scanner
new_xerox_1.inform_xerox

office_warehouse = Warehouse([])
print(office_warehouse.adding_warehouse(new_printer_1))
print(office_warehouse.adding_warehouse(new_printer_2))
office_warehouse.give_company('"КОМП_А"', new_printer_1)
print(office_warehouse.list_quantity)
office_warehouse.adding_warehouse(new_scanner_1)
office_warehouse.adding_warehouse(new_scanner_2)
office_warehouse.adding_warehouse(new_scanner_3)
office_warehouse.adding_warehouse(new_xerox_1)
print(office_warehouse.list_quantity)
office_warehouse.give_company('"КОМП_B"', new_xerox_1)
office_warehouse.give_company('"КОМП_C"', new_scanner_3)
print(office_warehouse.list_quantity)
office_warehouse.give_company('"КОМП_C"', new_scanner_3)
office_warehouse.add_quantity_of_one_technic(new_printer_2, 2)
print(office_warehouse.list_quantity)
office_warehouse.add_quantity_of_one_technic(new_printer_2, new_printer_2)  # проверка
