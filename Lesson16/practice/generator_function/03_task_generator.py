# Задача "Генератор случайных целых чисел"
# Напишите генераторную функцию random_integers(n), которая генерирует n случайных целых чисел
# в диапазоне от 1 до 100 (используйте модуль random).


import random

def random_integers(number):
    for _ in range(number):
        yield random.randint(1, 100)


print(list(random_integers(5)))