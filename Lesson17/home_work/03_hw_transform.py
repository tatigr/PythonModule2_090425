# У вас есть список словарей, представляющих студентов с их именами и средними баллами.
# Вам нужно отфильтровать студентов, чей средний балл выше 4.5,
# и округлить средний балл оставшихся студентов до двух знаков после запятой.


students = [{'name': 'Alice', 'grade': 4.8}, {'name': 'Bob', 'grade': 3.9}, {'name': 'Charlie', 'grade': 4.65},
             {'name': 'David', 'grade': 4.2}, {'name': 'Eve', 'grade': 4.91}]
names = list(filter(lambda person: person['grade'] > 4.5, students))
grades_after_round = list(map(lambda person: {'name': person['name'], 'grade': round(person['grade'], 2)}, names))
print(grades_after_round)


# names_after_round = list(map(lambda person: {'name': person['name'], 'grade': round(person['grade'], 1)}, names))
# print(names_after_round)