a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if (a + b) > c and (b + c) > a and (a + c) > b:
    if a == b != c or b == c != a or a == c != b:
        print("Равнобедренный")
    elif a != b != c:
        print("Не равнобедренный")
else:
    print("Не существует")