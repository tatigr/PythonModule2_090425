# import math
# def sum_two(a, b):
#     c = a + b
#     return c
#
# result = sum_two(sum_two(5, 8) , sum_two(-4, 6))
# # print(c) # not defined
# print(result)


def summa(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(summa(2, 4))
print(summa(2, 4, 6))
print(summa(2, 4, 8))
print("Hello", "World", sep=", ", end="!!!")
print("Hello", "World", sep="- ")
print("Hello", "World", sep=": ")

