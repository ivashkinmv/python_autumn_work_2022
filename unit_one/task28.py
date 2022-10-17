# todo 1: Для игры "Морской бой" файл sea_battle.py написать создание игрового поля nxn

# todo 2: В игровой матрице nxn найти кол-во всех 1

#  Задачи решить через генераторы списков (списковые включения)

# TODO Задача 1
from random import randint

arr = [[randint(0, 1) for y in range(5)] for x in range(5)]
print(arr)
# TODO Задача 2
arr2 = [j for i in arr for j in i].count(1)
print(arr2)
