string = input("Введите символы в формате id:2...: ")
# Проверить, соответствует ли данная строка формату:
# Строка начинается с "id:"
# Далее идет *один или боле*е символов, все символы после "id:" цифры.

if string.startswith("id:") and string[3:].isdigit():
    print("Да")
else:
    print("Нет")
