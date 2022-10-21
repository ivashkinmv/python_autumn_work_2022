# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.


from random import randint
# q_mstke = 10  # config Количество попыток
# def mistake():
#     global cntr
#     if cntr >= 3:
#         cntr = 0
#     cntr += 1
#     return cntr
#
words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это конструкция загадана",
         "Это объект загадан"]
#
x = randint(0, 2)

# a = "оператор"


a = words[x]
b = ["_"]*len(a)

mstke = 0


def mistake():
    global mstke
    global a
    mstke += 1
    return mstke


#
def letter():
    lttr = str(input("Введите букву: "))
    return lttr


def game():
    global b
    global a
    global mstke
    lttr = letter()
    cntr = 0
    if lttr not in a:
        print("Ошибка", mistake(), "из 3")
        if mstke == 3:
            print("Ваши попытки закончились")
    for i in a:
        if lttr == i:
            b[a.index(lttr, cntr, len(a))] = lttr
        cntr += 1


def compare():
    global a
    global b
    global mstke
    while a != "".join(b) and mstke != 3:
        print("".join(b), "здесь букв:", len(a), desc_[x])
        game()
    if a == "".join(b):
        print("Слово угадано - это", "".join(b))


compare()
