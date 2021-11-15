def salary():
    time = float(input('Введите выработку в часах: '))
    bet_time = float(input('Введите ставку в час: '))
    prize = float(input('Введите премию: '))
    sal_employee = time * bet_time + prize
    print (f'Заработная плата сотрудника составляет: {sal_employee} рубля(-ь,-ей)')
salary()
