# Дана строка.
# Определите, все ли символы в ней уникальны.

string = "шла Саша по шоссе"
string = string.replace(" ", "")
if len(string) == len(set(string)):
    print("Все символы уникальны")
else:
    print("Есть повторяющиеся символы")