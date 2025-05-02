# Дан словарь и ключ.
# Напишите программу,
# которая удаляет элемент из словаря по ключу. Если ключ отсутствует, ничего не делает.

my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Enter key: ")

#if key in my_dict:
   # del my_dict[key]
    #print(f"Ключ '{key}' удалён.")
#else:
   # print(f"Ключ '{key}' не найден.")

#print("Обновлённый словарь:", my_dict)

if key in my_dict:
  del my_dict[key]
else:
    pass # do nothing

print(f"Словарь после удаления валидного ключа: {my_dict}")