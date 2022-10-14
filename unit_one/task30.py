#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21

matrix = [[1, 2, 3], [4, 5, 6]]
# lst = []
# for x in matrix:
#     for y in x:
#         lst.append(y)
# print(sum(lst))
# TODO Решение
result = sum([y for x in matrix for y in x])
print(result)


