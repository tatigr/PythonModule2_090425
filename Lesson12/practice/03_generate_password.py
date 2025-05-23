# Задача "Генерация случайного пароля"
# Создайте строку, содержащую символы разных регистров, цифры и спецсимволы.
# Используйте функцию random.choice() для выбора случайных символов из этой строки.
# Сгенерируйте пароль заданной длины.
import random


import random

def generate_password(password_length: int):

    password = ""
    for i in range(password_length):
        password += random.choice(
            [chr(i) for i in range(ord('a'), ord('z'))] +
            [chr(i) for i in range(ord('A'), ord('Z'))] +
            [chr(i) for i in range(ord('0'), ord('9'))] + ['@','!', '%', '_', '*']
        )

    return password



print(generate_password(5))
print(generate_password(10))
print(generate_password(8))
print(generate_password(4))
print(generate_password(15))
print(generate_password(7))
print(generate_password(24))
print(generate_password(6))
print(generate_password(12))




# assert len(generate_password(5)) == 5
# assert len(generate_password(12)) == 12
# assert len(generate_password(16)) == 16
# assert len(generate_password(22)) == 22
# assert len(generate_password(2)) == 2

