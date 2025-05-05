def is_even(n):  # четное или нет
    if n % 2 == 0 and n != 0:
        return True
    return False

def is_even(n):  # четное или нет
    return n % 2 == 0


n = int(input("n: "))
if is_even(n):
    print("Число четное")
#elif n == 0:
    #print("Вы ввели ноль")
else:
    print("Число нечетное")


