n = int(input('ведите целое положительное число: '))
max = 0
while n > 0:
    k = n % 10
    if k > max:
        max = k
    n = n // 10
print(f'Самая большая цифра: {max}')