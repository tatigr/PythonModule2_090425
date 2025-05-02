# Дан код задачи "Числа, большие 5":
numbers = [3, 6, 1, 8, 2, 9]
<<<<<<< HEAD
greater_than_5 = []
#for num in numbers:
#    if num > 5:
#        greater_than_5.append(num)
#print(greater_than_5)
=======
# greater_than_5 = []
# for num in numbers:
#     if num > 5:
#         greater_than_5.append(num)
# print(greater_than_5)
>>>>>>> 91c6c03517893abab01a3c834a1a0cd1c826d49d

# Перепишите его, используя list comprehensions:

greater_than_5 = [num for num in numbers if num > 5]
print(greater_than_5)