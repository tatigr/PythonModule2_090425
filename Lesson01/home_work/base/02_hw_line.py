import math
math.pi # Число pi из библиотеки math
rad_cir = float(input("Введите радиус круга: "))
#print("Число pi", math.pi)
square_cir = math.pi * rad_cir ** 2
#f"{x:.2f}"
print("Площадь круга радиуса", rad_cir, "равна", f"{square_cir:.1f}")