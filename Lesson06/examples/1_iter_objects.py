# Итерируемые объекты — объекты, которые позволяют последовательно перебирать элементы коллекции.
# В Python это: списки, кортежи, строки и другие типы данных.

numbers = [1, 2, 3]
iterator = iter(numbers)
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break