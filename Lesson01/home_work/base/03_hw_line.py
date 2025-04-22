biker_speed = int(input("Введите скорость байкера: "))
biker_time = float(input("Введите время движения байкера: "))
mkad_distance = 108

if biker_speed > 0:
    biker_distance = biker_speed * biker_time
else:
   biker_distance = biker_distance % mkad_distance  # чтобы не выйти за границы кольца

print(f"Байкер остановится на отметке {biker_distance:.2f} км.")
