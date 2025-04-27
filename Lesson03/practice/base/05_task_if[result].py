number = int(input("Введите целое число: "))

if (number % 3 == 0 and number % 5 == 0):
    print("Foobar")
elif number % 3 == 0:
    print("Foo")
elif number % 5 == 0:
    print("Bar")
else:
    print("")
