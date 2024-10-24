import random

def generate_password(length, chars):
    password = []
    for _ in range (length):
        sign = random.choice(chars)
        password.append(sign)
    return ''.join (password)

if __name__ == '__main__':
    length = int(input('Enter password length: '))
    chars = input('Enter alphabet: ')
    password = generate_password(length, chars)
    print(password)
