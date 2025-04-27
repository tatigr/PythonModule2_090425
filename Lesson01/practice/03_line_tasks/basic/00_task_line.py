a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
perimetr = a + b + c
p = perimetr / 2
square = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"Периметр треугольника = {perimetr}")
print(f"Площадь треугольника = {square}")

