## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

```python
def price(worked, salary, norm):
    if int(worked) > int(norm):
        return int((((int(worked) - int(norm)) * (int(salary) / int(norm))) * 2) + int(salary))
    return int(int(salary) / int(norm) * int(worked))


workers = []
hours_of = []

with open('data/workers.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        workers += line.split()

with open('data/hours_of.txt', 'r', encoding='UTF-8') as w:
    for line in w:
        hours_of += line.split()

total_list = []

for string in range(5, int(len(workers))):
    for con in range(len(hours_of)):
        if workers[string] == hours_of[con] and workers[string - 1] == hours_of[con - 1]:
            print(workers[string - 1], workers[string], workers[string + 2], end=" ")
            print(price(hours_of[con + 1], workers[string + 1], workers[string + 3]))

```

---
