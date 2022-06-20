# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        half_1 = int(ticket_number / 100000) + int(ticket_number / 10000 % 10) + int(ticket_number / 1000 % 10)
        half_2 = int(ticket_number / 100 % 10) + int(ticket_number / 10 % 10) + int(ticket_number % 10)
        if half_1 == half_2:
            return True
        else:
            return False
    else:
        return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
