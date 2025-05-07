# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

<<<<<<< HEAD
# "5/6 + 2 4/7"
# "12 4/8 - 5 3/2" - "парсинг"
# "12 4/8 - 5 3/2".split

math_expression = str(input("Введите математическое выражение, содержащее простые дроби: "))
# парсинг на "слагаемые"
if "+" in math_expression:
    terms = math_expression.split("+")
elif " - " in math_expression:
    terms = math_expression.split(" - ")
else:
    terms = [math_expression]
print(terms)

whole_part_terms_0 = terms[0].split(" ")
print("Целая и дробная части для первого слагаемого:", whole_part_terms_0)

whole_part_terms_1 = terms[1].split(" ")
print("Целая и дробная части для второго слагаемого:", whole_part_terms_1)

integer_0 = whole_part_terms_0[0]
print("Целая часть первой дроби:", integer_0)

integer_1 = whole_part_terms_1[0]
print("Целая часть второй дроби:", integer_1)

num_denom_0 = whole_part_terms_0[1].split("/")
print("Числитель и знаменатель первой дроби:", num_denom_0)

num_denom_1 = whole_part_terms_1[1].split("/")
print("Числитель и знаменатель второй дроби:", num_denom_1)

from fractions import Fraction
=======
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139



