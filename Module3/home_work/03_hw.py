# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input("Введите число: "))
for i in range(n):
    numbers.append(random.randint(-100,100))
total = 0
for i in numbers:
    if i > 0 and i % 2 == 0:
        total += i
print(total)
