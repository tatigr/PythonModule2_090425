def distance(x1, y1, x2, y2):
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Семантические ошибки логики
print(distance(2, 4, 2, 9))
# assert distance(2, 4, 2, 9) == 5.0
# assert distance(12, 8, 12, -9) == 17.0