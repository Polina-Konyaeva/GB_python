class Worker:

    def __init__ (self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': float(wage),
            'bonus': float(bonus)
        }

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Доход составляет: {self._income["wage"] + self._income["bonus"]}')

worker_name = input('Введите имя сотрудника: ')
worker_surname = input('Введите фамилию сотрудника: ')
worker_position = input('Введите должность сотрудника: ')
worker_wage = int(input('Введите оклад сотрудника: '))
worker_bonus = int(input('Введите премию сотрудника: '))

employee = Position(worker_name, worker_surname, worker_position, worker_wage, worker_bonus)
employee.get_full_name()
employee.get_total_income()
