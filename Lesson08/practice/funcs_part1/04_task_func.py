# Задача: Дан список из n элементов, заполненный произвольными целыми числами.
# Найдите сумму всех положительных элементов.

def sum_positive(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number
    return summa

# Решение:
print(sum_positive([6, -4, 3, 8, -2, 0, 7])) #24
print(sum_positive([-2, 12, -35, 10, -5, 10, -7])) #32
print(sum_positive([2, -6, 4, 12, 0, -10])) # 18
print(sum_positive([5, -6, 4, -12, 8, -10])) # 17


