def user_data(name, surname, birth, city, email, phone):
    return (f'{name} {surname} родился(-ась) {birth} в городе {city}, данные пользователя: почта {email} и телефон {phone}')

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birth = input('Введите дату рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите почту с @: ')
user_phone = input('Введите телефон: ')
print(user_data(user_name, user_surname, user_birth, user_city, user_email, user_phone))



