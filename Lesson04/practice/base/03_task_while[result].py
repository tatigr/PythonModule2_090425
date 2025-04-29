n = int(input("n: "))
sum = 0
a = 0
while a <= n:
    if a % 2 == 0:
        sum += a
    a += 1
print(f"Сумма четных чисел от 0 до {n}: ", sum)
