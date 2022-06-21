# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    AB = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return AB


x1 = int(input("Координаты точки А. х = "))
y1 = int(input("Координаты точки А. у = "))
x2 = int(input("Координаты точки В. х = "))
y2 = int(input("Координаты точки В. у = "))
x3 = int(input("Координаты точки С. х = "))
y3 = int(input("Координаты точки С. у = "))

if distance(x1, y1, x2, y2) <= distance(x2, y2, x3, y3) and distance(x1, y1, x2, y2) <= distance(x1, y1, x3, y3):
    total = distance(x1, y1, x2, y2)
    lenght = 'AB'
elif distance(x1, y1, x2, y2) >= distance(x2, y2, x3, y3) and distance(x2, y2, x3, y3) <= distance(x1, y1, x3, y3):
    total = distance(x2, y2, x3, y3)
    lenght = 'BC'
else:
    total = distance(x1, y1, x3, y3)
    lenght = 'AC'

print(f"Самый короткий отрезок: {lenght} - {round(total, 2)}")
