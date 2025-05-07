# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

<<<<<<< HEAD
def average(*args):
    return sum(args) / len(args)
=======
def average(*args) -> float:
    # print(args)
    return sum(args)/len(args)
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139


def gen_list(size:int, at:int=-10, to:int=10) -> list[int]:
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10, 20, 90)
my_tuple = 5, 7, -4, 10, 8

<<<<<<< HEAD
result = average(*my_tuple) # операция распаковки
=======
result = average(*my_list)
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139
print(result)
