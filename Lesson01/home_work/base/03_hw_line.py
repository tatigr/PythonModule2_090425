biker_speed = int(input("Введите скорость байкера: "))
biker_time = float(input("Введите время движения байкера: "))
mkad_distance = 109

biker_distance = biker_speed * biker_time
point = biker_distance % mkad_distance

print(f"Байкер остановится на отметке {point:.2f} км.")
