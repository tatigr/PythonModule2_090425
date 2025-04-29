#i = 0  # Инициализация переменной
#while i <= 5:  # Условие: пока i меньше 5
#    print(i)  # Вывод значения i
#    i += 1  # Увеличение i на 1


# n = int(input("n: "))
# i = 0
# while i <= n:
#    print(i)
#    i += 1

#n = int(input("n: "))
#i = 0
#while True:
#    print(i)
#    i += 1
#    if i >= n:
#        break


#text = "abracadabra"
#print(f"Минимум: {min(text)}")
#print(f"Максимум: {max(text)}")


numbers = [3, 5, 7, 12] # <str/list/tuple>
#for el in <итерируемый обьект>
#    print(el)
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
