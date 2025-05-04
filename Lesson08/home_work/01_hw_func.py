# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    numbers_123 = ticket_number // 1000
    sum_123 = numbers_123 // 100 + numbers_123 // 10 % 10 + numbers_123 % 10
    numbers_456 = ticket_number % 1000
    sum_456 = numbers_456 // 100 + numbers_456 // 10 % 10 + numbers_456 % 10
    if sum_123 == sum_456:
        return f"Этот билет - счастливый"
    return f"Этот билет не является счастливым"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
#print(lucky_ticket(010151))
print(lucky_ticket(000000))
print(lucky_ticket(587677))
print(lucky_ticket(541918))
