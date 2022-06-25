# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    my_list = []
    len_list = 0
    if len_list <= size:
        for i in range(of, to):
            my_list.append(i)
            len_list += 1
    return my_list
