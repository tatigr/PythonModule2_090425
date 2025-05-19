# Дана функция
def count_vowels(text: str) -> int:
    "Подсчет гласных "
    vowels = "aeiouyаеёиоуыэюя"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
if __name__ == "__main__":
    assert int(count_vowels("мама мыла раму")) == 6
    assert int(count_vowels("текст какой-то там")) == 5
    assert int(count_vowels("")) == 0
    assert int(count_vowels("werhfgihgb opgikbn d pakdopkp")) == 6
    assert int(count_vowels("")) == 0
