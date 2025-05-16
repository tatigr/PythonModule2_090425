# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.





def countdown(number):
    for number in range(number, 0, -1):
        yield number

for number in countdown(14):
    print(number)

print(list(countdown(7)))
