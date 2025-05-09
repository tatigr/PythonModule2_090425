# Напишите функцию, которая принимает список чисел и возвращает новый список,
# содержащий только те числа, которые делятся на 3 без остатка.


def mult_3(number):
    return number % 3 == 0

def multiples3(numbers):
    return list(filter(mult_3, numbers))

# Проверка данных
print(multiples3([2, 8, -5, 2, 8, 1, -9, 15]))
print(multiples3([12, 11, 9, 10, 13, 6]))

