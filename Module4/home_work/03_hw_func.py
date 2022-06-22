# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def circle(x1, y1, r1, x2, y2, r2):
    lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if lenght + min(r1, r2) <= max(r1, r2):
        return True
    return False
