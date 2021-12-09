class CheckNumbers(Exception):

    def __init__(self, numbers):
        self.numbers = numbers


list = []
while True:
    try:
        num = input('Введите число:')
        if num == 'end':
            print(list)
            break
        if not num.isdigit():
            raise CheckNumbers('Вы ввели не число!')
        list.append(num)
        print(list)
    except CheckNumbers as numbers:
        print(numbers)


