def validate_email(email):
    # Добавьте проверку, что email содержит символ '@'.
    # Если email некорректный, выбросьте исключение ValueError.
    if '@' not in email:
        raise ValueError("Нет @")
    return email

# Добавьте обработку исключения ValueError
try:
    print(validate_email)
print(validate_email("us er.example.com"))