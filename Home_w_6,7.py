def int_func_6(word):
    new_word = word.capitalize()
    return (new_word)

new_str = input('Введите элементы: ')

for new_word in new_str.split(' '):
    print(f'{int_func_6(new_word)} ', end=' ')
