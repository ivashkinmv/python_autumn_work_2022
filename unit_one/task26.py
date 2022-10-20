# todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 classwork/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import pickle
import random
print("Давай сыграем в игру")

x = random.randint(0,100)
print(x)

cntr = 0

diction = {"rand": x, "cntr": cntr}
print(diction)

def mistake():
    global cntr
    if cntr >= 3:
        cntr = 0
    cntr += 1
    return cntr
# def num():
#     global cntr
#     global x
#     if cntr >= 3:
#         x = random.randint(0, 100)
#         print(x)
#     return x

def game():
    global cntr
    y = input("Угадай число: ")
    if y == str(x):
        print("Win")
    elif y == "m":
        menu()
    elif y != str(x) and y != "m":
        if mistake() < 3:
            print("Осталось попыток: ", 3 - cntr)
            game()
        else:
            print("Все")
            menu()

def save():
    name = input("Имя Save: ")
    name_save = {name: diction}
    print(name_save)
    pick = open("game_dump.pkl", "ab+")
    pickle.dump(name_save, pick)
def load():
    pick = open("game_dump.pkl", "rb")
    # print(pick.read)
    print(pickle.load(pick.read))
def menu():

    print(" 1. Новая игра", "\n", "2. Восстановить игру", "\n", "3. Сохранить игру")
    input_num = int(input())
    match input_num:
        case 1:
            game()
        case 2:
            load()
        case 3:
            save()

menu()



