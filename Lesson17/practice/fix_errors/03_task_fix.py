# Дана функция
from Lesson09.practice.demo import result


def remove_duplicates(data: list) -> list:
    "Удаление дубликатов из списка"
    result = []
    for item in data:
        if result.count(item) == 0:
            result.append(item)
    return result
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?


if __name__ == "__main__":
    assert sorted(remove_duplicates([2, 8, 4, -2, 8, -45])) == [-45, -2, 2, 4, 8]
    # assert remove_duplicates([2, 8, -2, -2, 8, -45]) == [2, 8, -2, -45]
    # assert remove_duplicates([2, 0, 4, -2, 0, -4, 4]) == [2, 0, 4, -2, -4]
    # assert remove_duplicates([1, 1, 1, 1, 1, 1]) == ([1])
    # assert remove_duplicates([1]) == [1]
    # assert remove_duplicates(["help", "help", "by", "by"]) == (["help", "by"])
    # print(remove_duplicates(2, 8, 4, -2, 8, -45))
    # print(remove_duplicates(2, 8, -2, -2, 8, -45))

