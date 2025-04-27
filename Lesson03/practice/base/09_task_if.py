number = int(input("Введите целоe число от 1 до 12: "))
if 1 <= number <= 2 or number == 12:
    print("Зима")
elif 3 <= number <= 5:
    print("Весна")
elif 6 <= number <= 8:
    print("Лето")
else:
    print("Осень")