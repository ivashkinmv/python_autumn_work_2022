# #todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# # Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from time import time, strftime

def decorator_render(func):
    # print("Call decorator function")

    def wrapper(text):
        # print(f"Логика перед вызовом функции", strftime("%c"))
        res = func(text)
        # print("Логика после вызова функции", strftime("%c"))
        return res
    return wrapper
@decorator_render
def render(text):
    print(f"{text}", strftime("%c"))
    menu()



@decorator_render
def show(text):
    print(f"{text}",strftime("%c"))
    menu()



def menu():
    input_num = int(input("Введи render или show: "))
    match input_num:
        case 1:
            render("render")
        case 2:
            show('show')

menu()




