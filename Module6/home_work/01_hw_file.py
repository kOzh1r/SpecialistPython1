# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(text)


log("hello world2")  # дописывает "hello world" в конец файла log.txt
log("message2", "log01.txt")  # дописывает "message" в конец файла log01.txt
