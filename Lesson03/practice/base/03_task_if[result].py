amount = float(input("Сумма наличных денег в кармане: "))
cost = float(input("Стоимость покупки: "))
if cost <= amount:
    print(f"Осталось {(amount - cost):.2f} рублей")
else:
    print("Данной суммы не достаточно для покупки")