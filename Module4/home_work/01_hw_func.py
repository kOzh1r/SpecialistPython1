# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        n1 = int(ticket_number / 100000)
        n2 = int(ticket_number / 10000 % 10)
        n3 = int(ticket_number / 1000 % 10)
        n4 = int(ticket_number / 100 % 10)
        n5 = int(ticket_number / 10 % 10)
        n6 = int(ticket_number % 10)
        len_1 = n1 + n2 + n3
        len_2 = n4 + n5 + n6
        if len_1 == len_2:
            return True
        else:
            return False
    else:
        return False
