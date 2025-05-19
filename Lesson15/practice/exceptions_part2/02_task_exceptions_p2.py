def validate_email(email):
    # Добавьте проверку, что email содержит символ '@'.
    # Если email некорректный, выбросьте исключение ValueError.
    if '@' not in email:
        raise ValueError("Нет @")
    return email

# Добавьте обработку исключения ValueError
try:

    email = (input("Введите email: "))
    print(validate_email(email))
except ValueError as e:
    print(e)