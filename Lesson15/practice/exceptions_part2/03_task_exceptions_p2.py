def check_string_length(text, min_length):
    # Добавьте проверку, что длина строки не меньше min_length.
    # Если строка слишком короткая, выбросьте исключение ValueError.
    if len(text) < min_length:
<<<<<<< HEAD
        raise ValueError("Слишком короткая строка")
=======
        raise ValueError("слишком короткая строка")
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
    return text


# Добавьте обработку исключения ValueError
try:
    min_length = 15
    text = (input("Введите произвольный текст: "))
    print(check_string_length(text, min_length))
except ValueError as e:
    print(e)

