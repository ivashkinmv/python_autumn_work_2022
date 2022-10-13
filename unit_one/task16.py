# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.

from random import randint

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это конструкция загадана",
         "Это объект загадан"]

q_mstke = 10  # config Количество попыток
x = randint(0, len(words)-1) # Генератор номера задания

def question():
    global x
    print(desc_[x])
    template = ["_"] * len(words[x])
    string = str("".join(template)) + " Количество букв в слове:  " + str(len(words[x]))
    return string
print(question())

# mstke = 0
# while word != "".join(template):
#     ans_letter = str(input("Введи букву, но только одну :"))
#     if ans_letter not in word:
#         mstke += 1
#         print("Нет такой буквы в слове", "Осталось ", q_mstke - mstke, "попыток")
#         if mstke == q_mstke:
#             print("У вас больше нет попыток")
#             break
#     cntr = 0
#     for lttr in word:
#         if ans_letter == lttr:
#             template[word.index(lttr, cntr, len(word))] = ans_letter
#             cntr = word.index(lttr, cntr, len(word)) + 1
#     print("".join(template), "Здесь", len(word), "букв")
