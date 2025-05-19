# Задача: добавьте обработку пользовательского ввода.
# Если будет введено некорректное значение, выведите сообщение об этом.
# При корректном значении, вычислите значение выражения и выведите результат.

while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение")
    # else:  # можно не использовать
    #     break  # переехал выше

<<<<<<< HEAD
result  = number ** 2 - 4 * number
print(f"Результат: {result}")
=======
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Некорректное значение")

result = number ** 2 - 4 * number
print(result)
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
