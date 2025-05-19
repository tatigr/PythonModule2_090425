<<<<<<< HEAD
# "Пропуск некорректных данных"
# Задание
# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число.
# Найдите сумму всех чисел, пропуская все строки, которые нельзя преобразовать к типу int.
#
# Формат входных данных
# Дан текстовый файл, на каждой строке которого целое число или произвольный текст.
#
# Формат выходных данных
# Программа ничего не выводит в терминал, все сообщения записываются в указанный файл или в файл по умолчанию.
# Уточнение: в сумму добавляем только те значения, которые можно преобразовать к int'у
# Например: int("-26") --> -26, а int("--26") --> ошибка

path = "data/info.txt"
path_out = "data/work_result.txt"
sum_numbers = 0
count = 0
with open("data/info.txt", "r") as file, open(path_out, "w") as file_out:
    for line in file:
        try:
            number = int(line.strip())
            sum_numbers += number
            count += 1

        except ValueError:
            pass

    file_out.write(f"Сумма чисел: {sum_numbers}\n")
=======
# import os
from pathlib import Path

summa = 0
# path = os.path.join('data', 'info.txt')
# path_out = os.path.join('data', 'info_out.txt')
path = Path("data") / "info.txt"
path_out = Path("data") / "info_out.txt"
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if line.strip().isnumeric() or (line[0] == '-' and line[1:].strip().isnumeric()):
            summa += int(line)
print(f"Сумма всех чисел = {summa}")
with open(path_out, 'w', encoding='UTF-8') as f:
    f.write(f"Сумма всех чисел = {summa}")
# Уточнение: в сумму добавляем только те значения, которые можно преобразовать к int'у
# Например: int("-26") --> -26, а int("--26") --> ошибка
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
