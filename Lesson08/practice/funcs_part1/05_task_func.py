# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.
import math

# def distance(x1=0, y1=0, x2=0, y2=0): # значения по умолчанию равны нулю


def distance(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Тестируем функцию
print(distance(2, 4, 2))
print(distance(2, 4)) # остальные не указанные по умолчанию равны нулю
#print(distance(())) # все аргументы равны по умолчанию нулю
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
print(distance(2, 4))
print(distance(2))
print(distance()) # значения аргументов равны нулю
# print(distance(12, 8, 12, -9))
# print(distance(23, 0, 15, 32))

