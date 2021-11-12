new_str = input('Введите предложение: ')
new_str = new_str.split()
for i in range (len(new_str)):
    print(f'{i+1} {new_str[i][:10]}')
