## "Высокооплачиваемые сотрудники"

### Задание
# В файле [data/salaries.txt](data/salaries.txt) даны зарплаты сотрудников.
#
# Выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000. \
# Формат вывода смотри в "Формат выходных данных"
#
# ### Формат входных данных
#
# Дан текстовый файл. \
# В первой строке указаны названия параметров сотрудника. \
# В каждой следующей строке дана информация о сотруднике.
#
# ### Формат выходных данных
#
# Записать информацию в файл highly_paid.txt о сотрудниках с зарплатой выше 60000.
#
# Сотрудников вывести в формате: Фамилия И.О., \
# например: **Иванов И.П.** (зарплаты в выходной файл не записывать)

### Решение задачи
import pprint

path = "data/salaries.txt"
path_out = "data/highly_paid.txt"
employees = []
with open(path, "r", encoding="UTF-8") as file, open(path_out, "w", encoding="UTF-8") as file_out:
    file.readline()
    for line in file:
        employee_data = line.split()
        employee = {
            "surname": employee_data[0],
            "name": employee_data[1],
            "middle_name": employee_data[2],
            "salary": int(employee_data[3]),
        }
        employees.append(employee)

# pprint.pprint(employees)
    for employee in employees:
        if employee["salary"] > 60000:
            formatted = f'{employee["surname"]} {employee["name"][0]}.{employee["middle_name"][0]}.'
            print(formatted)
            file_out.write(formatted + '\n')



