# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
<<<<<<< HEAD
    return sum(args) / len(args)
=======
    return sum(args)/len(args)
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
