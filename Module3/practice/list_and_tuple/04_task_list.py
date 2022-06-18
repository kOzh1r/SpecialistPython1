# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random

numbers = []
n = int(input("Введите число: "))
for i in range(n):
    numbers.append(random.randint(-100, 100))
total = 0
print(numbers)
for i in numbers:
    if i > 0:
        total += i
print(total)
