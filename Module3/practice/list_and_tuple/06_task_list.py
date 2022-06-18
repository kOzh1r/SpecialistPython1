# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())  # Первое число
second_number = int(input())  # Второе число
list_number = []

if first_number > second_number:
    first_number, second_number = second_number, first_number
for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        list_number.append(i)
        
print(list_number)
