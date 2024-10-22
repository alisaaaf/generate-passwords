import random

def generate_password(length, chars):
    password = []
    for _ in range (length):
        sign = random.choice(chars)
        password.append(sign)
    return ''.join (password)

if __name__ == '__main__':
    length = int(input('Введите длину пароля '))
    chars = input('Введите алфавит ')
    password = generate_password(length, chars)
    print(password)
