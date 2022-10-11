# todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
# и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

# Пример вывода:
# Сумма 2   комбинация [(1,1)]
# Сумма 3   комбинация [(1,2),(2,1)]
# Сумма 4   комбинация [(1,3),(3,1),(2,2)]
# ........................................
# Выводы комбинаций оформить в список кортежей.

# todo: Решение
dic = {}
for i in range(1, 7):
    for j in range(1, 7):
        addition = i + j
        z = (i, j)
        if addition not in dic:
            dic[addition] = [z]
        else:
            dic[addition] = dic.get(addition) + [z]
for k, value in dic.items():
    print("Сумма", k, "комбинация", value)

# lst = []
# lst2 = []
# lst3 = []
#
# for i in range(1, 7):
#     for j in range(1, 7):
#         addition = i + j
#         z = (i, j)
#         lst.append(addition)
#         lst2.append(z)
#         lst3.append(lst.count(addition))
# # for g in lst:
# #     print(lst.count(g))
#
#
#
# n_lst, n_lst2,n_lst3 = zip(*sorted(zip(lst, lst2, lst3)))
#
# for h in n_lst:
#     print(h)
# print(n_lst)
# print(n_lst2)
# print(n_lst3)
