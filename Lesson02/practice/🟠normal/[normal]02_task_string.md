## "Соответствие формату"

### Задание

Проверить, соответствует ли данная строка формату:
* Строка начинается с "id:"
* Далее идет *один или боле*е символов, все символы после "id:" цифры.

### Формат входных данных

Дана произвольная строка.

### Формат выходных данных

Вывести "Да", если данная строка соответствует указанному формату или "Нет", если не соответствует.

### Решение задачи

```python
string = input("Введите символы в формате id:2...: ")
# Проверить, соответствует ли данная строка формату:
# Строка начинается с "id:"
# Далее идет *один или боле*е символов, все символы после "id:" цифры.

if string.startswith("id:") and string[3:].isdigit():
    print("Да")
else:
    print("Нет")
```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    id:hell    | Нет |
|    id:234    | Да |
|    id234    | Нет |
|    234:id    | Нет |
|    id:12f    | Нет |
|    id:0    | Да |
|    id:    | Нет |

### Подсказки

<details>
<summary>Подсказка-1</summary>
Вспомните про срезы.
</details>
