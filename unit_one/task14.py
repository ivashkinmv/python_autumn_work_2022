#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы. 

# Пример:
mass = [1,2,17,54,30,89,2,1,6,2,0,2]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
# mass = [1, 1, 2, 17, 54, 30, 30, 89, 2, 1, 6, 2, 0, 2, 1, 30, 89]

for elem in mass:
    y = mass.index(elem)
    z = mass.count(elem)
    if z >= 2:
        i = 0
        indx = []
        for dig in range(1, z+1):
            x = mass.index(elem, i, len(mass))
            indx.append(x)
            i = x + 1
        diff = []
        res = 0
        while res < len(indx)-1:
            a = indx[res + 1] - indx[res]
            # print(a)
            diff.append(a)
            res += 1
        sett = {}
        cntr = diff[0]
        for i in diff:
            if i < cntr:
                cntr = i
        print(elem, cntr, indx)
        # if z == 1:
        #     print ("У остальных парные элементы осутсвуют")
