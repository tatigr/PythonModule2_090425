# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {'name': 'Алексей', 'surname': 'Петров', 'salary': 124300},
    {'name': 'Николай', 'surname': 'Петров', 'salary': 120000},
    {'name': 'Иван', 'surname': 'Павлов', 'salary': 34500},
    {'name': 'Василий', 'surname': 'Кукушкин', 'salary': 162500},
    {'name': 'Василий', 'surname': 'Павлов', 'salary': 47800},
]
# Вычислите: имя и фамилию сотрудника с самой высокой зарплатой
#highest_sal = staff[0]
#for item in staff:
#    if item["salary"] > highest_sal["salary"]:
#        highest_sal = item
#print(highest_sal["salary"])
#print(f"Имя и фамилия сотрудника с самой высокой зарплатой: {highest_sal["name"]} {highest_sal["surname"]}")



#Вычислите: имя и фамилию сотрудника с самой низкой зарплатой
#lowest_sal = staff[0]
#for item in staff:
#    if item["salary"] < lowest_sal["salary"]:
#        lowest_sal = item
#print(lowest_sal["salary"])
#print(f"Имя и фамилия сотрудника с самой низкой зарплатой: {lowest_sal["name"]} {lowest_sal["surname"]}")


#Вычислите cреднеарифметическую зарплату всех сотрудников
#sum_sal = 0
#for item in staff:
#    sum_sal += int(item["salary"])
#print(sum_sal)
#print(len(staff))
#print(f"Среднеарифметическая зарплата всех сотрудников равна {int(sum_sal/len(staff))}")


#Вычислите количество однофамильцев в организации

#frequency = {}

#for item in staff:
#    surname = item["surname"]
#    if surname in frequency:
#        frequency[surname] += 1
#    else:
#        frequency[surname] = 1

#print("Количество однофамильцев в организации:")
#for surname, count in frequency.items():
#    if count > 1:
#        print(f"{surname}: {count} человек(а)")
frequency = {}

for item in staff:
    surname = item["surname"]
    if surname in frequency:
        frequency[surname] += 1
    else:
        frequency[surname] = 1
print(f"Количество однофамильцев в организации: {frequency}")


# Напечатайте список всех сотрудников(имена и фамилии) в порядке возрастания их зарплат


#Вариант-1

#for i in range(len(staff)):
#    for j in range(0, len(staff) - 1):
#        if staff[j]['salary'] > staff[j + 1]['salary']:
            # Меняем местами
#            staff[j], staff[j + 1] = staff[j + 1], staff[j]
#print("Список всех сотрудников(имена и фамилии) в порядке возрастания их зарплат:")
#for item in staff:
#    print(f"{item['name']} {item['surname']}")

#Вариант-2
#for item in staff:
#    sorted_staff = sorted(staff, key=lambda x: x['salary'])
#print("Список всех сотрудников(имена и фамилии) в порядке возрастания их зарплат:")
#for item in sorted_staff:
#    print(f"{item['name']} {item['surname']}")



#print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")


