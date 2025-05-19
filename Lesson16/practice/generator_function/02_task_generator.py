# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

<<<<<<< HEAD




def countdown(number):
    for number in range(number, 0, -1):
        yield number

for number in countdown(14):
    print(number)

print(list(countdown(7)))
=======
def countdown(n):
    for number in range(n, 0, -1):
        yield number


print(list(countdown(8)))

>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
