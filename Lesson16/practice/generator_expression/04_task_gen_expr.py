# "Буквы верхнего регистра из строки"
# Генераторное выражение, возвращающее все буквы верхнего регистра из заданной строки.
<<<<<<< HEAD
string = "hello, world"
# result = (char.upper() for char in string)
result = (char for char in string.upper())
print(list(result))
=======

string = "hello world"
result = (char for char in string.upper())

print(list(result))
>>>>>>> 28dabd5918e5dd4ff491c5b35598f4546f748173
