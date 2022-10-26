# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import os
import sys
from time import time, strftime


def decorator_render(func):
    def wrapper(*a):
        f = open("debug.log", "a")
        wrapper.count += 1
        res = func(*a)
        print(res[0], wrapper.count, res[2])
        f.write(f"{res[0]} , {wrapper.count} , {res[2]} \n")
        return res
    wrapper.count = 0
    return wrapper


@decorator_render
def render(*args):
    return args


@decorator_render
def show(*args):
    return args


def menu():
    input_num = int(input("Введи 1 для render или 2 для show: "))
    match input_num:
        case 1:
            render("Render", render.count+1, strftime("%c"))
            menu()
        case 2:
            show("Show", show.count+1, strftime("%c"))
            menu()
        case 3:
            sys.exit('Окончено')

menu()
