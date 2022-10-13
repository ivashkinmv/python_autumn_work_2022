# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

# file = open("num_str.txt", "wt+", encoding="utf-8")
# file.write(num_str)
# todo: Решение
num_str = """8 5 12 12 15
8 5 12 12 15 , 0 23 15 18 12 4 !"""


letters_en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_en_dwn = letters_en_up.lower()

x = num_str.split(" ")
lst = []
cntr = 1
for i in x:
    if "\n" in i:
        y = i.split("\n")
        z = x.index(i)
        if len(y) == 2:
            y.insert(1, "\n")
            for f in y:
                lst.append(f)
    else:
        lst.append(i)
lst2 = []
for c in lst:
    try:
        if type(int(c)) is int:
            lst2.append(int(c))
        else:
            lst2.append(c)
    except ValueError:
        lst2.append(c)
output = []
for ind in lst2:
    if type(ind) is int:
        for let in range(1, len(letters_en_dwn)):
            if ind == let:
                output.append(letters_en_dwn[let-1])
        if ind == 0:
            output.append(" ")
    else:
        output.append(ind)

print("".join(output))




