# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
<<<<<<< HEAD
#random.seed(100)
=======

>>>>>>> 91c6c03517893abab01a3c834a1a0cd1c826d49d
n = int(input("n: "))
numbers = []

# Вариант-1:
<<<<<<< HEAD
#while n > 0:
#    number = (random.randint(-100, 100))
#    numbers.append(number)
#    n -= 1

#print(numbers)

# Вариант-2:

for i in range(n):
    number = (random.randint(-100, 100))
    numbers.append(number)
print(numbers)

#result = list(range(8))
#print(result)
=======
# while n > 0:
#     number = random.randint(-100, 100)
#     numbers.append(number)
#     n -= 1

# Вариант-2:
for i in range(n):
    number = random.randint(-100, 100)
    numbers.append(number)
print(numbers)

