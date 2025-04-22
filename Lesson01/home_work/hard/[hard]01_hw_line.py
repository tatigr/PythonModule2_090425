number = int(input("Введите число в секундах: "))
days = number // (3600 * 24)
hours = (number % (3600 * 24)) // 3600
minutes = (number % 3600) // 60
seconds = number % 60
print(f"Введенное количество секунд равно {days} : {hours} : {minutes} : {seconds}.")


