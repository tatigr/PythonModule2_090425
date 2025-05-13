def check_age(age):
    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
    if age < 0:
        raise ValueError("Возраст должен быть положительным числом.")
    return age

try:
    age = int(input("Введите возраст: "))
        print(check_age(age))
except ValueError as e:
    print(f"Ошибка: {e}")

