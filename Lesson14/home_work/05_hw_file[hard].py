# Задание
# Дана ведомость расчета заработной платы data/workers.txt.
#
# Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов.
# Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of.txt
#
# Формат входных данных
# Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.
#
# Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).
#
# Формат выходных данных
# Выведите зарплату сотрудников с учетом переработки и недоработки.