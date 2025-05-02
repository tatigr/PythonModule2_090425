# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"
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