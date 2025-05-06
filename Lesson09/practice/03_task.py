# Напишите функцию, которая принимает список чисел и возвращает новый список,
# содержащий только те числа, которые делятся на 3 без остатка.

def mult_3(numbers):
    return numbers % 3 == 0

def multiples3(numbers):
    return list(filter(mult_3, numbers))


print(multiples3([2, 8, -5, 2, 8, 1, -9]))