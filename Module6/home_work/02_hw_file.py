# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("info.txt", "r") as f:
    list_str = []
    for line in f:
        list_str.append(line.strip())

list_int = 0
for line in list_str:
    try:
        list_int += int(line)
    except ValueError:
        pass

print(list_int)
