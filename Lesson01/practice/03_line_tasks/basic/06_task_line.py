ap_number = int(input("Введите номер квартиры: "))
floor = (ap_number - 1) // 5 + 1
print("Данная квартира", ap_number, "расположена на", floor, "этаже")
print(f"Данная квартира {ap_number} расположена на {floor} этаже")
