# Задача: Дан список из n элементов, заполненный произвольными целыми числами.
# Найдите сумму всех положительных элементов.

<<<<<<< HEAD

=======
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
def sum_positive(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number
    return summa

<<<<<<< HEAD

=======
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
# Решение:
print(sum_positive([6, -4, 3, 8, -2, 0, 7])) #24
print(sum_positive([-2, 12, -35, 10, -5, 10, -7])) #32

<<<<<<< HEAD


=======
print(sum_positive([2, -6, 4, 12, 0, -10])) # 18
print(sum_positive([5, -6, 4, -12, 8, -10])) # 17
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405

