# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
#i = 1
#while i < len(fruits):
    #print(i, fruits[i])
    #i += 1
# Вариант-1
#i = 1
#for fruit in fruits:
#    print(i, fruit)
#    i += 1

# Вариант-2
for i, fruit in enumerate(fruits, 1):
    print(i, fruit)

#result = list(enumerate(fruits, 1))
#print(result)



