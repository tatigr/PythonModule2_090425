# Дана функция
def max_value(*args):
    "Нахождение максимального"
    maximum = args[0]
    for arg in args:
        if maximum < arg:
            maximum = arg
    return maximum


# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?

if __name__ == "__main__":
    assert max_value(2, 8, 48, -5, -45) == 48
    assert max_value(-12, 0, -2, -7, -45) == 0
    assert max_value(-2, -18, -8, -3, -42) == -2
    # assert max_value() == ()

    # print(max_value(2, 8, 48, -5, -45))
    # print(max_value(-12, 0, -2, -7, -45))
    # print(max_value(-2, -18, -8, -3, -42))