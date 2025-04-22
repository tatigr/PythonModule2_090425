fahr_temp = float(input("Введите температуру по Фарингейту: "))
#fahr_temp = (cel_temp * 9 / 5) + 32
cel_temp = (fahr_temp - 32) * 5 // 9
print("Введенная по Фарингейту температура", fahr_temp, "равна", cel_temp, "градусов по Цельсию")
