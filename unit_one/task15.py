# # Написать игру "Поле чудес"
#
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

from random import randint

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это конструкция загадана", "Это объект загадан" ]


x = randint(0, 2)
for n,i in enumerate(desc_):
    if n == x:
        print(desc_[x])
        # print(words[x])
        word = words[x]
        template = "_" * len(word)
        print(template , "Здесь", len(word), "букв")
        letter = str(input("Загадай букву, но только одну :"))

        for nl,w in enumerate(word):
            if letter == w:
                # template[nl] = w
                print(word[nl])
                print(nl, w)
                print(template[nl])



# print (x)
