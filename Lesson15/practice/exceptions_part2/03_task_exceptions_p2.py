def check_string_length(text, min_length):
    # Добавьте проверку, что длина строки не меньше min_length.
    # Если строка слишком короткая, выбросьте исключение ValueError.
    if len(text) < min_length:
        raise ValueError("Слишком короткая строка")
    return text


# Добавьте обработку исключения ValueError
try:
    min_length = 15
    text = (input("Введите произвольный текст: "))
    print(check_string_length(text, min_length))
except ValueError as e:
    print(e)

