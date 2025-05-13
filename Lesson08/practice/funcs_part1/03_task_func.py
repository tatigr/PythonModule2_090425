# Задача: Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.
# Решение:

# Оформите решение задачи в виде функции


def count_vowels(text: str): #-> int:
    vowels = "ауоыэяюёие"
    num_vowels = 0
    for char in text.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels


# Проверка данных (автотесты)
assert count_vowels("маМа мЫла РамУ") == 6 #6
assert count_vowels("Привет, как дела?") == 5 #5
assert count_vowels("После этого, возможно, функция ничего не возвращает (None), отсюда и вывод None") #25
assert count_vowels("мамА мыла РамУ") == 6 # 6
assert count_vowels("привет, как дела?") == 5 # 5
assert count_vowels("произвольный текст") == 5 # 5

