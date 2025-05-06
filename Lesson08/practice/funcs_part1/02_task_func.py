# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки
from audioop import reverse


<<<<<<< HEAD
def palindrome(number):
    number_str = str(number)
    return number_str == str(number)[::-1]

def palindrome_v2(number):
    #1234 % 10 -> 4
    #1234 // 10 -> 123
    #1234 -> 1 | 2 | 3 | 4 -> 4321 -> 4321
    # 1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1

=======
# def palindrome(number):
#     return str(number) == str(number)[::-1]

def palindrome_v2(number):
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
    reverse_number = 0
    number_copy = number
    while number_copy != 0:
        digit = number_copy % 10
<<<<<<< HEAD
        reverse_number  = reverse_number * 10 + digit
        number_copy = number_copy // 10
    print(reverse_number)
    return number == reverse_number

# 12321 | "1234"[::-1] -> "4321"

# Тестируем функцию
print(palindrome_v2(1234))
print(palindrome_v2(3454))
=======
        reverse_number = reverse_number * 10 + digit
        number_copy = number_copy // 10
    return number == reverse_number


# 1234 | "1234"[::-1] -> "4321"

# Тестируем функцию
print(palindrome_v2(1234))
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
print(palindrome_v2(3443))
print(palindrome_v2(1234541))
print(palindrome_v2(1234321))
print(palindrome_v2(77777))

# Подсказка:
# Самый простой способ решить задачу, работать с полученным числом как со строкой
# Преобразование к строке:  str(1234) --> "1234"
# Переворот строки:         "1234"[::-1] --> "4321"
