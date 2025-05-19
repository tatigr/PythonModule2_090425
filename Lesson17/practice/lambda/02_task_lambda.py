# Дан готовый код
def multiply_by_ten(y):
    return y * 10


values = [1, 5, 10]
multiplied_values = list(map(multiply_by_ten, values))
print(multiplied_values)

# Задача: перепишите код, используя lambda-функцию
values = [1, 5, 10]
multiplied_values = list(map(lambda value: value * 10, values))
print(multiplied_values)