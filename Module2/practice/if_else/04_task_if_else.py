a = int(input("Введите число: "))

if a % 3 == 0 and a % 5 == 0:
    print("Foobar")
elif a % 5 == 0:
    print("Bar")
elif a % 3 == 0:
    print("Foo")
