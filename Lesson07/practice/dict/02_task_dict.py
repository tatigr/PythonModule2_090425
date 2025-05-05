# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"
<<<<<<< HEAD
#freq = {}

#for char in text:
#    if char in freq:
#        freq[char] += 1
#    else:
#        freq[char] = 1

#for char, count in freq.items():
#    print(f"'{char}': {count}")

frequency = {}
#    'h' : 2,
#    'e' : 3,
#    'l' : 6

for char in text: # для каждого символа
    if char in frequency:
        frequency[char] += 1
    else: # символ встречаем первый раз
        frequency[char] = 1
print(frequency)
=======

frequency = {}

for char in text:
    if char in frequency: # уже встречали данный символ
        frequency[char] += 1
    else: # символ встречаем первый раз
        frequency[char] = 1

print(frequency)

>>>>>>> add97ec0f02a090feb9f8521b3c595486b4d804f
