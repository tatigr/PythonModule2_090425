from pathlib import Path
import json

# Задача: Прочитайте информацию из файлов json_data01.json ... json_data06.json
# Выведите названия файлов, содержащих некорректный JSON(с ошибками)

file_names = ['json_data01.json', 'json_data02.json', 'json_data03.json',
              'json_data04.json', 'json_data05.json', 'json_data06.json']

path = Path("data")

with open (path / file_names[2], "r") as file:
    try:
        data = json.load(file)
    except json.decoder.JSONDecoderError:
        print("Ошибка в JSON-файле")

# path / file_names[0]
# path / file_names[1]
# path / file_names[2]
# path / file_names[3]
# path / file_names[4]
# path / file_names[5]

# for file_name in file_names:
#     try:
#         with open (file_name, "r", encoding="utf-8") as file:
#             json.load(file)
#     except json.JSONDecodeError:
#         print(f"Некорректный JSON: {file_name}")
#     except FileNotFoundError:
#         print(f"Файл не найден: {file_name}")




