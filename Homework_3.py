class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        result = self.quantity + other.quantity
        return f'Количество клеток после сложения {result}'

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result > 0:
            return f'Количество клеток после вычитания {result}'
        else:
            return f'Разность меньше нуля'

    def __mul__(self, other):
        result = self.quantity * other.quantity
        return f'Количество клеток после умножения {result}'

    def __truediv__(self, other):
        result = self.quantity // other.quantity
        return f'Количество клеток после деления {result}'

    def make_order(self, kol_cell):
        ex_class = ''
        for i in range(int(self.quantity / kol_cell)):
            ex_class += '*' * kol_cell +'\n'
        ex_class += '*' * (self.quantity % kol_cell) +'\n'
        print(ex_class)


new_cell_1 = Cell(19)
new_cell_2 = Cell(5)
print(new_cell_1 + new_cell_2)
print(new_cell_1 - new_cell_2)
print(new_cell_1 * new_cell_2)
print(new_cell_1 / new_cell_2)
new_cell_1.make_order(4)
new_cell_2.make_order(2)
