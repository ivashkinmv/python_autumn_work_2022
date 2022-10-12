# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

num_str = """8 5 12 12 15
8 5 12 12 15 , 0 23 15 18 12 4 !"""
file = open("num_str.txt", "wt+", encoding="utf-8")
file.write(num_str)

letters_en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_en_dwn = letters_en_up.lower()

x = num_str.split(" ")
lst = []
for i in x:
    if "\n" in i:
        y = i.split("\n")
        z = x.index(i)
        for f in y:
            lst.append(f)
    else:
        lst.append(i)
lst.insert(z+1, "\n")
lst2 = []
for c in lst:
    try:
        if type(int(c)) is int:
            lst2.append(int(c))
        else:
            lst2.append(c)
    except ValueError:
        lst2.append(c)
# print(lst2)
output = []
for ind in lst2:
    if type(ind) is int:
    # print(type(ind))
        for let in range(1,len(letters_en_dwn)):
            if ind == let:
                output.append(letters_en_dwn[let-1])
                # print(letters_en_dwn[let-1])
        if ind == 0:
                output.append(" ")
    else:
        output.append(ind)
        # print(ind)

print("".join(output))


# print(x)
# for g in range(1, len(letters_en_dwn)+1):
# for i in x:
#     print(i.isnumeric())
    # try:
    #     if type(int(i)) is int:
    #         print(i)
    # except:
    #     print(type(int(i)) is not int)
        # print(i)
    # if str(g) ==
    # print(g)
    # v = letters_en_dwn.index(g)
    # print(v)
    # str_g = str(v)
    # print(x)
    # print(v)
    # print(str_g)
    # if str(v) == x[res]:
    #     print(letters_en_dwn[v-1])
    # res += 1
# lst.append(i)

