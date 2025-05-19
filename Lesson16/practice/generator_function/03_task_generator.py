# Задача "Генератор случайных целых чисел"
# Напишите генераторную функцию random_integers(n), которая генерирует n случайных целых чисел
# в диапазоне от 1 до 100 (используйте модуль random).
import random

<<<<<<< HEAD

import random

def random_integers(number):
    for _ in range(number):
        yield random.randint(1, 100)


print(list(random_integers(5)))
=======
def random_integers(n):
    for _ in range(n):
        yield random.randint(1, 100)


print(list(random_integers(6)))
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
