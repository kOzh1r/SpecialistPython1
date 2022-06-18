# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
max_len = 0
for i in tup:
    if i > max_len:
        max_len = i
print(max_len)
