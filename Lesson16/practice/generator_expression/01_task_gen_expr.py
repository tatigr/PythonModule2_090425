# "Квадраты нечетных чисел"
# Напишите генераторное выражение, которое генерирует квадраты всех нечетных чисел в диапазоне от 1 до 10 включительно.

<<<<<<< HEAD
# squares = (x ** 2 for x in range(1, 11) if x % 2 != 0)
#
# print(next(squares))  # 1
# print(next(squares))  # 9
# print(next(squares))  # 25
# print(next(squares))  # 49
# print(next(squares))  # 81

result = (el ** 2 for el in range(1, 11) if el % 2 != 0)
print(next(result))
print(next(result))
print(next(result))
=======

result = (el ** 2 for el in range(1, 11) if el % 2 != 0)
print(result)
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
