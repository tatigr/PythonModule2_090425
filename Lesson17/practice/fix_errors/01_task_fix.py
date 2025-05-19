# Дана функция
def celsius_to_fahrenheit(celsius: int | float) -> float:
    "Конвертация температуры из Цельсия в Фаренгейт"
    return float((celsius * 9 / 5) + 32)

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
if __name__ == "__main__":
    assert celsius_to_fahrenheit(36) == 96.8
    assert celsius_to_fahrenheit(10) == 50.0
    # print(celsius_to_fahrenheit(36))
    assert celsius_to_fahrenheit(-15) == 5.0
    assert celsius_to_fahrenheit(-2000) == -3568.0