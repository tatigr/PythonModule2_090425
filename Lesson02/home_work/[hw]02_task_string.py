# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = "Это поизвольный текст без знаков препинания есть только слова и пробелы"
words = text.split()
for word in words:
    if word.lower().startswith("б"):
        print(f"Первое слово, начинающееся на букву 'б': {word}")
        break
else:
    print("Слов на букву 'б' в данном тексте нет")
