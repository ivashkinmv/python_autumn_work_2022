#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы. 

# Пример:
mass = [1,2,17,54,30,89,2,1,6,2,0,2]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.


lst1 = []
lst2 = []
lst3 = []
list4 = []
list5 = []
list6 = []
i = 0

for elem in mass:
    x = mass.index(elem, i, len(mass))
    y = mass.index(elem)
    z = mass.count(elem)
    i += 1
    if x - y != 0:
        list4.append(elem)
        list5.append(x-y)
        print(elem, x-y)
    if z > 2:
        list6.append(x)
        print(x)
    lst1.append(x)
    lst2.append(y)
    lst3.append(z)

print(mass)
print(lst1)
print(lst2)
print(lst3)
print(list4)
print(list5)
print(list6)
