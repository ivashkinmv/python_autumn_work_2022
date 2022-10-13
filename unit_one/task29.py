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
transpose = ([[1, 2, 3], [4, 5, 6]])

len_trans = len(transpose)
# for i in range(0, len(transpose)):
#     for j in range(0, len(transpose[i])):
#         # print(i,j)
#         print(transpose)
# # result = [y for x in transpose for y in x]
# # print(result)
# r = 1
print(transpose)

