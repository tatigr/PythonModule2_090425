import os
import pathlib
from pathlib import Path


path = 'files/numbers.txt'  # не самый хороший способ задания пути
path = os.path.join('files', 'numbers.txt')  # хороший кроссплатформенный метод указания пути

# Наиболее правильный способ работы с файлами - использовать контекстный менеджер with
# По окончанию инструкции with файл гарантированно будет закрыт, даже если произойдет ошибка
with open(path, 'r', encoding='UTF-8') as f:
    # Находим сумму всех чисел в файле
    s = 0
    for line in f:
        s += int(line)
print(s)
