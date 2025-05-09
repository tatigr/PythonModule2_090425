# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

import math

def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


xa = int(input("Введите координату х для точки а: "))
ya = int(input("Введите координату y для точки а: "))
xb = int(input("Введите координату х для точки b: "))
yb = int(input("Введите координату y для точки b: "))
xc = int(input("Введите координату х для точки c: "))
yc = int(input("Введите координату y для точки c: "))

ab = distance(xa, ya, xb, yb)
bc = distance(xb, yb, xc, yc)
ac = distance(xa, ya, xc, yc)

min_length = min(ab, bc, ac)
if min_length == ab:
    print(f"Самый короткий отрезок: AB ({round(ab, 2)})")
elif min_length == bc:
    print(f"Самый короткий отрезок: BC ({round(bc, 2)})")
else:
    print(f"Самый короткий отрезок: AC ({round(ac, 2)})")


