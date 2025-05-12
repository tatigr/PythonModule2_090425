# Напишите декоратор validate_arguments, который проверяет,
# что все аргументы декорируемой функции являются положительными числами.
# Если какой-либо аргумент не удовлетворяет этому условию, декоратор должен выводить сообщение об ошибке.


def validate_arguments(func):
    def wrapper(*args, **kwargs):
<<<<<<< HEAD
        func(*args, **kwargs)
        for arg in args:
            if arg < 0:
                raise ValueError("Все аргументы должны быть > 0")
    return wrapper


=======
        for arg in args:
            if arg < 0:
                raise ValueError("Все аргументы должны быть > 0")
        return func(*args, **kwargs)

    return wrapper
>>>>>>> 040a54448726c63696683ea0a75a24518807d195


@validate_arguments
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 10))
print(calculate_sum(-1, 5))
