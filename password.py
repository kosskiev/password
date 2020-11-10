import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '~()!#$%&*+-=?@^_/'
chars = ''
print('Сколько паролей нужно?')
num = int(input())
print('Какая длина пароля?')
length = int(input())
print('Включать ли цифры 0123456789?; д = да, н = нет')
digit = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
upper = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
lower = input()
print('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет')
symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
similar_symbols = input()

if digit.lower() == 'д':
    chars += digits
if upper.lower() == 'д':
    chars += uppercase_letters
if lower.lower() == 'д':
    chars += lowercase_letters
if symbols.lower() == 'д':
    chars += punctuation
if similar_symbols.lower() == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)

for _ in range(num):
    generate_password(length, chars)
