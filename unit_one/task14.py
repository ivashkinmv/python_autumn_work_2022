# TODO: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
mass = [2, 2, 1, 2, 17, 54, 30, 89, 2, 1, 6, 2, 0, 2, 2, 54, 0]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
list1 = []
list2 = []
list3 = []
i = 0
for elem in mass:
    x = mass.index(elem, i, len(mass))
    y = mass.index(elem)
    z = mass.count(elem)
    i += 1
    if z == 2 and x-y > 0:
        print("Значение элемента: ", elem, ", Наименьшее растояние между индексами: ", x-y)
    if z > 2:
        list2.append(x)
        list3.append(elem)
cnter = 0
while cnter < len(list2)-1:
    a = list2[cnter+1]-list2[cnter]
    list1.append(a)
    cnter += 1

totl = list1[0]
for i in list1:
    if i < totl:
        totl = i

print("Значение элемента: ", list3[0], ", Наименьшее растояние между индексами: ", totl)
print("Для остальных элементов нет пар и невозможно определить расстояние")
