# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.


from random import randint
q_mstke = 10  # config Количество попыток
def mistake():
    global cntr
    if cntr >= 3:
        cntr = 0
    cntr += 1
    return cntr

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это конструкция загадана",
         "Это объект загадан"]

x = randint(0, 2)
print(desc_[x])
word = words[x]
# print(word) # Подсказка

template = ["_"] * len(word)
print("".join(template), "Здесь", len(word), "букв")
mstke = 0
while word != "".join(template):
    ans_letter = str(input("Введи букву, но только одну :"))
    if ans_letter not in word:
        mstke += 1
        print("Нет такой буквы в слове", "Осталось ", q_mstke - mstke, "попыток")
        if mstke == q_mstke:
            print("У вас больше нет попыток")
            break
    cntr = 0
    for lttr in word:
        if ans_letter == lttr:
            template[word.index(lttr, cntr, len(word))] = ans_letter
            cntr = word.index(lttr, cntr, len(word)) + 1
    print("".join(template), "Здесь", len(word), "букв")

a = "оператор"
b = ["_"]*len(a)

# cntr = 0
# def mistake():
#     global cntr
#     global a
#     if cntr >= len(a):
#         cntr += 1
#     return cntr
# lttr = str(input("Введите букву: "))

# def letter():
#     lttr = str(input("Введите букву: "))
#     # print(lttr)
#     return lttr
# # lttr = str(input("Введите букву: "))
# cntr = 0
# def game():
#     global a
#     global b
#     global cntr
#     lttr = str(input("Введите букву: "))
#     if letter() in a:
#         # x = a.index("о")
#         x = a.index(lttr, cntr, len(a))
#         for i in a:
#             if lttr == i:
#                 b[x] = lttr
#             cntr += 1
#         return "".join(b)
# # print(game())
# # def ng():
# #     global b
# #     global a
# #     # global lttr
# #     for i in a:
# #         if letter() == i:
# #             b[game()] = letter()
# #     print("".join(b))
#
# # while
# game()
# # letter()
# # ng()
#
#
# # print("".join(b))
