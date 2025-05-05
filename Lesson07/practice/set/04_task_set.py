# Дана строка.
# Определите, все ли буквы в ней уникальны.

<<<<<<< HEAD
string = "шла Саша по шоссе"
string = string.replace(" ", "")
if len(string) == len(set(string)):
    print("Все символы уникальны")
else:
    print("Есть повторяющиеся символы")
=======
string = "uniq strg "
string_no_space = string.replace(" ", "")

if len(set(string_no_space)) == len(string_no_space):
    print("Символы не повторяются")
else:
    print("Есть дублика символов")
>>>>>>> add97ec0f02a090feb9f8521b3c595486b4d804f
