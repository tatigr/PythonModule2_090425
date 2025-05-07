# Напишите функцию, которая принимает список чисел и возвращает новый список,
# содержащий только те числа, которые делятся на 3 без остатка.

<<<<<<< HEAD
def mult_3(numbers):
    return numbers % 3 == 0
=======
def mult_3(number):
    return number % 3 == 0
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139

def multiples3(numbers):
    return list(filter(mult_3, numbers))


<<<<<<< HEAD
print(multiples3([2, 8, -5, 2, 8, 1, -9]))
=======
print(multiples3([12, 11, 9, 10, 13, 6]))
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139
