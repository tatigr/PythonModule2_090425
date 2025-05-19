# Дан код:
my_list = [1, 2, 3]
index = int(input("Введите индекс: "))
<<<<<<< HEAD
=======

try:
    element = my_list[index]
except IndexError:
    print(f"Элемент с индексом {index} не существует")

>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
# Задача: добавьте обработку исключений
#   Если введен допустимый индекс, выведите значение по данному индексу
#   В противном случае выведите "Ошибка: индекс вне диапазона!"

try:
    element = my_list[index]

except (ValueError, IndexError):
    print("Ошибка: индекс вне диапазона!")
else:
    print(element)

