# Задача: Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.
# Решение:
<<<<<<< HEAD

=======
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
# Оформите решение задачи в виде функции

<<<<<<< HEAD
def count_vowels(text: str):
=======
def count_vowels(text: str) -> int:
>>>>>>> ebdecbfce68d73ae8292aa219db282690adf0139
    vowels = "ауоыэяюёие"
    num_vowels = 0
    for char in text.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels

<<<<<<< HEAD
print(count_vowels("маМа мЫла РамУ")) #6
print(count_vowels("Привет, как дела?")) #5
print(count_vowels("После этого, возможно, функция ничего не возвращает (None), отсюда и вывод None")) #25
=======

print(count_vowels("мамА мыла РамУ")) # 6
print(count_vowels("привет, как дела?")) # 5
print(count_vowels("произвольный текст")) # 5
>>>>>>> 8136760f2e4c90398bfaa30199e9553bc21e1405
