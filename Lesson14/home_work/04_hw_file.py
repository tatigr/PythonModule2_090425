<<<<<<< HEAD
# "Обработка списка фруктов"
# Задание
# Дан файл data/fruits.txt со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно. Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв, а также есть пустые строки, которые нужно пропустить.
# Не гарантируется, что фрукты идут по алфавиту. Т.е. сначала может быть фрукт на букву "В", а потом идти на букву "Б"
# Напишите универсальный код, который будет работать с любым списком фруктов и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
#
# Формат входных данных
# Дан текстовый файл, на каждой строке которого или название фрукта, или пустая строка.
#
# Формат выходных данных
# Записать названия фруктов в разные файлы в соответствии с условием задачи.

# Чтобы получить список больших букв русского алфавита:
#
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os
=======
import os
from pathlib import Path
from pprint import pprint

path = os.path.join('data', 'fruits.txt')
DIR = "data"
fruits = {}

with open(path, 'r', encoding="UTF-8") as f:
    for line in f:
        fruit_name = line.strip()
        if not fruit_name:
            continue

        first_letter = fruit_name[0]
        x = fruits.setdefault(first_letter, [])
        x.append(fruit_name)
        fruits[first_letter] = x
pprint(fruits)

for first_letter, fruit_names in fruits.items():
    path_out = Path(DIR, "fruits_" + first_letter)
    with open(path_out, "w", encoding="UTF-8") as f:
        for fruit_name in fruit_names:
            f.write(fruit_name + "\n")

# 10000 -> 20000
# Абрикос -> fruit_A
# Груша -> fruit_Г
# Арбуз -> fruit_А

# fruit_files = {
#     "А": open(".../fruits_А", "w", encoding="UTF-8"),
#     "Б": open(".../fruits_Б", "w", encoding="UTF-8"),
# }

path = "data/fruits.txt"
d = list(map(chr,range(ord("А"),ord("Я")+1)))
with open(path, "r", encoding="UTF-8") as f:
    for line in f:
        if line.strip():
            path1 = "data/"+"fruits_" + line[0] + ".txt"
            with open(path1,"a", encoding="UTF-8")as file:
                file.write(line)
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
