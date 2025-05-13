# Задаем путь к файлу:
path = "data/numbers.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если numbers.txt в той же папке, что и питоновский файл

# Открываем файл на чтение
f = open(path, "r")
sum_numbers = 0  # Переменная для подсчета суммы
# В переменную line считываем строку за стройкой из файла(f)
count = 0
for line in f:
    sum_numbers += int(line)
    count += 1


f.close() # Закрываем файл
print(f"Сумма чисел = {sum_numbers}")
print(f"Среднеарифметическое = {sum_numbers/count}")