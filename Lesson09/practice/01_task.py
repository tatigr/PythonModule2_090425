# Напишите функцию, которая принимает список строк и возвращает новый список,
# где каждая строка преобразована в верхний регистр.
<<<<<<< HEAD

# Вариант-1
#def upper_list(strings):
#    return [s.upper() for s in strings]

#input_list = ['hello', 'world', 'python']
#print(upper_list(input_list))

def string_to_upper(strings):
#    return string.upper()
=======
def string_to_upper(string):
    return string.upper()
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139

def to_upper(strings):
    return list(map(string_to_upper, strings))

<<<<<<< HEAD
print(to_upper('hello', 'world', 'python'))
=======
print(to_upper(["hello", "hi", "name"]))

>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139
