#todo. Транспонирование матрицы, transpose(matrix)
# level:hight
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.


# Пример:
# transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

# TODO Решение
transpose = [[1, 2, 3], [4, 5, 6]]

# lst2 = []
# for j in range(len(transpose[0])):
#     lst = []
#     lst2.append(lst)
#     for i in range(len(transpose)):
#         lst.append(transpose[i][j])
# print(lst2)


print([[transpose[i][j] for i in range(len(transpose))] for j in range(len(transpose[0]))])

