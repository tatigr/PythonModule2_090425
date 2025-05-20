# Напишите функцию is_leap_year(year), которая принимает целое число, представляющее год,
# и возвращает True, если год является високосным, и False в противном случае.
# (Напоминание: високосный год делится на 4, кроме годов, делящихся на 100, но не на 400).
from datetime import date

def is_leap_year(year: int) -> bool:
    try:
        date(year, 2, 29)
        return True
    except ValueError:
        return False

# Пример использования
year1 = 2024
year2 = 2100
print(f"{year1} - високосный год: {is_leap_year(year1)}")
print(f"{year2} - високосный год: {is_leap_year(year2)}")

# TODO: напишите тесты для функции, используя оператор assert
