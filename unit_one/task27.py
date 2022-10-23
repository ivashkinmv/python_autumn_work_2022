# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.
import sys
# Пример:
# game_field = []
# # нужно заменить статическую инициализацию списка на динамическую с помощью lambda выражения.
# row_one   = [0, 0, 0, 1, 0]
# row_two   = [0, 0, 0, 1, 0]
# row_three = [0, 1, 0, 0, 0]
# row_four  = [0, 0, 0, 1, 0]
# row_five  = [0, 0, 0, 1, 0]
#
# game_field.append(row_one)
# game_field.append(row_two)
# game_field.append(row_three)
# game_field.append(row_four)
# game_field.append(row_five)
# i = 0  # вхождение в первый массив
# j = 3  # вхождение в 4-ый элемент текущего массива
# # доступ к элементам двухмерного массива
# print(game_field[i][j])

from random import randint
x_pos = 5
y_pos = 5
game_field = []
for i in range(0, x_pos):
    horizon = [(lambda: randint(0, 1))() for vertical in range(0, y_pos)]
    game_field.append(horizon)
# print(game_field)


def coords():
    pos_i = int(input("Введите значение i "))-1
    pos_j = int(input("Введите значение j "))-1
    return pos_i, pos_j


def game():
    global game_field
    pos_i, pos_j = coords()

    if game_field[pos_i][pos_j] == 1:
        game_field[pos_i][pos_j] = "X"
        print("Попал")
        # print(game_field)
        exam_game()
    else:
        game_field[pos_i][pos_j] = "?"
        print("Промах")
        # print(game_field)
        exam_game()


def exam_game():
    for pos_i in game_field:
        for pos_j in pos_i:
            # print(j)
            if pos_j == 1:
                game()
    else:
        sys.exit("Win")


exam_game()
