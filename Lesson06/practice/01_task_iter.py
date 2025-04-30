text = "Hello world"
n = int(input("Сколько раз вывести данную строку: "))
i = 1
# Вариант-1
while i <= n:
    print(text)
    i += 1

# Вариант-2
for i in range(n):
    print(text)
