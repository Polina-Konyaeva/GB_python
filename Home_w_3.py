def my_func():
    a = float(input('Введите значение a: '))
    b = float(input('Введите значение b: '))
    c = float(input('Введите значение c: '))
    n1_max = max(a, b, c)
    if n1_max == a:
        n2_max = max(b, c)
    elif n1_max == b:
        n2_max = max(a, c)
    else:
        n2_max = max(a, b)
    return n1_max + n2_max
print(my_func())
