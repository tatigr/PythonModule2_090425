# Напишите функцию, которая принимает список строк и возвращает новый список,
# где каждая строка преобразована в верхний регистр.

# Вариант-1
#def upper_list(strings):
#    return [s.upper() for s in strings]

#input_list = ['hello', 'world', 'python']
#print(upper_list(input_list))

def string_to_upper(strings):
#    return string.upper()

def to_upper(strings):
    return list(map(string_to_upper, strings))

print(to_upper('hello', 'world', 'python'))