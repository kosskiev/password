import random
print('-'*50)
print('Генератор паролей!')
print('-'*50)

while True: # Проверка на количество паролей
    num = input('Сколько паролей нужно? ')
    if not num.isdigit() or int(num) < 1:
        print('Указано неверное количество')
        continue
    else:
        break
num = int(num)

while True: # проверка на длину пароля и цыфры
    length = input('Какая длина пароля? (Введите не меньше 8 и не больше 100) ')
    if not length.isdigit() or int(length) < 8 or  int(length) > 100:
        print('Указана неверная длина')
        continue
    else:
        break
length = int(length)

def generate_password(length, chars): # сгенерируем пароли
    password = ''
    for j in range(length):
        password += random.choice(chars)
    random.shuffle(list(password)) # перемешивает список
    return password
# символы из которых генерируют пароли
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '~()!#$%&*+-=?@^_/'

while True: # сбор ответов
    chars = ''
    digit = input(f'Включать ли цифры {digits}; д/да = да, н/нет = нет ')
    upper = input(f'Включать ли прописные буквы {uppercase_letters}?; д/да = да, н/нет = нет ')
    lower = input(f'Включать ли строчные буквы {lowercase_letters}?; д/да = да, н/нет = нет ')
    symbols = input(f'Включать ли символы {punctuation}; д/да = да, н/нет = нет ')
    similar_symbols = input('Исключать ли неоднозначные символы il1Lo0O?; д/да = да, н/нет = нет ')
    if digit.lower() == 'д' or digit.lower() == 'да':
        chars += digits
    if upper.lower() == 'д' or upper.lower() == 'да':
        chars += uppercase_letters
    if lower.lower() == 'д' or lower.lower() == 'да':
        chars += lowercase_letters
    if symbols.lower() == 'д' or symbols.lower() == 'да':
        chars += punctuation
    if similar_symbols.lower() == 'д':
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')
    if chars == '': # проверка на наличие символов в переменной
        print('Не включено ни одного символа, Давайте попробуем еще раз')
        continue
    else:
        break

print('*' * 50,)
print('Ваши долгожданные пароли: ')
for _ in range(num): #вывод нужного количества сгенерированных паролей
    print(generate_password(length, chars))
print('*' * 50,)
