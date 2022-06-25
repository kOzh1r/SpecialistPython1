# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    number_list = []
    length = 1
    for i in range(of, to):
        number_list.append(random.randint(of, to))
        if length == size:
            break
        length += 1
    return number_list
