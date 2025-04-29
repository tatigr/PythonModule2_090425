# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers = [4, -5, 9, -1, -9, 7, 0]
#i = 0
#count = 0
#while i < len(numbers):
#    if numbers[i] >= 0:
#        count = count + numbers[i]
#    i += 1
#print(count)

count = 0
for number in numbers:
    if number > 0:
        count += number
print(count)
