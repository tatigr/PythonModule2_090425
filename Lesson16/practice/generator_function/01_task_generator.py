# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

<<<<<<< HEAD
# Вариант-1 (мой)
# def is_even(number: int) -> bool:
#     """
#     Проверяет, является ли заданное целое число простым.
#     """
#     if number % 2 == 0:
#         return True
#     return False
#
#
#
# def even_numbers(number):
#     for number in range(2, number + 1):
#         if is_even(number):
#             yield number
#
# for number in even_numbers(100):
#     print(number)



# Вариант-2 (работает быстрее)
# def even_numbers(number):
#     for number in range(2, number + 1, 2):
#         yield number
#
# for number in even_numbers(25):
#      print(number)


# Вариант-3
def even_numbers(number):
    for number in range(2, number + 1):
        if number % 2 == 0:
            yield number

for number in even_numbers(25):
     print(number)
=======
def even_numbers(n):
    for el in range(0, n + 1, 2):
        yield el



for el in even_numbers(13):
    print(el)
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
