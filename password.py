import random

while True: # Проверка на количество паролей
    num = input('Сколько паролей нужно?')
    if not num.isdigit() or int(num) < 1:
        print('Указано неверное количество')
        continue
    else:
        break
num = int(num)
while True: # проверка на длину пароля и цыфры
    length = input('Какая длина пароля? (Введите не меньше 8 и не больше 100)')
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
    return password
# символы из которых генерируют пароли
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '~()!#$%&*+-=?@^_/'
chars = ''

while True: # сбор ответов
    digit = input('Включать ли цифры 0123456789?; д = да, н = нет')
    upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
    lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
    symbols = input('Включать ли символы ~()!#$%&*+-=?@^_/; д = да, н = нет')
    similar_symbols = input('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
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
    if chars == []: # попытка проверить на отсутствие символов, пока не получается
        print('Не включено ни одного символа, Давайте попробуем еще раз')
        print(chars)
        continue
    else:
        break

for _ in range(num): #вывод нужного количества сгенерированных паролей
    print(generate_password(length, chars))
