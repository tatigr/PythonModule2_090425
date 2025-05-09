# Дана строка.
# Определите, все ли буквы в ней уникальны.


string = "Шла Саша по шоссе"
string = string.replace(" ", "")
if len(string) == len(set(string)):
    print("Все символы уникальны")
else:
    print("Есть повторяющиеся символы")


