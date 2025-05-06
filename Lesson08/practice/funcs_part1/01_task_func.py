# Напишите функцию для расчета площади прямоугольника.
#
# Входные данные:
#   w: ширина прямоугольника.
#   h: высота прямоугольника.
# Результат:
#   площадь прямоугольника.

def calculate_rectangle_area(width: int|float, height: int|float):
    return width * height
<<<<<<< HEAD
=======


>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
width = int(input("width = "))
height = int(input("height = "))

area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника = {area}")
