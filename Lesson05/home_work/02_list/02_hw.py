# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
#random.seed(100)
n = int(input("n: "))
numbers = []

# Вариант-1:
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