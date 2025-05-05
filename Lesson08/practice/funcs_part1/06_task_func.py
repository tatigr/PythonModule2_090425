# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:
import math
def point_in_circle(x, y, xc, yc, r):
    return math.sqrt((x - xc) ** 2 + (y - yc) ** 2) <= r


# Не забудьте протестировать вашу функцию
print(point_in_circle(5, 3, 4, 7, 5))
print(point_in_circle(-2, 3, 10, -5, 5))