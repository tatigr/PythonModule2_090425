# # from Lesson09.practice.demo import is_positive
# # Отфильтровать только четные положительные элементы
# def is_positive(number):
#     print("is positive")
#     return number > 0
#
# def is_even(number):
#     print("is even")
#     return number % 2 == 0
#
# def my_filter(func, iterable):
#     for el in iterable:
#         if func(el):
#             print("my_filter")
#             yield el
#
# data = [12, 15, -22, 20, 5, -3, -8, 0, 10, 7]
#
# result = my_filter(is_even, my_filter(is_positive, data))
# next(result)
# print("----------------------")
# next(result)
#
# print(result)


def gen():
    while True:
        yield 1

result = list(gen()) # обернули в лист бесконечный генератор
print(result)
# for el in gen():
#     print(el)