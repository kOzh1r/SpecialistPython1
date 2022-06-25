# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    number = str(number)
    return number == number[::-1]

a = int(input())
b = int(input())
summ = 0
for i in range(a, b):
    if palindrome(i):
        summ += 1
print(summ)
