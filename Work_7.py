def factor(n):
    p = 1
    for el in range(1,n+1):
        p *= el
        yield p

n = int(input('Факториал числа: '))
for i in factor(n):
    print(i)