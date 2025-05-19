def check_age(age):
    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
    if age < 0:
<<<<<<< HEAD
        raise ValueError("Возраст должен быть положительным числом.")
    return age

try:
    age = int(input("Введите возраст: "))
    print(check_age(age))
except ValueError as e:
    print(e)

=======
        raise ValueError("Возраст должен быть положительный")
    return age

try:
    print(check_age(-5))
except ValueError as e:
    print(e)


# for i in [1, 2, 3, 0, 4, 5]:
#     try:
#         print(10/i)
#     except ZeroDivisionError:
#         print("Попытка деления на ноль")
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
