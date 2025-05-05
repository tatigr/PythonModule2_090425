import math
import matplotlib.pyplot as plt

# Функция расстояния между центрами окружностей
def point_in_circle(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Ввод координат и радиусов
x1 = int(input("Введите координату x1 центра первой окружности: "))
y1 = int(input("Введите координату y1 центра первой окружности: "))
R1 = int(input("Введите радиус R1 первой окружности: "))

x2 = int(input("Введите координату x2 центра второй окружности: "))
y2 = int(input("Введите координату y2 центра второй окружности: "))
R2 = int(input("Введите радиус R2 второй окружности: "))

length = point_in_circle(x1, y1, x2, y2)

if R1 > R2 and length + R2 <= R1:
    print("Окружность радиуса R2 находится целиком в окружности радиуса R1")
elif R2 > R1 and length + R1 <= R2:
    print("Окружность радиуса R1 находится целиком в окружности радиуса R2")
else:
    print("Ни одна из окружностей не находится внутри другой")

# Рисование окружностей
fig, ax = plt.subplots()
circle1 = plt.Circle((x1, y1), R1, color='blue', alpha=0.3, label='R1')
circle2 = plt.Circle((x2, y2), R2, color='red', alpha=0.3, label='R2')

ax.add_patch(circle1)
ax.add_patch(circle2)

# Центры
ax.plot(x1, y1, 'bo')  # Центр первой окружности
ax.plot(x2, y2, 'ro')  # Центр второй окружности

# Настройка графика
ax.set_aspect('equal')
padding = max(R1, R2) + 5
ax.set_xlim(min(x1, x2) - padding, max(x1, x2) + padding)
ax.set_ylim(min(y1, y2) - padding, max(y1, y2) + padding)
ax.set_title("Сравнение окружностей")
plt.grid(True)
plt.legend()
plt.show()


# Данные для тестирования:
# (x1 = 10, y1 = 5, R1 = 14, x2 = 5, y2 = -3, R2 = 2) # находится
# (x1 = 10, y1 = 5, R1 = 14, x2 = 5, y2 = -3, R2 = 8) # не находится
# (x1 = 10, y1 = 5, R1 = 8, x2 = 5, y2 = -3, R2 = 8) # не находится



